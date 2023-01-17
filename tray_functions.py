import threading
import pystray
from PIL import Image
from pystray import MenuItem, Menu
import json


class createTray():
    def __init__(self, start_callback, stop_callback):
        self.json_data = None
        with open('language.json', 'r', encoding='utf8') as fp:
            self.json_data = json.load(fp)  # 获取当前语言
        self.start_callback = start_callback
        self.stop_callback = stop_callback
        #self.menu = (Menu.SEPARATOR, MenuItem('退出', self.stop))
        self.menu = Menu(
            MenuItem(
                lambda text: self.json_data[self.json_data['language']]['menu_language'],   # 使用 icon.update_menu() 动态改变菜单的方法
                Menu(
                    MenuItem(
                        '简体中文',
                        lambda icon, item: self.set_language('简体中文')
                    ),
                    MenuItem(
                        'English',
                        lambda icon, item: self.set_language('English')
                    )
                )
            ),
            MenuItem(
                lambda text: self.json_data[self.json_data['language']]['menu_exit'],
                lambda icon, item: self.stop()
            )
        )
        self.program_icon = Image.open("static/icon.png")
        self.icon = pystray.Icon("icon", self.program_icon, self.json_data[self.json_data['language']]['tray_hint'], self.menu)
    
    def start(self):
        if(self.start_callback != None):
            self.start_callback()
        threading.Thread(target=self.icon.run, daemon=True).start()

    def stop(self):
        if(self.stop_callback != None):
            # print("stop callback")
            self.stop_callback()
        self.icon.stop()
    
    def get_pystray_icon(self):
        return self.icon
    
    def set_language(self, language):
        self.json_data['language'] = language
        json_string = json.dumps(self.json_data, ensure_ascii=False)
        with open('language.json', 'w', encoding='utf8') as fp:
            fp.write(json_string)
        self.icon.update_menu()     # 更新菜单
        self.icon.title = self.json_data[self.json_data['language']]['tray_hint']   # 更新托盘程序的 title（鼠标悬浮时显示的）
        
        