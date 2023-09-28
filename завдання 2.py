from tkinter import*
window = Tk()
c = Canvas(window, width = 200, height = 200, bg = 'white')
c.pack()

c.create_rectangle(60,80,140,190, fill = 'yellow', outline = 'blue', width = 3)
c.create_rectangle(10,10,190,60, fill = 'white', outline = 'black', width = 6) 
window.mainloop()
