import win32api
import win32con


key = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
                            0, win32con.KEY_SET_VALUE)
print(key)