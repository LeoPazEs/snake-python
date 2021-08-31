import sys 
import random 
from PIL import Image, ImageTk 
from tkinter import Tk, Frame, Canvas, ALL, NW 

WIDTH = 300 
HIGHT = 300 
DOT_SIZE = 10 
RAND_POS = 27 
DELAY = 100 

class Board(Canvas):
    
    def __init__(self,parent):
        super().__init__(width=WIDTH, hight=HIGHT,background='black',highlightthickness=0) 

        self.parent = parent
        self.ini_game()
        self.pack() 

    def ini_game(self):
        self.left = False 
        self.right = True 
        self.up = False 
        self.down = False 
        self.in_game = True 

        self.dot_x = 100 
        self.dot_y = 190 

        try: 
            self.ibody = Image.open('dot.png') 
            self.body = ImageTk.PhotoImage(self.ibody)
            self.ihead = Image.open('head.png') 
            self.body = ImageTk.PhotoImage(self.ihead)
            self.idot = Image.open('dot.png') 
            self.dot = ImageTk.PhotoImage(self.idot)
        except IOError as e:
            print(str(e))
            sys.exit(1) 

        self.focus_get() 
        self.bind_all('<Key>',self.on_key_press)
        self.after(DELAY,self.on_time) 

        def create_objects(self):

            self.create_image(self.dot_x, self.dot_y, image=self.dot, anchor=NW, tag='dot')
            self.create_image(50, 50, image=self.head, anchor=NW, tag='head')
            self.create_image(40, 50, image=self.body, anchor=NW, tag='body')
            self.create_image(30, 50, image=self.body, anchor=NW, tag='body') 
        
        def check_dot(self):
            dot = self.find_withtag('dot')
            head = self.find_withtag('head') 

            x1, y1, x2 , y2 = self.bbox(head) 
            overlap = self.find_overlapping(x1, y1 , x2, y2) 

            for ovr in overlap:
                if dot[0] == ovr:
                    x , y = self.coords(dot)
                    self.create_image(x, y, image = self.body, anchor=NW, tag ='body') 
                    self.locate_dot() 

        def locate_dot(self):
            dot = self.find_withtag('dot') 
            self.delete(dot[0]) 
            r = random.randint(0, RAND_POS) 
            self.dot_x = r * DOT_SIZE 
            r = random.randint(0, RAND_POS)
            self.dot_y = r * DOT_SIZE

            self.create_image(self.dot_x, self.dot_y, image = self.body, anchor=NW, tag ='body') 


        
