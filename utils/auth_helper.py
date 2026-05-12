# utils/auth_helper.py

def verifikasi_login(username, password, user_data):
    """
    Memverifikasi apakah input username dan password cocok dengan data dari database.
    user_data adalah hasil fetchone() dari tabel users.
    """
    if user_data:
# - hashingg
        if username == user_data['username'] and password == user_data['password']:
            return True
    return False