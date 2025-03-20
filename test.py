import customtkinter


# créer la première fenêt


window = customtkinter.CTk()


# personnaliser la fenêtre

window.title("my application")

window.geometry("620x620")

window.minsize(280, 280)

window.iconbitmap("budgetbuddy.ico")

window.config(background='#2CDF85')


# créer la frame
jls_extract_var = Frame
frame = jls_extract_varndow, (bg := '#2CDF85', bd:=1, relief:=SUNKEN)


# ajouter un texte

label_title = Label(frame, text="BUDGET BUDDY", font=("Double struck",40), bg='#2CDF85', fg='#FFFFFF')

label_title.pack()

 # sous titre

label_subtitle = Label(frame, text="BIENVENUE", font=("Double struck",25), bg='#2CDF85', fg='#FFFFFF')

label_subtitle.pack()


# ajouter un bouton



# ajouter la frame

frame.pack(expand=YES)


# afficher 
window.mainloop()