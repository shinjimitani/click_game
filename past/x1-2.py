#coding:utf-8


#py3.4
#変更履歴--------
#初版 ver1-1.py 

#仕様
#
##############
##[status1]
##画面と動作
##　１　２
##  ３  ４  
##１ー４が色が変化。スキャン 
#(#msg_number)が変化
##
#クリック時
#メッセージが変更
#statusの変更　1->2
#################
##[status2]
###画面と動作
##　１　２
##  ３  ４ 
##メッセージの中身はmsg11-14,msg21-24,msg31-34,msg41-44
##１ー４が色が変化。スキャン 
#(#msg_number)が変化
#-クリック時
#ストップ
#他のメッセージも消える
##statusの変更　2->3
########################
#[status3]
###画面と動作
##　１　-
##  -   -
##止まったまま
#クリック時
#最初に戻る
##statusの変更　3->1
#------------------------------------------------

#msg
msg1='1'
msg2='2'
msg3='3'
msg4='4'

msg11='11あたま' 
msg12='12おなか'
msg13='13て'
msg14='14あし'

msg21='21あたま' 
msg22='22おなか'
msg23='23て'
msg24='24あし'

msg31='31あたま' 
msg32='32おなか'
msg33='33て'
msg34='34あし'

msg41='41あたま' 
msg42='42おなか'
msg43='43て'
msg44='44あし'



#------------------------------------------------

#-------------------------------
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
CANVAS_WIDTH=450 
CANVAS_HEIGHT=300

TXT_SIZE=50
TXT_W=100
TXT_H=100

#------------------------------------

canvas1=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas2=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas3=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas4=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)


# ラベル変更
class Change:
	msg_number=1     #どのメッセージを表示するか 1-4 
#	t=3000 #time 
	t=500
	status=1 #(1,2,3)1:画面１　2:画面２　3:画面２でストップ
###############################################################
	def __init__(self):
	#初期
		self.nsg_number=1
		self.status=1
		self.change_msg()
###############################################################
	def change_msg(self):
		#場面に応じてのメッセージを作成	

		if self.status==1:
			self.msg=[msg1,msg2,msg3,msg4]
			self.status=2

		elif self.status==2:
			if self.msg_number==1:
				self.msg=[msg11,msg12,msg13,msg14]
			elif self.msg_number==2:
				self.msg=[msg21,msg22,msg23,msg24]
			elif self.msg_number==3:
				self.msg=[msg31,msg32,msg33,msg34]
			elif self.msg_number==4:
				self.msg=[msg31,msg32,msg33,msg34]
			self.status=3

		elif self.status==3:
 		#loop stop and clear
			if self.msg_number==1:
				self.canvas1('#ff0000')
				#選択以外を消す
				canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				

			elif self.msg_number==2:
				self.canvas2('#ff0000')			
				canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				
			elif self.msg_number==3:
				self.canvas3('#ff0000')			
				canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
			
			elif self.msg_number==4:
				self.canvas4('#ff0000')			
				canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
							
			#msg_number stop
			self.msg_number=5
			self.status=1


	def click(self,ev):

		self.change_msg()
		print ("loop")
		print (self.msg_number)
		print ("status")
		print (self.status)
		if self.msg_number==5:	
			self.msg_number=1

	
	def canvas1(self,color): 
		canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas1.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック', TXT_SIZE),text=self.msg[0])

	def canvas2(self,color): 
		canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas2.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text=self.msg[1])

	def canvas3(self,color): 
		canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas3.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text=self.msg[2])

	def canvas4(self,color): 
		canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas4.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text=self.msg[3])
	

	
	def show_time(self):
	#判定            

		if self.msg_number!=5:  #msg_number==5 :stop
			tk.after(self.t,self.show_time)    


	#loop 1-4
		if self.msg_number==1:
			self.canvas1('#ff0000')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			
			self.msg_number=2
	
		elif self.msg_number==2:
			self.canvas1('#ffffff')
			self.canvas2('#ff0000')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			
			self.msg_number=3

		elif self.msg_number==3:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ff0000')
			self.canvas4('#ffffff')			
			self.msg_number=4

		elif self.msg_number==4:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ff0000')			
			self.msg_number=1




c=Change()
c.show_time()

#クリックにて反応
tk.bind('<Button>',c.click)

canvas1.grid(row=0,column=0)
canvas2.grid(row=0,column=1)
canvas3.grid(row=1,column=0)
canvas4.grid(row=1,column=1)


tk.mainloop()




