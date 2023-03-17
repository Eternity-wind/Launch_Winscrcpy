import win32api
import win32con


# 获取注册表值 不存在返回False
def getRegValue(handle, key):
    try:
        return win32api.RegQueryValueEx(handle, key)[0]
    except Exception as e:
        return False


key = 'Nextcloud'
handle = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
                               0, win32con.KEY_ALL_ACCESS)
# 获取注册表的值
values = getRegValue(handle, key)
print(values)
