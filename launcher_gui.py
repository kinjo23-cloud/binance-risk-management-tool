import ctypes
import sys
import tkinter as tk
from threading import Thread
import subprocess

if sys.platform == "win32":
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)

def run_buy():
    Thread(target=lambda: subprocess.run(["python", "executebuy.py"])).start()

def run_sell():
    Thread(target=lambda: subprocess.run(["python", "executesell.py"])).start()

# GUI window
root = tk.Tk()
root.title("RISK MANAGEMENT TOOOL")
root.geometry("300x150")
root.configure(bg="orange")
#always above all windows
root.attributes("-topmost", True)



# Buy Button
buy_button = tk.Button(root, text="🚀 buy/long", command=run_buy, fg="white", bg="green", height=2, width=25)
buy_button.pack(pady=10)

# Sell Button
sell_button = tk.Button(root, text="🔻 sell/short", command=run_sell, fg="white", bg="red", height=2, width=25)
sell_button.pack(pady=10)

# Subtitle label
subtitle_label = tk.Label(root, text="Created by KingJo Lamattyn", font=("Arial", 8), bg="orange", fg="black")
subtitle_label.pack(pady=(0, 5))


# Start the GUI
root.mainloop()
