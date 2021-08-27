import tkinter.messagebox
import requests
import json
from tkinter import *
from tkinter import ttk

def get_data():
    try:
        kmlist={
            '全国大学英语四级考试(CET4)':'1',
            '全国大学英语六级考试(CET6)':'2',
            '全国大学日语四级考试(CJT4)':'3',
            '全国大学日语六级考试(CJT6)':'4',
            '全国大学德语四级考试(PHS4)':'5',
            '全国大学德语六级考试(PHS6)':'6',
            '全国大学俄语四级考试(CRT4)':'7',
            '全国大学俄语六级考试(CRT6)':'8',
            '全国大学法语四级考试(TFU4)':'9'
        }
        url='http://cachecloud.neea.cn/api/latest/results/cet'
        headers={
            'Host': 'cachecloud.neea.cn',
            'Origin': 'http://cet.neea.cn',
            'Referer': 'http://cet.neea.cn/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }
        km=com.get()
        name=entry1.get()
        id=entry2.get()
        params={
            'e': 'CET_202106_DANGCI',
            'km': kmlist[km],
            'xm': name,
            'no': id
        }
        response=requests.get(url,headers=headers,params=params)
        data=json.loads(response.content.decode())
        if data['code']!=404:
            datalist={
                '姓名':data['xm'],
                '准考证号':data['zkzh'],
                '总分':data['score'],
                '听力':data['sco_lc'],
                '阅读':data['sco_rd'],
                '写作和翻译':data['sco_wt']
            }
            for i in datalist:
                text.insert(END,'{}:{}'.format(i,datalist))
                text.see(END)
                text.update()
            if int(data['score'])>=425:
                tkinter.messagebox.showinfo(message='恭喜你，通过考试啦！！！&#128077;')
            if int(data['score'])<425:
                tkinter.messagebox.showinfo(message='很遗憾，你没通过考试哦，继续加油！！！&#129470;')
        else:
            text.insert(END,data['msg'])
    except:
        tkinter.messagebox.showerror(message='请登录后再点击，谢谢')

window=Tk()
window.title('四六级成绩查询')
screenwidth = window.winfo_screenwidth()  # 屏幕宽度
screenheight = window.winfo_screenheight()  # 屏幕高度
width = 1000
height = 500
x = int((screenwidth - width) / 2)
y = int((screenheight - height) / 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

#查询科目下拉菜单
com=ttk.Combobox(window,width=30)
com.pack()
com['value']=('全国大学英语四级考试(CET4)','全国大学英语六级考试(CET6)','全国大学日语四级考试(CJT4)','全国大学日语六级考试(CJT6)','全国大学德语四级考试(PHS4)','全国大学德语六级考试(PHS6)','全国大学俄语四级考试(CRT4)','全国大学俄语六级考试(CRT6)','全国大学法语四级考试(TFU4)')
com.current(0)

#输入框
frm1=Frame(window,height=150,width=100)
l1=Label(frm1,text='姓名：',font=('宋体',20))
l1.grid()
l2=Label(frm1,text='身份证或准考证号：',font=('宋体',20))
l2.grid(row=1) #网格布局
entry1=Entry(frm1,font=('宋体',20))
entry1.grid(row=0,column=1)
entry2=Entry(frm1,font=('宋体',20))
entry2.grid(row=1,column=1)
frm1.pack()
#结果框
frm2=Frame(window,height=350,width=800)
sc=Scrollbar(frm2)
sc.pack(side=RIGHT,fill=Y)
text=Listbox(frm2,font=('宋体',20),width=50,yscrollcommand=sc.set)
text.pack(side=LEFT,fill=BOTH,expand=False)
sc.config(command=text.yview)
frm2.pack()
#查询按钮
frm3=Frame(window,height=50,bg='green',width=100)
button1=Button(frm3,text='登录',command=get_data)
button1.pack()
frm3.pack()
window.mainloop()
