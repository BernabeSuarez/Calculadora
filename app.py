from tkinter import *
from tkinter import ttk



root = Tk()
root.title('Calculadora Py')
root.iconbitmap(r'C:\Users\suare\Desktop\Cursos Web\Python\Calculadora\icon.ico')
root['background']= 'slate gray'
root.resizable(0,0)


display = Entry(root, width=32,justify=RIGHT)
display.grid(row=0, column=0,columnspan=5,pady=10,padx=2)
display.config(font =("Calibri", 15))
display['background']='bisque'



index = 0


def click_btn(val):
    """
    It takes a value as an argument and inserts it into the display at the current index
    
    :param val: The value of the button that was clicked
    """
    global index
    display.insert(index, val)
    index += 1

def del_input():
    """
    It deletes the input from the calculator.
    """
    display.delete(0,END)
    index=0

def operacion():
    """
    It takes the data from the display, evaluates it, and then inserts the result into the display
    """
    data = display.get()
    resultado = eval(data)
    display.delete(0,END)
    display.insert(0, resultado)
    index=0


# Creating the buttons for the calculator.
bot_1=Button(root, text="1",width=5, height=2, command = lambda:click_btn(1))
bot_2=Button(root, text="2", width=5, height=2, command = lambda:click_btn(2))
bot_3=Button(root, text="3", width=5, height=2,command = lambda:click_btn(3))
bot_4=Button(root, text="4", width=5, height=2,command = lambda:click_btn(4))
bot_5=Button(root, text="5", width=5, height=2,command = lambda:click_btn(5))
bot_6=Button(root, text="6", width=5, height=2,command = lambda:click_btn(6))
bot_7=Button(root, text="7", width=5, height=2,command = lambda:click_btn(7))
bot_8=Button(root, text="8", width=5, height=2,command = lambda:click_btn(8))
bot_9=Button(root, text="9", width=5, height=2,command = lambda:click_btn(9))
bot_0=Button(root, text="0", width=13, height=2,command = lambda:click_btn(0))

bot_div=Button(root, text="/", width=5, height=2,command = lambda:click_btn("/"))
bot_mult=Button(root, text="*", width=5, height=2,command = lambda:click_btn("*"))
bot_rest=Button(root, text="-", width=5, height=2,command = lambda:click_btn("-"))
bot_sum=Button(root, text="+", width=5, height=2,command = lambda:click_btn("+"))
bot_dot=Button(root, text=".", width=5, height=2,command = lambda:click_btn("."))
bot_eq=Button(root, text="=", width=5, height=5,command = lambda:operacion())
bot_delete=Button(root, text="C", width=13, height=2,command = del_input)


bot_1.grid(row=4, column=0, pady=5, padx=2)
bot_1.config(font =("Calibri", 14), bg='khaki')
bot_2.grid(row=4, column=1, pady=5, padx=2)
bot_2.config(font =("Calibri", 14), bg='khaki')
bot_3.grid(row=4, column=2, pady=5, padx=2)
bot_3.config(font =("Calibri", 14), bg='khaki')
bot_4.grid(row=3, column=0, pady=5, padx=2)
bot_4.config(font =("Calibri", 14), bg='khaki')
bot_5.grid(row=3, column=1, pady=5, padx=2)
bot_5.config(font =("Calibri", 14), bg='khaki')
bot_6.grid(row=3, column=2, pady=5, padx=2)
bot_6.config(font =("Calibri", 14), bg='khaki')
bot_7.grid(row=2, column=0, pady=5, padx=2)
bot_7.config(font =("Calibri", 14), bg='khaki')
bot_8.grid(row=2, column=1, pady=5, padx=2)
bot_8.config(font =("Calibri", 14), bg='khaki')
bot_9.grid(row=2, column=2, pady=5, padx=2)
bot_9.config(font =("Calibri", 14), bg='khaki')
bot_0.grid(row=5, column=0,columnspan=2, pady=5, padx=2)
bot_0.config(font =("Calibri", 14), bg='khaki')
bot_div.grid(row=1, column=2, pady=5, padx=2)
bot_div.config(font =("Calibri", 14, "bold"),bg='tan1')
bot_mult.grid(row=1, column=4, pady=5, padx=2)
bot_mult.config(font =("Calibri", 14, "bold"),bg='tan1')
bot_rest.grid(row=2, column=4, pady=5, padx=2)
bot_rest.config(font =("Calibri", 14, "bold"),bg='tan1')
bot_sum.grid(row=3, column=4, pady=5, padx=2)
bot_sum.config(font =("Calibri", 14, "bold"),bg='tan1')
bot_eq.grid(row=4,rowspan =  2, column=4, pady=5, padx=2)
bot_eq.config(font =("Calibri", 14, "bold"), bg="PaleGreen2")
bot_delete.grid(row=1, column=0, columnspan=2, pady=5, padx=2)
bot_delete.config(font =("Calibri", 14, "bold"), bg="OrangeRed4", fg="white")
bot_dot.grid(row=5, column=2, pady=5, padx=2)
bot_dot.config(font =("Calibri", 14, "bold"),bg='tan1')



root.mainloop()