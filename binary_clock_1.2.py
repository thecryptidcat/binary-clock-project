import customtkinter as ctk # type: ignore
import time
from datetime import datetime

#ctk.set_appearance_mode("dark")

# ------------------------------------------------------------------------------------------------------------- #
#																												#
#      _   _                              _    _    _             _    _   										#                                               .--.
#    _| |_| |_  ___  ___  _ _  _ _  ___ _| |_ <_> _| | ___  ___ _| |_ |/ ___									                                                 `.  \
#     | | | . |/ ._>/ | '| '_>| | || . \ | |  | |/ . |/ | '<_> | | |    <_-<									                                                   \  \
#     |_| |_|_|\___.\_|_.|_|  `_. ||  _/ |_|  |_|\___|\_|_.<___| |_|    /__/									                                                    .  \
#                              <___'|_|                                     									                                                    :   .
#																												                                                    |    .
#                                                                                                                                                                   |    :
#                                                                                                                                                                   |    |                                                  
#	 $$$$$$$\  $$\                                                $$$$$$\  $$\                     $$\      	    ..._  ___                                       |    |
#	 $$  __$$\ \__|                                              $$  __$$\ $$ |                    $$ |      	   `."".`''''""--..___                              |    |
#	 $$ |  $$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\       $$ /  \__|$$ | $$$$$$\   $$$$$$$\ $$ |  $$\ 	   ,-\  \             ""-...__         _____________/    |
#	 $$$$$$$\ |$$ |$$  __$$\  \____$$\ $$  __$$\ $$ |  $$ |      $$ |      $$ |$$  __$$\ $$  _____|$$ | $$  |	   / ` " '                    `""""""""                  .
#	 $$  __$$\ $$ |$$ |  $$ | $$$$$$$ |$$ |  \__|$$ |  $$ |      $$ |      $$ |$$ /  $$ |$$ /      $$$$$$  / 	   \                                                      L
#	 $$ |  $$ |$$ |$$ |  $$ |$$  __$$ |$$ |      $$ |  $$ |      $$ |  $$\ $$ |$$ |  $$ |$$ |      $$  _$$<  	   (>                                                      \
#	 $$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |$$ |      \$$$$$$$ |      \$$$$$$  |$$ |\$$$$$$  |\$$$$$$$\ $$ | \$$\ 	  /                                                         \
#	 \_______/ \__|\__|  \__| \_______|\__|       \____$$ |       \______/ \__| \______/  \_______|\__|  \__|	  \_    ___..---.                                            L
#                                     	         $$\   $$ |                                                		    `--'         '.                                           \
#                                     	         \$$$$$$  |                                                		                   .                                           \_
#                                     	          \______/                                                 		                  _/`.                                           `.._
#                                                                                                                              .'     -.                                             `.
#      															                    _     _ 					              /     __.-Y     /"'''''-...___,...--------.._            |
#     														        _ _  ___  _ _  / |   / |					             /   _."    |    /                ' .      \   '---..._    |
#     														       | | |/ ._>| '_> | | _ | |					            /   /      /    /                _,. '    ,/           |   |
#      															   |__/ \___.|_|   |_|<_>|_|					#           \_,'     _.'   /              /''     _,-'            _|   |
#                                                                                                               #                   '     /               `-----''               /     |
# ------------------------------------------------------------------------------------------------------------- #                   `...-'                                       `...-'

c1 = "#3ec71f"
c2 = "#006aff"
c3 = "#c82727"
c4 = "#ffffff"

buttn_text_color = "#ffffff"
inv_text_color = "#000000"
on_color = c1
off_color = "transparent"

#backg_col = "#1B1B1B"

show_bin_status = "Yes"

time_list = []
binary_time = []
col_binarylen_f = ["02b", "04b", "03b", "04b", "03b", "04b"]

buttons = []

binary_time = []
display_texts = []

# --------------------------------------------------------------------------------------

def on_exit():
	label.configure(text="Exiting app...")
	root.after(500, exit)


def time_update():
	current_time = datetime.now().strftime("%H:%M:%S")
	time_display.configure(text=f"{current_time}")
	update_display()

	now = time.time()
	ms_left = int((1.0 - (now % 1.0)) * 1000)								# uses 'now' at that point in the loop to find the time remaining til the next second
	if ms_left <= 0:														# if ms_left is 0 then changes to 1000ms
		ms_left = 1000
	root.after(ms_left, time_update)										# updates the time after the time remaining til the next second

def update_display():
	label.configure(text=" ")

	current_time = datetime.now().strftime("%H%M%S")
	time_list = list(current_time)

	binary_time = []
	for i in range(len(time_list)):
		binary_val = format(int(time_list[i]), col_binarylen_f[i])				# assigns variable at each point in the list of each digit in the time to its correct binary format (depending on its column/required bits)
		binary_time.append(binary_val)											# appends variable to the list of each binary digit of the time

	buttn_num = 0
	for col in range(len(binary_time)):											# iterates through all columns: length of 'binary_time' is total number of columns printed by time_list, which is 6 as its prints HH:MM:SS
		display_texts[col].configure(text=time_list[col])						# changes the column's display text to the time
		for row in range(len(binary_time[col])):								# iterates for the length of that column's value
			binary_unit = str(binary_time[col])[row]							# re/assigns variable to the nth character of that column's binary time with n = row
			if show_bin_status == "Yes":										# if showing binary is on:
				buttons[buttn_num].configure(text=binary_unit)					# configures the text of the button in that row in that column
			else:																# otherwise empties the text
				buttons[buttn_num].configure(text=" ")
			if binary_unit == "1":												# changes button's colour depending on if the just-assigned text is 1 or 0
				buttons[buttn_num].configure(fg_color=on_color)					
				if on_color != c4:												# if the chosen colour is not white, changes the text colour to	chosen colour
					buttons[buttn_num].configure(text_color=buttn_text_color)
				else:															# else text colour is white, changes text colour to inverted (black)
					buttons[buttn_num].configure(text_color=inv_text_color)
			else:																# else button is off, changes to off colour
				buttons[buttn_num].configure(fg_color=off_color)
				buttons[buttn_num].configure(text_color=buttn_text_color)		# changes colour to usual colour if off (accomodates if colour is white to turn colour back after button becomes off from on)
			buttn_num = buttn_num + 1											# used to iterate through the button list

#def menu_choice(choice):

def change_buttn_col(choice):
	global on_color
	
	if choice == "Green":
		on_color=c1
		label.configure(text="Colour changed to green")
	elif choice == "Blue":
		on_color=c2
		label.configure(text="Colour changed to blue")
	elif choice == "Red":
		on_color=c3
		label.configure(text="Colour changed to red")
	elif choice == "White":
		on_color=c4
		label.configure(text="Colour changed to white")
	else:
		c_custom=str(choice)
		on_color=c_custom

def change_show_bin(choice):
	global show_bin_status
	show_bin_status=str(choice)
	print(show_bin_status)

def change_text_col(choice):
	print("Changing text")

# --------------------------------------------------------------------------------------

# main window

root = ctk.CTk()
root.title("Binary Clock Display")
root.configure(bg_color="#ffffff")
root.geometry("500x600")

#root.overrideredirect(True)

# ------------------------------------------------

top_frame = ctk.CTkFrame(root, fg_color="transparent")
top_frame.grid(row=0, column=1, columnspan="10", padx=5, pady=10, sticky="ew")
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)

label = ctk.CTkLabel(top_frame, text=" ", font=("Consolas", 15))
label.grid(row=0, column=0, padx=10, pady=10)

time_display = ctk.CTkLabel(top_frame, text="Time will be displayed here", font=("Consolas", 15))
time_display.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

#root.grid_columnconfigure(11, weight=1)

# ------------------------------------------------

clock_frame = ctk.CTkFrame(root, fg_color="transparent")
clock_frame.grid(row=2, column=1, columnspan=10, padx=10, pady=5)

clock_frame.rowconfigure((5, 6, 7, 8), weight=1)

labels = ["HrTens", "HrOnes", "MinTens", "MinOnes", "SecTens", "SecOnes"]

for col_idx in range(6):
	btn = ctk.CTkLabel(clock_frame, text=" ", font=("Consolas", 20))
	btn.grid(row=9, column=col_idx+1, padx=10, pady=10)
	display_texts.append(btn)

# ------------------------------------------------
	
menu_frame= ctk.CTkFrame(root, fg_color="#2D2D2D")
menu_frame.grid(row=11, column=1, padx=10, pady=10)

settings_title = ctk.CTkLabel(root, text="Settings:", font=("Consolas", 15))
settings_title.grid(row=10, column=1, columnspan=4, padx=5, pady=5)


color_menu = ctk.CTkComboBox(master = menu_frame, font=("Consolas", 12), values=["Green", "Blue", "Red", "White"], command=change_buttn_col)
color_menu.grid(row=1, column=3, padx=10, pady=10)
colour_menu_title = ctk.CTkLabel(menu_frame, text="Clock colour", font=("Consolas", 12))
colour_menu_title.grid(row=1, column=1, padx=10, pady=10)

show_bin_menu = ctk.CTkOptionMenu(master = menu_frame, font=("Consolas", 12), values=["Yes", "No"], command=change_show_bin)
show_bin_menu.grid(row=2, column=3, padx=10, pady=10)
colour_menu_title = ctk.CTkLabel(menu_frame, text="Show binary?", font=("Consolas", 12))
colour_menu_title.grid(row=2, column=1, padx=10, pady=10)

text_col_menu = ctk.CTkComboBox(master= menu_frame, font=("Consolas", 12), values=["Opt1", "Opt2"], command=change_text_col)
text_col_menu.grid(row=3, column=3, padx=10, pady=10)



# --------------------------------------------------------------------------------------

# Clock buttons

#hours
for row_idx in range(2):
	binary_value = 2 ** (1 - row_idx)
	btn_h = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=off_color, text_color=buttn_text_color, font=("Consolas", 15), width=50, height=50, corner_radius=15, hover=False)
	btn_h.grid(row=row_idx + 2, column=1, padx=5, pady=5)
	buttons.append(btn_h) 
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_h2 = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=off_color, text_color=buttn_text_color, font=("Consolas", 15), width=50, height=50, corner_radius=15, hover=False)
	btn_h2.grid(row=row_idx, column=2, padx=5, pady=5)
	buttons.append(btn_h2)

#minutes
for row_idx in range(3):
	binary_value = 2 ** (2 - row_idx)
	btn_m = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=off_color, text_color=buttn_text_color, font=("Consolas", 15), width=50, height=50, corner_radius=15, hover=False)
	btn_m.grid(row=row_idx + 1, column=3, padx=5, pady=5)
	buttons.append(btn_m)
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_m2 = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=off_color, text_color=buttn_text_color, font=("Consolas", 15), width=50, height=50, corner_radius=15, hover=False)
	btn_m2.grid(row=row_idx, column=4, padx=5, pady=5)
	buttons.append(btn_m2)

#seconds
for row_idx in range(3):
	binary_value = 2 ** (2 - row_idx)
	btn_s = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=off_color, text_color=buttn_text_color, font=("Consolas", 15), width=50, height=50, corner_radius=15, hover=False)
	btn_s.grid(row=row_idx + 1, column=5, padx=5, pady=5)
	buttons.append(btn_s)
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_s2 = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=off_color, text_color=buttn_text_color, font=("Consolas", 15), width=50, height=50, corner_radius=15, hover=False)
	btn_s2.grid(row=row_idx, column=6, padx=5, pady=5)
	buttons.append(btn_s2)

# Other buttons

start_button = ctk.CTkButton(root, text="Start", command=time_update, height=3, width=7)
start_button.grid(row=0, column=0, padx=10, pady=10, sticky="n")

exit_button = ctk.CTkButton(root, height=8, width=10,text="Exit", fg_color="#CC4646", hover_color="#8F2C2C", command=on_exit)
exit_button.grid(row=0, column=12, padx=15, pady=10, sticky="n")

# ---------------------------------------------------------------------------------------

root.mainloop()

#      .--. 
#   .'     )
# <     --: 
#   `.     )
#      `--'      
