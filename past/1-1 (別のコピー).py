#coding:utf-8


#py3.4
#変更履歴--------
#初版 ver1-1.py 
#画面１と画面２で切り替わる
#canvasは、４つ
#
#
#------------------------------------------------

#msg
msg1='1'
msg2='2'
msg3='3'
msg4='4'

msg11='1あたま' 
msg12='1おなか'
msg13='1て'
msg14='1あし'

msg21='2あたま' 
msg22='2おなか'
msg23='2て'
msg24='2あし'

msg31='3あたま' 
msg32='3おなか'
msg33='3て'
msg34='3あし'

msg41='4あたま' 
msg42='4おなか'
msg43='4て'
msg44='4あし'




#------------------------------------------------


#-------------------------------
#画面1にて選択→　画面2
#クリックで選択します
#もう一度クリックで、再度動き出します
#クリックしないと元に戻る
#------------------------------------------------------



import tkinter
import time
tk=tkinter.Tk()


#設定項目
#---------------------------------------------------------------
#キャンバスのサイズ 
CANVAS_WIDTH=250 
CANVAS_HEIGHT=250

TXT_WIDTH=300
TXT_HEIGHT=300


#------------------------------------

#1
canvas1=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
#2
canvas2=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
#3
canvas3=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
#4
canvas4=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)




# ラベル変更
class Change:
	loop=1     #ループ用 1-4

	t=3000 #time 
#	t=500

	status=1 #(1,2,3)1:画面１　2:画面２　3:画面２でストップ

	def __init__(self):
	#初期
		self.loop=1
		self.status=1
		canvas1.create_rectangle(5,5,400,400,fill='#ff0000')
		canvas1.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg1)

		canvas2.create_rectangle(5,5,400,400,fill='#ffffff')
		canvas2.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg2)

		canvas3.create_rectangle(5,5,400,400,fill='#ffffff')
		canvas3.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg3)

		canvas4.create_rectangle(5,5,400,400,fill='#ffffff')
		canvas4.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg4)


	def status1(self):
	#画面１でクリック時の処理
	#処理：loop==1 
		pass


	def status2(self):
	#画面２でクリック時の処理
	#処理：
		pass
	def status3(self):
	#画面２のストップ時の処理
	#処理：初期へ戻る
		__init__(self)


	def click(self,ev):
		pass
	#クリック時
	#画面１と画面２の場合で処理を分ける


	#画面1の場合
	#画面２へ
	#loopを1に


	#画面２の場合
	#次にクリックされるまでストップ


	
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
	#画面１の場合と画面２の場合
		pass
	#
	#loop 1-4
		if self.loop==1:
			self.canvas1('#ff0000')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			
	
		elif self.loop==2:
			self.canvas1('#ffffff')
			self.canvas2('#ff0000')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			

		elif self.loop==3:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ff0000')
			self.canvas4('#ffffff')			

		elif self.loop==4:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ff0000')			


	#loop 

		if self.loop!=4:
			self.loop +=1
		else:
			self.loop=1


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




