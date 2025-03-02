import os

from locust import HttpUser, task

SERVER_IP_ADDR_FOR_LOAD_TEST = os.environ.get('SERVER_IP_ADDR_FOR_LOAD_TEST')


class LoadTesting(HttpUser):
    """Нагрузочное тестирование"""
    @task
    def test_some_pages_open(self):
        self.client.get(f"http://{SERVER_IP_ADDR_FOR_LOAD_TEST}/authapp/register/")
        self.client.get(f"http://{SERVER_IP_ADDR_FOR_LOAD_TEST}/authapp/login/")