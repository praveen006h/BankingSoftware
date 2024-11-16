from tkinter import Tk,Label,Entry,Button
import mysql.connector as mycon

con = mycon.connect(host = 'localhost', port = '3306', charset = 'utf8', user = 'root' ,password = 'root')
cur = con.cursor()
cur.execute("create database if not exists bankingsystem")
cur.execute("use bankingsystem")
cur.execute("create table if not exists userinfo (acc_no int, username varchar(20), mobile_number int, password varchar(20), city varchar(20), balance int)")
con.commit()

def clean_win(del_tup):
	try:
		for i in del_tup:
			i.destroy()

	except:
		pass

def login():

	def login_page():
		cur.execute("select * from userinfo where acc_no = {}".format(e_accno.get()))
		acc_list = cur.fetchall()
		a = input(acc_list)
		u_name,u_nmum,u_pin,u_city,u_balance = acc_list
		clean_win((l1,l2,l3,l4,e_accno,e_pinno,b_mask,b_create,b_login,l_accwaring))
		top1 = Tk()
		top1.title("Banking Software - "+u_name)
		top1.geometry("450x600")
		top1.resizable(0,0)

		def transaction_result():
			msg = Tk()
			msg.geometry("500x200")
			msg.title("Transaction Success!!")
			l_msg = Label(msg,text = "Transaction Success \n Your Balance : "+str( dat_dict[acc_no]["balance"]),font = 'aerial 20 bold')
			l_msg.place(x=70,y = 40)
			b_wmsg = Button(msg,text = "Okay",command = msg.destroy,font = "aerial 15 ")
			b_wmsg.place(x = 200,y = 150)

		def cancel():
			top1.destroy()
			login_page()

		def withdraw():
			def w_draw():
				u_wbalance = dat_dict[acc_no]["balance"] 
				l_inv_wdraw = Label(top1,text = "   "*20,font = "aerial 15")
				l_inv_wdraw.place(x = 150,y = 260)

				if e_wdraw.get().isdigit():
					wdraw_amt = int(e_wdraw.get())

					if u_wbalance >= wdraw_amt and wdraw_amt >= 0:
						cur_balance = u_wbalance-wdraw_amt
						dat_dict[acc_no]["balance"] = cur_balance
						
						dat_sav_file = open("acc_data.dat","wb")
						pk.dump(dat_dict,dat_sav_file)
						dat_sav_file.close()
						
						transaction_result()
						e_wdraw.delete(0,'end')

					if u_wbalance < wdraw_amt:
						msg = Tk()
						msg.geometry("500x200")
						msg.title("Insufficient Funds1")
						l_msg = Label(msg,text = "Insufficient Balance Available",font = 'aerial 20 bold underline',fg = 'red')
						l_msg.place(x=70,y = 40)
						l_msg2 = Label(msg,text = "    Your Balance : "+str(u_wbalance),font = 'aerial 20 bold')
						l_msg2.place(x=70,y = 80)
						b_wmsg = Button(msg,text = "Okay",command = msg.destroy,font = "aerial 15 ")
						b_wmsg.place(x = 200,y = 150)

				else :
					l_inv_wdraw = Label(top1,text = "*Invalid Input*",font = "aerial 15",fg = "red")
					l_inv_wdraw.place(x = 150,y = 260)


			top1.geometry("450x350")
			clean_win((b_withd,b_depo,b_transf,b_bal,b_back,l_loginchoose,l_greet))

			l_wdraw = Label(top1,text = "Enter Amount to Withdraw:",font = "aerial 20 bold")
			l_wdraw.place(x = 20,y = 20)
			e_wdraw = Entry(top1,width = 10, font = "aerial 25")
			e_wdraw.place(x = 130, y = 80)
			b_wdraw = Button(top1,command = w_draw,text = "Withdraw",font = "aerial 15 ")
			b_wdraw.place(x = 70,y= 200 )
			b_cancel = Button(top1,command = cancel,text = "Back",font = "aerial 15")
			b_cancel.place(x = 290,y = 200)

		def deposit():
			def _dep():
				u_wbalance = dat_dict[acc_no]["balance"] 
				l_inv_wdraw = Label(top1,text = "   "*20,font = "aerial 15")
				l_inv_wdraw.place(x = 150,y = 260)

				if e_dep.get().isdigit():
					dep_amt = int(e_dep.get())
					u_wbalance += dep_amt
					dat_dict[acc_no]["balance"] = u_wbalance
					transaction_result()
					e_dep.delete(0,'end')

					dat_sav_file = open("acc_data.dat","wb")
					pk.dump(dat_dict,dat_sav_file)
					dat_sav_file.close()

				else :
					l_inv_wdraw = Label(top1,text = "*Invalid Input*",font = "aerial 15",fg = "red")
					l_inv_wdraw.place(x = 150,y = 260)

			clean_win((b_withd,b_depo,b_transf,b_bal,b_back,l_loginchoose,l_greet))
			top1.geometry("450x350")
			l_dep = Label(top1,text = "Enter Amount to Deposit :",font = "aerial 20 bold")
			l_dep.place(x = 20,y = 20)
			e_dep = Entry(top1,width = 10, font = "aerial 25")
			e_dep.place(x = 130, y = 80)
			b_dep = Button(top1,command = _dep,text = "Deposit",font = "aerial 15 ")
			b_dep.place(x = 70,y= 200 )
			b_cancel = Button(top1,command = cancel,text = "Back",font = "aerial 15")
			b_cancel.place(x = 290,y = 200)

		def transfer():
			def trnsfr_acc():
				u_wbalance = dat_dict[acc_no]["balance"] 
				l_inv_wdraw = Label(top1,text = "   "*20,font = "aerial 15")
				l_inv_wdraw.place(x = 210,y = 60)
				l_inv_wdraw1 = Label(top1,text = "   "*20,font = "aerial 15")
				l_inv_wdraw1.place(x = 210,y = 200)

				if not e_trnsfr_ac.get().isdigit():
					if e_trnsfr_ac.get() == '':
						l_inv_wdraw = Label(top1,text = "*Enter Account No.*",font = "aerial 12",fg = "red")
						l_inv_wdraw.place(x = 210,y = 60)

					else:	
						l_inv_wdraw = Label(top1,text = "*Invalid Account No.*",font = "aerial 12",fg = "red")
						l_inv_wdraw.place(x = 210,y = 60)

				if not e_trnsfr_amt.get().isdigit():
					if e_trnsfr_amt.get() == '':
						l_inv_wdraw = Label(top1,text = "*Enter Amount *",font = "aerial 12",fg = "red")
						l_inv_wdraw.place(x = 210,y = 200)

					else:
						l_inv_wdraw = Label(top1,text = "*Invalid Amount Entered*",font = "aerial 12",fg = "red")
						l_inv_wdraw.place(x = 210,y = 200)

				if e_trnsfr_ac.get().isdigit() and e_trnsfr_amt.get().isdigit():
					trnsfr_ac = int(e_trnsfr_ac.get() )
					trnsfr_amt = int(e_trnsfr_amt.get())

					if trnsfr_ac in dat_dict.keys() and trnsfr_amt>0 and trnsfr_amt <= u_wbalance:
						if trnsfr_ac != acc_no:
							cur_balance = u_wbalance - trnsfr_amt
							a_wbalance =  dat_dict[trnsfr_ac]["balance"]
							a_wbalance += trnsfr_amt

							dat_dict[acc_no]["balance"] = cur_balance
							dat_dict[trnsfr_ac]["balance"] = a_wbalance

							dat_sav_file = open("acc_data.dat","wb")
							pk.dump(dat_dict,dat_sav_file)
							dat_sav_file.close()

							e_trnsfr_ac.delete(0,"end")
							e_trnsfr_amt.delete(0,'end')

							transaction_result()

						else:
							msg = Tk()
							msg.geometry("700x200")
							msg.title("Invalid Account No. Entered")
							l_msg = Label(msg,text = "Transfer Account No. Cannot Be Your Account No.",font = 'aerial 20 bold underline',fg = 'red')
							l_msg.place(x=12,y = 40)
							b_wmsg = Button(msg,text = "Okay",command = msg.destroy,font = "aerial 15 ")
							b_wmsg.place(x = 310,y = 150)
						
					if trnsfr_ac not in dat_dict.keys():
						l_inv_wdraw = Label(top1,text = "*Account No. Not Found",font = "aerial 12",fg = "red")
						l_inv_wdraw.place(x = 210,y = 60)

					if trnsfr_amt > u_wbalance:
						msg = Tk()
						msg.geometry("500x200")
						msg.title("Insufficient Funds")
						l_msg = Label(msg,text = "Insufficient Balance Available",font = 'aerial 20 bold underline',fg = 'red')
						l_msg.place(x=70,y = 40)
						l_msg2 = Label(msg,text = "    Your Balance : "+str(u_wbalance),font = 'aerial 20 bold')
						l_msg2.place(x=70,y = 80)
						b_wmsg = Button(msg,text = "Okay",command = msg.destroy,font = "aerial 15 ")
						b_wmsg.place(x = 200,y = 150)

			clean_win((b_withd,b_depo,b_transf,b_bal,b_back,l_loginchoose,l_greet))
			top1.geometry("450x350")
			l_trnsfr_ac = Label(top1,text = "Enter Account No. to Transfer :",font = "aerial 20 bold")
			l_trnsfr_ac.place(x = 20,y = 20)
			l_trnsfr_amt = Label(top1,text = "Enter Amount to Transfer :",font = "aerial 20 bold")
			l_trnsfr_amt.place(x = 20,y = 160)

			e_trnsfr_ac = Entry(top1,width = 10, font = "aerial 25")
			e_trnsfr_ac.place(x = 20, y = 60)
			e_trnsfr_amt = Entry(top1,width = 10, font = "aerial 25")
			e_trnsfr_amt.place(x = 20, y = 200)

			b_trnsfr = Button(top1,command = trnsfr_acc,text = "Transfer",font = "aerial 15 ")
			b_trnsfr.place(x = 70,y= 280 )
			b_cancel = Button(top1,command = cancel,text = "Back",font = "aerial 15")
			b_cancel.place(x = 290,y = 280)

		def balance():
			clean_win((b_withd,b_depo,b_transf,b_bal,b_back,l_loginchoose,l_greet))
			top1.geometry("600x200")
			top1.title = ("Balance - "+dat_dict[acc_no]["name"])
			u_wbalance = dat_dict[acc_no]["balance"]
			l_balance = Label(top1,text = "Your Account Balance: "+str(u_wbalance),font = "aerial 20 bold")
			l_balance.place(x=100,y=70)
			b_cancel = Button(top1,command = cancel,text = "Back",font = "aerial 15")
			b_cancel.place(x = 270,y = 150)

		def logout():
			clean_win((b_withd,b_depo,b_transf,b_bal,b_back,l_loginchoose,l_greet))
			top1.destroy()
			main()

		l_greet = Label(top1,text = "Hello "+u_name+",", font = "aerial 20 bold underline")
		l_greet.place(x = 30,y = 15)
		l_loginchoose = Label(top1,text = "Choose Any Option",font = "aerial 20 bold underline")
		l_loginchoose.place(x = 30,y = 50)

		b_withd = Button(top1,command = withdraw,text = "Withdraw",font = "aerial 20 bold",width = 14)
		b_withd.place(x = 100, y = 100)
		b_depo = Button(top1,command = deposit, text = "Deposit",font = "aerial 20 bold",width = 14)
		b_depo.place(x = 100,y = 200)
		b_transf = Button(top1,command = transfer,text = "Money Transfer",font = "aerial 20 bold",width = 14)
		b_transf.place(x = 100,y = 300)
		b_bal = Button(top1,command = balance,text = "Balance",font = "aerial 20 bold",width = 14)
		b_bal.place(x = 100,y = 400)
		b_back = Button(top1,command = logout,text = "Log Out",font = "aerial 20 bold",width = 14)
		b_back.place(x = 100,y = 500)

	global l_accwaring
	cur.execute("select * from userinfo")
	dat = cur.fetchall()
	u_accno = dat
	input(dat)
	l_accwaring = Label(top,text = "  "*30,font = "aerial 10",fg = "red")
	l_accwaring.place(x=130,y=220)

	if e_accno.get().isdigit():
		if int(e_accno.get()) in u_accno and e_pinno.get() != '':
			if dat_dict[int(e_accno.get())]["pin"] == e_pinno.get():
				l_accwaring = Label(top,text = "      Logging in                  ",font = "aerial 10",fg = "blue")
				l_accwaring.place(x=135,y=220)
				acc_no = int(e_accno.get())
				top.destroy()
				login_page()

			else:
				l_accwaring = Label(top,text = "   *Incorrect password*   ",font = "aerial 10",fg = "red")
				l_accwaring.place(x=130,y=220)
		else:
			l_accwaring = Label(top,text = "*Account No. not found*" ,font = "aerial 10",fg = "red")
			l_accwaring.place(x=130,y=220)
	else:
		l_accwaring = Label(top,text = "*Invalid Account No.*",font = "aerial 10",fg = "red")
		l_accwaring.place(x=135,y=220)

def create_acc():

	def sav_acc():
		def accept_accno():
			nn_acc.destroy()

		dat_file = open("acc_data.dat",'rb')
		existing_dict = pk.load(dat_file)
		dat_file.close()	
		condition = e_name.get() != "" and e_mnum.get() != '' and e_npinno.get() != '' and e_cnpinno.get() != '' and e_city.get()
		l_crwarning = Label(n_acc,text = "   "*30,fg = 'red')
		l_crwarning.place(x = 130,y = 300)
		l_crwarning = Label(n_acc,text = "   "*30,fg = 'red')
		l_crwarning.place(x = 130,y = 320)
		
		if condition:
			if e_npinno.get()!= e_cnpinno.get():
				l_crwarning = Label(n_acc,text = "*Pin and Confirm Pin doesn't match*",fg = 'red')
				l_crwarning.place(x = 130,y = 300)

			if not (e_mnum.get().isdigit() and len(e_mnum.get())==10):
				l_crwarning = Label(n_acc,text = "*Invalid Mobile Number*",fg = 'red')
				l_crwarning.place(x = 130,y = 320)

			if len(e_cnpinno.get()) < 4 and e_npinno.get()== e_cnpinno.get():
				l_crwarning = Label(n_acc,text = "*Pin Must Be 4 Characters Long*",fg = 'red')
				l_crwarning.place(x = 130,y = 300)

			if e_npinno.get() == e_cnpinno.get() and e_mnum.get().isdigit() and len(e_mnum.get())==10 and len(e_cnpinno.get()) >= 4:
				if 1:
					acc_dict = {max(existing_dict)+1:{'name':e_name.get(),'mnum':e_mnum.get(),'pin':e_cnpinno.get(),'city':e_city.get(),'balance':0}}
					existing_dict.update(acc_dict)

					dat_file=open("acc_data.dat",'wb')
					pk.dump(existing_dict,dat_file)
					dat_file.close()

					n_acc.destroy()
					nn_acc = Tk()
					nn_acc.title("Account Number")
					nn_acc.geometry("500x100")
					nn_acc.resizable(0,0)
					l_dispacc = Label(nn_acc,text = "Your Account Number is: "+str(max(existing_dict)),font = "aerial 20 bold")
					l_dispacc.place(x = 10,y = 10)
					b_dispacc = Button(nn_acc,command = accept_accno,text = "    Ok    ")
					b_dispacc.place(x=200,y = 70)
					
		if not condition :
			l_crwarning = Label(n_acc,text = "*All Fields are Mandatory*",fg = 'red')
			l_crwarning.place(x = 130,y = 300)
		
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
	l3 = Label(n_acc, text = "Enter Mobile No     :", font = "aerial 10 ")
	l3.place(x = 50,y = 120)
	l4 = Label(n_acc, text = "Enter pin                :", font = "aerial 10 ")
	l4.place(x = 50,y = 170)
	l5 = Label(n_acc, text = "Confirm Your pin     :", font = "aerial 10 ")
	l5.place(x = 50,y = 220)
	l6 = Label(n_acc, text = "Enter your city        :", font = "aerial 10 ")
	l6.place(x = 50,y = 260)

	e_name = Entry(n_acc)
	e_name.place(x = 190,y = 70)
	e_mnum = Entry(n_acc)
	e_mnum.place(x = 190,y = 120)
	e_npinno = Entry(n_acc,show = '*')
	e_npinno.place(x = 190, y = 170)
	e_cnpinno = Entry(n_acc,show="*")
	e_cnpinno.place(x = 190, y = 220)
	e_city = Entry(n_acc)
	e_city.place(x = 190, y = 260)

	b_mask = Button(n_acc, text = "Show",command = mask_pass, font = "aerial 8")
	b_mask.place(x = 320,y = 195)
	b_savenquit = Button (n_acc, text = "Save & Quit",command = sav_acc)
	b_savenquit.place(x = 170, y = 350)
	b_cancel = Button(n_acc,text = "cancel", command = n_acc.destroy)
	b_cancel.place(x = 300, y = 350)

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
	l3 = Label(top, text = "Enter pin            :", font = "aerial 10 ")
	l3.place(x = 50,y = 150)
	l4 = Label(top,text = "Don't Have An Account ?",font = "aerial 8 underline")
	l4.place(x = 135,y = 247)

	e_accno = Entry(top)
	e_accno.place(x = 190,y = 100)
	e_pinno = Entry(top,show = "*")
	e_pinno.place(x = 190, y = 150)

	b_mask = Button(top, text = "Show",command = mask_pass, font = "aerial 8")
	b_mask.place(x = 320,y = 147)
	b_create = Button(top,text = "Create Account",command = create_acc, font = "aerial 8 ")
	b_create.place(x = 150, y = 270)
	b_login = Button(top, text = "Login", command = login, font = "aerial 13 bold")
	b_login.place(x = 160, y = 180)

	top.mainloop()

if __name__ == '__main__':
	main()


