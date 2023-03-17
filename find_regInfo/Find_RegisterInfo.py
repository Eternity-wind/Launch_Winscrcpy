import winreg


def find_ResInfo():
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE) as key_handle:
        value, reg_type = winreg.QueryValueEx(key_handle, "Nextcloud")
        print(value)
        print(reg_type)


def main():
    find_ResInfo()


if __name__ == '__main__':
    main()
