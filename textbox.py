import customtkinter

class TextBox:
    def __init__(self, parent, label_text, button_text, row) :
        self.parent = parent

        self.label_instruction = customtkinter.CTkLabel(parent, text=label_text)
        self.label_instruction.grid(row=row-1, column=0, padx=10, pady=5, sticky="w")

        self.input = customtkinter.CTkEntry(parent, width=300)
        self.input.grid(row = row, column=0, padx=10, pady=5)
    
    def get_text(self) :
        content = self.input.get()

