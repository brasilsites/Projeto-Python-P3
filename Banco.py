import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect(('banco.db'))
        self.createTable()
        self.createTblSalas()
        self.createTblReunioes()
        self.createTblParticipantes()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios(
                    idusuario integer primary key autoincrement,
                    nome text,
                    login text,
                    senha text,
                    nivel text);""")
        self.conexao.commit()
        c.close()

    def createTblSalas(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists salas(
                    idsala integer primary key autoincrement,
                    nomesala text,
                    numsala text,
                    capacidade text,
                    status text);""")
        self.conexao.commit()
        c.close()

    def createTblReunioes(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists reunioes(
                    idreuniao integer primary key autoincrement,
                    idsala text,
                    idcoordenador text,
                    pauta text,
                    dataini date,
                    datafim date,
                    pubprivada text,
                    status text,
                    atagerada text);""")
        self.conexao.commit()
        c.close()

    def createTblParticipantes(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists participantes(
                    idparticipante integer primary key autoincrement,
                    idusuario text,
                    idreuniao text,
                    status text);""")
        self.conexao.commit()
        c.close()