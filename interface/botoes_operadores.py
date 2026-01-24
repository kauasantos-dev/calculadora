from tkinter import Button, Tk

class OperadoresCalculadora:
    def __init__(self, aplicacao: Tk):
        self.aplicacao = aplicacao

    def operadores_aritmeticos(self):
        self.divisao = Button(
            self.aplicacao, 
            text="÷", 
            font=("Arial", 25),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.divisao.place(
            relx=0.76,
            rely=0.30,
            relwidth=0.14,
            relheight=0.09
        )

        self.multiplicacao = Button(
            self.aplicacao, 
            text="×", 
            font=("Arial", 25), 
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.multiplicacao.place(
            relx=0.61,
            rely=0.30,
            relwidth=0.14,
            relheight=0.09
        )

        self.subtracao = Button(
            self.aplicacao, 
            text="-", 
            font=("Arial", 25),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.subtracao.place(
            relx=0.76,
            rely=0.40,
            relwidth=0.14,
            relheight=0.09
        )

        self.soma = Button(
            self.aplicacao, 
            text="+", 
            font=("Arial", 25),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.soma.place(
            relx=0.61,
            rely=0.40,
            relwidth=0.14,
            relheight=0.09
        )

        self.raiz_quadrada = Button(
            self.aplicacao, 
            text="√2", 
            font=("Arial", 18),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.raiz_quadrada.place(
            relx=0.61,
            rely=0.50,
            relwidth=0.14,
            relheight=0.09
        )

        self.potencia = Button(
            self.aplicacao, 
            text="x²", 
            font=("Arial", 18),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.potencia.place(
            relx=0.76,
            rely=0.50,
            relwidth=0.14,
            relheight=0.09
        )