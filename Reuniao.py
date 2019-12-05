from Banco import Banco
from Salas import Salas
from Datas import Datas
import os

class Reuniao(object):
    def __init__(self,idreuniao="",idsala="",idcoordenador="",pauta="",dataini="",datafim="",pubprivada="0",status="0"):
        self.idreuniao=idreuniao
        self.idsala=idsala
        self.idcoordenador=idcoordenador
        self.pauta=pauta
        self.dataini=dataini
        self.datafim=datafim
        self.status=status
        self.pubprivada=pubprivada
        self.banco = Banco()
        self.qtdreuniao=""

    def cadastraReuniao(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("insert into reunioes(idsala,idcoordenador,pauta,dataini,datafim,pubprivada,status,atagerada) values ('"+self.idsala+"','"+self.idcoordenador+"','"+self.pauta+"','"+self.dataini+"','"+self.datafim+"','"+self.pubprivada+"','"+self.status+"','0')")
            self.ultimoid=str(c.lastrowid)
            self.banco.conexao.commit()

            return "Reuniao cadastrada com sucesso! "
        except:
            return "Ocorreu um erro no cadastro da reuniao!"

    def buscaUltimoId(self):
        return self.ultimoid

    def buscarReuniaoDatas(self,dataini,datafim):
        self.dataini=dataini
        self.datafim=datafim
        versala=Salas()
        #banco = Banco()
        try:
            salas=["Selecione uma sala."]
            d = self.banco.conexao.cursor()
            d.execute("select * from salas WHERE status=1")
            for linha in d:
                salas.append(linha[2])

            c = self.banco.conexao.cursor()
            #c.execute("select * from reunioes where status>0 OR dataini='" + self.dataini + "' OR datafim='"+self.dataini+"' OR dataini='" + self.datafim + "' OR datafim='"+self.datafim+"' GROUP By idsala")
            c.execute("select * from reunioes where status=1 AND (dataini='" + self.dataini + "' OR datafim='"+self.dataini+"' OR dataini='" + self.datafim + "' OR datafim='"+self.datafim+"') GROUP By idsala")
            for linha in c:
                salas.remove(linha[1])
        except:
            salas.append("Nenhuma sala encontrada!")
        return salas

    def listaReuniaoPublica(self):
        c = self.banco.conexao.cursor()
        datas=Datas()
        reunioes=""
        c.execute("select reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,usuarios.nome from reunioes,usuarios where reunioes.pubprivada='0' AND reunioes.idcoordenador=usuarios.idusuario AND reunioes.status='1' AND reunioes.atagerada='0'")
        for linha in c:
            sala=" Sala: "+linha[0]+"\n"
            pauta="Pauta: "+linha[1]+"\n"
            organizador="Organizador: "+linha[4]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[2],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[3],"/")+"\n"
            reunioes+=sala+" "+pauta+" "+dataini+" "+datafim+" "+organizador+"\n"

        return reunioes

    def qtdReuniao(self,pubprivada):
        d = self.banco.conexao.cursor()
        d.execute("select * from reunioes where pubprivada='"+pubprivada+"'")
        self.qtdreuniao=len(d.fetchall())
        return self.qtdreuniao

    def qtdReuniaoUsuario(self,participante):
        self.participante=str(participante)
        datas=Datas()
        reunioes=""
        d = self.banco.conexao.cursor()
        d.execute("select reunioes.idreuniao,reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,participantes.status from reunioes,participantes where participantes.idreuniao=reunioes.idreuniao AND participantes.idusuario='"+self.participante+"' AND participantes.status='0'")
        self.qtdreuniao=len(d.fetchall())
        for linha in d:
            id="ID: "+str(linha[0])+"\n"
            sala="Sala: "+linha[1]+"\n"
            pauta="Pauta: "+linha[2]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[3],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[4],"/")+"\n"
            if (linha[5]=="0"):
                status="Pendente"
            elif(linha[5]=="1"):
                status="Confirmado"
            reunioes+=" "+id+" "+sala+" "+pauta+" "+dataini+" "+datafim+" "+status+"\n\n"
        if reunioes=="":
            reunioes="Nenhuma reunião encontrada. "
        return reunioes

    def qtdReuniaoUsuarioStatus(self,participante,status):
        self.participante=str(participante)
        self.status=str(status)
        if self.status=="0":
            atagerada="AND reunioes.atagerada='0'"
        else:
            atagerada=""

        datas=Datas()
        reunioes=""
        d = self.banco.conexao.cursor()
        d.execute("select reunioes.idreuniao,reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,participantes.status from reunioes,participantes where participantes.idreuniao=reunioes.idreuniao AND participantes.idusuario='"+self.participante+"' AND reunioes.status='1' AND participantes.status='"+self.status+"' "+atagerada+" GROUP By reunioes.idsala")
        self.qtdreuniao=len(d.fetchall())
        for linha in d:
            id="ID: "+str(linha[0])+"\n"
            sala="Sala: "+linha[1]+"\n"
            pauta="Pauta: "+linha[2]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[3],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[4],"/")+"\n"
            if (linha[5]=="0"):
                status="Pendente"
            elif(linha[5]=="1"):
                status="Confirmado"
            reunioes+=" "+id+" "+sala+" "+pauta+" "+dataini+" "+datafim+" "+status+"\n\n"
        if reunioes=="":
            reunioes="Nenhuma reunião encontrada. "
        return reunioes

    def printQtdReuniao(self):
        return self.qtdreuniao

    def filtraReuniao(self,pubpriva,concfut,orgpart,aguardaaprov,idorganizador):
        datas=Datas()

        self.pubprivada=pubpriva
        self.concfut=concfut
        self.orgpart=orgpart
        self.idorganizador=idorganizador
        self.aguardaaprov=aguardaaprov

        #0 - Publica ; 1 - Privada
        select1=" reunioes.pubprivada='"+str(self.pubprivada)+"' "

        #0 - Concluida ; 1 - Futura
        if self.concfut==0:
            select2=" reunioes.datafim<'"+str(datas.getHoje())+"' AND reunioes.atagerada='1' " #2019-11-26
        else:
            select2=" reunioes.datafim>='"+str(datas.getHoje())+"' "

        #0 - Organizador ; 1 - Participante
        if self.orgpart==0:
            select3=" reunioes.idcoordenador='"+str(self.idorganizador)+"' "
        else:
            select3=" participantes.idusuario='"+str(self.idorganizador)+"' "
        #0 - Aguarda aprovação; 1 - Aprovada
        select4=" reunioes.status='"+str(self.aguardaaprov)+"' "

        c = self.banco.conexao.cursor()
        datas=Datas()
        self.qtdreuniao=0
        reunioes=""
        c.execute("select reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,usuarios.nome,reunioes.status from reunioes,usuarios,participantes where "+select1+" AND "+select2+" AND "+select3+" GROUP By idsala") # AND "+select4+"
        for linha in c:
            self.qtdreuniao+=1
            sala=" Sala: "+linha[0]+"\n"
            pauta="Pauta: "+linha[1]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[2],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[3],"/")+"\n"

            reunioes+=sala+" "+pauta+" "+dataini+" "+datafim+"\n"
        if self.qtdreuniao==0:
            reunioes="Nenhuma reunião localizada com as opções selecionadas"
        return reunioes

    def reunioesAprovadaPendente(self,participante):
        datas=Datas()
        self.participante=str(participante)

        c = self.banco.conexao.cursor()
        self.qtdreuniao=0
        self.selectreunioes=""
        reunioes=""
        c.execute("select reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,participantes.idparticipante from reunioes,participantes where participantes.idusuario='"+self.participante+"' AND participantes.idreuniao=reunioes.idreuniao AND reunioes.status='1' AND participantes.status='0' AND reunioes.atagerada='0'")
        for linha in c:
            self.qtdreuniao+=1
            strip=linha[1].replace(" ","-")
            self.selectreunioes+=str(linha[4])+"-Sala:"+linha[0]+"-Pauta:"+strip+" "
            sala=" Sala: "+linha[0]+"\n"
            pauta="Pauta: "+linha[1]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[2],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[3],"/")+"\n"
            reunioes+=sala+" "+pauta+" "+dataini+" "+datafim+"\n"
        if self.qtdreuniao==0:
            reunioes="Nenhuma reunião localizada para o seu perfil"
        return reunioes

    def reunioesAprovadaConfirmada(self,participante):
        datas=Datas()
        self.participante=str(participante)

        c = self.banco.conexao.cursor()
        self.qtdreuniao=0
        self.selectreunioes=""
        reunioes=""
        c.execute("select reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,reunioes.idreuniao from reunioes,participantes where participantes.idusuario='"+self.participante+"' AND reunioes.status='1' AND participantes.idreuniao=reunioes.idreuniao") # AND participantes.status='1'
        for linha in c:
            self.qtdreuniao+=1
            strip=linha[1].replace(" ","-")
            self.selectreunioes+=str(linha[4])+"-Sala:"+linha[0]+"-Pauta:"+strip+" "
            sala=" Sala: "+linha[0]+"\n"
            pauta="Pauta: "+linha[1]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[2],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[3],"/")+"\n"
            reunioes+=sala+" "+pauta+" "+dataini+" "+datafim+"\n"
        if self.qtdreuniao==0:
            reunioes="Nenhuma reunião localizada para o seu perfil"
        return reunioes

    ##########################################################
    def reunioesOrganizadorAtiva(self,participante):
        datas=Datas()
        self.participante=str(participante)

        c = self.banco.conexao.cursor()
        self.qtdreuniao=0
        self.selectreunioes=""
        reunioes=""
        c.execute("select reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,reunioes.idreuniao from reunioes,participantes where reunioes.idcoordenador='"+self.participante+"' AND reunioes.status='1' AND reunioes.datafim>='"+str(datas.getHoje())+"' AND reunioes.atagerada='0' GROUP BY reunioes.idreuniao")
        for linha in c:
            self.qtdreuniao+=1
            strip=linha[1].replace(" ","-")
            self.selectreunioes+=str(linha[4])+"-Sala:"+linha[0]+"-Pauta:"+strip+" "
            sala=" Sala: "+linha[0]+"\n"
            pauta="Pauta: "+linha[1]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[2],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[3],"/")+"\n"
            reunioes+=sala+" "+pauta+" "+dataini+" "+datafim+"\n"
        if self.qtdreuniao==0:
            reunioes="Nenhuma reunião localizada para o seu perfil"
        return reunioes

    def reunioesOrganizadorFinalizada(self,participante,atagerada="0"):
        datas=Datas()
        self.participante=str(participante)

        c = self.banco.conexao.cursor()
        self.qtdreuniao=0
        self.selectreunioes=""
        reunioes=""
        c.execute("select reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim,reunioes.idreuniao from reunioes,participantes where reunioes.idcoordenador='"+self.participante+"' AND reunioes.status='1' AND reunioes.datafim<='"+str(datas.getHoje())+"' AND reunioes.atagerada='"+atagerada+"' GROUP BY reunioes.idreuniao") # AND participantes.status='1'
        for linha in c:
            caminho = 'arquivo/'+str(linha[4])+"-arquivo-reuniao.txt"
            if not os.path.exists(caminho):
                self.qtdreuniao+=1
                strip=linha[1].replace(" ","-")
                self.selectreunioes+=str(linha[4])+"-Sala:"+linha[0]+"-Pauta:"+strip+" "
                sala=" Sala: "+linha[0]+"\n"
                pauta="Pauta: "+linha[1]+"\n"
                dataini="Data inicio: "+datas.converteDataBRL(linha[2],"/")+"\n"
                datafim="Data fim: "+datas.converteDataBRL(linha[3],"/")+"\n"
                reunioes+=sala+" "+pauta+" "+dataini+" "+datafim+"\n"
        if self.qtdreuniao==0:
            reunioes="Nenhuma reunião localizada para o seu perfil"
        return reunioes

    def printSelectReunioes(self):
        return self.selectreunioes

    def reunioesParaAprovar(self):
        datas=Datas()

        c = self.banco.conexao.cursor()
        self.qtdreuniao=0
        self.selectreunioes=""
        reunioes=""
        c.execute("select reunioes.idreuniao,reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim from reunioes where reunioes.status='0' ORDER BY dataini ASC")
        for linha in c:
            self.qtdreuniao+=1
            strip=linha[2].replace(" ","-")
            self.selectreunioes+=str(linha[0])+"-Sala:"+linha[1]+"-Pauta:"+strip+" "
            idsala=" ID: "+str(linha[0])+"\n"
            sala=" Sala: "+linha[1]+"\n"
            pauta="Pauta: "+linha[2]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[3],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[4],"/")+"\n"
            reunioes+=idsala+" "+sala+" "+pauta+" "+dataini+" "+datafim+"\n"
        if self.qtdreuniao==0:
            reunioes="Nenhuma reunião localizada para o seu perfil"
        return reunioes

    def reunioesParticipantePendente(self,participante):
        self.participante=str(participante)
        datas=Datas()
        reunioes=""
        self.qtdreuniao=0
        d = self.banco.conexao.cursor()
        d.execute("select reunioes.idreuniao,reunioes.idsala,reunioes.pauta,reunioes.dataini,reunioes.datafim FROM reunioes,participantes WHERE participantes.idreuniao=reunioes.idreuniao AND participantes.idusuario='"+self.participante+"' AND participantes.status='0' AND reunioes.status='1'")
        for linha in d:
            self.qtdreuniao+=1
            id="ID: "+str(linha[0])+"\n"
            sala="Sala: "+linha[1]+"\n"
            pauta="Pauta: "+linha[2]+"\n"
            dataini="Data inicio: "+datas.converteDataBRL(linha[3],"/")+"\n"
            datafim="Data fim: "+datas.converteDataBRL(linha[4],"/")+"\n"
            reunioes+=" "+id+" "+sala+" "+pauta+" "+dataini+" "+datafim+"\n\n"
        if reunioes=="":
            reunioes="Nenhuma reunião encontrada. "
        return reunioes

    def alterarStatusReuniao(self,idreuniao,status):
        self.idreuniao=idreuniao
        self.status=status
        try:
            c = self.banco.conexao.cursor()
            e = self.banco.conexao.cursor()
            d = self.banco.conexao.cursor()
            c.execute(
                "update reunioes set status='" + self.status + "' WHERE idreuniao='"+self.idreuniao+"'")

            d.execute("select dataini,datafim,idsala FROM reunioes WHERE idreuniao='"+self.idreuniao+"'")
            for linha in d:
                e.execute("update reunioes set status='2' WHERE idreuniao!='"+self.idreuniao+"' AND (dataini='"+linha[0]+"' OR datafim='"+linha[0]+"' OR dataini='"+linha[1]+"' OR datafim='"+linha[1]+"') AND idsala='"+linha[2]+"'")

            self.banco.conexao.commit()

            self.mensagem="Reunião atualizada com sucesso!"
        except:
            self.mensagem="Ocorreu um erro na atualização da reunião"

    def printMensagem(self):
        return self.mensagem

    def atualizaAtaGerada(self,idreuniao):
        c = self.banco.conexao.cursor()
        c.execute("update reunioes set atagerada='1' WHERE idreuniao='"+idreuniao+"'")
        self.banco.conexao.commit()

    def gerarAtaReuniao(self,idreuniao):
        datas=Datas()
        self.idreuniao=idreuniao
        self.texto=""
        c = self.banco.conexao.cursor()
        c.execute("select * FROM reunioes WHERE idreuniao='"+self.idreuniao+"'")
        for linha in c:
            self.idreuniao=linha[0]
            self.sala=linha[1]
            self.idcoordenador=linha[2]
            self.pauta=linha[3]
            self.dataini=linha[4]
            self.datafim=linha[5]
            self.pubprivada=linha[6]
        c.execute("select nome FROM usuarios WHERE idusuario='"+self.idcoordenador+"'")
        for linha in c:
            self.nome=linha[0]

        self.usuarioconfirmou=[]
        self.usuariorecusou=[]

        c.execute("select usuarios.nome,participantes.status,participantes.idusuario FROM usuarios,participantes WHERE usuarios.idusuario=participantes.idusuario AND participantes.idreuniao='"+str(self.idreuniao)+"' GROUP By participantes.idparticipante")
        for linha in c:
            if linha[1]=="1":
                self.usuarioconfirmou.append(linha[0])
            elif linha[1]=="0":
                self.usuariorecusou.append(linha[0])

        self.texto+="    João Pessoa, "+str(datas.converteHojeBRL("/"))+"\n\n"
        self.texto+="    Dia "+str(datas.converteDataBRL(self.dataini,'/'))+" foi realizada a reunião com a pauta "+str(self.pauta)+" "
        self.texto+=", onde tivemos a presença de "+str(len(self.usuarioconfirmou))+" convidado(s), onde abordamos os diversos assuntos.\n"
        self.texto+=" "+str(len(self.usuariorecusou))+" convidado(s) não esteve(iveram) presente(s) no evento.\n\n"
        self.texto+=" A reunião foi presidida por "+str(self.nome)+"\n\n"
        self.texto+=" Lista de participantes da reunião: "
        for i in range(len(self.usuarioconfirmou)):
            if i<len(self.usuarioconfirmou):
                self.texto+=str(self.usuarioconfirmou[i])+", "
            else:
                self.texto+=str(self.usuarioconfirmou[i])
        self.texto+="\n\n Lista dos que faltaram a reunião: "
        for i in range(len(self.usuariorecusou)):
            if i<len(self.usuariorecusou):
                self.texto+=str(self.usuariorecusou[i])+", "
            else:
                self.texto+=str(self.usuariorecusou[i])
        self.texto+="\n\n    A reunião teve encerramento no dia "+str(datas.converteDataBRL(self.datafim,'/'))+" \n\n\n\n"
        self.texto+=" _________________________________\n"
        self.texto+="           Assinatura \n"

        return self.texto

    def atualizaReuniao(self,idreuniao,sala,dataini,datafim):
        c = self.banco.conexao.cursor()
        c.execute(
            "update reunioes set dataini='"+dataini+"',datafim='"+datafim+"',idsala='"+sala+"' WHERE idreuniao='"+idreuniao+"'")
        self.banco.conexao.commit()
        return "Reunião relocada com sucesso!"

    def pegaDetalhesReuniao(self,idreuniao,organizador):
        datas=Datas()
        self.organizador=str(organizador)
        self.idreuniao=str(idreuniao)

        c = self.banco.conexao.cursor()
        c.execute("select reunioes.dataini,reunioes.datafim,reunioes.idsala,reunioes.idreuniao from reunioes,participantes where reunioes.idcoordenador='"+self.organizador+"' AND reunioes.idreuniao='"+self.idreuniao+"'") # AND reunioes.datafim>='"+str(datas.getHoje())+"' AND reunioes.atagerada='0' GROUP BY reunioes.idreuniao
        for linha in c:
            self.dataini=linha[0]
            self.datafim=linha[1]
            self.idsala=linha[2]
            self.idreuniao=linha[3]

    def getDataIni(self):
        return self.dataini

    def getDataFim(self):
        return self.datafim

    def getIdSala(self):
        return self.idsala



#teste=Reuniao("1","101","1","Teste manual","2019-11-11","2019-11-11","0","1")
#teste.verificaReuniaoExpirada()
#print(teste.cadastraReuniao())
#print(teste.buscaUltimoId())
##print (teste.reunioesParticipantePendente("2"))
##print(teste.filtraReuniao("0","1","1","4"))
#teste=Reuniao()
##print(teste.listaReuniaoPublica())
#print(teste.listaReuniaoPublica())
#print(teste.qtdReuniao("1"))
#print (teste.qtdReuniaoUsuario("1"))

#teste=Reuniao()
#teste.pegaDetalhesReuniao("3","1")
#print(teste.getIdSala())
#teste.updateReuniao()
##print(teste.gerarAtaReuniao("1"))
#print(teste.reunioesAprovadaConfirmada("2"))
#teste.reunioesOrganizadorAtiva('1')
#reunioesOrganizadorAtiva
#print(teste.printSelectReunioes())
