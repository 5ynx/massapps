from base_test import BaseTest
from selenium.webdriver.common.by import By
import time
import os

class AddDataTest(BaseTest):
    def __init__(self):
        super().__init__("/add-data")

    def run_tests(self):
        if not self.login():
            return

        self.driver.get(self.target_url)
        
        # Test 1: Cek Semua Elemen
        print("\n--- Test 1: Cek Semua Elemen ---")
        self.check_element("id", "judul")
        self.check_element("id", "penulis")
        self.check_element("id", "konten")
        self.check_element("name", "gambar")
        self.check_element("name", "id_kategori")
        self.check_element("xpath", "//button[@type='submit']")

        # Test 2: Kasus Normal (Tambah Berita)
        print("\n--- Test 2: Kasus Normal (Tambah Berita) ---")
        try:
            self.driver.find_element(By.ID, "judul").send_keys("Berita Testing Selenium")
            self.driver.find_element(By.ID, "penulis").send_keys("Bot Tester")
            self.driver.find_element(By.ID, "konten").send_keys("Ini adalah konten berita yang dibuat secara otomatis oleh Selenium.")
            
            # Pilih kategori pertama yang tersedia
            category_select = self.driver.find_element(By.NAME, "id_kategori")
            options = category_select.find_elements(By.TAG_NAME, "option")
            if len(options) > 1:
                options[1].click() # Indeks 0 biasanya placeholder "-- Pilih Kategori --"

            # Scroll ke bawah agar tombol terlihat dan tidak terhalang footer
            submit_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
            time.sleep(1)
            
            try:
                submit_btn.click()
            except:
                # Jika masih gagal (terhalang element lain), gunakan JS Click
                self.driver.execute_script("arguments[0].click();", submit_btn)
            
            time.sleep(2)
            
            if "dashboard" in self.driver.current_url.lower():
                print("[PASS] Berita berhasil ditambahkan.")
            else:
                print("[FAIL] Gagal menambahkan berita atau tidak dialihkan ke dashboard.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Normal: {e}")

        # Test 3: Kasus Abnormal (Input Kosong)
        print("\n--- Test 3: Kasus Abnormal (Input Kosong) ---")
        self.driver.get(self.target_url)
        try:
            # Kosongkan judul dan submit
            self.driver.find_element(By.ID, "judul").clear()
            # Scroll ke bawah agar tombol terlihat
            submit_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
            time.sleep(1)
            
            try:
                submit_btn.click()
            except:
                self.driver.execute_script("arguments[0].click();", submit_btn)
            
            time.sleep(1)
            
            # Jika HTML menggunakan attribute 'required', form tidak akan tersubmit
            # Kita cek apakah masih di halaman yang sama
            if "add-data" in self.driver.current_url:
                print("[PASS] Sistem mencegah submit form kosong (HTML5 Required).")
            else:
                print("[FAIL] Sistem memproses form meskipun input wajib kosong.")
        except Exception as e:
            print(f"[FAIL] Error pada Kasus Abnormal: {e}")

if __name__ == "__main__":
    test = AddDataTest()
    test.run_tests()
    test.close()
