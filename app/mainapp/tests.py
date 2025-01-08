from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from http import HTTPStatus

from django.core import mail as django_mail
from django.test import Client, TestCase
from django.urls import reverse

from authapp import models as authapp_models
from mainapp import models as mainapp_models
from mainapp import tasks as mainapp_tasks


class TestNewsPage(TestCase):
    fixtures = (
        "authapp/fixtures/001_user_admin.json",
        "mainapp/fixtures/001_news.json",
    )

    def setUp(self):
        """Логинимся под админом"""
        super().setUp()
        self.client_with_auth = Client()
        self.user_admin = authapp_models.CustomUser.objects.get(username="admin")
        self.client_with_auth.force_login(
            self.user_admin, backend="django.contrib.auth.backends.ModelBackend"
        )

    def test_page_open_list(self):
        """Тест страницы списка новостей"""
        path = reverse("mainapp:news")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_page_open_detail(self):
        """Тест детальной страницы новостей"""
        news_obj = mainapp_models.News.objects.first()
        path = reverse("mainapp:news_detail", args=[news_obj.pk])
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_page_open_crete_deny_access(self):
        """Тест на открытие страницы создания новости"""
        path = reverse("mainapp:news_create")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_page_open_crete_by_admin(self):
        """Тест на открытие страницы создания новости под администратором"""
        path = reverse("mainapp:news_create")
        result = self.client_with_auth.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_create_in_web(self):
        """Тест на создание новости администратором"""
        counter_before = mainapp_models.News.objects.count()
        path = reverse("mainapp:news_create")
        self.client_with_auth.post(
            path,
            data={
                "title": "NewTestNews001",
                "preambule": "NewTestNews001",
                "body": "NewTestNews001",
            },
        )
        self.assertGreater(mainapp_models.News.objects.count(), counter_before)

    def test_page_open_update_deny_access(self):
        """Тест на открытие страницы изменения новости"""
        news_obj = mainapp_models.News.objects.first()
        path = reverse("mainapp:news_update", args=[news_obj.pk])
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_page_open_update_by_admin(self):
        """Тест на открытие страницы изменения новости под администратором"""
        news_obj = mainapp_models.News.objects.first()
        path = reverse("mainapp:news_update", args=[news_obj.pk])
        result = self.client_with_auth.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_update_in_web(self):
        """Тест на обновление новости под администратором"""
        new_title = "NewTestTitle001"
        news_obj = mainapp_models.News.objects.first()
        self.assertNotEqual(news_obj.title, new_title)
        path = reverse("mainapp:news_update", args=[news_obj.pk])
        result = self.client_with_auth.post(
            path,
            data={
                "title": new_title,
                "preambule": news_obj.preambule,
                "body": news_obj.body,
            },
        )
        self.assertEqual(result.status_code, HTTPStatus.FOUND)
        news_obj.refresh_from_db()
        self.assertEqual(news_obj.title, new_title)

    def test_delete_deny_access(self):
        """Проверка на удаление новости"""
        news_obj = mainapp_models.News.objects.first()
        path = reverse("mainapp:news_delete", args=[news_obj.pk])
        result = self.client.post(path)
        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_delete_in_web(self):
        """Проверка на удаление новости под администратором"""
        news_obj = mainapp_models.News.objects.first()
        path = reverse("mainapp:news_delete", args=[news_obj.pk])
        self.client_with_auth.post(path)
        news_obj.refresh_from_db()
        self.assertTrue(news_obj.deleted)


class TestTaskMailSend(TestCase):
    fixtures = ("authapp/fixtures/001_user_admin.json",)

    def test_mail_send(self):
        """Тест отправки электронного письма"""
        message_text = "test_message_text"
        mainapp_tasks.send_feedback_mail(message_text)
        self.assertEqual(django_mail.outbox[0].body, message_text)


class TestNewsSelenium(StaticLiveServerTestCase):
    fixtures = (
        "authapp/fixtures/001_user_admin.json",
        "mainapp/fixtures/001_news.json",
    )

    def setUp(self):
        """
        Функция setUp в тестовом классе используется для настройки начальных условий перед выполнением каждого тестового
        метода в этом классе. В данном коде она создает экземпляр веб-драйвера Chrome, устанавливает неявное ожидание в
        10 секунд, открывает страницу авторизации, вводит имя пользователя и пароль, и ждет, пока элемент с классом
        "mt-auto" станет видимым. Это позволяет гарантировать, что перед запуском каждого теста будут выполнены
        определенные предварительные действия.
        """
        super().setUp()
        self.selenium = webdriver.Chrome()
        self.selenium.implicitly_wait(10)
        self.selenium.get(f"{self.live_server_url}{reverse('authapp:login')}")
        self.selenium.find_element(By.ID, "id_username").send_keys("admin")
        self.selenium.find_element(By.ID, "id_password").send_keys("admin")
        self.selenium.find_element(By.CLASS_NAME, "loginButton").click()
        WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "mt-auto"))
        )

    def test_create_button_clickable(self):
        """Тест кнопки создания новости"""
        path_list = f"{self.live_server_url}{reverse('mainapp:news')}"
        path_add = reverse("mainapp:news_create")
        self.selenium.get(path_list)
        button_create = WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f'[href="{path_add}"]'))
        )
        print("Trying to click button ...")
        button_create.click()  # Test that button clickable
        WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.ID, "id_title"))
        )
        print("Button clickable!")

    def test_pick_color(self):
        """Тест цвета хедера, если не соответствует делем скриншот"""
        path = f"{self.live_server_url}{reverse('mainapp:main_page')}"
        self.selenium.get(path)
        navbar_el = WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "navbar"))
        )
        try:
            self.assertEqual(
                navbar_el.value_of_css_property("background-color"),
                "rgba(255, 255, 255, 1)",
            )
        except AssertionError:
            with open("var/screenshots/001_navbar_el_scrnsht.png", "wb") as outf:
                outf.write(navbar_el.screenshot_as_png)
            raise

    def tearDown(self):
        """Закрываем браузер"""
        self.selenium.quit()
        super().tearDown()
