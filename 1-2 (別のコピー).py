#coding:utf-8


#py3.4
#変更履歴--------
#初版 ver1-1.py 

#仕様
#
#
#canvasは、４つ
#
#status1
#-最初の画面　１　２
#　　　　　　      ３  ４
#-ここでクリックすると
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
CANVAS_WIDTH=350 
CANVAS_HEIGHT=300

TXT_SIZE=130
#TXT_HEIGHT=300


#------------------------------------

canvas1=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas2=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas3=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas4=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)


# ラベル変更
class Change:
	msg_number=0     #どのメッセージを表示するか 1-4 
#	t=3000 #time 
	t=500
	status=1 #(1,2,3)1:画面１　2:画面２　3:画面２でストップ

	def __init__(self):
	#初期
		self.nsg_number=0
		self.status=1
		self.change_msg()
	#	self.status=2

	def change_msg(self):
		#場面に応じてのメッセージを作成	

		if self.status==1:
			self.msg=[msg1,msg2,msg3,msg4]
			self.status=2

		elif self.status==2:
			if self.msg_number==0:
				self.msg=[msg11,msg12,msg13,msg14]
			elif self.msg_number==1:
				self.msg=[msg21,msg22,msg23,msg24]
			elif self.msg_number==2:
				self.msg=[msg31,msg32,msg33,msg34]
			elif self.msg_number==3:
				self.msg=[msg41,msg42,msg43,msg44]
		elif self.status==3:
			print ("st3")
 			#loop stop and clear
		#loop 1-4
			if self.msg_number==0:
				self.canvas1('#ff0000')
		#	self.canvas2('#ffffff')
		#	self.canvas3('#ffffff')
		#	self.canvas4('#ffffff')			
				canvas2.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas3.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas4.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")

			elif self.msg_number==1:
		#	self.canvas1('#ffffff')
				self.canvas2('#ff0000')
				canvas1.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas3.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas4.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")

	#	self.canvas3('#ffffff')
		#	self.canvas4('#ffffff')			

			elif self.msg_number==2:
		#	self.canvas1('#ffffff')
		#	self.canvas2('#ffffff')
				self.canvas3('#ff0000')
		#	self.canvas4('#ffffff')			
				canvas1.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas2.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas4.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")


			elif self.msg_number==3:
		#	self.canvas1('#ffffff')
		#	self.canvas2('#ffffff')
		#	self.canvas3('#ffffff')
				self.canvas4('#ff0000')			
				canvas1.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas2.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")
				canvas4.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text="")


			self.msg_number=5

		elif self.status==4:
			self.msg=[msg1,msg2,msg3,msg4]



	def click(self,ev):
		self.change_msg()
		print ("loop")
		print (self.msg_number)
		print ("status")
		print (self.status)
	
	#status change
		if self.status==1:
			self.status=2
		elif self.status==2:
			self.status=3
		elif self.status==3:
			self.status=4
		elif self.status==4:
			self.status=1

		if self.msg_number==5:
			self.msg_number=0
	
	
	def canvas1(self,color): 
		canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas1.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text=self.msg[0])

	def canvas2(self,color): 
		canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas2.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text=self.msg[1])

	def canvas3(self,color): 
		canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas3.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text=self.msg[2])

	def canvas4(self,color): 
		canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas4.create_text(TXT_SIZE,TXT_SIZE,font=(u'ＭＳ ゴシック', 100),text=self.msg[3])
	

	
	def show_time(self):
	#判定            
	#画面１の場合と画面２の場合
#		pass
		if self.msg_number!=3:
			self.msg_number +=1
		else:
			self.mag_number=0


	#loop 1-4
		if self.msg_number==0:
			self.canvas1('#ff0000')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			
	
		elif self.msg_number==1:
			self.canvas1('#ffffff')
			self.canvas2('#ff0000')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			

		elif self.msg_number==2:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ff0000')
			self.canvas4('#ffffff')			

		elif self.msg_number==3:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ff0000')			


##        #タイマー
		if self.msg_number!=5:
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




