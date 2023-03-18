import subprocess
import re
import os
import time


def exe_scrcpy():
    adb_path = '../scrcpy-win64-v2.0'
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
        # 等待5s
        time.sleep(5)
    return "Running"

def main():
        exe_scrcpy()

if __name__ == '__main__':
    main()
