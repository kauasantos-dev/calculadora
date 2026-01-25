from tkinter import Tk, Frame, StringVar, Label

class DisplayResultadoOperacoes:
    def __init__(self, aplicacao: Tk):
        self.aplicacao = aplicacao
        self.valor_display = StringVar()
        self.valor_display.set("0")

    def frame_resultado_operacoes(self):
        self.frame_resultados = Frame(
            self.aplicacao, 
            bg="#222020",
            highlightbackground="white",
            highlightthickness=2
        )

        self.frame_resultados.place(
            relx=0.1, 
            rely=0.05,
            relwidth=0.8, 
            relheight=0.16
        )

        self.display = Label(
            self.frame_resultados,
            textvariable=self.valor_display,
            bg="white",
            fg="black",
            anchor="e",
            font=("Arial", 20)
        )

        self.display.place(
            relwidth=1,
            relheight=1
        )

    def inserir(self, valor):
        valor_atual = self.valor_display.get()
        if valor is None:
            self.valor_display.set("0")

        elif valor_atual == "0":
            self.valor_display.set(str(valor))

        else:
            self.valor_display.set(valor_atual + str(valor))