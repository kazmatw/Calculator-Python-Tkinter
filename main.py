from tkinter import *

root = Tk()
root.title('Calculator')

# initial windows size and its location
root.geometry('330x450+1500+200')

# make windows size fixed
root.resizable(0, 0)

# set background color
root.configure(bg='black')

# the real equation which will affect answer directly
equation = ''

# it decide the text show on the calculator
display = '0'

# create a set of operators to help me check is a char variable a operator
operators = {'*', '/', '+', '-'}

# finish is a bool variable which help me display correctly after pressing '='
finish = False

# this is a function which helps me debug
def checkStatus():
    print('display: ', display)
    print('equation: ', equation)

# status in the beginning
checkStatus()

# behavior of button number
def show(value):
    global finish
    global equation
    global display
    if display == '0':
        display = value
        equation += value
    elif equation[-1] in operators:
        display = value
        equation += value
    else:
        if finish:
            finish = False
            display = value
            equation = value
        else:
            display += value
            equation += value
    label_result.config(text=display)
    checkStatus()

# behavior of button operator
def operator(value):
    global finish
    global equation
    if finish:
        finish = False
    if len(equation) >= 1 and equation[-1] in operators:
        equation[-1] = equation[:-1]+value
    else:
        equation += value
    checkStatus()

# behavior of button 'c'
def backspace():
    global display
    if len(display):
        display = display[:-1]
    label_result.config(text=display)
    checkStatus()

# behavior of button 'AC'
def clear():
    global equation
    global display
    equation = ''
    display = '0'
    label_result.config(text=display)
    checkStatus()

# behavior of button '='
def calculate():
    global finish
    global equation
    if equation:
        try:
            equation = str(eval(equation))
        except:
            equation = 'error'
    label_result.config(text=equation)
    if equation == 'error':
        equation = ''
    finish = True
    checkStatus()

# the display screen
label_result = Label(root, width=18, height=2, text='0', fg='white',
                     bg='black', font=('arial', 30, 'bold'), anchor='se')
label_result.pack()

# layout
Button(root, text='AC', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='black', bg='silver', command=lambda: clear()).place(x=10, y=100)
Button(root, text='C', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='black', bg='silver', command=lambda: backspace()).place(x=90, y=100)
Button(root, text='%', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='black', bg='silver', command=lambda: operator('*0.01')).place(x=170, y=100)
Button(root, text='/', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: operator('/')).place(x=250, y=100)

Button(root, text='7', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('7')).place(x=10, y=170)
Button(root, text='8', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('8')).place(x=90, y=170)
Button(root, text='9', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('9')).place(x=170, y=170)
Button(root, text='X', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: operator('*')).place(x=250, y=170)

Button(root, text='4', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('4')).place(x=10, y=240)
Button(root, text='5', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('5')).place(x=90, y=240)
Button(root, text='6', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('6')).place(x=170, y=240)
Button(root, text='-', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: show('-')).place(x=250, y=240)

Button(root, text='1', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('1')).place(x=10, y=310)
Button(root, text='2', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('2')).place(x=90, y=310)
Button(root, text='3', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('3')).place(x=170, y=310)
Button(root, text='+', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: operator('+')).place(x=250, y=310)

Button(root, text='0', width=5, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('0')).place(x=10, y=380)
Button(root, text='.', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('.')).place(x=170, y=380)
Button(root, text='=', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: calculate()).place(x=250, y=380)
       
root.mainloop()

