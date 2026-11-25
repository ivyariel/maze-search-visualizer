# -*- coding: utf-8 -*-

import json
import tkinter as tk
from tkinter.messagebox import showinfo
from Node import Node
import time
map_visited=[]
class Maze(object):
    def __init__(self,maze,initial_state,goal_state,visited,path):
        self.maze=maze
        self.initial_state=initial_state
        self.goal_state=goal_state
        self.visited=visited
        self.path=path
        self.row_cells=len(self.maze)
        self.col_cells=len(self.maze[0])
        self.cell_size=50
        self.cell_gap=1
        self.color_dict = {0:  '#2d2d44',
                           1:   '#00d4ff',
                           2:  '#00ff88',
                           3:      '#ff4757',
                           4:  '#808080',
                           5: '#ffa502',
                           6:'#8b0000'}
        self.canvas_bg  = '#2d2d44'
        self.frame_x    = 15
        self.frame_y    = 15
        self.wall_width = 6
        self.path_coordinates = []
        self.run_game()


    def window_center(self,window,w_size,h_size):
        screenWidth  =  window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        left =  (screenWidth - w_size) // 2
        top  = (screenHeight - h_size) // 2
        window.geometry("%dx%d+%d+%d" % (w_size, h_size, left, top))
    
    def create_map(self):

        global game_map
        game_map = [] 
        for i in range(0,self.col_cells):
            game_map.append([])
        for i in range(0,self.col_cells):
           for j in range(0,self.row_cells):
              game_map[i].append(j)   
              game_map[i][j] = 0
              if self.maze[i][j]['cost']==7:
                  game_map[i][j]=6
        game_map[self.initial_state[0]][self.initial_state[1]]=2
        game_map[self.goal_state[0]][self.goal_state[1]]=3
        
    def create_canvas(self):
        global canvas, background_canvas
        canvas_h = self.cell_size * self.col_cells + self.frame_y*2
        canvas_w = self.cell_size * self.row_cells + self.frame_x*2

        win_h_size = self.col_cells * self.cell_size + self.frame_y*2 + 150
        win_w_size = self.row_cells * self.cell_size + self.frame_x*2 + 100

        background_canvas = tk.Canvas(window, bg='#1a1a2e', 
                                    height=win_h_size, width=win_w_size,
                                    highlightthickness=0)
        background_canvas.place(x=0, y=0)

        background_canvas.configure(bg='#1a1a2e')

        self.add_decorative_elements(win_w_size, win_h_size)

        canvas = tk.Canvas(window, bg='#2d2d44', 
                          height=canvas_h, width=canvas_w,
                          highlightthickness=0)
        canvas.place(x=50, y=80)
    
    def add_decorative_elements(self, win_w_size, win_h_size):
        title_label = tk.Label(background_canvas, 
                              text="🎮 MAZE VISUALIZATION", 
                              bg='#1a1a2e', fg='#00d4ff',
                              font=("Arial", 14, "bold"))
        background_canvas.create_window(win_w_size//2, 20, window=title_label)
                
    def draw_line(self,x1,y1,x2,y2,thick=3):
        canvas.create_line((x1, y1), (x2, y2), width=thick, fill="#00d4ff")
        
    
    def create_wall(self):
        for y in range(0,self.row_cells):
            for x in range(0,self.col_cells):
                if 'n' not in self.maze[y][x]['move']:
                    x1=self.frame_x+self.cell_size*(x)
                    y1=self.frame_y + self.cell_size*(y)
                    x2=self.frame_x + self.cell_size*(x+1)
                    y2=self.frame_y + self.cell_size*(y)
                    self.draw_line(x1,y1,x2,y2)
                if 'e' not in self.maze[y][x]['move']:
                    x1=self.frame_x+self.cell_size*(x+1)
                    y1=self.frame_y + self.cell_size*(y)
                    x2=self.frame_x + self.cell_size*(x+1)
                    y2=self.frame_y + self.cell_size*(y+1)
                    self.draw_line(x1,y1,x2,y2)
                if 's' not in self.maze[y][x]['move']:
                    x1=self.frame_x+self.cell_size*(x)
                    y1=self.frame_y + self.cell_size*(y+1)
                    x2=self.frame_x + self.cell_size*(x+1)
                    y2=self.frame_y + self.cell_size*(y+1)
                    self.draw_line(x1,y1,x2,y2)
                if 'w' not in self.maze[y][x]['move']:
                    x1=self.frame_x+self.cell_size*(x)
                    y1=self.frame_y + self.cell_size*y
                    x2=self.frame_x + self.cell_size*(x)
                    y2=self.frame_y + self.cell_size*(y+1)
                    self.draw_line(x1,y1,x2,y2)

  
    def create_cells(self):
        for y in range(0,self.col_cells):
            for x in range(0,self.row_cells):
                a = self.frame_x + self.cell_size*x+2
                b = self.frame_y + self.cell_size*y+2
                c = self.frame_x + self.cell_size*(x+1)-2
                d = self.frame_y + self.cell_size*(y+1)-2
                e = self.canvas_bg
                f = self.cell_gap

                is_trap = self.maze[y][x]['cost'] == 7
                is_start = (y == self.initial_state[0] and x == self.initial_state[1])
                is_goal = (y == self.goal_state[0] and x == self.goal_state[1])

                if is_trap:
                    rect = canvas.create_rectangle(a,b,c,d, outline=e, width=f, fill='#8b0000')
                elif is_start:
                    rect = canvas.create_rectangle(a,b,c,d, outline=e, width=f, fill='#00ff88')
                elif is_goal:
                    rect = canvas.create_rectangle(a,b,c,d, outline=e, width=f, fill='#ff4757')
                elif game_map[y][x] in [0, 4]:
                    g = self.color_dict[game_map[y][x]]
                    rect = canvas.create_rectangle(a,b,c,d, outline=e, width=f, fill=g)

                if game_map[y][x] in [1, 5]:
                    center_x = (a + c) // 2
                    center_y = (b + d) // 2
                    radius = 8 if game_map[y][x] == 1 else 10
                    g = self.color_dict[game_map[y][x]]
                    canvas.create_oval(center_x - radius, center_y - radius, 
                                    center_x + radius, center_y + radius, 
                                    fill=g, outline='')
        self.draw_path_lines()
    
    def draw_path_lines(self):
        if len(self.path_coordinates) > 1:
            for i in range(len(self.path_coordinates) - 1):
                x1, y1 = self.path_coordinates[i]
                x2, y2 = self.path_coordinates[i + 1]
                canvas.create_line(x1, y1, x2, y2, 
                                 fill='#ffa502', width=4, capstyle='round')
    
    def creat_path(self,path):
        self.path_coordinates = []

        start_x = self.frame_x + self.cell_size * path[0].column + self.cell_size // 2
        start_y = self.frame_y + self.cell_size * path[0].row + self.cell_size // 2
        self.path_coordinates.append((start_x, start_y))
        
        for i in range(1,len(path)-1):
            game_map[path[i].row][path[i].column]=5
            center_x = self.frame_x + self.cell_size * path[i].column + self.cell_size // 2
            center_y = self.frame_y + self.cell_size * path[i].row + self.cell_size // 2
            self.path_coordinates.append((center_x, center_y))

        end_x = self.frame_x + self.cell_size * path[-1].column + self.cell_size // 2
        end_y = self.frame_y + self.cell_size * path[-1].row + self.cell_size // 2
        self.path_coordinates.append((end_x, end_y))
            
    def maze_update(self,visited):
        if len(visited)>=1:
            self.create_map()
            map_visited.append(visited.pop(0))
            for node in map_visited:
                if node.row == self.initial_state[0] and node.column == self.initial_state[1]:
                    continue
                if node.row == self.goal_state[0] and node.column == self.goal_state[1]:
                    continue
                game_map[node.row][node.column]=1
        else:self.creat_path(self.path)
            
    
    def maze_loop(self):
        global loop_id
        canvas.delete('all')
        time.sleep(0.1)
        self.maze_update(self.visited)
        self.create_cells()
        self.create_wall()
        if loop == 1:
            loop_id  = window.after(10, self.maze_loop)
    def game_start(self):
        global window, loop
        loop = 1
        self.create_map()
        self.create_wall()
        self.add_control_panel()
        self.maze_loop()
        
        def close_w():
            global loop
            loop = 0
            window.after_cancel(loop_id)
            window.destroy()
            
        window.protocol('WM_DELETE_WINDOW', close_w)
        window.mainloop()
    
    def add_control_panel(self):
        win_h_size = self.col_cells * self.cell_size + self.frame_y*2 + 150
        win_w_size = self.row_cells * self.cell_size + self.frame_x*2 + 100

        control_frame = tk.Frame(background_canvas, bg='#2d2d44', relief='raised', bd=2)
        background_canvas.create_window(win_w_size//2, win_h_size-30, window=control_frame)

        status_label = tk.Label(control_frame, 
                               text="🔍 Algorithm Running...", 
                               bg='#2d2d44', fg='#00d4ff',
                               font=("Arial", 12, "bold"))
        status_label.pack(side='left', padx=10)

        legend_frame = tk.Frame(control_frame, bg='#2d2d44')
        legend_frame.pack(side='right', padx=10)

        legend_items = [
            ("🟢", "Start"),
            ("🔴", "Goal"), 
            ("🔵", "Visited"),
            ("🟠", "Path"),
            ("⚫", "Trap")
        ]
        
        for color, text in legend_items:
            item = tk.Label(legend_frame, 
                          text=f"{color} {text}", 
                          bg='#2d2d44', fg='#ffffff',
                          font=("Arial", 9))
            item.pack(side='left', padx=5)
        
        
    def run_game(self):
        global window
        
        window = tk.Tk()
        window.focus_force()
        window.title('🎮 Advanced Maze Visualization - Search Algorithm Demo')
        window.configure(bg='#1a1a2e')
        window.resizable(False, False)

        win_w_size = self.row_cells * self.cell_size + self.frame_x*2 + 100
        win_h_size = self.col_cells * self.cell_size + self.frame_y*2 + 150
        self.window_center(window,win_w_size,win_h_size)
        self.create_canvas()
        self.game_start()
        
