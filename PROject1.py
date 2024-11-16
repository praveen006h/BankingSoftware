from tkinter import *
import time
import pickle as pk

def login():
	dat_file = open("acc_data.dat",'rb')
	dat_dict = pk.load(dat_file)
	print(dat_dict)
	if e_accno.get().isalnum():
		if int(e_accno.get()) in dat_dict.keys():

			if dat_dict[int(e_accno.get())]["pin"] == e_pinno.get():
				global l_acgrnted
				l_acgrnted = Label(top,text = "      Logging in                  ",font = "aerial 10",fg = "blue")
				l_acgrnted.place(x=135,y=220)
				login_page()
			else:
				l_passwaring = Label(top,text = "   *Incorrect password*   ",font = "aerial 10",fg = "red")
				l_passwaring.place(x=130,y=220)
	else:
		l_accwaring = Label(top,text = "*Account No. not found*",font = "aerial 10",fg = "red")
		l_accwaring.place(x=135,y=220)

def clean_win(del_tup):
	for i in del_tup:
		i.destroy()

def login_page():
	dat_file = open("acc_data.dat","rb")
	dat_dict = pk.load(dat_file)
	u_name,u_nmum,u_pin,u_city,u_balance = list(dat_dict[int(e_accno.get())].values())

	def withdraw():
		clean_win((b_withd,b_depo,b_transf,b_bal))

	def deposit():
		clean_win((b_withd,b_depo,b_transf,b_bal))

	def transfer():
		clean_win((b_withd,b_depo,b_transf,b_bal))

	def balance():
		clean_win((b_withd,b_depo,b_transf,b_bal))

	clean_win((l1,l2,l3,l4,e_accno,e_pinno,b_mask,b_create,b_login,l_acgrnted))
	top.geometry("900x500")
	b_withd = Button(top,command = withdraw,text = "Withdraw",font = "aerial 20 bold",width = 14)
	b_withd.place(x = 600, y = 50)
	b_depo = Button(top,command = deposit, text = "Deposit",font = "aerial 20 bold",width = 14)
	b_depo.place(x = 600,y = 150)
	b_transf = Button(top,command = transfer,text = "Money Transfer",font = "aerial 20 bold",width = 14)
	b_transf.place(x = 600,y = 250)
	b_bal = Button(top,command = clean_win((b_withd,b_depo,b_transf)),text = "Balance",font = "aerial 20 bold",width = 14)
	b_bal.place(x = 600,y = 350)

def create_acc():

	def sav_acc():
		dat_file = open("acc_data.dat",'rb')
		existing_dict = pk.load(dat_file)
		dat_file.close()
		acc_dict = {max(existing_dict)+1:{'name':e_name.get(),'mnum':e_mnum.get(),'pin':e_cnpinno.get(),'city':e_city.get(),'balance':0}}
		existing_dict.update(acc_dict)
		print(existing_dict,'\n',acc_dict)
		dat_file=open("acc_data.dat",'wb')
		pk.dump(existing_dict,dat_file)
		dat_file.close()

		n_acc.destroy()
	n_acc = Tk()
	n_acc.title("Create New Account")
	n_acc.geometry("500x400")
	n_acc.resizable(0,0)

	def mask_pass():
		e_npinno.config(show = "")
		e_cnpinno.config(show = "")
		b_mask.config(text = "Hide ",command = unmask_pass,font = "aerial 8")

	def unmask_pass():
		e_npinno.config(show = "*")
		e_cnpinno.config(show = "*")
		b_mask.config(text = "Show",command = mask_pass,font = "aerial 8")


	l1 = Label(n_acc,text = "Enter the details",font = "aerial 25 underline")
	l1.place(x = 125, y = 20)
	l2 = Label(n_acc, text = "Enter Name           :", font = "aerial 10 ")
	l2.place(x = 50,y = 70)
	e_name = Entry(n_acc)
	e_name.place(x = 190,y = 70)
	l3 = Label(n_acc, text = "Enter Mobile No     :", font = "aerial 10 ")
	l3.place(x = 50,y = 120)
	e_mnum = Entry(n_acc)
	e_mnum.place(x = 190,y = 120)
	l4 = Label(n_acc, text = "Enter pin                :", font = "aerial 10 ")
	l4.place(x = 50,y = 170)
	e_npinno = Entry(n_acc,show = '*')
	e_npinno.place(x = 190, y = 170)
	l5 = Label(n_acc, text = "Confirm Your pin     :", font = "aerial 10 ")
	l5.place(x = 50,y = 220)
	e_cnpinno = Entry(n_acc,show="*")
	e_cnpinno.place(x = 190, y = 220)
	l6 = Label(n_acc, text = "Enter your city        :", font = "aerial 10 ")
	l6.place(x = 50,y = 260)
	e_city = Entry(n_acc)
	e_city.place(x = 190, y = 260)
	b_mask = Button(n_acc, text = "Show",command = mask_pass, font = "aerial 8")
	b_mask.place(x = 320,y = 195)
	b_savenquit = Button (n_acc, text = "Save & Quit",command = sav_acc)
	b_savenquit.place(x = 70, y = 300)
	b_cancel = Button(n_acc,text = "cancel", command = n_acc.destroy)
	b_cancel.place(x = 200, y = 300)

def mask_pass():
	e_pinno.config(show = "")
	b_mask.config(text = "Hide ",command = unmask_pass,font = "aerial 8")

def unmask_pass():
	e_pinno.config(show = "*")
	b_mask.config(text = "Show",command = mask_pass,font = "aerial 8")

def main():
	global top,l1,l2,l3,l4,e_accno,e_pinno,b_login,b_mask,b_create
	top = Tk()
	top.title("Banking Software")
	top.geometry('400x300')
	top.resizable(0,0)
	l1 = Label(top,text = "BANKING SOFTWARE", font = "aerial 25 bold underline")
	l1.place(x = 18, y = 20)

	l2 = Label(top, text = "Enter Account No.:", font = "aerial 10 ")
	l2.place(x = 50,y = 100)
	e_accno = Entry(top)
	e_accno.place(x = 190,y = 100)

	l3 = Label(top, text = "Enter pin            :", font = "aerial 10 ")
	l3.place(x = 50,y = 150)
	e_pinno = Entry(top,show = "*")
	e_pinno.place(x = 190, y = 150)

	b_mask = Button(top, text = "Show",command = mask_pass, font = "aerial 8")
	b_mask.place(x = 320,y = 147)
	l4 = Label(top,text = "Don't Have An Account ?",font = "aerial 8 underline")
	l4.place(x = 135,y = 247)
	b_create = Button(top,text = "Create Account",command = create_acc, font = "aerial 8 ")
	b_create.place(x = 150, y = 270)
	b_login = Button(top, text = "Login", command = login, font = "aerial 13 bold")
	b_login.place(x = 160, y = 180)

	top.mainloop()

if __name__ == '__main__':
	main()


