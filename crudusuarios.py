import xml.etree.cElementTree as ET
from pathlib import Path

class initUsuarios():
    def __init__(self):
        file = Path("usuarios.xml")
        isFile = file.is_file()
        if isFile==False:
            usuarios = ET.Element("usuarios")
            no_usuario = ET.SubElement(usuarios, "usuario")
            ET.SubElement(no_usuario, "id", name="id").text = '1'

            ET.SubElement(no_usuario, "login", name="login").text = 'admin'
            ET.SubElement(no_usuario, "senha", name="senha").text = '1234'
            ET.SubElement(no_usuario, "nome", name="nome").text = 'Admin'
            ET.SubElement(no_usuario, "nivel", name="nivel").text = '1' #1=Coordenador, 2=Gestor de Recursos, 3 - Usuario comum
            arquivo = ET.ElementTree(usuarios)
            arquivo.write("usuarios.xml")

            ntree = ET.parse('usuarios.xml')
            root = ntree.getroot()

            no_usuario = ET.SubElement(root, "usuario")
            ET.SubElement(no_usuario, "id", name="id").text = '2'
            ET.SubElement(no_usuario, "login", name="login").text =  'efsilva'
            ET.SubElement(no_usuario, "senha", name="senha").text = '1234'
            ET.SubElement(no_usuario, "nome", name="nome").text = 'Gestor'
            ET.SubElement(no_usuario, "nivel", name="nivel").text = '2'
            ntree.write("usuarios.xml")
initUsuarios()

class Comandos():
    def __init__(self,logusuario='',senha='',nome='',nivel=''):
        self.logusuario=logusuario
        self.senha=senha
        self.nome=nome
        self.nivel=nivel

    def cadastraUsuario(self):
        self.cadastrook=True
        ntree = ET.parse('usuarios.xml')
        root = ntree.getroot()

        no_usuario = ET.SubElement(root, "usuario")
        ET.SubElement(no_usuario, "id", name="id").text = str(self.profId())
        ET.SubElement(no_usuario, "login", name="login").text =  self.logusuario
        ET.SubElement(no_usuario, "senha", name="senha").text = self.senha
        ET.SubElement(no_usuario, "nome", name="nome").text = self.nome
        ET.SubElement(no_usuario, "nivel", name="nivel").text = self.nivel
        ntree.write("usuarios.xml")
        return self.cadastrook

    def validaLogin(self,login,nivel):
        self.login=login
        self.nivel=nivel
        valida=True
        ntree = ET.parse('usuarios.xml')
        root = ntree.getroot()
        for usuario in root.findall('usuario'):
            if usuario.find('login').text==self.login and usuario.find('nivel').text==self.nivel:
                valida=False
        return valida

    def profId(self):
        ntree = ET.parse('usuarios.xml')
        root = ntree.getroot()

        maxid = 0
        for usuario in root.findall('usuario'):
            id = int(usuario.find('id').text)
            if id > maxid:
                maxid = id
        return maxid+1

class usuarioLista():

    # ------------------------------------------------------------
    # Função para buscar usuarios
    # ------------------------------------------------------------
    def buscarUsuario(self,login,senha,nivel):
        ntree = ET.parse('usuarios.xml')
        root = ntree.getroot()
        achausuario=False

        for usuario in root.findall('usuario'):
            userid = usuario.find('login').text
            snhid = usuario.find('senha').text
            nivelid = usuario.find('nivel').text

            if userid == str(login) and snhid==str(senha) and nivelid==str(nivel):
                achausuario=True
        return achausuario
