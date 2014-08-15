#coding:utf-8

#py3.4
#変更履歴--------
#初版 ver1-1 #2014/06/03
#ver1-2 2014/06/04
#画像のサイズと位置の変更

#ver1-3 2014/06/20





#------------------------------------------------
#






#------------------------------------------------








#-------------------------------
#写真が４つ現れる
#クリックで選択
#もう一度クリックで動く

#注意
#写真はpng形式で 200x200 ｐｘぐらいで

#名前は、1.png 2.png 3.png 4.png

#------------------------------------------------------

#

import tkinter
import time
tk=tkinter.Tk()


#設定項目


#---------------------------------------------------------------
#キャンバスのサイズ 
CANVAS_WIDTH=350 
CANVAS_HEIGHT=250
#msg
msg1='11111111'
msg2='22222222222'
msg3='333333333'
msg4='444444444'

#
#SCAN_TIME=


#------------------------------------


#1
canvas1=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas1.create_rectangle(5,5,400,400,fill='#ff0000')
canvas1.create_text(180,130,font=100,text=msg1)



#2
canvas2=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas2.create_rectangle(5,5,400,400,fill='#ffffff')
canvas2.create_text(180,130,text=msg2)

#3
canvas3=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas3.create_rectangle(5,5,400,400,fill='#ffffff')
canvas3.create_text(180,130,text=msg3)

#4
canvas4=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas4.create_rectangle(5,5,400,400,fill='#ffffff')
canvas4.create_text(180,130,text=msg4)



# ラベル変更
class Change:
	i=1     #ループ用
#	t=3000 #time 
	t=500
	flg=0 #stopのフラグ

	def click(self,ev):
		if self.flg==0:
			self.flg=1
		else:
			self.flg=0
			      			
   
	
	def show_time(self):
	#判定            
		if self.i==1 and self.flg==0:
			self.i+=1
			canvas1.create_rectangle(5,5,400,400,fill='#ff0000')
			canvas1.create_text(180,130,font=500,text=msg1)
			canvas4.create_rectangle(5,5,400,400,fill='#ffffff')
			canvas4.create_text(180,130,text=msg4)
		elif self.i==2 and self.flg==0:      	
			self.i+=1
			canvas2.create_rectangle(5,5,400,400,fill='#ff0000')
			canvas2.create_text(180,130,font=500,text=msg2)
			canvas1.create_rectangle(5,5,400,400,fill='#ffffff')
			canvas1.create_text(180,130,text=msg1)

		elif self.i==3 and self.flg==0:
			self.i+=1
			canvas3.create_rectangle(5,5,400,400,fill='#ff0000')
			canvas3.create_text(180,130,font=500,text=msg3)
			canvas2.create_rectangle(5,5,400,400,fill='#ffffff')
			canvas2.create_text(180,130,text=msg2)

		elif self.i==4 and self.flg==0:
			self.i=1
			canvas4.create_rectangle(5,5,400,400,fill='#ff0000')
			canvas4.create_text(180,130,font=500,text=msg4)
			canvas3.create_rectangle(5,5,400,400,fill='#ffffff')
			canvas3.create_text(180,130,text=msg3)


##        #タイマー
		tk.after(self.t,self.show_time)    
		#print ("tes")
		#print (self.i)

c=Change()
c.show_time()

#クリックにて反応
tk.bind('<Button>',c.click)


canvas1.grid(row=0,column=0)
canvas2.grid(row=0,column=1)
canvas3.grid(row=1,column=0)
canvas4.grid(row=1,column=1)

tk.mainloop()


