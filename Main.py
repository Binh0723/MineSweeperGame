from tkinter import *
from cell import Cell
import setting
import util

root = Tk() 
root.configure(bg = "black")
root.geometry(f'{setting.WIDTH}x{setting.HEIGHT}')
root.title("Mineswepper game")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg = 'black',
    width = setting.WIDTH,
    height = util.height_prct(20)
)
top_frame.place(x=0,y=0)

game_title = Label(top_frame,bg = 'black',fg = 'white',text = 'Minesweeper game',font = ('',30))

game_title.place(x = util.width_prct(25), y = 0)

left_frame = Frame(root, bg = 'black',width = setting.WIDTH/4,height = util.height_prct(80) )
left_frame.place(x = 0, y = setting.HEIGHT/5)

center_frame = Frame(root, bg = 'black', width = util.width_prct(75), height = util.height_prct(80))
center_frame.place(x = util.width_prct(25),y = util.height_prct(20))

for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c = Cell(x,y)
        c.create_But_Ob(center_frame)
        c.ButOb.grid(column = x, row = y)

Cell.create_cell_count_label(left_frame)
Cell.create_cell_count_label_object.place(x = 0,y = 0)
Cell.randomize_mines() 

root.mainloop()