#coding:utf-8

#3-1.py

#py3.4
#変更履歴--------
#初版 ver1-2#2014/07/02
#2-1.py 2014/07/09
#ストップ時に他の色を消す
#2-2.py 2014/08/01
#

#------------------------------------------------
#画面を４分割
#以下に文字を入力
#'文字' と'' の間に文字を入れて下さい

#msg
msg1='あたま'
msg2='おなか'
msg3='て'
msg4='あし'


#------------------------------------------------


#-------------------------------
#文字が４つ現れます
#クリックで選択します
#もう一度クリックで、再度動き出します
#------------------------------------------------------



import tkinter
import time
tk=tkinter.Tk()


#設定項目
#---------------------------------------------------------------
#キャンバスのサイズ 
CANVAS_WIDTH=350 
CANVAS_HEIGHT=250

#
#SCAN_TIME=

#------------------------------------


#1
canvas1=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas1.create_rectangle(5,5,400,400,fill='#ff0000')
canvas1.create_text(180,130,font=(u'ＭＳ ゴシック', 60),text=msg1)

#2
canvas2=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas2.create_rectangle(5,5,400,400,fill='#ffffff')
canvas2.create_text(180,130,font=(u'ＭＳ ゴシック', 60),text=msg2)

#3
canvas3=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas3.create_rectangle(5,5,400,400,fill='#ffffff')
canvas3.create_text(180,130,font=(u'ＭＳ ゴシック', 60),text=msg3)

#4
canvas4=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas4.create_rectangle(5,5,400,400,fill='#ffffff')
canvas4.create_text(180,130,font=(u'ＭＳ ゴシック', 60),text=msg4)



# ラベル変更
class Change:
	i=1     #ループ用
	t=3000 #time 
#	t=500
	flg=0 #stopのフラグ

	def click(self,ev):
		if self.flg==0:
			self.flg=1
			#選択以外の文字を消す
			if self.i==1:				
				canvas1.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas2.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas3.create_rectangle(5,5,400,400,fill='#ffffff')				
			elif self.i==2:				
				canvas2.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas3.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas4.create_rectangle(5,5,400,400,fill='#ffffff')				
			elif self.i==3:				
				canvas1.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas3.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas4.create_rectangle(5,5,400,400,fill='#ffffff')				
			elif self.i==4:				
				canvas1.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas2.create_rectangle(5,5,400,400,fill='#ffffff')				
				canvas4.create_rectangle(5,5,400,400,fill='#ffffff')				

		else:
			self.flg=0
			      			
	def canvas1(self,color): 
		canvas1.create_rectangle(5,5,400,400,fill=color)
		canvas1.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=msg1)

	def canvas2(self,color): 
		canvas2.create_rectangle(5,5,400,400,fill=color)
		canvas2.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=msg2)

	def canvas3(self,color): 
		canvas3.create_rectangle(5,5,400,400,fill=color)
		canvas3.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=msg3)

	def canvas4(self,color): 
		canvas4.create_rectangle(5,5,400,400,fill=color)
		canvas4.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=msg4)
	
	def show_time(self):
	#判定            
		if self.i==1 and self.flg==0:
			self.i+=1

			self.canvas1('#ff0000')
			self.canvas4('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')			

		elif self.i==2 and self.flg==0:      	
			self.i+=1
			self.canvas2('#ff0000')
			self.canvas1('#ffffff')
			self.canvas4('#ffffff')
			self.canvas3('#ffffff')	

		elif self.i==3 and self.flg==0:
			self.i+=1
			
			self.canvas3('#ff0000')
			self.canvas2('#ffffff')
			self.canvas1('#ffffff')
			self.canvas4('#ffffff')	

		elif self.i==4 and self.flg==0:
			self.i=1

			self.canvas4('#ff0000')
			self.canvas3('#ffffff')
			self.canvas2('#ffffff')
			self.canvas1('#ffffff')	

##        #タイマー
		tk.after(self.t,self.show_time)    

c=Change()
c.show_time()

#クリックにて反応
tk.bind('<Button>',c.click)

canvas1.grid(row=0,column=0)
canvas2.grid(row=0,column=1)
canvas3.grid(row=1,column=0)
canvas4.grid(row=1,column=1)

tk.mainloop()




