from Banco import Banco

class Salas(object):
    def __init__(self,idsala="",nomesala="", numsala="", capacidade="", status=""):
        self.idsala=idsala
        self.nomesala=nomesala
        self.numsala=numsala
        self.status=status
        self.capacidade=capacidade

    def criarSala(self):
        #print("insert into salas(nomesala,numsala,capacidade,status) values ('"+self.nomesala+"','"+self.numsala+"','"+self.capacidade+"','"+self.status+"')")
        banco = Banco()
        if self.verDuplicidade(self.numsala)==0:
            try:
                c = banco.conexao.cursor()
                c.execute("insert into salas(nomesala,numsala,capacidade,status) values ('"+self.nomesala+"','"+self.numsala+"','"+self.capacidade+"','"+self.status+"')")
                banco.conexao.commit()
                c.close()
                return "Sala cadastrada com sucesso!"
            except:
                return "Ocorreu um erro no cadastro da sala!"
        else:
            return "ERRO! Sala já incluida anteriormente"

    def verDuplicidade(self,numsala):
        self.numsala=numsala
        banco = Banco()
        total=0
        c = banco.conexao.cursor()
        c.execute("select * from salas where numsala='" + self.numsala + "'")
        for linha in c:
            total+=1
        return total
        c.close()

    def listaSalas(self,status):
        self.status=status
        banco = Banco()
        c = banco.conexao.cursor()
        dados=""
        c.execute("select * from salas where status='"+self.status+"'")
        if self.status==0:
            imprime="Lista de salas inativas"
        else:
            imprime="Lista de salas ativas"

        for linha in c:
            nome="Nome: "+linha[1]+"\n"
            numero="Numero: "+linha[2]+"\n\n"
            dados+=nome+" "+numero+"\n"
        if dados:
            return imprime+"\n"+dados
        else:
            return "Nenhuma sala cadastrada com o status selecionado"
        c.close()

    def listaSalasTodas(self):
        banco = Banco()
        c = banco.conexao.cursor()
        dados=""
        c.execute("select * from salas")
        if self.status==0:
            imprime="Lista de salas inativas"
        else:
            imprime="Lista de salas ativas"

        for linha in c:
            nome="Nome: "+linha[1]+"\n"
            numero="Numero: "+linha[2]+"\n"
            capacidade="Capacidade: "+linha[3]+" pessoas\n"
            if linha[4]==0:
                status="Status: Em análise\n"
            else:
                status="Status: Ativa\n"
            dados+=nome+" "+numero+" "+capacidade+" "+status+"\n"
        if dados:
            return imprime+"\n"+dados
        else:
            return "Nenhuma sala cadastrada com o status selecionado"
        c.close()

    def salaDisponivel(self,sala):
        self.sala=sala
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("select * from salas where idsala='"+self.sala+"'")
        for linha in c:
            self.status=linha[3]
        return self.status

    def imprimeSala(self,idsala):
        self.idsala=idsala
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("select * from salas where idsala='"+self.idsala+"'")
        imprime=c.fetchone()
        return imprime[2]



    '''def verSala(self):
        
    def atualizaSala(self):

    def excluiSala(selfs):

    '''

'''cadastra=Salas("0","Copacabana","102","1")
print(cadastra.criarSala())'''
'''teste=Salas()
imprime=teste.imprimeSala("1")
print(imprime)'''
'''for i in range(len(imprime))
    print(imprime[i])'''