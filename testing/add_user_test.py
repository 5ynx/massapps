from base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class AddUserTest(BaseTest):
    def __init__(self):
        super().__init__("/add-user")

    def run_tests(self):
        if not self.login():
            return

        self.driver.get(self.target_url)
        
        # Test 1: Cek Semua Elemen
        print("\n--- Test 1: Cek Semua Elemen ---")
        self.check_element("id", "username")
        self.check_element("id", "nama_lengkap")
        self.check_element("id", "role")
        self.check_element("id", "password")
        self.check_element("xpath", "//button[@type='submit']")

        # Test 2: Kasus Normal (Tambah User)
        print("\n--- Test 2: Kasus Normal (Tambah User) ---")
        try:
            self.driver.find_element(By.ID, "username").send_keys("user_test_" + str(int(time.time())))
            self.driver.find_element(By.ID, "nama_lengkap").send_keys("Selenium User")
            self.driver.find_element(By.ID, "password").send_keys("password123")
            
            role_select = self.driver.find_element(By.ID, "role")
            role_select.find_element(By.XPATH, "//option[@value='mahasiswa']").click()

            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
            
            if "kelola-user" in self.driver.current_url.lower():
                print("[PASS] User baru berhasil ditambahkan.")
            else:
                print("[FAIL] Gagal menambahkan user atau tidak dialihkan ke kelola-user.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Normal: {e}")

        # Test 3: Kasus Abnormal (Username Kosong)
        print("\n--- Test 3: Kasus Abnormal (Username Kosong) ---")
        self.driver.get(self.target_url)
        try:
            self.driver.find_element(By.ID, "username").clear()
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(1)
            
            if "add-user" in self.driver.current_url:
                print("[PASS] Sistem mencegah submit form tanpa username.")
            else:
                print("[FAIL] Sistem memproses form meskipun username kosong.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Abnormal: {e}")

if __name__ == "__main__":
    test = AddUserTest()
    test.run_tests()
    test.close()
