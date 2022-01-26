# -*- coding: utf-8 -*-
from datetime import date
import calendar


class DataAtual(object):

    def __init__(self, diames="", diasemana="",
                 dataAtual="", mes=""):
        self.dataAtual = dataAtual
        self.diames = diames
        self.diasemana = diasemana

        self.mes = mes

    def diaAtual(self):
        self.diames = date.today()

        self.diames = self.diames.strftime('%d/%m')
        self.diasemana = ["SEGUNDA", "TERÇA", "QUARTA",
                          "QUINTA", "SEXTA", "SABÁDO", "DOMINGO"]
        self.diasemana = self.diasemana[date.today().weekday()]


    def lb_mesAtualHome(self):
        self.mes = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
                    5: "Maio", 6: "Junho",
                    7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro",
                    11: "Novembro", 12: "Dezembro"}
        self.mes = self.mes[date.today().month]
        return self.mes
