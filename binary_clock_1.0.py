import customtkinter as ctk # type: ignore
from datetime import datetime

ctk.set_appearance_mode("dark")

# ------------------------------------------------------------------------------------------------------------- #
                                                               
#	 $$$$$$$\  $$\                                                $$$$$$\  $$\                     $$\      	#
#	 $$  __$$\ \__|                                              $$  __$$\ $$ |                    $$ |      	#
#	 $$ |  $$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\       $$ /  \__|$$ | $$$$$$\   $$$$$$$\ $$ |  $$\ 	#
#	 $$$$$$$\ |$$ |$$  __$$\  \____$$\ $$  __$$\ $$ |  $$ |      $$ |      $$ |$$  __$$\ $$  _____|$$ | $$  |	#
#	 $$  __$$\ $$ |$$ |  $$ | $$$$$$$ |$$ |  \__|$$ |  $$ |      $$ |      $$ |$$ /  $$ |$$ /      $$$$$$  / 	#
#	 $$ |  $$ |$$ |$$ |  $$ |$$  __$$ |$$ |      $$ |  $$ |      $$ |  $$\ $$ |$$ |  $$ |$$ |      $$  _$$<  	#
#	 $$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |$$ |      \$$$$$$$ |      \$$$$$$  |$$ |\$$$$$$  |\$$$$$$$\ $$ | \$$\ 	#
#	 \_______/ \__|\__|  \__| \_______|\__|       \____$$ |       \______/ \__| \______/  \_______|\__|  \__|	#
#                                             $$\   $$ |                                                  		#
#                                             \$$$$$$  |                                                  		#
#                                              \______/                                                   		#
#                          _     ___ 																			#
#          _ _  ___  _ _  / |   |   |																			#
#         | | |/ ._>| '_> | | _ | / |																			#
#         |__/ \___.|_|   |_|<_>`___'																			#

# ------------------------------------------------------------------------------------------------------------- #

ON_COLOR = "#51AC51"
OFF_COLOR = "#292929"

time_list = []
binary_time = []

buttons = []

binary_time = []
display_texts = []

# --------------------------------------------------------------------------------------

def on_exit():
	label.configure(text="Exiting app...")
	root.after(500, exit)
	
def update_time():
	current_time = datetime.now().strftime("%H:%M:%S")
	time_display.configure(text=f"Current time: {current_time}")

	time_list = datetime.now().strftime("%H%M%S")
	time_list = list(time_list)

	binary_time = []
	for i in time_list:
		binary_val = format(int(i), "04b")
		binary_time.append(binary_val)

	for col in range(len(binary_time)):                                      # iterates through all columns: length of 'binary_time' is total number of columns printed by time_list, which is 6 as its prints HH:MM:SS
		display_texts[col].configure(text=time_list[col])                    # changes the column's display text to the time
		for row in range(len(binary_time[col])):                             # iterates for the length of that column's value (default 4)
			binary_unit = str(binary_time[col])[row]                         # re/assigns variable to the nth character of that column's binary time with n = row
			buttons[row + (col * 4)].configure(text=binary_unit)             # configures the text of the button in that row in that column
			if binary_unit == "1":                                           # changes button's colour depending on if the just-assigned text is 1 or 0
				buttons[row + (col * 4)].configure(fg_color=ON_COLOR)
			else:
				buttons[row + (col * 4)].configure(fg_color=OFF_COLOR)
	
	root.after(1000, update_time)

# --------------------------------------------------------------------------------------

# main window

root = ctk.CTk()
root.title("Binary Clock Display")
root.configure(bg="#222222")
root.geometry("505x450")

root.overrideredirect(True)

label = ctk.CTkLabel(root, text=" ")
label.grid(row=0, column=5, columnspan=4, padx=10, pady=10)

time_display = ctk.CTkLabel(root, text="Time will be displayed here")
time_display.grid(row=1, column=3, columnspan=7, padx=10, pady=10)

root.grid_columnconfigure(11, weight=1)

clock_frame = ctk.CTkFrame(root, fg_color="#2D2D2D")
clock_frame.grid(row=2, column=1, columnspan=10, padx=10, pady=10)

clock_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
clock_frame.rowconfigure((5, 6, 7, 8), weight=1)

labels = ["HrTens", "HrOnes", "MinTens", "MinOnes", "SecTens", "SecOnes"]

for col_idx in range(6):
	btn = ctk.CTkLabel(clock_frame, text=" ", font=("Courier", 20))
	btn.grid(row=9, column=col_idx+1, padx=10, pady=10)
	display_texts.append(btn)

# --------------------------------------------------------------------------------------

# Clock buttons

#hours
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_h = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=OFF_COLOR, width=50, height=50, corner_radius=15, hover=False)
	btn_h.grid(row=row_idx, column=1, padx=5, pady=5)
	buttons.append(btn_h) 
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_h2 = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=OFF_COLOR, width=50, height=50, corner_radius=15, hover=False)
	btn_h2.grid(row=row_idx, column=2, padx=5, pady=5)
	buttons.append(btn_h2)

#minutes
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_m = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=OFF_COLOR, width=50, height=50, corner_radius=15, hover=False)
	btn_m.grid(row=row_idx, column=3, padx=5, pady=5)
	buttons.append(btn_m)
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_m2 = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=OFF_COLOR, width=50, height=50, corner_radius=15, hover=False)
	btn_m2.grid(row=row_idx, column=4, padx=5, pady=5)
	buttons.append(btn_m2)

#seconds
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_s = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=OFF_COLOR, width=50, height=50, corner_radius=15, hover=False)
	btn_s.grid(row=row_idx, column=5, padx=5, pady=5)
	buttons.append(btn_s)
for row_idx in range(4):
	binary_value = 2 ** (3 - row_idx)
	btn_s2 = ctk.CTkButton(clock_frame, text=str(binary_value), fg_color=OFF_COLOR, width=50, height=50, corner_radius=15, hover=False)
	btn_s2.grid(row=row_idx, column=6, padx=5, pady=5)
	buttons.append(btn_s2)

# Other buttons

start_button = ctk.CTkButton(root, text="Start", command=update_time, height=3, width=7)
start_button.grid(row=0, column=0, padx=10, pady=10)

exit_button = ctk.CTkButton(root, height=8, width=10,text="Exit", fg_color="#CC4646", hover_color="#8F2C2C", command=on_exit)
exit_button.grid(row=0, column=12, sticky="e", padx=10, pady=10)

# ---------------------------------------------------------------------------------------

root.mainloop()

#      .--. 
#   .'     )
# <     --: 
#   `.     )
#      `--'      
