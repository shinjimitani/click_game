#coding:utf-8

#クリックコミュニケーションボード
#場面切替版

#2-1.py
#初版：2014/10/04
#
#スキャン時間
#t=3000 #time
t=500
#
#####################################
#メッセージを入力する
#メニュー
msg1='1'
msg2='2'
msg3='3'
msg4='4'

#メニュー以下の階層
msg11='11' 
msg12='12'
msg13='13'
msg14='14'

msg21='21' 
msg22='22'
msg23='23'
msg24='24'

msg31='31' 
msg32='32'
msg33='33'
msg34='34'

msg41='41' 
msg42='42'
msg43='43'
msg44='44'
################################################
#仕様
#
#１、左クリックにて操作
#２、４つのウィンドウ
#３、画面遷移
# クリックにて(1)->(2)->(3)->(1)....と遷移する
# (1) メニュー画面　
# (2) 「メニュー画面」にて、選択した項目
# (3) ストップ
#４、メッセージは、このファイル上部を変更する事
#################################################


import tkinter
import time
tk=tkinter.Tk()


#設定項目
#---------------------------------------------------------------
#キャンバスのサイズ 
CANVAS_WIDTH=550 
CANVAS_HEIGHT=300

TXT_SIZE=40
TXT_W=40
TXT_H=50
#------------------------------------

canvas1=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas2=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas3=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
canvas4=tkinter.Canvas(tk,width=CANVAS_WIDTH,height=CANVAS_HEIGHT)


# ラベル変更
class Change:
	msg_number=1     #どのメッセージを表示するか 1-4 
	status=1 #(1,2,3)1:画面１　2:画面２　3:画面２でストップ
	stop_flg=1 #1:go 2:stop
	
	def __init__(self):
	#初期
		self.nsg_number=1
		self.status=1
		self.change_msg(1) #メニューのメッセージ
		self.status=2	
	def change_msg(self,s):
	#statusに応じてのメッセージを作成	
	#引数
	#s:status(1 or 2)
		if s==1:#menu
			self.msg=[msg1,msg2,msg3,msg4]
		elif s==2:#menu にて選択した内容
			if self.msg_number==2:
				self.msg=[msg11,msg12,msg13,msg14]
			elif self.msg_number==3:
				self.msg=[msg21,msg22,msg23,msg24]
			elif self.msg_number==4:
				self.msg=[msg31,msg32,msg33,msg34]
			elif self.msg_number==1:
				self.msg=[msg41,msg42,msg43,msg44]
			
				
	def clear(self):
	#画面をストップし選択以外のメッセージを消す	
		self.stop_flg=0　#スキャンのストップ
		if self.msg_number==2:
				self.canvas1('#ff0000')
				canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				

		elif self.msg_number==3:
				self.canvas2('#ff0000')			
				canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				
		elif self.msg_number==4:
				self.canvas3('#ff0000')			
				canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
			
		elif self.msg_number==1:
				self.canvas4('#ff0000')			
				canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
				canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
			

	def click(self,ev):
	#クリック時
		if self.stop_flg==0:　#スキャンのストップを解除
			self.status=1
			self.stop_flg=1
		#statusに応じての処理
		if self.status==1:
			self.change_msg(1)
			self.status=self.status+1
					
		elif self.status==2:
			self.change_msg(2)
			self.status+=1

		elif self.status==3: 
			self.clear()
			self.status=1
	
	

	def show_time(self):

		if self.msg_number==1 and self.stop_flg==1:
			self.canvas1('#ff0000')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			
	
		elif self.msg_number==2 and self.stop_flg==1:
			self.canvas1('#ffffff')
			self.canvas2('#ff0000')
			self.canvas3('#ffffff')
			self.canvas4('#ffffff')			

		elif self.msg_number==3 and self.stop_flg==1:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ff0000')
			self.canvas4('#ffffff')			

		elif self.msg_number==4 and self.stop_flg==1:
			self.canvas1('#ffffff')
			self.canvas2('#ffffff')
			self.canvas3('#ffffff')
			self.canvas4('#ff0000')			

	#判定            
		if self.msg_number==4:
			self.msg_number=1
		else:
			self.msg_number+=1
		
		tk.after(t,self.show_time)   

　　	#canvasの作成
	def canvas1(self,color): 
		canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas1.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text=self.msg[0])

	def canvas2(self,color): 
		canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas2.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text=self.msg[1])

	def canvas3(self,color): 
		canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas3.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text=self.msg[2])

	def canvas4(self,color): 
		canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas4.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text=self.msg[3])
	

c=Change()
c.show_time()

#クリックにて反応
tk.bind('<Button>',c.click)

canvas1.grid(row=0,column=0)
canvas2.grid(row=0,column=1)
canvas3.grid(row=1,column=0)
canvas4.grid(row=1,column=1)


tk.mainloop()

######################
#メモ#################
#2014/10/04
#・もう少し、スッキリとさせる必要あり
#
#
#
#
#
#


