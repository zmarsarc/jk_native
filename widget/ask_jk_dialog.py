import tkinter
import tkinter.ttk

class InputJKInfoWidget(tkinter.Frame):

    def __init__(self, parent):
        super(InputJKInfoWidget, self).__init__(parent)
        tkinter.Label(self, text='name').grid(row=0,column=0)
        tkinter.Entry(self).grid(row=0,column=1)
        tkinter.Label(self, text='size').grid(row=0,column=2)
        tkinter.ttk.Combobox(self).grid(row=0,column=3)
        tkinter.Label(self, text='length').grid(row=0,column=4)
        tkinter.Entry(self).grid(row=0, column=5)
        tkinter.Label(self, text='count').grid(row=0,column=6)
        tkinter.Entry(self).grid(row=0,column=7)

if __name__ == '__main__':
    root = tkinter.Tk()
    InputJKInfoWidget(root).grid(row=0,column=0)
    root.mainloop()