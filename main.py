import request
from tkinter import *

def findPhoneFromQQ(qq):
    request.findPhoneFromQQ(qq)
def findQQFromPhone(phone):
    request.findQQFromPhone(phone)


def main():
    i = input("参数 :")
    root = Tk()
    root.title("查询工具")

    root.geometry("300x200")
    label = Label(root, text="Q反", font=("Arial", 20), fg="blue", pady=10)
    label.bind("<Button-1>", lambda e: findPhoneFromQQ(i))
    label.pack()
    label = Label(root, text="P反", font=("Arial", 20), fg="blue", pady=10)
    label.bind("<Button-1>", lambda e: findQQFromPhone(i))
    label.pack()


    root.mainloop()

if __name__ == "__main__":
    main()