from Banco import Banco

class Usuarios(object):
    def __init__(self, nome="", login="", senha="", nivel=""):
        self.nome=nome
        self.login=login
        self.senha=senha
        self.nivel=nivel
        self.idusuario=""

    def insereUsuario(self,nome,login,senha,nivel):
        self.nome=nome
        self.login=login
        self.senha=senha
        self.nivel=nivel

        if self.verificaDuplicidade(self.login,self.senha,self.nivel)==0:
            banco = Banco()
            try:
                c = banco.conexao.cursor()
                c.execute("insert into usuarios(nome,login,senha,nivel) values ('"+self.nome+"','"+self.login+"','"+self.senha+"','"+self.nivel+"')")
                banco.conexao.commit()
                c.close()
                return "Usuário cadastrado com sucesso!"
            except:
                return "Ocorreu um erro na inserção do usuário"
        else:
            return "Usuário já cadastrado com os mesmos dados"

    def updateUser(self,idusuario):
        self.idusuario=idusuario
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute(
                "update usuarios set nome='" + self.nome + "',login='" + self.login + "',senha='" + self.senha +
                "',nivel='" + self.nivel + "' WHERE idusuario='"+self.idusuario+"'")
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self,idusuario):
        self.idusuario=idusuario
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario='" + self.idusuario + "'")
            banco.conexao.commit()
            c.close
            return "Usuário excluido com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self,idusuario,nivel):
        self.idusuario = idusuario
        self.nivel=nivel
        banco = Banco()

        c = banco.conexao.cursor()
        c.execute("select from usuarios where idusuario='" + self.idusuario + "' AND nivel='"+self.nivel+"'")
        for linha in c:
            self.idusuario = linha[0]
            self.nomeusu = linha[1]
            self.loginusu = linha[2]
            self.senhausu = linha[3]
            self.nivelusu = linha[4]
        c.close()

    def nomeUsuario(self):
        return self.nomeusu

    def idUsuario(self):
        return self.idusuario

    def verificaDuplicidade(self,login,senha,nivel):
        self.login=login
        self.senha=senha
        self.nivel=nivel

        total=0
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("select * from usuarios where login='" + self.login + "' AND senha='"+self.senha+"' AND nivel='"+self.nivel+"'")
        for linha in c:
            total+=linha[0]
            self.nomeusu=linha[1]
            self.idusuario=linha[0]
        c.close()
        return total

    def usuarioParticipante(self,organizador):
        #self.valores = StringVar()
        self.valores =""
        lista=""
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("select * from usuarios WHERE idusuario!='"+str(organizador)+"'")
        for linha in c:
            lista+=str(linha[0])+"-"+str(linha[1])+" "

        return lista

    def idUsuario(self):
        return self.idusuario

#listapart=Usuarios()
#print(listapart.usuarioParticipante())