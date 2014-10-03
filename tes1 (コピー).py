#coding:utf-8



#msg
msg1='1'
msg2='2'
msg3='3'
msg4='4'



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
	#	self.change_msg()
		color='#ff0000'


		canvas1.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas1.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text="1")

		canvas2.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas2.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text="2")

		canvas3.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas3.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text="3")

		canvas4.create_rectangle(5,5,CANVAS_WIDTH,CANVAS_HEIGHT,fill=color)
		canvas4.create_text(TXT_W,TXT_H,font=(u'ＭＳ ゴシック',TXT_SIZE),text="1")


###############################################################
	def change_msg(self):
		#場面に応じてのメッセージを作成	

		if self.status==1:
			pass
		elif self.status==2:
			pass
		elif self.status==3:
 		#loop stop and clear
			pass
				


	def click(self,ev):
		if self.status!=3: 
			self.status+=1
		else:
			self.status=1
		print('---------------')	
		print (self.status)
		print (self.msg_number)
		print('--------------')

	
	
	def show_time(self):
	#判定            
		if self.msg_number!=4:
			self.msg_number+=1
		else:
			self.msg_number=1


	#loop 1-4
		if self.msg_number==1:
			print (self.msg_number)	
		elif self.msg_number==2:
			print (self.msg_number)
		elif self.msg_number==3:
			print (self.msg_number)
		elif self.msg_number==4:
			print (self.msg_number)


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




