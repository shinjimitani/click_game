#coding:utf-8



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


import tkinter
import time
tk=tkinter.Tk()


#設定項目
#---------------------------------------------------------------
#キャンバスのサイズ 
CANVAS_WIDTH=450 
CANVAS_HEIGHT=300

TXT_SIZE=30
TXT_W=30
TXT_H=50

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
	stop_flg=1 #1:go 2:stop
	
	def __init__(self):
	#初期
		self.nsg_number=1
		self.status=1
		self.change_msg()
	
	def change_msg(self):
		#場面に応じてのメッセージを作成	

		if self.status==1:
			self.msg=[msg1,msg2,msg3,msg4]
		elif self.status==2:
			if self.msg_number==1:
				self.msg=[msg11,msg12,msg13,msg14]
			elif self.msg_number==2:
				self.msg=[msg21,msg22,msg23,msg24]
			elif self.msg_number==3:
				self.msg=[msg31,msg32,msg33,msg34]
			elif self.msg_number==4:
				self.msg=[msg31,msg32,msg33,msg34]
			
				
	def clear(self):
		self.stop_flg=0
		print("stop")
		if self.msg_number==2:
				self.canvas1('#ff0000')
				#選択以外を消す
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
				canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill='#ffffff')				
			

	def click(self,ev):
		print ("click")
		if self.stop_flg==0:
			self.status=1
			self.stop_flg=1

		if self.status==1:
			print(self.status)
			self.change_msg()
			self.status=self.status+1
					
		elif self.status==2:
			print("222")
			self.change_msg()
			self.status+=1

		elif self.status==3: 
			print("333")
			self.clear()
			self.status=1
	
#		elif self.status==4:
#			self.status=1
	
	#	if self.stop_flg==0:
	#		self.stop_flg=1

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
		
		tk.after(self.t,self.show_time)   


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
	

c=Change()
c.show_time()

#クリックにて反応
tk.bind('<Button>',c.click)

canvas1.grid(row=0,column=0)
canvas2.grid(row=0,column=1)
canvas3.grid(row=1,column=0)
canvas4.grid(row=1,column=1)


tk.mainloop()




