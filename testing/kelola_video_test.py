from base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class KelolaVideoTest(BaseTest):
    def __init__(self):
        super().__init__("/kelola-video")

    def run_tests(self):
        if not self.login():
            return

        self.driver.get(self.target_url)
        
        # Test 1: Cek Semua Elemen
        print("\n--- Test 1: Cek Semua Elemen ---")
        self.check_element("xpath", "//a[contains(., 'Tambah Video')]")
        self.check_element("css", "table")
        self.check_element("css", "th")

        # Test 2: Kasus Normal (Navigasi ke Tambah Video)
        print("\n--- Test 2: Kasus Normal (Navigasi ke Tambah Video) ---")
        try:
            self.driver.find_element(By.XPATH, "//a[contains(., 'Tambah Video')]").click()
            time.sleep(1)
            if "add-video" in self.driver.current_url:
                print("[PASS] Navigasi ke halaman Tambah Video berhasil.")
            else:
                print("[FAIL] Gagal navigasi ke halaman Tambah Video.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Normal: {e}")

        # Test 3: Kasus Abnormal (Verifikasi Keberadaan Tabel)
        # Untuk halaman list, kita cek jika tabel ada meskipun data mungkin kosong
        print("\n--- Test 3: Kasus Abnormal (Cek Tabel) ---")
        self.driver.get(self.target_url)
        try:
            table = self.driver.find_element(By.CSS_SELECTOR, "table")
            if table.is_displayed():
                print("[PASS] Tabel Manajemen Video ditampilkan dengan benar.")
            else:
                print("[FAIL] Tabel Manajemen Video tidak terlihat.")
        except Exception as e:
            print(f"[FAIL] Elemen tabel tidak ditemukan: {e}")

if __name__ == "__main__":
    test = KelolaVideoTest()
    test.run_tests()
    test.close()
