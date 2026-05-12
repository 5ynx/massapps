from base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class PraktikumTest(BaseTest):
    def __init__(self):
        super().__init__()

    def run_it_02_navigasi(self):
        print("\n--- [IT-02] Navigasi: Klik Judul Berita ---")
        self.driver.get(self.base_url)
        time.sleep(1)
        try:
            # Mencari elemen judul berita (yang sekarang sudah menjadi link)
            titles = self.driver.find_elements(By.CLASS_NAME, "berita-title")
            if not titles:
                print("[FAIL] Tidak ada berita yang ditemukan di halaman indeks.")
                return

            target = titles[0]
            # Scroll ke elemen agar terlihat (mencegah terhalang navbar)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", target)
            time.sleep(1)
            
            # Coba klik biasa, jika gagal gunakan JS click
            try:
                target.click()
            except:
                self.driver.execute_script("arguments[0].click();", target)

            time.sleep(2)
            if "berita/" in self.driver.current_url:
                print("[PASS] Berhasil navigasi ke halaman detail berita.")
            else:
                print(f"[FAIL] Gagal navigasi ke halaman detail. URL saat ini: {self.driver.current_url}")
        except Exception as e:
            print(f"[FAIL] Error pada IT-02: {e}")

    def run_it_03_big_bang(self):
        print("\n--- [IT-03] Big Bang: Navigasi Cepat ---")
        try:
            # Berpindah antar menu secara cepat
            self.driver.get(self.base_url + "/video-gallery")
            self.driver.get(self.base_url)
            self.driver.get(self.base_url + "/login")
            print("[PASS] Navigasi cepat antar menu tidak menyebabkan crash/error.")
        except Exception as e:
            print(f"[FAIL] Terjadi crash saat navigasi cepat: {e}")

    def run_st_02_security_cookie(self):
        print("\n--- [ST-02] Security: Akses Dashboard Tanpa Cookie ---")
        if not self.login(): return
        
        # Hapus semua cookie
        self.driver.delete_all_cookies()
        
        # Coba akses dashboard lagi
        self.driver.get(self.base_url + "/dashboard")
        time.sleep(1)
        
        if "login" in self.driver.current_url:
            print("[PASS] Sistem melakukan redirect ke login setelah cookie dihapus.")
        else:
            print("[FAIL] Dashboard masih bisa diakses tanpa cookie!")

    def run_st_03_security_captcha(self):
        print("\n--- [ST-03] Security: Login CAPTCHA Kosong ---")
        self.driver.get(self.base_url + "/login")
        try:
            self.driver.find_element(By.NAME, "username").send_keys("mhs1")
            self.driver.find_element(By.NAME, "password").send_keys("123")
            # Captcha dikosongkan
            self.driver.find_element(By.NAME, "captcha").clear()
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(1)
            
            if "login" in self.driver.current_url:
                print("[PASS] Login ditolak karena CAPTCHA kosong.")
            else:
                print("[FAIL] Login berhasil meskipun CAPTCHA kosong!")
        except Exception as e:
            print(f"[FAIL] Error: {e}")

    def run_st_04_regression(self):
        print("\n--- [ST-04] Regression: Kelola User Normal ---")
        if not self.login(): return
        self.driver.get(self.base_url + "/kelola-user")
        if "kelola-user" in self.driver.current_url:
            print("[PASS] Menu Kelola User terbuka normal.")
        else:
            print("[FAIL] Gagal membuka menu Kelola User.")

if __name__ == "__main__":
    test = PraktikumTest()
    test.run_it_02_navigasi()
    test.run_it_03_big_bang()
    test.run_st_02_security_cookie()
    test.run_st_03_security_captcha()
    test.run_st_04_regression()
    test.close()
