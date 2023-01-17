import tkinter as tk
from tkinter import ttk     # tkinter 官方的拓展，界面更漂亮
import sv_ttk               # ttk 的一个主题
from PIL import Image, ImageTk
import screen_brightness_control as sbc 
import darkdetect           # 获取系统亮暗

class CreateBrightnessCtrlWindow:
    def __init__(self):
        # 创建一个主窗口对象
        self.window = tk.Tk()
        self.window.title("亮度修改")
        self.window.resizable(False, False)
        self.window.attributes("-topmost", 1)                   # 置顶
        self.window.attributes('-alpha', 0.9)                   # 不透明度
        self.screen_width = self.window.winfo_screenwidth()     # 获取屏幕宽度
        self.screen_height = self.window.winfo_screenheight()   # 获取屏幕高度
        self.window.geometry(str(int(0.2*self.screen_width)) 
            + "x" 
            + str(int(0.08*self.screen_height)) 
            + "+" 
            + str(int(0.75*self.screen_width)) 
            + "+" 
            + str(int(0.86*self.screen_height)))
        
        self.bright_value = tk.StringVar()  # 创建可绑定的变量，需要在 window 创建之后
        
        # 放置 lable
        file = 'static/sun.png'
        img = Image.open(file)
        img_size = int(0.03*self.screen_height)
        self.sun_icon = ImageTk.PhotoImage(img.resize((img_size, img_size)))             # 使用 PIL 库调整图片大小
        lab = ttk.Label(self.window, image=self.sun_icon, width=int(0.01*self.screen_height))
        lab.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
        
        # 放置滑块
        self.scale = ttk.Scale(self.window, 
            from_=1,                             # 范围
            to=100, 
            orient=tk.HORIZONTAL,                # 水平显示
            length=int(0.10*self.screen_width),  # 长度
            command=self.select_price)           # 调用执行函数，是数值显示在 Lable 控件中
        self.scale.set(sbc.get_brightness()[0])  # 设置初始值
        self.scale.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # 组件居中
        
        if darkdetect.isDark():
            sv_ttk.set_theme("dark")             # 使用 Sun-Valley-ttk-theme 风格
        else:
            sv_ttk.set_theme("light")
        self.window.overrideredirect(True)       # 删除顶栏及边框
        self.window_flag = True                  # 记录 Window 状态
        
        # 放置数值显示
        self.label_value = ttk.Label(text=str(sbc.get_brightness()[0]), 
            font=('Times New Roman', int(0.015*self.screen_height), ''), 
            textvariable=self.bright_value)      # 绑定变量
        self.label_value.place(relx=0.85, rely=0.5, anchor=tk.CENTER)
        
    def select_price(self, value):
        sbc.set_brightness(int(float(value)))
        self.bright_value.set(str(int(float(value))) + "%")
    
    def get_scale_value(self):
        return self.scale.get()
    
    def set_scale_value(self, value):
        self.scale.set(value)
    
    def get_window(self):
        return self.window
        
    def display_window(self):
        self.window_flag = True
        self.window.mainloop()
    
    def quit_window(self):
        self.window_flag = False
        self.window.withdraw()

    def show_window(self):
        self.window_flag = True
        self.window.deiconify()

    def toggle_window(self):
        if(self.window_flag):
            self.quit_window()
        else:
            self.show_window()

    def on_exit(self):
        self.window.destroy()