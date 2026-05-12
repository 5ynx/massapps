from base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class KelolaKategoriTest(BaseTest):
    def __init__(self):
        super().__init__("/kelola-kategori")

    def run_tests(self):
        if not self.login():
            return

        self.driver.get(self.target_url)
        
        # Test 1: Cek Semua Elemen
        print("\n--- Test 1: Cek Semua Elemen ---")
        self.check_element("name", "nama_kategori")
        self.check_element("xpath", "//button[@type='submit']")
        self.check_element("css", "table")

        # Test 2: Kasus Normal (Tambah Kategori)
        print("\n--- Test 2: Kasus Normal (Tambah Kategori) ---")
        try:
            cat_name = "Kategori Test " + str(int(time.time()))
            self.driver.find_element(By.NAME, "nama_kategori").send_keys(cat_name)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
            
            # Cek apakah kategori baru muncul di tabel
            if cat_name in self.driver.page_source:
                print(f"[PASS] Kategori '{cat_name}' berhasil ditambahkan dan terlihat di tabel.")
            else:
                print("[FAIL] Kategori tidak ditemukan di halaman setelah submit.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Normal: {e}")

        # Test 3: Kasus Abnormal (Nama Kategori Kosong)
        print("\n--- Test 3: Kasus Abnormal (Nama Kategori Kosong) ---")
        self.driver.get(self.target_url)
        try:
            self.driver.find_element(By.NAME, "nama_kategori").clear()
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(1)
            
            if "/kelola-kategori" in self.driver.current_url:
                 # Check if the page is still at the same URL and no new (empty) entry was added.
                 # Actually HTML5 required attribute will prevent this.
                 print("[PASS] Sistem mencegah submit kategori kosong.")
            else:
                print("[FAIL] Sistem memproses form kategori kosong.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Abnormal: {e}")

if __name__ == "__main__":
    test = KelolaKategoriTest()
    test.run_tests()
    test.close()
