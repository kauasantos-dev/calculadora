from tkinter import *
from botoes_numeros import NumerosCalculadora
from botoes_operadores import OperadoresCalculadora
from ver_apagar_historico import GerenciarHistorico
from botoes_ponto_igual import BotoesPontoIgual
from display_resultado import DisplayResultadoOperacoes

class Calculadora:
    def __init__(self):
        self.aplicacao = Tk()
        self.janela_principal()
        DisplayResultadoOperacoes(self.aplicacao).frame_resultado_operacoes()
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

calculadora = Calculadora()