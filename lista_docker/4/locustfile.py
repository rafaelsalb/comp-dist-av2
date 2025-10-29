from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(1, 2.5)
    websites = [
        "https://google.com",
        "https://wikipedia.org",
        "https://reddit.com",
        "https://youtube.com",
        "https://github.com",
        "https://youtube.com",
        "https://ead.unifor.br",
        "https://uol.unifor.br",
        "http://example.com",
        "https://g1.globo.com"
    ]

    @task
    def extract_links(self):
        for website in self.websites:
            path = f"/api/{website}"
            self.client.get(path, name=f"/api/{website}")
