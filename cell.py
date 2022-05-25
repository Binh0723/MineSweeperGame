from msilib.schema import Property
from tkinter import Button,Label
import setting
import random
import ctypes
import sys

class Cell:
    all = []
    cell_count = setting.CELL_COUNT
    create_cell_count_label_object = None
    def __init__(self,x, y, isMine = False):
        self.isMine = isMine  
        self.is_opened = False  
        self.is_Mine_candidate = False
        self.ButOb  = None
        self.x = x
        self.y = y


        Cell.all.append(self)

    def create_But_Ob(self, location):
        btn = Button(location, width = 10, height = 3)
        btn.bind('<Button-1>',self.left_click_action)
        btn.bind('<Button-3>',self.right_click_action)
        self.ButOb = btn

    @staticmethod
    def create_cell_count_label(location): 
        lbl = Label(location,bg = "black",fg = 'white', text = f"Cells Left: {Cell.cell_count}",font = ("",30))

        Cell.create_cell_count_label_object=lbl 

    def left_click_action(self,event):
        if self.isMine:
            self.show_mine()
        else:
            if self.surrounded_cells_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

            self.show_cell()
            self.ButOb.configure(bg = 'SystemButtonFace')
        self.ButOb.unbind('<Button-1>')
        self.ButOb.unbind('<Button-3>')

        if Cell.cell_count == setting.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0 , 'Congratulation! You won the game!','Game Over',0)
                sys.exit()


    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1,self.y - 1),
            self.get_cell_by_axis(self.x - 1,self.y),
            self.get_cell_by_axis(self.x - 1,self.y + 1),
            self.get_cell_by_axis(self.x ,self.y - 1),
            self.get_cell_by_axis(self.x + 1,self.y - 1),
            self.get_cell_by_axis(self.x +1,self.y),
            self.get_cell_by_axis(self.x +1,self.y + 1),
            self.get_cell_by_axis(self.x ,self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surrounded_cells_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.isMine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.ButOb.configure(text = self.surrounded_cells_length)

            if Cell.create_cell_count_label_object:
                Cell.create_cell_count_label_object.configure(text =  f"Cells Left: {Cell.cell_count}")

            self.is_opened = True

    def show_mine(self):
        ctypes.windll.user32.MessageBoxW(0 , 'You clicked on a mine','Game Over',0)
        self.ButOb.configure(bg = 'red')
        sys.exit()

    def right_click_action(self,event):
        if not self.is_Mine_candidate:
            self.ButOb.configure(bg = 'orange')
            self.is_Mine_candidate = True
        else:
            self.ButOb.configure(bg = 'SystemButtonFace')
            self.is_Mine_candidate = False

    @staticmethod
    def randomize_mines():
      pick_cells = random.sample(Cell.all, setting.MINES_COUNT)
      print(pick_cells)
      for pick_sell in pick_cells:
          pick_sell.isMine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"