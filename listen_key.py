from pynput import keyboard


F7 = keyboard.Key.f7
F8 = keyboard.Key.f8

class createKeyLinster():
    def __init__(self):
        self.listen_key_list = []       # 监听的按键列表
        self.listen_function_list = []  # 监听的按键列表对应的回调，[short_press, long_press]
        self.listen_flag_list = []      # 标识按键状态  0 未按下 1 按下 2 长按
        self.listen_key_nblock()
    
    def on_press(self, key):
        """定义按下时候的响应，参数传入key"""
        if key in self.listen_key_list:
            index = self.listen_key_list.index(key)
            if(self.listen_flag_list[index] == 0):
                self.listen_flag_list[index] = 1
            elif(self.listen_flag_list[index] == 1):
                self.listen_flag_list[index] = 2    
            if(self.listen_flag_list[index] == 2):      # 长按
                self.listen_function_list[index][1](key)
            
    def on_release(self, key):
        """定义释放时候的响应"""
        if key in self.listen_key_list:
            index = self.listen_key_list.index(key)
            if(self.listen_flag_list[index] == 1):
                self.listen_function_list[index][0](key)
            self.listen_flag_list[index] = 0

    # 监听写法1
    #def listen_key_block(self):
    #    with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
    #        listener.join()  # 加入线程池，阻塞写法
    
    # 监听写法2
    def listen_key_nblock(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()  # 启动线程
    
    def add_to_listen_list(self, listen_key, short_cb, long_cb):
        """ 监听的键、短按回调、长按回调"""
        if listen_key != None and short_cb != None and long_cb != None:
            self.listen_key_list.append(listen_key)
            self.listen_flag_list.append(0)
            self.listen_function_list.append([short_cb, long_cb])
            return True
        else:
            return False
    
    def remove_from_listen_list(self, listen_key):
        """ listen_key 是一个列表，包含监听的键、短按回调、长按回调"""
        if listen_key != None and listen_key in listen_key_list:
            index = self.listen_key_list.index(listen_key)
            del self.listen_key_list[index]
            del self.listen_flag_list[index]
            del self.listen_function_list[index]
            return True
        else:
            return False
        
#def pts(key):
#    print("pts:" + str(key))
#
#def ptl(key):
#    print("ptl:" + str(key))
# 
#if __name__ == '__main__':
#    listener = createKeyLinster()
#    if listener.add_to_listen_list(F7, pts, ptl):
#        print("add F7")
#    if listener.add_to_listen_list(F8, pts, ptl):
#        print("add F8")
#    while True: # 这里应该用一个循环维持主线程，否则主线程结束了子线程就自动结束了
#        pass