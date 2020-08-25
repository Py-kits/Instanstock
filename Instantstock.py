import os
import tkinter as tk
#import yfinance as yf

InstStock = tk.Tk()
InstStock.geometry('700x300')
InstStock.title("Instanstock")

# stock_list = ['Tesla', 'Yahoo','Amazon','Alphabet','Facebook']

for i in range(4):
	for j in range(5):
		frame = tk.Frame(
			master=window,
			relief=tk.RAISED,
			borderwidth=1
		)
		frame.grid(row=i, column=j)
		label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
		label.pack()

# api = 
# Shows major stock listings
# Shows their daily movement 


InstStock.mainloop()