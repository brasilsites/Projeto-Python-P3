from datetime import date

class manipulaData():
    def formataHoje(self,data=date.today()):
        self.dia=str(data.day)
        self.mes=str(data.month)
        self.ano=str(data.year)
        print ("{}/{}/{}".format(self.dia, self.mes,self.ano))
    def comparaData(self,data1,data2):
        datadisponivel=True
        self.data1=str(data1)
        self.data2=str(data2)
        #1º Passo: Compara se o ano é igual
        if (self.data1.split("/")[2]==self.data2.split("/")[2]) and (self.data1.split("/")[1]==self.data2.split("/")[1]) and (self.data1.split("/")[0]==self.data2.split("/")[0]):
            datadisponivel=False
        return datadisponivel
    def validaInputData(self,data):
        validadata=False
        if (len(data.split("/")[0])==2) and (len(data.split("/")[1])==2) and (len(data.split("/")[2])==4):
            validadata=True
        return validadata