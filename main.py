import json
from DFS import DFS
from BFS import BFS
from Node import Node
from UCS import UCS
from GreedyBestFirstSearch import GreedyBestFirstSearch
from AStar import AStar
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from MazeGenerator import Maze
import time
import threading


def main(file, mode,n):
    with open(file) as maze_file:
        maze_data = json.load(maze_file)
        maze = maze_data["maze"]
        initial_state = maze_data["initial_state"]
        initial_state = Node(initial_state[0], initial_state[1])
        goal_states = maze_data["goal_states"]
        window.destroy()

        
        if n==1:
            dfs = DFS("DEPTH-FIRST SEARCH", maze, initial_state, goal_states)
            dfs.execute(mode)
        elif n==2:
            bfs = BFS("BREADTH-FIRST SEARCH", maze, initial_state, goal_states)
            bfs.execute(mode)
        elif n==3:
            ucs = UCS("UNIFORM-COST SEARCH", maze, initial_state, goal_states)
            ucs.execute(mode)
        elif n==4:
            gbfs = GreedyBestFirstSearch("Greedy Best First Search", maze, initial_state, goal_states)
            gbfs.execute(mode)
        elif n==5:
            astar = AStar("A Star Search", maze, initial_state, goal_states)
            astar.execute(mode)
        else:print("error")


if __name__ == '__main__':

    file_input = "maze2.json"
    exec_mode = '1'

    window = tk.Tk()
    window.title('🔍 Advanced Search Algorithm Explorer')
    window.geometry('500x600')
    window.configure(bg='#1a1a2e')
    window.resizable(False, False)

    # 创建渐变背景效果
    canvas = tk.Canvas(window, width=500, height=600, bg='#1a1a2e', highlightthickness=0)
    canvas.pack()

    # 绘制渐变背景
    for i in range(600):
        color_intensity = int(26 + (i / 600) * 20)
        color = f"#{color_intensity:02x}{color_intensity:02x}{46:02x}"
        canvas.create_line(0, i, 500, i, fill=color, width=1)

    # 添加装饰性元素
    canvas.create_oval(50, 100, 80, 130, fill='#00d4ff', outline='', width=0)
    canvas.create_oval(420, 150, 450, 180, fill='#ff6b6b', outline='', width=0)
    canvas.create_oval(30, 300, 60, 330, fill='#4ecdc4', outline='', width=0)
    canvas.create_oval(440, 400, 470, 430, fill='#feca57', outline='', width=0)

    # 装饰线
    canvas.create_line(0, 80, 500, 80, fill='#00d4ff', width=2)
    canvas.create_line(0, 520, 500, 520, fill='#00d4ff', width=2)

    var = tk.StringVar()

    # 主标题
    title_frame = tk.Frame(canvas, bg='#1a1a2e')
    canvas.create_window(250, 50, window=title_frame)

    l = tk.Label(title_frame, bg='#1a1a2e', fg='#00d4ff',
                 text='🚀 Please Select a Search Algorithm',
                 font=("Arial", 18, "bold"))
    l.pack()

    dic = {'dfs': 1, 'bfs': 2, 'ucs': 3, 'greedy': 4, 'astar': 5}

    radiobuttons = []


    def select():
        global s
        s = dic.get(var.get())
        status_label.config(text=f"✅ Selected: {var.get().upper()} Algorithm")

        for rb in radiobuttons:
            if rb['value'] == var.get():
                rb.config(bg='#00d4ff', fg='#1a1a2e')
            else:
                rb.config(bg='#2d2d44', fg='#ffffff')


    options_frame = tk.Frame(canvas, bg='#1a1a2e')
    canvas.create_window(250, 200, window=options_frame)

    algorithm_styles = {
        'bg': '#2d2d44',
        'fg': '#ffffff',
        'activebackground': '#3d3d54',
        'activeforeground': '#00d4ff',
        'font': ("Arial", 14, "bold"),
        'relief': 'flat',
        'bd': 0,
        'padx': 20,
        'pady': 10,
        'indicatoron': 0,
        'highlightthickness': 0
    }

    r1 = tk.Radiobutton(options_frame, text='🔍 Depth-First Search', variable=var, value='dfs',
                        command=select, **algorithm_styles)
    r1.pack(pady=5, fill='x')
    radiobuttons.append(r1)

    r2 = tk.Radiobutton(options_frame, text='🌊 Breadth-First Search', variable=var, value='bfs',
                        command=select, **algorithm_styles)
    r2.pack(pady=5, fill='x')
    radiobuttons.append(r2)

    r3 = tk.Radiobutton(options_frame, text='⚖️ Uniform-Cost Search', variable=var, value='ucs',
                        command=select, **algorithm_styles)
    r3.pack(pady=5, fill='x')
    radiobuttons.append(r3)

    r4 = tk.Radiobutton(options_frame, text='🎯 Greedy Best-First Search', variable=var, value='greedy',
                        command=select, **algorithm_styles)
    r4.pack(pady=5, fill='x')
    radiobuttons.append(r4)

    r5 = tk.Radiobutton(options_frame, text='⭐ A* Search', variable=var, value='astar',
                        command=select, **algorithm_styles)
    r5.pack(pady=5, fill='x')
    radiobuttons.append(r5)


    def run():
        if not var.get():
            messagebox.showwarning("⚠️ Warning", "Please select an algorithm first!")
            return
        main(file_input, exec_mode, s)


    # 创建按钮框架
    button_frame = tk.Frame(canvas, bg='#1a1a2e')
    canvas.create_window(250, 450, window=button_frame)

    # 搜索按钮
    search_button = tk.Button(button_frame,
                              text="🚀 START SEARCH",
                              font=("Arial", 16, "bold"),
                              bg='#00d4ff',
                              fg='#1a1a2e',
                              activebackground='#00b8e6',
                              activeforeground='#ffffff',
                              relief='raised',
                              bd=3,
                              padx=30,
                              pady=10,
                              command=run)
    search_button.pack()


    def on_enter(e):
        search_button.config(bg='#00b8e6', relief='sunken')


    def on_leave(e):
        search_button.config(bg='#00d4ff', relief='raised')


    search_button.bind("<Enter>", on_enter)
    search_button.bind("<Leave>", on_leave)

    # 状态标签
    status_label = tk.Label(canvas,
                            text="💡 Select an algorithm and click START SEARCH",
                            bg='#1a1a2e',
                            fg='#888888',
                            font=("Arial", 10, "italic"))
    canvas.create_window(250, 520, window=status_label)


    # 键盘快捷键
    def on_key_press(event):
        if event.keysym == 'Return':
            run()
        elif event.keysym in ['1', '2', '3', '4', '5']:
            algorithms = ['dfs', 'bfs', 'ucs', 'greedy', 'astar']
            var.set(algorithms[int(event.keysym) - 1])
            select()  # 触发同步高亮


    window.bind('<Key>', on_key_press)
    window.focus_set()

    window.mainloop()