from win32api import *
from win32com import *
from win32con import *
from win32gui import *
from win32process import *
from ctypes import *

_window_name = "GitKraken"
_sun_address = 0x293D7650
_sun_number = 10000

if __name__ == '__main__':
    window_handle = FindWindow(None, _window_name)  # 获得窗口句柄
    process_id = GetWindowThreadProcessId(window_handle)[1]  # 获得进程ID
    process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, process_id) # 获得进程句柄

    kernel32 = windll.LoadLibrary("kernel32.dll")
    kernel32.WriteProcessMemroy(int(process_handle), _sun_address, byref(c_int(_sun_number)), 4, byref(c_int(0)))
