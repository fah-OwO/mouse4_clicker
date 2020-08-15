import time
import threading
import win32api,win32con

class autoclick(threading.Thread):
    def __init__(self,button):
        super(autoclick,self).__init__()
        self.button=button
        self.running=False
        self.program_running=True

    def start_clicking(self):
        self.running=True

    def stop_clicking(self):
        self.running=False

    def exit(self):
        self.running=False
        self.program_running=False

    def run(self):
        while self.program_running:
            while self.running:
                try:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
                    time.sleep(0.001)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
                except :
                    print('x')
                    time.sleep(5)
                
                
            time.sleep(0.1)
    

clicker=autoclick(0x01)
clicker.start()
XButton1=0x06
XButton2=0x05
ExitKey=0xC0#0x08
state_4 = win32api.GetKeyState(XButton1) 
state_5 = win32api.GetKeyState(XButton2) 
state_exit = win32api.GetKeyState(ExitKey) 

#print(win32api.GetCursorPos())
while True:
    #print('a')
    now_4 = win32api.GetKeyState(XButton1)
    now_exit = win32api.GetKeyState(ExitKey)
    now_5 = win32api.GetKeyState(XButton2) 
    if now_4 != state_4:
        state_4=now_4
        clicker.running=not clicker.running
        #print(now_4)#print(win32api.GetCursorPos())
    elif now_5!=state_5 and now_5<0:
        state_5=now_5
        clicker.running=not clicker.running
        #print('xxx')
    elif now_exit!=state_exit:
        clicker.exit()
        break
    # time.sleep(0.01)
print('exit')
time.sleep(3)
