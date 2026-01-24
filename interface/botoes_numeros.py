from tkinter import Button, Tk

class NumerosCalculadora:
    def __init__(self, aplicacao: Tk):
        self.aplicacao = aplicacao

    def valores(self):
        self.numero7 = Button(
            self.aplicacao, 
            text="7", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )

        self.numero7.place(
            relx=0.1,
            rely=0.30,
            relwidth=0.14,
            relheight=0.09,
        )
        
        self.numero8 = Button(
            self.aplicacao, 
            text="8", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )

        self.numero8.place(
            relx=0.25, 
            rely=0.30, 
            relwidth=0.14, 
            relheight=0.09
        )

        self.numero9 = Button(
            self.aplicacao, 
            text="9", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )
        self.numero9.place(
            relx=0.40,
            rely=0.30,
            relwidth=0.14,
            relheight=0.09
        )

        self.numero4 = Button(
            self.aplicacao, 
            text="4", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )

        self.numero4.place(
            relx=0.1,
            rely=0.40,
            relwidth=0.14,
            relheight=0.09
        )

        self.numero5 = Button(
            self.aplicacao, 
            text="5", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )

        self.numero5.place(
            relx=0.25,
            rely=0.40,
            relwidth=0.14,
            relheight=0.09
        )

        self.numero6 = Button(
            self.aplicacao, 
            text="6", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
            )
        
        self.numero6.place(
            relx=0.40,
            rely=0.40,
            relwidth=0.14,
            relheight=0.09
        )

        self.numero1 = Button(
            self.aplicacao, 
            text="1", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )
        self.numero1.place(
            relx=0.1,
            rely=0.50,
            relwidth=0.14,
            relheight=0.09
        )

        self.numero2 = Button(
            self.aplicacao, 
            text="2", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )
        self.numero2.place(
            relx=0.25,
            rely=0.50,
            relwidth=0.14,
            relheight=0.09
        )

        self.numero3 = Button(
            self.aplicacao, 
            text="3", 
            font=("Arial", 16),
            background="white",
            bd=1,
            relief="raised"
        )
        self.numero3.place(
            relx=0.40,
            rely=0.50,
            relwidth=0.14,
            relheight=0.09
        )

        self.numero0 = Button(
            self.aplicacao, 
            text="0", 
            font=("Arial", 16),
            background="white", 
            fg="black",
            bd=1,
            relief="raised"
        )

        self.numero0.place(
            relx=0.1,
            rely=0.60,
            relwidth=0.14,
            relheight=0.09
        )