import tkinter as tk
import tkinter.ttk as ttk

def button_select(row, col):
    if selections[row][col] != 0 or endgame:
        return
    global current_player
    color = "blue"
    if current_player == "X":
        color = "blue"
        current_player = "O"
        label.config(text=player_2+" to move")
    else:
        color = "red"
        current_player = "X"
        label.config(text=player_1+" to move")
    buttons[row][col].config(text=current_player, bg=color, fg="white")
    selections[row][col] = current_player
    check_game_status()

def check_game_status():
    global label
    global endgame
    for i in range(3):
        if selections[i][0] != 0 and selections[i][0] == selections[i][1] and selections[i][0] == selections[i][2]:
            label.config(text=get_user_name(current_player)+" wins!")
            endgame = True
        elif selections[0][i] != 0 and selections[0][i] == selections[1][i] and selections[0][i] == selections[2][i]:
            label.config(text=get_user_name(current_player)+" wins!")
            endgame = True
        elif selections[1][1] != 0 and ((selections[0][0] == selections[1][1] and selections[0][0] == selections[2][2]) or (selections[0][2] == selections[1][1] and selections[0][2] == selections[2][0])):
            label.config(text=get_user_name(current_player)+" wins!")
            endgame = True
        else:
            empty_found = False
            for i in range(3):
                for j in range(3):
                    if selections[i][j] == 0:
                        empty_found = True
            if empty_found == False:
                endgame = True
                label.config(text="draw")

def get_user_name(symbol):
    if symbol == "X":
        return player_1
    elif symbol == "O":
        return player_2
    else:
        return ""
                
def start_game():
    global player_1
    global player_2
    global label
    global window
    player_1 = player_1_name.get()
    player_2 = player_2_name.get()
    if player_1 == "" or player_2 == "":
        return
    login_frame.pack_forget()
    login_label.pack_forget()
    header_frame.pack()
    play_zone_frame.pack()
    label.config(text=player_1_name.get()+" to move")
    window.geometry("320x360")

current_player = "O"
player_1 = ""
player_2 = ""

endgame=False

window = tk.Tk()
window.geometry("180x200")

header_frame = tk.Frame(master=window)

play_zone_frame = tk.Frame(master=window)

login_label = ttk.Label(master=window, text="Hello!\n", font=("Helvetica, 14"))
login_label.pack()

login_frame = tk.Frame(master=window)
login_frame.pack()

player_1_label = ttk.Label(master=login_frame, text="player 1:", font=("Helvetica, 14"))
player_1_label.pack()

player_1_name = tk.Entry(master=login_frame)
player_1_name.pack()

player_2_label = ttk.Label(master=login_frame, text="player 2:", font=("Helvetica, 14"))
player_2_label.pack()

player_2_name = tk.Entry(master=login_frame)
player_2_name.pack()

empty = ttk.Label(master=login_frame)
empty.pack()

start_button = tk.Button(master=login_frame, text="Start", command=start_game)
start_button.pack()

label = ttk.Label(master=header_frame, font=("Helvetica, 14"))
label.pack()

buttons=[[0,0,0],[0,0,0],[0,0,0]]
selections=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        button = tk.Button(master=play_zone_frame, height=5, width=10, command=lambda row=i,col=j : button_select(row,col))
        button.grid(row=i,column=j,padx=4,pady=4)
        buttons[i][j] = button

window.mainloop()