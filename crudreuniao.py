import xml.etree.cElementTree as ET
from pathlib import Path
import verificaarquivo,crudsalas

class initReuniao():
    def __init__(self):
        file = Path("reunioes.xml")
        isFile = file.is_file()
        if isFile==False:
            reunioes = ET.Element("reunioes")
            arquivo = ET.ElementTree(reunioes)
            arquivo.write("reunioes.xml")
initReuniao()

ntree = ET.parse('reunioes.xml')
root = ntree.getroot()

class reuniaoClass():
    def __init__(self,coordenador,datainicio,datafim,sala,assunto,status,visibilidade):
        self.coordenador=coordenador
        self.datainicio=datainicio
        self.datafim=datafim
        self.sala=sala
        self.assunto=assunto
        self.status=status
        self.visibilidade=visibilidade
        file = Path("reunioes.xml")
        isFile = file.is_file()
        if isFile==False:
            self.cadastraReuniao()
        else:
            self.incluiReuniao()

    def cadastraReuniao(self):
        reunioes = ET.Element("reunioes")
        no_reuniao = ET.SubElement(reunioes, "reuniao")
        ET.SubElement(no_reuniao, "id", name="id").text = '1'

        ET.SubElement(no_reuniao, "coordenador", name="coordenador").text = self.coordenador
        ET.SubElement(no_reuniao, "datainicio", name="datainicio").text = self.datainicio
        ET.SubElement(no_reuniao, "datafim", name="datafim").text = self.datafim
        ET.SubElement(no_reuniao, "sala", name="sala").text = self.sala
        ET.SubElement(no_reuniao, "assunto", name="assunto").text = self.assunto
        ET.SubElement(no_reuniao, "status", name="status").text = self.status
        ET.SubElement(no_reuniao, "visibilidade", name="visibilidade").text = self.visibilidade
        arquivo = ET.ElementTree(reunioes)
        arquivo.write("reunioes.xml")

    def incluiReuniao(self):
        ntree = ET.parse('reunioes.xml')
        root = ntree.getroot()

        no_reuniao = ET.SubElement(root, "reuniao")
        ET.SubElement(no_reuniao, "id", name="id").text = str(self.profId())
        ET.SubElement(no_reuniao, "coordenador", name="coordenador").text =  self.coordenador
        ET.SubElement(no_reuniao, "datainicio", name="datainicio").text = self.datainicio
        ET.SubElement(no_reuniao, "datafim", name="datafim").text = self.datafim
        ET.SubElement(no_reuniao, "sala", name="sala").text = self.sala
        ET.SubElement(no_reuniao, "assunto", name="assunto").text = self.assunto
        ET.SubElement(no_reuniao, "status", name="status").text = self.status
        ET.SubElement(no_reuniao, "visibilidade", name="visibilidade").text = self.visibilidade
        ntree.write("reunioes.xml")

    def profId(self):
        ntree = ET.parse('reunioes.xml')
        root = ntree.getroot()

        maxid = 0
        for reuniao in root.findall('reuniao'):
            id = int(reuniao.find('id').text)
            if id > maxid:
                maxid = id
        return maxid+1

class reuniaoLista():
    def listaReuniaoUsuario(self,loginusuario):
        disponivel=False
        ntree = ET.parse('reunioes.xml')
        root = ntree.getroot()
        for reuniao in root.findall('reuniao'):
            visibilidade=''
            if reuniao.find('coordenador').text==loginusuario:
                disponivel=True
                if reuniao.find('visibilidade').text == '1':
                    visibilidade=" Privado"
                else:
                    visibilidade=" Publico"
                print('======================================================')
                print('  Reuniao Sala: {} \n  nome: {} \n  data inicio: {} \n  data fim: {}'.format(reuniao.find('sala').text,reuniao.find('assunto').text,reuniao.find('datainicio').text,reuniao.find('datafim').text))
                print('  visibilidade: {}'.format(visibilidade))
                print('======================================================')
        if disponivel==False:
            print(' Nenhuma reuniao disponivel')
    def listaReuniaoPublica(self):
        disponivel=False
        ntree = ET.parse('reunioes.xml')
        root = ntree.getroot()
        for reuniao in root.findall('reuniao'):
            #print(str(reuniao.find('datainicio').text))
            if reuniao.find('visibilidade').text=='0':
                disponivel=True
                print('======================================================')
                print('  Reuniao nome: {} \n data inicio: {} \n data fim: {} \n'.format(reuniao.find('assunto').text,reuniao.find('datainicio').text,reuniao.find('datafim').text))
                print('======================================================')

        if disponivel==False:
            print(' Nenhuma reuniao publica para o periodo')
    def salaDisponivel(self,inputdataini,inputdatafim):
        self.inputdataini=inputdataini
        self.inputdatafim=inputdatafim

        ntree = ET.parse('reunioes.xml')
        root = ntree.getroot()

        ntreesala = ET.parse('salas.xml')
        rootsala = ntreesala.getroot()

        listasala=''
        achou=0
        #Primeiro lista as salas cadastradas
        if len(rootsala.findall('sala'))>0:
            for sala in rootsala.findall('sala'):
                #listasala=listasala+(sala.find('numsala').text+',')
                #Passo: Verificar se a sala esta cadastrada em alguma lista de reuniao
                for reuniao in root.findall('reuniao'):
                    if (reuniao.find('sala').text == sala.find('numsala').text):
                        #Passo: Se encontrou a sala na lista de reuniao, agora deve verificar se as datas sao iguais
                        if (verificaarquivo.manipulaData().comparaData(reuniao.find('datainicio').text,self.inputdataini)==False) or (verificaarquivo.manipulaData().comparaData(reuniao.find('datainicio').text,self.inputdatafim)==False) or (verificaarquivo.manipulaData().comparaData(reuniao.find('datafim').text,self.inputdataini)==False) or (verificaarquivo.manipulaData().comparaData(reuniao.find('datafim').text,self.inputdatafim)==False):
                            achou=1
                    #se nao encontrou na lista, é porque ainda não foi cadastrado nenhuma reuniao para a sala
                if achou==0:
                    listasala=listasala+(sala.find('numsala').text+',')
                achou=0
        return listasala
#reuniaoLista.salaDisponivel('21/01/2019','21/01/2019')