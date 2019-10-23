import xml.etree.cElementTree as ET
from pathlib import Path

class initSalas():
    def __init__(self):
        file = Path("salas.xml")
        isFile = file.is_file()
        if isFile==False:
            salas = ET.Element("salas")
            arquivo = ET.ElementTree(salas)
            arquivo.write("salas.xml")
initSalas()

ntree = ET.parse('salas.xml')
root = ntree.getroot()

class Comandos():
    # ------------------------------------------------------------
    # Função para verificar sala disponivel
    # ------------------------------------------------------------
    def salaDisponivel(self):
        for sala in root.findall('sala'):
            numsala = sala.find('numsala').text
            id = sala.find('id').text
            #utilizador = sala.find('utilizador').text
            #status = sala.find('status').text
            print("===============================================")
            print("Sala " + id)
            print("Sala: " + numsala)
            print("===============================================")
        print("Fim da lista!")

    # ------------------------------------------------------------
    # Função para listar todas as salas
    # ------------------------------------------------------------
    def listarSalas(self):
        numsala=''
        for sala in root.findall('sala'):
            numsala += "{}, ".format(sala.find('numsala').text)
        return("  {}".format(numsala))

    # ------------------------------------------------------------
    # Função para buscar sala
    # ------------------------------------------------------------
    def buscarSala(self,idsala):
        achasala=False

        for sala in root.findall('sala'):
            salaid = sala.find('numsala').text
            #print("sala: " + salaid)

            if salaid == str(idsala):
                achasala=True
                id = sala.find('id').text
                numsala = sala.find('numsala').text
                #utilizador = sala.find('utilizador').text
                #status = sala.find('status').text
                print("--------------------------------------------")
                print("ID: " + id)
                print("Sala: " + numsala)
                print("--------------------------------------------")
        if (achasala==False):
            print("--------------------------------------------")
            print("          Sala nao encontrada!")
            print("--------------------------------------------")

    # ------------------------------------------------------------
    # Função para verificar se a sala existe
    # ------------------------------------------------------------
    def salaExiste(self,idsala):
        retornoValor = False

        for sala in root.findall('sala'):
            salaid = sala.find('numsala').text
            if salaid == str(idsala):
                retornoValor = True

        return retornoValor

    # -----------------------------------------------------------------
    # Função que faz um loop na ordem de id cadastrado e gera o próximo
    # -----------------------------------------------------------------
    def proxId(self):
        maxid = 0
        for sala in root.findall('sala'):
            id = int(sala.find('id').text)
            if id > maxid:
                maxid = id
        return maxid + 1

    # ------------------------------------------------------------
    # Função para cadastrar uma nova sala
    # ------------------------------------------------------------
    def cadastraSala(self,idsala,utilizador=0,status=0):
        if self.salaExiste(idsala) == False:

            proximoid = self.proxId()

            novoregistro = ET.SubElement(root, "sala", id=str(proximoid))
            ET.SubElement(novoregistro, "id", name="id").text = str(proximoid)
            ET.SubElement(novoregistro, "numsala", name="numsala").text = str(idsala)
            ntree.write("salas.xml")
            print("--------------------------------------------")
            print("      Sala registrada com sucesso!          ")
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
            print("    Sala ja foi registrada anteriormente.   ")
            print("--------------------------------------------")

    def excluirSala(self,idsala):
        for sala in root.findall('sala'):
            salaid = sala.find('numsala').text
            if salaid == str(idsala):
                root.remove(sala)
                ntree.write("salas.xml")
                print("--------------------------------------------")
                print("      Sala removida com sucesso!          ")
                print("--------------------------------------------")
            else:
                print("--------------------------------------------")
                print("         Sala nao encontrada                ")
                print("--------------------------------------------")