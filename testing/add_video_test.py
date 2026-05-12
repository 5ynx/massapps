from base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class AddVideoTest(BaseTest):
    def __init__(self):
        super().__init__("/add-video")

    def run_tests(self):
        if not self.login():
            return

        self.driver.get(self.target_url)
        
        # Test 1: Cek Semua Elemen
        print("\n--- Test 1: Cek Semua Elemen ---")
        self.check_element("name", "judul")
        self.check_element("name", "youtube_id")
        self.check_element("name", "keterangan")
        self.check_element("xpath", "//button[@type='submit']")

        # Test 2: Kasus Normal (Tambah Video)
        print("\n--- Test 2: Kasus Normal (Tambah Video) ---")
        try:
            video_title = "Video Test " + str(int(time.time()))
            self.driver.find_element(By.NAME, "judul").send_keys(video_title)
            self.driver.find_element(By.NAME, "youtube_id").send_keys("dQw4w9WgXcQ") # Rickroll ID
            self.driver.find_element(By.NAME, "keterangan").send_keys("Deskripsi video testing.")
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
            
            if "kelola-video" in self.driver.current_url.lower():
                print("[PASS] Video baru berhasil ditambahkan.")
            else:
                print("[FAIL] Gagal menambahkan video atau tidak dialihkan ke kelola-video.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Normal: {e}")

        # Test 3: Kasus Abnormal (YouTube ID Kosong)
        print("\n--- Test 3: Kasus Abnormal (YouTube ID Kosong) ---")
        self.driver.get(self.target_url)
        try:
            self.driver.find_element(By.NAME, "youtube_id").clear()
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(1)
            
            if "add-video" in self.driver.current_url:
                print("[PASS] Sistem mencegah submit video tanpa ID YouTube.")
            else:
                print("[FAIL] Sistem memproses form meskipun ID YouTube kosong.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Abnormal: {e}")

if __name__ == "__main__":
    test = AddVideoTest()
    test.run_tests()
    test.close()
