# フルスクリーン状態を解除するときは
# (Ubuntu) : Alt+F1 -> Enterで適当なアプリ開くなりして横のタブを出さないと操作を受け付けないから気を付けて
# (Windows): 二画面とかでタブバーからアプリ落とすしかない（確認した限りでは）

# そもそもフルスクうざいってことなら26行目コメントアウトして

import os, sys, time
import tkinter as tk
from datetime import datetime

abst = datetime(2019,1,17,17,0,0)
repo = datetime(2019,1,29,17,0,0)

m_ab = datetime(2019,2,1,17,0,0)
m_re = datetime(2019,2,14,15,0,0)

w = 1920
h = 1080

fsize = 85

bc = '#000000'
fc = "#ff0000"

root = tk.Tk()
#root.attributes("-fullscreen",True)
root.title("DeadLine")
root.geometry(str("{}x{}".format(w,h)))
canvas = tk.Canvas(root,width=w,height=h)
canvas.configure(background=bc)
canvas.pack()

while(True):
    canvas.delete('all')
    deadline_abst = abst - datetime.now()
    deadline_repo = repo - datetime.now()
    deadline_m_ab = m_ab - datetime.now()
    deadline_m_re = m_re - datetime.now()
    canvas.create_text(50,h/2-(fsize + 250), text = "Bachelor", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(200,h/2-(fsize + 150), text = "Abstract", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(200,h/2-(fsize + 50), text = "F_Report", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(700,h/2-(fsize + 150), text = ":", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(700,h/2-(fsize + 50), text = ":", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(w-50,h/2-(fsize + 150), text = str(deadline_abst)[:-3], font = ('bitstream charter', fsize), fill = fc, anchor = "e")
    canvas.create_text(w-50,h/2-(fsize + 50), text = str(deadline_repo)[:-3], font = ('bitstream charter', fsize), fill = fc, anchor = "e")
    canvas.create_text(50,h/2+(fsize + 50), text = "Master", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(200,h/2+(fsize + 150), text = "Abstract", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(200,h/2+(fsize + 250), text = "F_Report", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(700,h/2+(fsize + 150), text = ":", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(700,h/2+(fsize + 250), text = ":", font = ('bitstream charter', fsize), fill = fc, anchor = "w")
    canvas.create_text(w-50,h/2+(fsize + 150), text = str(deadline_m_ab)[:-3], font = ('bitstream charter', fsize), fill = fc, anchor = "e")
    canvas.create_text(w-50,h/2+(fsize + 250), text = str(deadline_m_re)[:-3], font = ('bitstream charter', fsize), fill = fc, anchor = "e")
    root.update()
    
root.mainloop()
