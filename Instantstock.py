import os
import tkinter as tk
import yfinance as yf

#InstStock = tk.Tk()
#InstStock.geometry('700x300')
#InstStock.title("Instanstock")

# current_stock_list = ['Tesla', 'Apple', 'Yahoo', 'Amazon' , 'Alphabet' , 'Facebook', 'Bitcoin']

tsla = yf.Ticker("TSLA")
aapl = yf.Ticker("AAPL")
amzn = yf.Ticker("AMZN")
goog = yf.Ticker("GOOG")
nvda = yf.Ticker("NVDA")
msft = yf.Ticker("MSFT")
amd = yf.Ticker("AMD")

print(tsla)
print(aapl)
print(amzn)
print(goog)
print(nvda)
print(msft)
print(amd)


tsla.info

tsla.history(period="max")


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


#InstStock.mainloop()