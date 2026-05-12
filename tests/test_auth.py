import sys
import os

# Menambahkan path root agar bisa import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.auth_helper import verifikasi_login

def test_verifikasi_login_sukses():
    """Tes login dengan data yang benar."""
    user_data = {'username': 'admin', 'password': '123'}
    assert verifikasi_login('admin', '123', user_data) == True

def test_verifikasi_login_password_salah():
    """Tes login dengan password salah."""
    user_data = {'username': 'admin', 'password': '123'}
    assert verifikasi_login('admin', 'wrong_pass', user_data) == False

def test_verifikasi_login_user_tidak_ada():
    """Tes login jika user_data None."""
    assert verifikasi_login('admin', '123', None) == False

# Instruksi Jalankan:
# pytest tests/test_auth.py
