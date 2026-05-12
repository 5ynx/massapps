from locust import HttpUser, task, between

class MasAppsUser(HttpUser):
    # Tunggu antara 1 hingga 5 detik antar task
    wait_time = between(1, 5)

    @task(3)
    def index_page(self):
        """Mengakses halaman utama (prioritas tinggi)."""
        self.client.get("/")

    @task(2)
    def detail_berita(self):
        """Simulasi membuka detail berita (ID 3 adalah contoh dari SQL)."""
        self.client.get("/berita/3")

    @task(1)
    def video_gallery(self):
        """Mengakses galeri video."""
        self.client.get("/video-gallery")

    @task(1)
    def login_page(self):
        """Mengakses halaman login."""
        self.client.get("/login")

# Instruksi Jalankan:
# 1. Buka terminal
# 2. Jalankan: locust -f locustfile.py
# 3. Buka browser: http://localhost:8089
# 4. Masukkan 'Number of users': 100, 'Spawn rate': 10, 'Host': http://127.0.0.1:5000