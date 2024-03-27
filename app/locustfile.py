from locust import HttpUser, task

SERVER_IP_ADDR = "188.225.37.37"


class LoadTesting(HttpUser):
    @task
    def test_some_pages_open(self):
        self.client.get(f"http://{SERVER_IP_ADDR}/authapp/register/")
        self.client.get(f"http://{SERVER_IP_ADDR}/authapp/login/")