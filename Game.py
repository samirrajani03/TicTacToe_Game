import tkinter as tk
turn = 0

def clear():
    lbl_start.grid_remove()
    btn_start.grid_remove()

def setUp():
    clear()
    window.rowconfigure([0,2], minsize=100, weight=1)
    window.columnconfigure([0,2], minsize=100, weight=1)

    def click(r, c):
        global turn
        if button[r][c]["text"] == " ":
            if turn == 0:
                button[r][c]["text"] = "X"
                turn = 1
            else:
                button[r][c]["text"] = "O"
                turn = 0
        else:
            return

    button = [[None, None, None] , [None, None, None] , [None, None, None]]

    for i in range(3):
        for j in range(3):
            button[i][j] = tk.Button(width=10, height=7, text=" ")
            button[i][j].grid(row=i, column=j)
            button[i][j].configure(command=lambda r=i, c=j: click(r, c))
    
    def reset():
        for i in range(3):
            for j in range(3):
                button[i][j]["text"] = " "

    btn_reset = tk.Button(text="Reset", command=reset)
    btn_reset.grid(row=3, column=1)

    def end():
        exit()
    
    btn_end = tk.Button(text="End", command=end)
    btn_end.grid(row=4, column=1)


window = tk.Tk()
window.title("Tic Tac Toe")
window.rowconfigure(0, minsize=100)
window.columnconfigure(0, minsize=100)


lbl_start = tk.Label(window, text="Wanna Play Tic Tac Toe?")
lbl_start.grid(row=0, column=0, sticky="n")
btn_start = tk.Button(window, text="Start?", command=setUp)
btn_start.grid(row=0, column=0)



window.mainloop()
