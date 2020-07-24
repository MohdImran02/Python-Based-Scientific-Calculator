#A simple calculator programe..

from tkinter import *
import math as maths

cal = Tk()
cal.title("Simple Calculator")

label = Label(cal, text="result")
label.grid(row=0,column=0)
dis = Entry(cal, width=20, borderwidth = 5,justify=LEFT,relief=SUNKEN)
dis.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def welcome():
    dis.set('Welcome Mohd Imran')
    
def Clear_Display():
    #dis.set('Welcome Hassan')
    dis.delete(0,END)

def button_click(num):
    current = dis.get()
    dis.delete(0,END)

    dis.insert(0,str(current)+str(num))  

def num_conv(first_number):
    if (first_number[-1] == '.'):
        num = (first_number[:-1])
        #num = int(num)    
        numf = float(num)
    else:
        #num1 = int(first_number)   
        numf = float(first_number)
    return numf

def proper_format(val):
    if(val[0:2] == '00'):
        if(max(val) == '1'):
            x = '0b'+str(val)
            print('x in oct part:', str(x))
            return str(x)
    elif((val[0] == '0') and (val[2] != 'X' or 'x' 'b')):
        if(max(val) == '1'):
            x = '0b'+str(val)
            print('x in oct part:', str(x))
            return str(x)

    elif((val[2] == 'x') or (val[2] == 'X')):
        x = str(val)
        print('x in hex part:', x)
        return x
        
    else:
        x = str(val)
        print('x in dec part:', x)
        return x

def button_add():
    first_number = dis.get()
    global f_num
    global math
    math = "addition"
    #f_num = int(first_number)
    f_num = num_conv(first_number)
    dis.delete(0, END)
def button_sub():
    first_number = dis.get()
    global f_num
    global math
    math = "subtraction"
    #f_num = int(first_number)
    f_num = num_conv(first_number)
    dis.delete(0, END)
def button_mul():
    first_number = dis.get()
    global f_num
    global math
    math = "multiplication"
    #f_num = int(first_number)
    f_num = num_conv(first_number)
    dis.delete(0, END)
    
def button_div():
    first_number = dis.get()
    global f_num
    global math
    math = "division"
    #f_num = int(first_number)
    f_num = num_conv(first_number)
    dis.delete(0, END)

def button_ddiv():
    first_number = dis.get()
    global f_num
    global math
    math = "ddivision"
    #f_num = int(first_number)
    f_num = num_conv(first_number)
    dis.delete(0, END)

def button_log():
    first_number = dis.get()
    global f_num
    math = "log"
    #f_num = int(first_number)
    f_num = num_conv(first_number)
    dis.delete(0, END)
    val = maths.log10(f_num)
    dis.insert(0,val)  

def button_nlog():
    first_number = dis.get()
    global f_num
    #f_num = int(first_number)
    f_num = num_conv(first_number)
    dis.delete(0, END)
    val = maths.log(f_num)
    dis.insert(0,val)    

def button_bin():
    first_number = dis.get()
    global f_num
    if(first_number.isalnum()):
        #if(first_number[0:2] == '0X'):
        if((first_number[0:2] == ('0X')) or (first_number[0:2] == ('0x'))):
            val = "{0:08b}".format(int(first_number, 16))
        elif(first_number[0:2] == '0o'):
            val = "{0:08b}".format(int(first_number, 8))
        else:
            f_num = int(first_number)
            val = bin(f_num)
            
    val = str(val)
    #print('button_bin-> val = ',val)          
    #x = proper_format(val) 
    dis.delete(0, END)
    dis.insert(0,val)

def button_oct():
    '''first_number = dis.get()
    global f_num
    f_num = int(first_number)
    dis.delete(0, END)
    val = oct(f_num)
    dis.insert(0,val)'''

    first_number = dis.get()
    global f_num
    if(first_number.isalnum()):
        if((first_number[0:2] == '0X') or (first_number[0:2] == '0x')):
            val = "{0:08o}".format(int(first_number, 16))
        #elif(first_number[0:2] == '0b'):
        elif(first_number[0:2] == ('0b')):
            val = "{0:08o}".format(int(first_number, 2))
        else:
            f_num = int(first_number)
            val = oct(f_num)
            
    val = str(val)
    #print('button_oct-> val = ',val)        
    #x = proper_format(val) 
    dis.delete(0, END)
    dis.insert(0, val)

def button_hex():
    '''first_number = dis.get()
    global f_num
    f_num = int(first_number)
    dis.delete(0, END)
    val = hex(f_num)
    val1 = val.upper()
    dis.insert(0,val1)'''
    
    first_number = dis.get()
    global f_num
    if(first_number.isalnum()):
        if(first_number[0:2] == '0o'):
            val = "{0:08x}".format(int(first_number, 8))
        elif(first_number[0:2] == '0b'):
            val = "{0:08x}".format(int(first_number, 2))
        else:
            f_num = int(first_number)
            val = hex(f_num)
            
    val = str(val)
    #x = proper_format(val)
    y = val.upper()
    dis.delete(0, END)
    dis.insert(0,y)


def dot_display():
    first_number = dis.get()
    dis.delete(0, END)
    val = first_number + '.'
    dis.insert(0,val)

def dec_display():
    first_number = dis.get()
    global f_num
    if(first_number[0:2] == ('0X' or '0x' or '00')):
        if(max(first_number[2:])!='1'):
            f_num = int(first_number, 16)
    elif(first_number[0:2] == ('0o' or '00')):
        if(max(first_number[2:])!='1'):
            f_num = int(first_number, 8)
    elif(first_number[0:2] == ('0b' or '00')):
        if(max(first_number[2:])=='1'):
            f_num = int(first_number, 2)
    else:
        f_num = first_number
      
    val = str(f_num)
    dis.delete(0, END)
    dis.insert(0,val)

def button_equal():
    if(math == "addition"):
        sec_num = dis.get()
        x = float(sec_num)
        dis.delete(0, END)
        val = str(f_num+x)
        dis.insert(0, val)
    elif(math == "subtraction"):
        sec_num = dis.get()
        x = float(sec_num)
        dis.delete(0, END)
        val = str(f_num-x)
        dis.insert(0, val)
    elif(math == "division"):
        sec_num = dis.get()
        x = float(sec_num)
        dis.delete(0, END)
        val = str(f_num/x)
        dis.insert(0, val)
    elif(math == "multiplication"):
        sec_num = dis.get()
        x = float(sec_num)
        dis.delete(0, END)
        val = str(f_num*x)
        dis.insert(0, val)
    elif(math == "ddivision"):
        '''sec_num = dis.get()
        dis.delete(0, END)
        dis.insert(0, f_num//int(sec_num))'''
        sec_num = dis.get()
        x = float(sec_num)
        dis.delete(0, END)
        val = str(f_num//x)
        dis.insert(0, val)

button_1 = Button(cal, text="1",padx=40,pady=20,command = lambda: button_click(1))
button_2 = Button(cal, text="2",padx=40,pady=20,command = lambda: button_click(2))
button_3 = Button(cal, text="3",padx=40,pady=20,command = lambda: button_click(3))
button_4 = Button(cal, text="4",padx=40,pady=20,command = lambda: button_click(4))
button_5 = Button(cal, text="5",padx=40,pady=20,command = lambda: button_click(5))
button_6 = Button(cal, text="6",padx=40,pady=20,command = lambda: button_click(6))
button_7 = Button(cal, text="7",padx=40,pady=20,command = lambda: button_click(7))
button_8 = Button(cal, text="8",padx=40,pady=20,command = lambda: button_click(8))
button_9 = Button(cal, text="9",padx=40,pady=20,command = lambda: button_click(9))
button_0 = Button(cal, text="0",padx=40,pady=20,command = lambda: button_click(0))

button_add = Button(cal, text="+",padx=40,pady=20,command = button_add)
button_sub = Button(cal, text="-",padx=40,pady=20,command = button_sub)
button_mul = Button(cal, text="*",padx=40,pady=20,command = button_mul)
button_div = Button(cal, text="/",padx=40,pady=20,command = button_div)

button_ddiv = Button(cal, text="//",padx=30,pady=20,command = button_ddiv)
button_log = Button(cal, text="log10",padx=30,pady=20,command = button_log)
button_nlog = Button(cal, text="Nlog",padx=30,pady=20,command = button_nlog)

button_bin = Button(cal, text="Bin",padx=35,pady=20,command = button_bin)
button_oct = Button(cal, text="Oct",padx=35,pady=20,command = button_oct)
button_hex = Button(cal, text="Hex",padx=35,pady=20,command = button_hex)

button_equal = Button(cal, text="=",padx=40,pady=20,command = button_equal)
button_dec = Button(cal, text="Dec",padx=35,pady=20,command = dec_display)

#button_dec = Button(cal, text="Dec",padx=35,pady=20, state = DISABLED)

button_Clr = Button(cal, text="Clr",padx=35,pady=20,command = Clear_Display)
button_dot = Button(cal, text=".",padx=40,pady=20,command = dot_display)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_Clr.grid(row=4,column=1)
button_dot.grid(row=4,column=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1)
button_dec.grid(row=5,column=2)

button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)

button_ddiv.grid(row=7,column=0)
button_log.grid(row=7,column=1)
button_nlog.grid(row=7,column=2)

button_bin.grid(row=8,column=0)
button_oct.grid(row=8,column=1)
button_hex.grid(row=8,column=2)

cal.mainloop()
