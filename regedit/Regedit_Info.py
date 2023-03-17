import winreg


def add_to_startup(file_path):
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE) as key_handle:
        winreg.SetValueEx(key_handle, "MyScript", 0, winreg.REG_SZ, file_path)
