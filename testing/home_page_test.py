from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class HomePageTest:
    def __init__(self):
        """Metode inisialisasi untuk menyiapkan WebDriver dan membuka browser."""
        print("[SETUP] Menginisialisasi Chrome WebDriver...")
        
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1:5000"
        
        # Buka halaman utama
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)

    def checkElement(self, locator_type, locator_value):
        """Memeriksa keberadaan elemen di halaman."""
        try:
            if locator_type.lower() == 'id':
                self.driver.find_element(By.ID, locator_value)
            elif locator_type.lower() == 'css':
                self.driver.find_element(By.CSS_SELECTOR, locator_value)
            
            print(f"[PASS] Elemen '{locator_value}' ({locator_type}) ditemukan.")
            return True
        except:
            print(f"[FAIL] Elemen '{locator_value}' ({locator_type}) TIDAK ditemukan.")
            return False

    def clickButtonLihatSemuaVideo(self):
        """Mengklik tombol menuju galeri video."""
        try:
            btn = self.driver.find_element(By.XPATH, "//a[contains(., 'Lihat Semua Video')]")
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
            time.sleep(1)
            btn.click()
            print("[PASS] Tombol 'Lihat Semua Video' berhasil diklik.")
            time.sleep(1)
        except Exception as e:
            print(f"[FAIL] Gagal mengklik tombol 'Lihat Semua Video'. Error: {e}")

    def closeBrowser(self):
        """Menutup browser."""
        self.driver.quit()
        print("[TEARDOWN] Browser ditutup.")


if __name__ == "__main__":
    test_home = HomePageTest()
    print("\n--- Memulai Pengujian Halaman Utama ---")
    test_home.checkElement("id", "video")
    test_home.checkElement("css", ".navbar-brand")
    test_home.clickButtonLihatSemuaVideo()
    print("--- Pengujian Selesai ---\n")
    test_home.closeBrowser()

