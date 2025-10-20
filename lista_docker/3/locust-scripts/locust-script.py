from locust import HttpUser, task, between


class WordPressUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    @task(1)  # Weight: 2
    def view_posts1(self):
        # Visit different posts (adjust IDs based on your posts)
        self.client.get("/?p=1")

    @task(1)  # Weight: 2
    def view_posts11(self):
        # Visit different posts (adjust IDs based on your posts)
        self.client.get("/?p=11")

    @task(1)  # Weight: 2
    def view_posts31(self):
        # Visit different posts (adjust IDs based on your posts)
        self.client.get("/?p=31")

