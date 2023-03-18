import subprocess
import re
import os
import time
import winreg
import win32api
import win32con


# 执行scrcpy.exe
def exe_scrcpy():
    adb_path = 'C:/Users/11561/Desktop/scrcpy-win64-v2.0'
    os.chdir(adb_path)
    # print(os.getcwd())
    cmd_check_devices = 'adb.exe devices'

    # 检查设备连接状态，输出信息
    output = subprocess.check_output(cmd_check_devices, shell=True).decode('utf-8')
    while True:
        devices = re.findall(r'^([\w\d]+)\s+device\s*$', output, flags=re.MULTILINE)
        if devices:
            subprocess.Popen('./scrcpy.exe')
            break
        # 没找到设备等待5s
        time.sleep(5)
    return "Running"


# 注册表开机自启动
def add_to_startup(file_path):
    key = winreg.HKEY_CURRENT_USER
    key_value = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE) as key_handle:
        winreg.SetValueEx(key_handle, "MyScript", 0, winreg.REG_SZ, file_path)


# 查找注册表中的信息
def getRegValue(handle, key):
    try:
        return win32api.RegQueryValueEx(handle, key)[0]
    except Exception as e:
        return False


def findRegeInfo(name):
    key = name
    handle = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
                                 0, win32con.KEY_ALL_ACCESS)
    # 获取注册表的值
    values = getRegValue(handle, key)
    # 判断是否返回值
    if isinstance(values, str):
        return True
    else:
        return False


# 入口函数
def entrance():
    '''
    findRegeIndo:用于查找注册表信息，是否有开机自启动信息
    add_to_startup:向注册表中写入开机启动信息
    exe_scrcpy:用于执行scrcpy
    '''
    regeditName = 'MyScript'
    filePath = 'E:\workspace\Launch_Winscrcpy\dispatcher\dist\entrance\entrance.exe'
    regExistsInfo = findRegeInfo(regeditName)
    if regExistsInfo:
        runResult = exe_scrcpy()
        if runResult == 'Running':
            exit()
    else:
        add_to_startup(filePath)
        runResult = exe_scrcpy()
        if runResult == 'Running':
            exit()


if __name__ == '__main__':
    entrance()