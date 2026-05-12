from base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class LoginPageTest(BaseTest):
    def __init__(self):
        super().__init__("/login")

    def attempt_login(self, username, password, captcha_answer):
        """Fungsi pembantu untuk mengisi form dan menekan tombol login."""
        try:
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.NAME, "captcha").send_keys(captcha_answer)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(1)
        except Exception as e:
            print(f"[FAIL] Gagal mengeksekusi form login. Error: {e}")

    def test_wrong_captcha(self):
        """Test Case 1: Username & Password BENAR, tapi CAPTCHA SALAH"""
        print("\n--- Menjalankan Test Case 1: CAPTCHA Salah ---")
        self.driver.get(self.target_url)
        self.attempt_login("mhs1", "123", "999")
        if "login" in self.driver.current_url:
            print("[PASS] Sistem berhasil MENOLAK login karena CAPTCHA salah.")
        else:
            print("[FAIL] Sistem kebobolan dengan CAPTCHA salah!")

    def test_wrong_credentials(self):
        """Test Case 2: Username/Password SALAH, tapi CAPTCHA BENAR"""
        print("\n--- Menjalankan Test Case 2: Kredensial Salah ---")
        self.driver.get(self.target_url)
        jawaban_benar = self.solve_captcha()
        self.attempt_login("hacker", "password123", jawaban_benar)
        if "login" in self.driver.current_url:
            print("[PASS] Sistem berhasil MENOLAK kredensial yang salah.")
        else:
            print("[FAIL] Sistem membiarkan user tak dikenal masuk!")

    def test_success_login(self):
        """Test Case 3: Login Berhasil (Happy Path)"""
        print("\n--- Menjalankan Test Case 3: Login Berhasil ---")
        self.driver.get(self.target_url)
        jawaban_benar = self.solve_captcha()
        self.attempt_login("mhs1", "123", jawaban_benar)
        if "dashboard" in self.driver.current_url.lower():
            print("[PASS] Login sukses! Berhasil masuk ke dasbor.")
        else:
            print("[FAIL] Login gagal, tidak dialihkan ke dasbor.")

if __name__ == "__main__":
    test_login = LoginPageTest()
    
    # Navigasi ke halaman login sebelum pemeriksaan
    test_login.driver.get(test_login.target_url)
    
    print("\n[PRE-FLIGHT] Memeriksa Elemen Input Form...")
    test_login.check_element("name", "username")
    test_login.check_element("name", "password")
    test_login.check_element("name", "captcha")
    
    test_login.test_wrong_captcha()
    test_login.test_wrong_credentials()
    test_login.test_success_login()
    test_login.close()

