from tray_functions import createTray
from create_window_ctl_bright import CreateBrightnessCtrlWindow
from listen_key import createKeyLinster, F7, F8
import time

def minus_scale_1(key):
    global ctl
    val = int(ctl.get_scale_value() - 1)
    if val < 0:
        val = 0
    ctl.set_scale_value(val)

def plus_scale_1(key):
    global ctl
    val = int(ctl.get_scale_value() + 1)
    if val > 100:
        val = 100
    ctl.set_scale_value(val)

def show_window(key):
    global ctl
    ctl.show_window()

def quit_window(key):
    global ctl
    ctl.quit_window()


# 创建一个主窗口对象
ctl = CreateBrightnessCtrlWindow()

# 创建一个托盘
tray = createTray(ctl.quit_window, ctl.on_exit)
tray.start()

# 创建快捷键映射
listener = createKeyLinster()
if listener.add_to_listen_list(F7, minus_scale_1, show_window):
    print("add F7")
if listener.add_to_listen_list(F8, plus_scale_1, quit_window):
    print("add F8") 


# 运行主窗口
ctl.display_window()