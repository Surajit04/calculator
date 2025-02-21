import tkinter as tkr
app = tkr.Tk(__name__)
app.title('Calculator')
app.geometry('300x400')

tkr.Label(app,text = 'Calculator',font = ('Arial',20),fg = 'blue').pack()

tkr.Label(app,text='First Value',font=(10)).place(x = 30 , y = 50)
tkr.Label(app,text='Second Value',font=(10)).place(x = 150 , y = 50)


fv = tkr.Variable(app)
sv = tkr.Variable(app)


tkr.Entry(app, width = 15,textvariable = fv, font = ( 'Arial', 11)).place(x = 30 , y = 80)
tkr.Entry(app , width = 15 ,textvariable = sv, font = ('Arial',11)).place(x = 150, y = 80)

def opt_add():
    res.set(eval(fv.get()+'+'+sv.get()))

def opt_sub():
    res.set(eval(fv.get()+'-'+sv.get()))

def opt_mul():
    res.set(eval(fv.get()+'*'+sv.get()))

def opt_div():
    res.set(eval(fv.get()+'/'+sv.get()))
    
    
    

tkr.Button(app,text='+',width = 3, bg='white', fg='black', command = opt_add, font=(10)).place(x = 30, y = 120)
tkr.Button(app,text='-',width = 3, bg='white', fg='black', command = opt_sub, font=(10)).place(x = 90, y = 120)
tkr.Button(app,text='*',width = 3, bg='white', fg='black', command = opt_mul, font=(10)).place(x = 170, y = 120)
tkr.Button(app,text='/',width = 3, bg='white', fg='black', command = opt_div, font=(10)).place(x = 230, y = 120)

tkr.Label(app , text = 'Result' , font = (10)).place(x = 120 , y = 210)


res = tkr.Variable()
res.set('0')
tkr.Label(app , textvariable = res  ,font=('Arial' , 20)).place( x = 180 , y = 205)



app.mainloop()
