from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re

class BaseTest:
    def __init__(self, target_url=None):
        """Inisialisasi WebDriver dan navigasi ke URL target."""
        print(f"[SETUP] Menginisialisasi Chrome WebDriver...")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1:5000"
        self.driver.implicitly_wait(5)
        
        if target_url:
            self.target_url = self.base_url + target_url
        else:
            self.target_url = self.base_url

    def solve_captcha(self):
        """Membaca dan menghitung hasil CAPTCHA matematika."""
        try:
            page_text = self.driver.find_element(By.TAG_NAME, "body").text
            match = re.search(r'(\d+)\s*\+\s*(\d+)', page_text)
            if match:
                angka1, angka2 = int(match.group(1)), int(match.group(2))
                hasil = angka1 + angka2
                print(f"[INFO] CAPTCHA Terpecahkan: {angka1} + {angka2} = {hasil}")
                return str(hasil)
            return "0"
        except Exception as e:
            print(f"[ERROR] Gagal memecahkan CAPTCHA: {e}")
            return "0"

    def login(self, username="mhs1", password="123"):
        """Melakukan login ke aplikasi."""
        print(f"[ACTION] Mencoba login sebagai '{username}'...")
        self.driver.get(self.base_url + "/login")
        
        try:
            captcha_ans = self.solve_captcha()
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.NAME, "captcha").send_keys(captcha_ans)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            
            time.sleep(1)
            if "dashboard" in self.driver.current_url.lower():
                print("[PASS] Login Berhasil.")
                return True
            else:
                print("[FAIL] Login Gagal.")
                return False
        except Exception as e:
            print(f"[FAIL] Error saat login: {e}")
            return False

    def check_element(self, locator_type, locator_value):
        """Memeriksa keberadaan elemen."""
        try:
            if locator_type.lower() == 'id':
                self.driver.find_element(By.ID, locator_value)
            elif locator_type.lower() == 'name':
                self.driver.find_element(By.NAME, locator_value)
            elif locator_type.lower() == 'css':
                self.driver.find_element(By.CSS_SELECTOR, locator_value)
            elif locator_type.lower() == 'xpath':
                self.driver.find_element(By.XPATH, locator_value)
            print(f"[PASS] Elemen '{locator_value}' ({locator_type}) ditemukan.")
            return True
        except:
            print(f"[FAIL] Elemen '{locator_value}' ({locator_type}) TIDAK ditemukan.")
            return False

    def close(self):
        """Menutup browser."""
        self.driver.quit()
        print("[TEARDOWN] Browser ditutup.")
