from tkinter import Button, Tk

class BotoesPontoIgual:
    def __init__(self, aplicacao: Tk):
        self.aplicacao = aplicacao

    def botoes_ponto_igual(self):
        self.ponto = Button(
            self.aplicacao,
            text=".",
            font=("Arial", 20),
            bg="orange",
            fg="white",
            bd=1,
            relief="raised"
        )

        self.ponto.place(
            relx=0.25,
            rely=0.60,
            relwidth=0.14,
            relheight=0.09
        )

        self.igual = Button(
            self.aplicacao,
            text="=", font=("Arial", 20),
            bg="orange",
            fg="white",
            bd=1,
            relief="raised"
        )

        self.igual.place(
            relx=0.40,
            rely=0.60,
            relwidth=0.14,
            relheight=0.09
        )