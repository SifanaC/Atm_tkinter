import tkinter as tk
from tkinter import messagebox as m
import time

balance = 10000
password = 1234

def check_pin():
    try:
        entered_pin = int(pin_entry.get())
        if entered_pin == password:
            show_options()
        else:
            m.showerror("Error", "Wrong PIN. Please try again.")
    except ValueError:
        m.showerror("Error", "Please enter a valid PIN (numeric).")

def show_options():
    main.withdraw()
    show_options.new_window = tk.Tk()
    show_options.new_window.title("ATM Options")
    show_options.new_window.geometry("650x450")
    show_options.new_window.configure(bg="#d7dae2")

    text_title = tk.Label(show_options.new_window, text='\nABC BANK',font=("arial",20,'bold'),fg="black",bg="#d7dae2")
    text_title.pack()

    text_label=tk.Label(show_options.new_window,text='PLEASE SELECT YOUR OPTION',font=("arial",12,'bold'),fg="navyblue",bg="#d7dae2")
    text_label.pack(pady=20)

    def withdraw_func():
        try:
            withdraw_amount = int(withdraw_entry.get())
            global balance
            if withdraw_amount > balance:
                m.showerror("Error", "Insufficient balance.")
            else:
                balance -= withdraw_amount
                m.showinfo("Success", f"{withdraw_amount} debited from your account successfully.")
                m.showinfo("Balance", f"Your remaining balance is {balance}")
        except ValueError:
            m.showerror("Error", "Please enter a valid amount.")

    def deposit_func():
        try:
            deposit_amount = int(deposit_entry.get())
            global balance
            balance += deposit_amount
            m.showinfo("Success", f"{deposit_amount} credited to your account successfully.")
            m.showinfo("Balance", f"Your total balance is {balance}")
        except ValueError:
            m.showerror("Error", "Please enter a valid amount.")
            
    def check_balance():
        m.showinfo("Balance", f"Your current balance is {balance}")

   
    withdraw_entry = tk.Entry(show_options.new_window)
    withdraw_entry.pack(pady=10)
    withdraw_button = tk.Button(show_options.new_window, text="WITHDRAW",font=("arial",10,'bold'),fg="white",bg="green", command=withdraw_func)
    withdraw_button.pack(pady=10)
    
    deposit_entry = tk.Entry(show_options.new_window)
    deposit_entry.pack(pady=10)
    deposit_button = tk.Button(show_options.new_window, text="DEPOSIT",font=("arial",10,'bold'),fg="white",bg="green", command=deposit_func)
    deposit_button.pack(pady=10)
    
    balance_button = tk.Button(show_options.new_window, text="CHECK BALANCE", font=("arial",10,'bold'),fg="white",bg="green",command=check_balance)
    balance_button.pack(pady=10)
    
    exit_button = tk.Button(show_options.new_window, text="EXIT", font=("arial",10,'bold'),fg="white",bg="red",command=show_options.new_window.destroy)
    exit_button.pack(pady=10) 
    
main = tk.Tk()
main.title("ATM")
main.geometry("600x400")
main.configure(bg="#d7dae2")

main_label=tk.Label(main,text='WELCOME TO ABC BANK',font=("arial",20,'bold'),fg="black",bg="#d7dae2")
main_label.pack(pady=10)

localtime = time.asctime(time.localtime(time.time()))

time_info = tk.Label(main,font=('aria',15,'bold'),text=localtime,fg ="black", bg ="#d7dae2")
time_info.pack(pady=10)

pin_label = tk.Label(main, text="ENTER YOUR ATM PIN:",font=("arial",12,'bold'),fg="navyblue",bg="#d7dae2")
pin_label.pack(pady=10)
pin_entry = tk.Entry(main, show="*")
pin_entry.pack(pady=10)
pin_button = tk.Button(main, text="SUBMIT",font=("arial",10,'bold'),fg="white",bg="green", command=check_pin)
pin_button.pack(pady=10)

main.mainloop()
