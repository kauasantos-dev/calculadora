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
        self.display_resultados = DisplayResultadoOperacoes(self.aplicacao)
        self.display_resultados.frame_resultado_operacoes()
        NumerosCalculadora(self.aplicacao, self.display_resultados).valores()
        OperadoresCalculadora(self.aplicacao, self.display_resultados).operadores_aritmeticos()
        GerenciarHistorico(self.aplicacao, self.display_resultados).historico_operacoes()
        BotoesPontoIgual(self.aplicacao).botoes_ponto_igual()
        self.aplicacao.mainloop()
    
    def janela_principal(self):
        self.aplicacao.title("Calculadora")
        self.aplicacao.configure(background="#272828")
        self.aplicacao.geometry("550x580")
        self.aplicacao.resizable(True, True)
        self.aplicacao.maxsize(width=720, height=880)

calculadora = Calculadora()