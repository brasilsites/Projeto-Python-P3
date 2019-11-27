from Banco import Banco

class Participantes(object):
    def __init__(self,idusuario="",idreuniao="",status="0"):
        self.idusuario=idusuario
        self.idreuniao=idreuniao
        self.status=status
        self.banco = Banco()
        self.mensagem=""

    def insereParticipante(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("insert into participantes(idusuario,idreuniao,status) values ('"+self.idusuario+"','"+self.idreuniao+"','"+self.status+"')")
            self.banco.conexao.commit()
            c.close()
            return True
        except:
            return False

    def updateParticipante(self,idparticipante,status):
        self.idparticipante=idparticipante
        self.status=status
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute(
                "update participantes set status='" + self.status + "' WHERE idparticipante='"+self.idparticipante+"'")
            banco.conexao.commit()
            c.close()
            self.mensagem="Participante atualizado com sucesso!"
        except:
            self.mensagem="Ocorreu um erro na alteração do participante"

    def printMensagem(self):
        return self.mensagem

    def listarParticipantes(self):
        banco = Banco()
        c = banco.conexao.cursor()
        reunioes=""

        c.execute("select * from participantes")
        for linha in c:
            id=" ID: "+str(linha[0])+"\n"
            usuario="Usuario: "+linha[1]+"\n"
            reuniao="Reuniao: "+linha[2]+"\n"
            status="Status: "+linha[3]+"\n"

            reunioes+=id+" "+usuario+" "+reuniao+" "+status+"\n"

        return reunioes

    def buscarParticipantesAdicionar(self,idreuniao,idorganizador):
        banco = Banco()
        c = banco.conexao.cursor()
        d = banco.conexao.cursor()
        self.mensagem=""
        self.total=0
        c.execute("select idusuario,nome from usuarios WHERE idusuario!='"+idorganizador+"'")
        for linha in c:
            d.execute("select participantes.idusuario,reunioes.idreuniao FROM reunioes,participantes WHERE reunioes.idreuniao='"+idreuniao+"' AND reunioes.idreuniao=participantes.idreuniao AND participantes.idusuario='"+str(linha[0])+"'")
            participante=len(d.fetchall())
            if participante==0:
                self.mensagem+=str(linha[0])+"-"+str(linha[1])+" "
                self.total+=1

        return self.mensagem

    def printTotal(self):
        return self.total

'''partic=Participantes()

partic.buscarParticipantesAdicionar("2","1")
if partic.printTotal()>0:
    print(partic.printMensagem())
else:
    print("Nenhum novo participante localizado!")'''