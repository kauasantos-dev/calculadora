from tkinter import *
from botoes_numeros import NumerosCalculadora
from botoes_operadores import OperadoresCalculadora
from ver_apagar_historico import GerenciarHistorico
from botoes_ponto_igual import BotoesPontoIgual

class Calculadora:
    def __init__(self):
        self.aplicacao = Tk()
        self.janela_principal()
        self.frame_resultado_operacoes()
        NumerosCalculadora(self.aplicacao).valores()
        OperadoresCalculadora(self.aplicacao).operadores_aritmeticos()
        GerenciarHistorico(self.aplicacao).historico_operacoes()
        BotoesPontoIgual(self.aplicacao).botoes_ponto_igual()
        self.aplicacao.mainloop()
    
    def janela_principal(self):
        self.aplicacao.title("Calculadora")
        self.aplicacao.configure(background="#272828")
        self.aplicacao.geometry("550x580")
        self.aplicacao.resizable(True, True)
        self.aplicacao.maxsize(width=720, height=880)

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

calculadora = Calculadora()