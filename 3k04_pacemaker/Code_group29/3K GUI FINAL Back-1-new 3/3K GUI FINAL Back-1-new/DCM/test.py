import tkinter as tk

window = tk.Tk() #对象，object
window.title('my window')
window.geometry('500x300')

var1 = tk.StringVar() # 也是一个对象，字符串对象

l = tk.Label(window,bg = 'yellow',width = 14,textvariable = var1)
l.pack()

# var1通过光标选择对应计算的值
def print_selection():
    value = lb.get(lb.curselection()) #选择光标的值

    a1 = 963.256
    b1 = 985.32
    c1 = 9854.2145

    # 通过选择listbox的值，显示相应的结果
    if value == '岭估计':
        var1.set(a1)
    elif value == 'uv分解':
        var1.set(b1)
    elif value == '遗传法':
        var1.set(c1)

b1 = tk.Button(window,text = '打印 所选',width = 15,height = 2,command = print_selection)
b1.pack()


# 方式一
var2 = tk.StringVar()
var2.set(('岭估计','uv分解','遗传法')) #元祖列表
lb = tk.Listbox(window,listvariable = var2,width = 8,height = 4) # list里面的值是var2变量


### 方式二，列表赋值
##list_items = [1,2,3,4] #
##for item in list_items:
##    lb.insert('end',item) #起始插入位置为end
##
###方式三，逐个插入
##lb.insert(1,'first') #插入字符，插入位置
##lb.insert(2,'second')
##lb.delete(2)

lb.pack()

window.mainloop()# 更新窗口数据
# entry text
