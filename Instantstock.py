import os
import tkinter as tk
import yfinance as yf

InstStock = tk.Tk()
InstStock.geometry('700x300')
InstStock.title("Instanstock")

# current_stock_list = ['Tesla', 'Apple', 'Yahoo', 'Amazon' , 'Alphabet' , 'Facebook', 'Bitcoin']

tsla.stock = yf.Ticker()
aapl.stock = yf.Ticker()
amzn.stock = yf.Ticker()
alph.stock = yf.Ticker()
goog.stock = yf.Ticker()
btc-usd.stock = yf.Ticker


tsla.info

tsla.history(period=max)


#for i in range(4):
#	for j in range(5):
#		frame = tk.Frame(
#			master=InstStock,
#			relief=tk.RAISED,
#			borderwidth=1
#		)
#		frame.grid(row=i, column=j)
#		label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#		label.pack()

# api = 
# Shows major stock listings
# Shows their daily movement 


InstStock.mainloop()