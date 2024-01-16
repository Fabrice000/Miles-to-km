import tkinter


def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609344
    km_output.config(text=round(km,4))


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20,pady=20)
#label 

miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial",18,"italic"))
miles_label.grid(column=2,row=0)

is_equal_label = tkinter.Label(text="is equal to",font=("Arial",18,"italic"))
is_equal_label.grid(column=0,row=1)



km_output = tkinter.Label(text="",font=("Arial",18,"italic"))
km_output.grid(column=1,row=1)
km_output.config(padx=10)


km_label = tkinter.Label(text="Km",font=("Arial",18,"italic"))
km_label.grid(column=2,row=1)



# button

button = tkinter.Button(text="calculate" ,command=miles_to_km)
button.grid(column=1,row=2)






window.mainloop()