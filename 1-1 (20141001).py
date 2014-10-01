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
#	loop=1     #ループ用 1-4

#	t=3000 #time 
	t=500

#	status=1 #(1,2,3)1:画面１　2:画面２　3:画面２でストップ

	def __init__(self):
	#初期
		self.loop=1
		self.status=1
		self.msg=[msg1,msg2,msg3,msg4]

		canvas1.create_rectangle(5,5,400,400,fill='#ff0000')
		canvas1.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=self.msg[0])

		canvas2.create_rectangle(5,5,400,400,fill='#ffffff')
		canvas2.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=self.msg[1])

		canvas3.create_rectangle(5,5,400,400,fill='#ffffff')
		canvas3.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=self.msg[2])

		canvas4.create_rectangle(5,5,400,400,fill='#ffffff')
		canvas4.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=self.msg[3])

	def change_msg(self):
		#場面に応じてのメッセージを作成	

		if self.status==1:
			if self.loop==1:
				self.msg=[msg11,msg12,msg13,msg14]
				self.loop=2
			elif self.loop==2:
				self.msg=[msg21,msg22,msg23,msg24]
				self.loop=3
			elif self.loop==3:
				self.msg=[msg31,msg32,msg33,msg34]
				self.loop=4
			elif self.loop==4:
				self.msg=[msg41,msg42,msg43,msg44]
				self.loop=1

		


	def status1(self):
	#画面１でクリック時の処理
	#処理：loop==1 
#		if self.loop==1:		
#			canvas1.create_rectangle(5,5,400,400,fill='#ff0000')
#			canvas1.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg11)
#
#			canvas2.create_rectangle(5,5,400,400,fill='#ffffff')
#			canvas2.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg12)

#			canvas3.create_rectangle(5,5,400,400,fill='#ffffff')
#			canvas3.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg13)

#			canvas4.create_rectangle(5,5,400,400,fill='#ffffff')
#			canvas4.create_text(130,130,font=(u'ＭＳ ゴシック', 60),text=msg14)

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
#		pass
		self.change_msg()

	#クリック時
	#画面１、画面２、画面３で処理を分ける
	#self.status=1 or 2 or 3

	
	#画面1の場合 self.status==1
	#画面２へ
	#	if self.status==1:
	#		self.status1()



	#画面２の場合
	#次にクリックされるまでストップ


	
	def canvas1(self,color): 
		canvas1.create_rectangle(5,5,400,400,fill=color)
		canvas1.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=self.msg[0])

	def canvas2(self,color): 
		canvas2.create_rectangle(5,5,400,400,fill=color)
		canvas2.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=self.msg[1])

	def canvas3(self,color): 
		canvas3.create_rectangle(5,5,400,400,fill=color)
		canvas3.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=self.msg[2])

	def canvas4(self,color): 
		canvas4.create_rectangle(5,5,400,400,fill=color)
		canvas4.create_text(180,130,font=(u'ＭＳ ゴシック', 100),text=self.msg[3])
	

	
	def show_time(self):
	#判定            
	#画面１の場合と画面２の場合
#		pass
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




