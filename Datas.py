from datetime import *
import calendar

class Datas(object):
    def __init__(self):
        self.hj=date.today()
        self.datain=""
        self.dataof=""
        self.dataconvert=""

    def getHoje(self):
        return self.hj

    def getDia(self):
        return self.hj.day
    def getMes(self):
        return self.hj.month
    def getAno(self):
        return self.hj.year

    def diasEntreDatas(self,data1,data2):
        self.datain=date.fromisoformat(data1)
        self.dataof=date.fromisoformat(data2)

        diferenca = self.dataof.toordinal() - self.datain.toordinal()
        return diferenca

    def converteDataBRL(self,data,separador): #converte a data formato EUA em formato BRL
        data=date.fromisoformat(data)
        self.dataconvert=data.strftime("%d"+separador+"%m"+separador+"%Y")
        return self.dataconvert

    def converteDataEUA(self,data,separador): #converte a data formato BRL em formato EUA
        data=data.split('-',3)
        novadata=data[2]+'-'+data[1]+'-'+data[0]
        data=date.fromisoformat(novadata)
        self.dataconvert=data.strftime("%Y"+separador+"%m"+separador+"%d")
        return self.dataconvert

    def converteHojeBRL(self,separador):
        self.dataconvert=self.hj.strftime("%d"+separador+"%m"+separador+"%Y")
        return self.dataconvert

    def imprimeDiaSemana(self,data):
        data=self.converteStringEmData(data)
        dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        return dias[data.weekday()]

    def imprimeMes(self,data,separador):
        mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
        dia, mes, ano = data.split(separador)
        return mes_ext[int(mes)]

    def imprimeCalendario(self,ano,mes):
        cal=calendar.month(ano, mes)
        return (cal)

    def converteStringEmData(self,datastring):
        datastring=datastring+'T00:00:00Z'
        datetime_object = datetime.strptime(datastring, '%Y-%m-%dT%H:%M:%S%z')
        dataFormatada = datetime_object.strftime("%d/%m/%Y")
        return datetime_object

    def comparaDatas(self,dataini,datafim,datareservaini,datareservafim):
        if (self.diasEntreDatas(dataini,datareservaini)<=0
                or self.diasEntreDatas(datafim,datareservaini)<=0
                or self.diasEntreDatas(dataini,datareservafim)<=0
                or self.diasEntreDatas(datafim,datareservaini)<=0
        ):
            return False
        else:
            return True

    def validaDatas(self,dataini,datafim):
        self.dataini=dataini
        self.datafim=datafim
        truefalse=True
        if self.diasEntreDatas(self.dataini,self.datafim)<0:
            truefalse=False

        dataini=date.fromisoformat(dataini)
        datafim=date.fromisoformat(datafim)
        #print(date.toordinal())

        if (dataini.toordinal() - date.today().toordinal())<0:
            truefalse=False
        if (datafim.toordinal() - date.today().toordinal())<0:
            truefalse=False
        return truefalse

#printdata=Datas()
#print(printdata.validaDatas('2019-11-28','2019-11-27'))

'''print(printdata.getHoje())
print(printdata.converteDataBRL('2019-12-04','-'))
print(printdata.converteDataEUA('04-12-2019','-'))
print(printdata.converteHojeBRL('/'))
print(printdata.imprimeDiaSemana('2019-11-21'))
print(printdata.imprimeMes('2019-11-21','-'))
print(printdata.imprimeCalendario(2019,11))
print(printdata.converteStringEmData('2018-05-01'))
if printdata.comparaDatas('2019-11-20','2019-11-20','2019-11-21','2019-11-21')==False:
    print("Erro")
else:
    print("Ok")'''

