from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Weight Convertor App")
root.geometry("1000x800+50+50")
f = ("Century", 20, "bold")
root.configure(bg="aquamarine")


lab_title = Label(root, text="Weight Convertor", font=f, bg="aquamarine")
lab_title.pack(pady=10)

lab_pound = Label(root, text="Pounds:", font=f, bg="aquamarine")
ent_pound = Entry(root, font=f, width=15)
lab_pound.pack(pady=10)
ent_pound.pack(pady=10)
lab_kilogram = Label(root, text="Kilograms: ", font=f, bg="aquamarine")
ent_kilogram = Entry(root, font=f, width=15)
lab_kilogram.pack(pady=10)
ent_kilogram.pack(pady=10)


def convert_pound():
	pound_value = ent_pound.get()
	if pound_value == "":
		showerror("issue", "pound amt cannot be empty")		
		return
	
	if pound_value.isalpha():
		showerror("invalid input", "pound amount cannot be text")
		return

	if pound_value.isspace():
		showerror("Invalid Input", "pound amount cannot be spaces")
		return
		
	try:

		pound = float(pound_value)

		if pound < 0:
			showerror("invalid input","pound amt cannot be negative")
			return
	
		if pound < 1 or pound > 1000:
			showerror("issue", "pound value must be between 1 and 1000")
			return

		kg = pound * 0.453592
		round_result = round(kg, 4)
		msg = "Pounds to Kilograms = " + str(round_result)
		lab_result1.configure(text=msg)
		showinfo("success", "success")
		ent_kilogram.delete(0, END)
		ent_kilogram.focus()

	except Exception:
		showerror("invalid input", "values must be a numeric")
		return
	

def convert_kg():
	kg_value = ent_kilogram.get()

	if kg_value == "":
		showerror("issue", "kg amt cannot be empty")
		return
	if kg_value.isalpha():
		showerror("invalid input", "pound amount cannot be text")
		return

	if kg_value.isspace():
		showerror("Invalid Input", "kg amount cannot be spaces")
		return
	try:

		kilogram = float(kg_value)
	
		if kilogram < 0:
			showerror("invalid input","kg amt cannot be negative")
			return

		if kilogram < 1 or kilogram > 1000:
			showerror("issue", "Kg value must be between 1 and 1000")
			return

		pound = kilogram * 2.20462
		round_result = round(pound, 4)
		msg = "Kilograms  to Pounds = " + str(round_result)
		lab_result2.configure(text=msg)
		showinfo("success", "success")
		ent_pound.delete(0, END)
		ent_pound.focus()

	except Exception:
		showerror("invalid input", "values must be a numeric")
		return

def clear():
	ent_pound.delete(0, END)
	ent_kilogram.delete(0, END)
	lab_result1.configure(text="")
	lab_result2.configure(text="")
	ent_pound.focus()


btn_convert = Button(root, text="Pounds to Kilograms",width=17, font=f, bg="ghost white", command=convert_pound)
btn_convert.pack(pady=10)
lab_result1 = Label(root, bg="aquamarine", font=f)
lab_result1.pack(pady=10)

btn_convert = Button(root, text="Kilograms to pound", font=f, bg="ghost white", width=17, command=convert_kg)
btn_convert.pack(pady=10)

lab_result2 = Label(root, bg="aquamarine", font=f)
lab_result2.pack(pady=10)

btn_clear = Button(root, text="Clear", font=f, width=10,bg="ghost white",  command=clear)
btn_clear.pack(pady=10)


root.mainloop()