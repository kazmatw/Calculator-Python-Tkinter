from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('330x450+1500+200')
root.resizable(0, 0)
root.configure(bg='black')

equation = ''
display = ''
operation = {'*', '/', '+', '-'}


def show(value):
    global equation
    if len(equation) > 0 and equation[-1] in operation and value in operation:
        equation = equation[:-1]+value
    else:
        equation += value
    label_result.config(text=equation)


def backspace():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)


def clear():
    global equation
    equation = ''
    label_result.config(text=equation)


def calculate():
    global equation
    if equation != '':
        try:
            equation = str(eval(equation))
        except:
            equation = 'error'
    label_result.config(text=equation)
    if equation == 'error':
        equation = ''


label_result = Label(root, width=18, height=2, text='', fg='white',
                     bg='black', font=('arial', 30, 'bold'), anchor='se')
label_result.pack()

Button(root, text='AC', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='black', bg='silver', command=lambda: clear()).place(x=10, y=100)
Button(root, text='C', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='black', bg='silver', command=lambda: backspace()).place(x=90, y=100)
Button(root, text='%', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='black', bg='silver', command=lambda: show('*0.01')).place(x=170, y=100)
Button(root, text='/', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: show('/')).place(x=250, y=100)

Button(root, text='7', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('7')).place(x=10, y=170)
Button(root, text='8', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('8')).place(x=90, y=170)
Button(root, text='9', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('9')).place(x=170, y=170)
Button(root, text='X', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: show('*')).place(x=250, y=170)

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
       bd=1, fg='white', bg='orange', command=lambda: show('+')).place(x=250, y=310)

Button(root, text='0', width=5, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('0')).place(x=10, y=380)
Button(root, text='.', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='#444444', command=lambda: show('.')).place(x=170, y=380)
Button(root, text='=', width=2, height=1, font=('arial', 30, 'bold'),
       bd=1, fg='white', bg='orange', command=lambda: calculate()).place(x=250, y=380)
root.mainloop()
