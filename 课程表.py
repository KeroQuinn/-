import tkinter as tk
from tkinter import ttk
from tkinter import *
window  =tk.Tk()
window.title('课程表')#窗口名
window.geometry('900x800')#设置窗口大小
tk.Label(window, text='课程表').pack()
tree = ttk.Treeview(window)
columns = ("1", "2", "3", "4", "5", "6", "7")
tree = ttk.Treeview(window, show = "headings", height = 60, columns = columns, selectmode = tk.BROWSE)
tree.column('1', width=100, anchor='center')  # 定义列
tree.column('2', width=100, anchor='center')  
tree.column('3', width=100, anchor='center')  
tree.column('4', width=100, anchor='center')  
tree.column('5', width=100, anchor='center')  
tree.column('6', width=100, anchor='center')  
tree.column('7', width=100, anchor='center')

tree.heading("1", text = "周一")
tree.heading("2", text = "周二")
tree.heading("3", text = "周三")
tree.heading("4", text = "周四")
tree.heading("5", text = "周五")
tree.heading("6", text = "周六")
tree.heading("7", text = "周日")
tree.pack()


mon = []
tue = []
wed = []
thu = []
fri = []
sat = []
sun = []
for i in range(min(len(mon),len(sun))): 
    tree.insert('', i, values=(mon[i], tue[i], wed[i], thu[i], fri[i], sat[i], sun[i]))#可选择性忽略这段代码 之前写入默认数据用的 怕之后还要用我就留着了

 
def set_cell_value(event): # 双击进入编辑状态
    for item in tree.selection():
            #item = I001
        item_text = tree.item(item, "values")
        print(item_text[0:7])  # 输出所选行的值
    column= tree.identify_column(event.x)# 列
    row = tree.identify_row(event.y)  # 行
    cn = len(column)
    rn = len(row)
    entryedit = Text(window, width=9+(cn-1)*16,height = 1)
    entryedit.place(x=16+(cn-1)*130, y=6+rn*20)
    
    def saveedit():       #编辑后的保存操作
        tree.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()
        tree.update()
        item1= str(tree.set(item))
        print(item_text[0:7])    
    okb = ttk.Button(window, text='OK', width=4, command=saveedit)
    okb.place(x=90+(cn-1)*242 ,y=2+rn*20)    
    
    def getall():  #导出时，遍历整个tree
        t = tree.get_children()
        data=open("C:\data.txt",'w+') 
        for i in t:
            print(tree.item(i,'values'))
            print(str(tree.item(i,'values')),file=data)
        data.close()
    savebutton = ttk.Button(window, text='保存并输出', width=18, command=getall)
    savebutton.place(x=650, y=650) 

    
        
tree.bind('<Double-1>', set_cell_value)#与鼠标事件绑定
tree.bind('<ButtonRelease-1>', set_cell_value)
tree.update()

   
        
def newrow():   #新增行
    mon.append('待命名')
    tue.append('待命名')
    wed.append('待命名')
    thu.append('待命名')
    fri.append('待命名')
    sat.append('待命名')
    sun.append('待命名')
    tree.insert('', len(mon)-1, values=(mon[len(mon)-1], tue[len(tue)-1], wed[len(wed)-1], thu[len(thu)-1], fri[len(fri)-1], sat[len(tue)-1], sun[len(tue)-1]))
    tree.update()
    newb.place(x=400, y=(len(thu)+1)*20+45)
    newb.update()
 
newb = ttk.Button(window, text='新建课程', width=20, command=newrow)#与鼠标事件绑定
newb.place(x=400, y=(len(thu)+1)*20+45)

window.mainloop()