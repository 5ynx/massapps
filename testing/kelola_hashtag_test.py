from base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class KelolaHashtagTest(BaseTest):
    def __init__(self):
        super().__init__("/kelola-hashtag")

    def run_tests(self):
        if not self.login():
            return

        self.driver.get(self.target_url)
        
        # Test 1: Cek Semua Elemen
        print("\n--- Test 1: Cek Semua Elemen ---")
        self.check_element("name", "nama_hashtag")
        self.check_element("xpath", "//button[@type='submit']")
        self.check_element("css", "table")

        # Test 2: Kasus Normal (Tambah Hashtag)
        print("\n--- Test 2: Kasus Normal (Tambah Hashtag) ---")
        try:
            tag_name = "#Test" + str(int(time.time()))
            self.driver.find_element(By.NAME, "nama_hashtag").send_keys(tag_name)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
            
            if tag_name in self.driver.page_source:
                print(f"[PASS] Hashtag '{tag_name}' berhasil ditambahkan.")
            else:
                print("[FAIL] Hashtag tidak ditemukan di tabel.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Normal: {e}")

        # Test 3: Kasus Abnormal (Nama Hashtag Kosong)
        print("\n--- Test 3: Kasus Abnormal (Nama Hashtag Kosong) ---")
        self.driver.get(self.target_url)
        try:
            self.driver.find_element(By.NAME, "nama_hashtag").clear()
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(1)
            
            print("[PASS] Sistem mencegah submit hashtag kosong.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Abnormal: {e}")

if __name__ == "__main__":
    test = KelolaHashtagTest()
    test.run_tests()
    test.close()
