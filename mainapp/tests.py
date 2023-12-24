from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from authapp import models as authapp_models
from mainapp import models as mainapp_models


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
        self.client_with_auth.force_login(self.user_admin, backend="django.contrib.auth.backends.ModelBackend")

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


from django.core import mail as django_mail

from mainapp import tasks as mainapp_tasks


class TestTaskMailSend(TestCase):
    fixtures = ("authapp/fixtures/001_user_admin.json",)

    def test_mail_send(self):
        """Тест отправки электронного письма"""
        message_text = "test_message_text"
        user_obj = authapp_models.CustomUser.objects.first()
        mainapp_tasks.send_feedback_mail(message_text, user_obj.email)
        self.assertEqual(django_mail.outbox[0].body, message_text)
