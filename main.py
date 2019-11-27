from tkinter import *
from tkinter import ttk,filedialog
from Usuarios import Usuarios
from Salas import Salas
from Reuniao import Reuniao
import Class as cl
import Datas,os,shutil
import Participantes as part

#############################################################
#############################################################
'''
    Projeto P3 - Estrutura de Dados
    Professora: Aline Marques de Morais
    Alunos: Diomar Victor
            Edson Ferreira
            Italo Matheus
            Leonardo Hiago 
'''
#############################################################
#############################################################

root=Tk()
v=IntVar()
###
veradmin=Usuarios()
if veradmin.verificaDuplicidade("admin","1234","1")==0:
    veradmin.insereUsuario("Admin","admin","1234","1")
usuarios=Usuarios()
listagem=cl.Class()

class App():
    def __init__(self,master=None):
        self.frame1=Frame(master)
        self.frame2=Frame(master)
        self.frame3=Frame(master)
        self.frame4=Frame(master)
        self.frame5=Frame(master)
        self.frame6=Frame(master)
        self.frame7=Frame(master)
        self.frame8=Frame(master)
        self.frame9=Frame(master)
        self.frame10=Frame(master)
        self.frame11=Frame(master)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.frame9.pack()
        self.frame10.pack()
        self.frame11.pack()

        self.fontePadrao=("Arial","10")
        self.fonteVermelho=("Arial","12","bold")
        self.fonteBold=("Arial","10","bold")
        self.fonteGrande=("Calibre","18","bold")

        self.xscrollbar=""
        self.yscrollbar=""

        self.idcoordenador=""
        self.idusuario=""

        self.telaInicio()

    ####################################################################################
    # Criação da telaInicio com as informações iniciais e carregamento do menu principal
    ####################################################################################
    def telaInicio(self):
        self.limparTela()
        self.menuInicio()

        self.photo=PhotoImage(file="img\MoraesCorporation.png")
        self.label=Label(self.frame1, image=self.photo)
        self.label.pack()

        self.label_1=Label(self.frame2,text="Bem vindo(a) ao Sistema e-meeting, \n utilize o menu para acessar as opções",font=self.fonteGrande)
        self.label_1.pack()

    def menuInicio(self):
        self.menu=Menu(root)
        root.config(menu=self.menu)
        comandomenu=Menu(self.menu)
        comandomenu.add_command(label="Inicio ",command=self.telaInicio)
        comandomenu.add_command(label="Reuniões Públicas ",command=self.printReuniaoPublica)
        comandomenu.add_command(label="Login Usuário ",command=self.loginUsuario)
        comandomenu.add_command(label="Login Coordenador ",command=self.loginCoord)
        comandomenu.add_command(label="Login Gestor ",command=self.loginGestor)
        comandomenu.add_command(label="Cadastro Usuário ",command=self.formCadastraUsuario)
        self.menu.add_cascade(label="Menu",menu=comandomenu)
        self.segundoMenu(self.menu)

    ##############################################################################################
    # Tela de Usuário: Exibe dados de reuniões a confirmar/confirmadas e aponta para demais telas
    ##############################################################################################
    def menuUsuario(self):
        self.menu=Menu(root)
        root.config(menu=self.menu)
        comandomenu=Menu(self.menu)
        comandomenu.add_command(label="Inicio ",command=self.homeUsuario)
        submenu=Menu(comandomenu)
        submenu.add_command(label="Criar",command=self.formReuniao)
        submenu.add_command(label="Ver Reuniões",command=self.verReuniao)
        submenu.add_command(label="Ver Salas",command=self.listagemSalas)
        submenu.add_command(label="Gerar atas",command=self.selecionaAtaReuniao)
        submenu.add_command(label="Alterar atas",command=self.selecionaAtaAlterar)
        submenu.add_command(label="Confirmar presença",command=self.formConfirmaPresenca)
        submenu.add_command(label="Enviar arquivo de atas",command=self.selecionaAtaEnvioArquivo)
        submenu.add_command(label="Adicionar participantes",command=self.reuniaoParticipanteIncluir)
        comandomenu.add_cascade(label="Reunião ",menu=submenu)
        self.menu.add_cascade(label="Menu",menu=comandomenu)
        self.segundoMenu(self.menu)

    def homeUsuario(self):
        self.limparTela()
        self.menuUsuario()
        listreun=Reuniao()
        listreun.qtdReuniaoUsuarioStatus(self.idusuario,"0")
        #self.idusuario
        self.photo=PhotoImage(file="img\MoraesCorporation.png")
        self.label=Label(self.frame1, image=self.photo,height=120)
        self.label.pack()

        self.label_1=Label(self.frame2,text=str(veradmin.nomeUsuario())+", bem vindo(a) ao Sistema e-meeting, \n utilize o menu para acessar as opções",font=self.fonteGrande)
        self.label_1.pack()

        self.label2=Label(self.frame3,text="Reuniões a confirmar: "+str(listreun.printQtdReuniao()),font=self.fonteVermelho,fg="#e60000",height=3)
        self.label2.pack()

        listreun.qtdReuniaoUsuarioStatus(self.idusuario,"1")

        self.label3=Label(self.frame4,text="Reuniões confirmadas: "+str(listreun.printQtdReuniao()),font=self.fonteVermelho,fg="#00994d",height=2)
        self.label3.pack()

    def loginUsuario(self):
        self.limparTela()
        self.menuInicio()

        self.titulo=Label(self.frame1,text="Dados do usuário",font=self.fonteVermelho,height=5)
        self.titulo.pack()

        self.nomeLabel=Label(self.frame2,text="Login",font=self.fonteBold,height=2)
        self.nomeLabel.pack(side=LEFT)

        self.nome=Entry(self.frame2)
        self.nome["width"]=30
        self.nome["font"]=self.fontePadrao
        self.nome.pack(side=RIGHT)

        self.senhaLabel=Label(self.frame3,text="Senha",font=self.fonteBold,height=2)
        self.senhaLabel.pack(side=LEFT)

        self.senha=Entry(self.frame3)
        self.senha["width"]=30
        self.senha["font"]=self.fontePadrao
        self.senha["show"]="*"
        self.senha.pack(side=RIGHT)

        self.autenticar=Button(self.frame4)
        self.autenticar["text"]="Autenticar"
        self.autenticar["font"]=("Calibri","8")
        self.autenticar["width"]=12
        self.autenticar["command"]=self.verificaLoginUsu
        self.autenticar.pack()

        self.mensagem=Label(self.frame5,text="",font=self.fonteVermelho)
        self.mensagem.pack()

    def verificaLoginUsu(self):
        self.nivel="3"

        usuario=self.nome.get()
        senha=self.senha.get()
        if veradmin.verificaDuplicidade(usuario,senha,"3")>0:
            self.idusuario=veradmin.idUsuario()
            self.homeUsuario()
        else:
            self.mensagem["text"]="Erro na autenticação"

    def formCadastraUsuario(self):
        self.limparTela()
        self.menuInicio()

        self.titulo=Label(self.frame1,text="Cadastro do usuário",font=self.fonteVermelho,height=5)
        self.titulo.pack()

        self.nomeLabel=Label(self.frame2,text="Nome",font=self.fonteBold,height=2)
        self.nomeLabel.pack(side=LEFT)

        self.nome=Entry(self.frame2)
        self.nome["width"]=30
        self.nome["font"]=self.fontePadrao
        self.nome.pack(side=RIGHT)

        self.loginLabel=Label(self.frame3,text="Login",font=self.fonteBold,height=2)
        self.loginLabel.pack(side=LEFT)

        self.login=Entry(self.frame3)
        self.login["width"]=30
        self.login["font"]=self.fontePadrao
        self.login.pack(side=RIGHT)

        self.senhaLabel=Label(self.frame4,text="Senha",font=self.fonteBold,height=2)
        self.senhaLabel.pack(side=LEFT)

        self.senha=Entry(self.frame4)
        self.senha["width"]=30
        self.senha["font"]=self.fontePadrao
        self.senha["show"]="*"
        self.senha.pack(side=RIGHT)

        self.autenticar=Button(self.frame5)
        self.autenticar["text"]="Cadastrar"
        self.autenticar["font"]=("Calibri","8")
        self.autenticar["width"]=12
        self.autenticar["command"]=self.cadastraUsuario
        self.autenticar.pack()

        self.mensagem=Label(self.frame5,text="",font=self.fonteVermelho)
        self.mensagem.pack()

    def cadastraUsuario(self):
        nome=self.nome.get()
        login=self.login.get()
        senha=self.senha.get()

        if veradmin.verificaDuplicidade(login,senha,"3")==0:
            self.mensagem["text"]=veradmin.insereUsuario(nome,login,senha,"3")
        else:
            self.mensagem["text"]="Usuario já foi cadastrado anteriormente"

    ##############################################################################################
    # Tela de Coordenador: Carrega o menu do Coordenador que abrirá páginas especificas
    ##############################################################################################
    def menuCoordenador(self):
        self.menu=Menu(root)
        root.config(menu=self.menu)
        comandomenu=Menu(self.menu)
        comandomenu.add_command(label="Inicio ",command=self.homeCoordenador)
        submenu=Menu(comandomenu)
        submenu.add_command(label="Criar",command=self.formReuniao)
        submenu.add_command(label="Ver Reuniões",command=self.verReuniao)
        submenu.add_command(label="Gerar atas",command=self.selecionaAtaReuniao)
        submenu.add_command(label="Alterar atas",command=self.selecionaAtaAlterar)
        submenu.add_command(label="Enviar arquivo de atas",command=self.selecionaAtaEnvioArquivo)
        submenu.add_command(label="Confirmar presença",command=self.formConfirmaPresenca)
        submenu.add_command(label="Realocar reunião/sala",command=self.selectSalaRelocar)
        submenu.add_command(label="Adicionar participantes",command=self.reuniaoParticipanteIncluir)
        comandomenu.add_cascade(label="Reunião ",menu=submenu)
        self.menu.add_cascade(label="Menu",menu=comandomenu)
        self.segundoMenu(self.menu)

    def homeCoordenador(self):
        self.limparTela()
        self.menuCoordenador()

        self.photo=PhotoImage(file="img\MoraesCorporation.png")
        self.label=Label(self.frame1, image=self.photo,height=120)
        self.label.pack()

        self.label_1=Label(self.frame2,text="Coordenador(a),\n bem vindo(a) ao Sistema e-meeting, \n utilize o menu para acessar as opções",font=self.fonteGrande)
        self.label_1.pack()

    def loginCoord(self):
        self.limparTela()
        self.menuInicio()

        self.titulo=Label(self.frame1,text="Dados do Coordenador",font=self.fonteVermelho,height=5)
        self.titulo.pack()

        self.nomeLabel=Label(self.frame2,text="Login",font=self.fontePadrao,height=2)
        self.nomeLabel.pack(side=LEFT)

        self.nome=Entry(self.frame2)
        self.nome["width"]=30
        self.nome["font"]=self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel=Label(self.frame3,text="Senha",font=self.fontePadrao,height=2)
        self.senhaLabel.pack(side=LEFT)

        self.senha=Entry(self.frame3)
        self.senha["width"]=30
        self.senha["font"]=self.fontePadrao
        self.senha["show"]="*"
        self.senha.pack(side=LEFT)

        self.autenticar=Button(self.frame4)
        self.autenticar["text"]="Autenticar"
        self.autenticar["font"]=("Calibri","8")
        self.autenticar["width"]=12
        self.autenticar["command"]=self.verificaLoginCoo
        self.autenticar.pack()

        self.mensagem=Label(self.frame5,text="",font=self.fonteVermelho,height=2)
        self.mensagem.pack()

    def verificaLoginCoo(self):
        self.nivel="1"

        usuario=self.nome.get()
        senha=self.senha.get()
        if veradmin.verificaDuplicidade(usuario,senha,self.nivel)>0:
            self.idcoordenador=veradmin.idUsuario()
            self.homeCoordenador()
        else:
            self.mensagem["text"]="Erro na autenticação"

    ##############################################################################################
    # Tela de Gestor: Responsável por criar as salas e autorizar as reuniões
    ##############################################################################################
    def menuGestor(self):
        self.menu=Menu(root)
        root.config(menu=self.menu)
        comandomenu=Menu(self.menu)
        comandomenu.add_command(label="Inicio ",command=self.homeGestor)
        comandomenu.add_separator()
        comandomenu.add_command(label="Reunião - aprovar ",command=self.listaReuniaoAprovar)
        comandomenu.add_command(label="Salas - cadastrar ",command=self.cadastraSala)
        self.menu.add_cascade(label="Menu",menu=comandomenu)
        self.segundoMenu(self.menu)

    def homeGestor(self):
        self.limparTela()
        self.menuGestor()

        self.photo=PhotoImage(file="img\MoraesCorporation.png")
        self.label=Label(self.frame1, image=self.photo,height=120)
        self.label.pack()

        self.label_1=Label(self.frame2,text="Gestor(a),\n bem vindo(a) ao Sistema e-meeting, \n utilize o menu para acessar as opções",font=self.fonteGrande)
        self.label_1.pack()

    def loginGestor(self):
        self.limparTela()
        self.menuInicio()

        self.titulo=Label(self.frame1,text="Dados do Gestor",font=self.fonteVermelho,height=5)
        self.titulo.pack()

        self.nomeLabel=Label(self.frame2,text="Login",font=self.fontePadrao,height=2)
        self.nomeLabel.pack(side=LEFT)

        self.nome=Entry(self.frame2)
        self.nome["width"]=30
        self.nome["font"]=self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel=Label(self.frame3,text="Senha",font=self.fontePadrao,height=2)
        self.senhaLabel.pack(side=LEFT)

        self.senha=Entry(self.frame3)
        self.senha["width"]=30
        self.senha["font"]=self.fontePadrao
        self.senha["show"]="*"
        self.senha.pack(side=LEFT)

        self.autenticar=Button(self.frame4)
        self.autenticar["text"]="Autenticar"
        self.autenticar["font"]=("Calibri","8")
        self.autenticar["width"]=12
        self.autenticar["command"]=self.verificaLoginGestor
        self.autenticar.pack()

        self.mensagem=Label(self.frame5,text="",font=self.fonteVermelho,height=2)
        self.mensagem.pack()



    def verificaLoginGestor(self):
        self.nivel="2"

        usuario=self.nome.get()
        senha=self.senha.get()
        if usuario=="edsonfsilva" and senha=="1234":
            self.homeGestor()
        else:
            self.mensagem["text"]="Erro na autenticação"


    ##################
    # Comandos gerais
    ##################
    def cadastraSala(self):
        self.limparTela()
        self.menuGestor()

        data_contents = StringVar()

        self.titulo=Label(self.frame1,text="Cadastro de Salas")
        self.titulo["font"]=("Arial","10","bold")
        self.titulo.pack()

        self.nomeLabel=Label(self.frame2,text="Nome da Sala",font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome=Entry(self.frame2)
        self.nome["width"]=30
        self.nome["font"]=self.fontePadrao
        self.nome.pack(side=LEFT)

        self.loginLabel=Label(self.frame3,text="Numero da Sala",font=self.fontePadrao)
        self.loginLabel.pack(side=LEFT)

        self.numero=Entry(self.frame3)
        self.numero["width"]=30
        self.numero["font"]=self.fontePadrao
        self.numero.pack(side=LEFT)

        self.senhaLabel=Label(self.frame4,text="Status",font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.var = IntVar()
        self.status=Radiobutton(self.frame4,text="Inativa",value=0,padx=20,variable=self.var)
        self.status.pack(side=LEFT)
        self.status=Radiobutton(self.frame4,text="Ativa",value=1,padx=20,variable=self.var)
        self.status.select()
        self.status.pack(side=RIGHT)

        self.mensagem=Label(self.frame5,text="Capacidade (nº Pessoas)",font=self.fontePadrao)
        self.mensagem.pack()

        self.capacidade=Entry(self.frame5)
        self.capacidade["width"]=30
        self.capacidade["font"]=self.fontePadrao
        self.capacidade.pack(side=LEFT)

        self.mensagem=Label(self.frame6,text="",font=self.fontePadrao)
        self.mensagem.pack()

        self.autenticar=Button(self.frame6)
        self.autenticar["text"]="Cadastrar"
        self.autenticar["font"]=("Calibri","8")
        self.autenticar["width"]=12
        self.autenticar["command"]=self.cadastrarSala
        self.autenticar.pack()

        salalista=Salas()
        self.lista=Label(self.frame7,text="Salas",font=self.fontePadrao)
        self.barraRolagem()
        text = Text(self.frame7,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        text.insert(INSERT, salalista.listaSalas("1"))
        text.pack(side=LEFT,padx=20,pady=20)
        self.barraRolagemPack(text)
        self.lista.pack()

    def cadastrarSala(self):
        self.statussala=str(self.var.get())
        salacadastra=Salas(" ",self.nome.get(),self.numero.get(),self.capacidade.get(),self.statussala)
        self.mensagem["text"]=salacadastra.criarSala()
        self.mensagem.pack()

        self.limparTela()
        self.menuGestor()
        self.cadastraSala()

    def formReuniao(self):
        self.limparTela()
        if self.idcoordenador:
            self.menuCoordenador()
        elif self.idusuario:
            self.menuUsuario()

        self.titulo=Label(self.frame1,text="Reserva de Sala de Reunião",height=2)
        self.titulo["font"]=("Arial","14","bold")
        self.titulo.pack()

        self.titulo=Label(self.frame1,text="\n Obs: o cadastro fica pendente de aprovação pelo gestor",fg="#e60000",height=2)
        self.titulo["font"]=("Arial","10","bold")
        self.titulo.pack()

        self.datainiLabel=Label(self.frame2,text="Data de Inicio (dd/mm/aaaa): ",font=self.fontePadrao,height=3)
        self.datainiLabel.pack(side=LEFT)

        listagem.inputDia()

        self.selectDia=StringVar()
        dia=listagem.printDia()
        self.dia=ttk.Combobox(self.frame2,width=15,textvariable=self.selectDia,values=dia,height=1)
        self.dia.set(Datas.Datas().getDia())
        self.dia["width"]=2
        #self.dia.grid(column=1,row=0)
        self.dia.pack(side=LEFT)

        self.barra=Label(self.frame2,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectMes=StringVar()
        mes=listagem.inputMes()
        self.mes=ttk.Combobox(self.frame2,width=15,textvariable=self.selectMes,values=mes,height=1)
        self.mes.set(Datas.Datas().getMes())
        self.mes["width"]=2
        self.mes.pack(side=LEFT)

        self.barra=Label(self.frame2,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectAno=StringVar()
        ano=listagem.inputAno()
        self.ano=ttk.Combobox(self.frame2,width=15,textvariable=self.selectAno,values=ano,height=1)
        self.ano.set(Datas.Datas().getAno())
        self.ano["width"]=4
        self.ano.pack(side=LEFT)


        self.datafimLabel=Label(self.frame3,text="Data Fim (dd/mm/aaaa): ",font=self.fontePadrao,height=3)
        self.datafimLabel.pack(side=LEFT)

        self.selectDiaFim=StringVar()
        dia=listagem.printDia()
        self.diafim=ttk.Combobox(self.frame3,width=15,textvariable=self.selectDiaFim,values=dia,height=1)
        self.diafim.set(Datas.Datas().getDia())
        self.diafim["width"]=2
        self.diafim.pack(side=LEFT)

        self.barra=Label(self.frame3,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectMesFim=StringVar()
        mes=listagem.inputMes()
        self.mesfim=ttk.Combobox(self.frame3,width=15,textvariable=self.selectMesFim,values=mes,height=1)
        self.mesfim.set(Datas.Datas().getMes())
        self.mesfim["width"]=2
        self.mesfim.pack(side=LEFT)

        self.barra=Label(self.frame3,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectAnoFim=StringVar()
        ano=listagem.inputAno()
        self.anofim=ttk.Combobox(self.frame3,width=15,textvariable=self.selectAnoFim,values=ano,height=1)
        self.anofim.set(Datas.Datas().getAno())
        self.anofim["width"]=4
        self.anofim.pack(side=LEFT)

        self.periodo=Button(self.frame4)
        self.periodo["text"]="Buscar Salas"
        self.periodo["font"]=("Calibri","8")
        self.periodo["width"]=30
        self.periodo["command"]=self.listaSalas
        self.periodo.pack()

        self.mensagem=Label(self.frame5,text="",font=self.fontePadrao,height=1)
        self.mensagem.pack()


    def listaSalas(self):
        self.frame4.destroy()
        self.dataini=self.ano.get()+"-"+self.mes.get()+"-"+self.dia.get()
        self.datafim=self.anofim.get()+"-"+self.mesfim.get()+"-"+self.diafim.get()

        if Datas.Datas().validaDatas(self.dataini,self.datafim)==True:
            self.selectSalas=StringVar()
            self.arraylista=Reuniao().buscarReuniaoDatas(self.dataini,self.datafim)
            self.listas1=Label(self.frame6,text=self.arraylista[0],font=self.fontePadrao)
            self.listas1.pack(side=LEFT)

            self.salas=ttk.Combobox(self.frame6,textvariable=self.selectSalas,values=self.arraylista)
            self.salas["width"]=22
            self.salas.pack(side=LEFT)

            self.nomePauta=Label(self.frame7,text="Pauta da Reunião",font=self.fontePadrao,height=2)
            self.nomePauta.pack(side=LEFT)

            self.pauta=Entry(self.frame7)
            self.pauta["width"]=30
            self.pauta["font"]=self.fontePadrao
            self.pauta.pack(side=LEFT)

            self.var = IntVar()
            self.pubprivada=Radiobutton(self.frame8,text="Privada",value=1,padx=20,variable=self.var) #
            self.pubprivada.pack(side=RIGHT)
            self.pubprivada=Radiobutton(self.frame8,text="Pública",value=0,padx=20,variable=self.var) #
            self.pubprivada.pack()

            self.finaliza=Button(self.frame9)
            self.finaliza["text"]="Cadastrar"
            self.finaliza["font"]=("Calibri","8")
            self.finaliza["width"]=30
            self.finaliza["command"]=self.cadastraReuniao
            self.finaliza.pack()

            self.mensagemFim=Label(self.frame10,text="",font=self.fonteVermelho, height=5)
            self.mensagemFim.pack()
        else:
            self.mensagemFim=Label(self.frame10,text="Erro! Tente novamente com o periodo correto",font=self.fonteVermelho, height=5)
            self.mensagemFim.pack()

    def cadastraReuniao(self):
        self.pubp=str(self.var.get())
        if self.idcoordenador:
            organizador=self.idcoordenador
        elif self.idusuario:
            organizador=self.idusuario

        cadReuniao=Reuniao("",self.salas.get(),str(organizador),self.pauta.get(),self.dataini,self.datafim,self.pubp,"0")
        self.mensagemFim["text"]=cadReuniao.cadastraReuniao()
        self.idultimareuniao=cadReuniao.buscaUltimoId()
        self.selectParticipantes()

    def printReuniaoPublica(self):
        self.limparTela()

        self.photo=PhotoImage(file="img\MoraesCorporation.png")
        self.label=Label(self.frame1, image=self.photo)
        self.label.pack()

        listreun=Reuniao()
        if listreun.qtdReuniao("0")>0:
            self.label_1=Label(self.frame2,text="Lista de Reuniões Públicas",font=self.fonteGrande)
            self.label_1.pack()

            self.label2=Label(self.frame3,text="Listagem apenas de reuniões aprovadas",font=self.fonteBold,fg="#e60000")
            self.label2.pack()

            self.barraRolagem()
            text = Text(self.frame4,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
            text.insert(INSERT, listreun.listaReuniaoPublica())
            text.pack(side=LEFT,padx=20,pady=20)
            self.barraRolagemPack(text)
        else:
            self.label_1=Label(self.frame2,text="Não foi(ram) encontrada(s) \n Reunião(ões) Pública(s)",font=self.fonteGrande)
            self.label_1.pack()

    def printReuniaoUsuarioAceitar(self):
        self.limparTela()
        #self.idusuario

        listreun=Reuniao()
        if listreun.qtdReuniao("0")>0:
            self.label_1=Label(self.frame2,text="Lista de Reuniões para confirmar",font=self.fonteGrande)
            self.label_1.pack()

            self.barraRolagem()
            text = Text(self.frame2,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
            text.insert(INSERT, listreun.listaReuniaoPublica())
            text.pack(side=LEFT,padx=20,pady=20)
            self.barraRolagemPack(text)
        else:
            self.label_1=Label(self.frame2,text="Não foi(ram) encontrada(s) \n Reunião(ões) Pública(s)",font=self.fonteGrande)
            self.label_1.pack()

    def selectParticipantes(self):
        self.limparTela()

        if self.idcoordenador:
            organizador=self.idcoordenador
        elif self.idusuario:
            organizador=self.idusuario

        self.mensagem=Label(self.frame1,text="Selecione o(s) participante(s) para a reunião",font=self.fonteVermelho,height=3)
        self.mensagem.pack()

        self.valores = StringVar()
        self.valores.set(usuarios.usuarioParticipante(organizador))

        self.lstbox = Listbox(self.frame2, listvariable=self.valores, selectmode=MULTIPLE, width=20, height=5)
        self.lstbox.grid(column=0, row=0, columnspan=2)

        self.btn = Button(self.frame3, text="Inserir")
        self.btn["command"]=self.selectSelect
        self.btn.grid(column=1, row=1)

        self.label=Label(self.frame4,text="",font=self.fonteGrande)
        self.label.pack()

    ####################################
    ####################################
    ####################################
    def reuniaoParticipanteIncluir(self):
        self.limparTela()
        if self.idcoordenador:
            self.organizador=self.idcoordenador
        elif self.idusuario:
            self.organizador=self.idusuario

        listreun=Reuniao()
        listreun.reunioesOrganizadorAtiva(self.organizador)
        if listreun.printQtdReuniao()>0:
            self.label_1=Label(self.frame1,text="Lista de Reuniões para incluir participante",font=self.fonteGrande)
            self.label_1.pack()

            self.selectReunioes=StringVar()
            self.listareuniao=ttk.Combobox(self.frame2,width=15,textvariable=self.selectReunioes,values=listreun.printSelectReunioes(),height=2)
            self.listareuniao["width"]=40
            self.listareuniao.pack(side=LEFT)

            self.btn = Button(self.frame3, text="Inserir")
            self.btn["command"]=self.selectParticipantesNovo
            self.btn.grid(column=1, row=1)
        else:
            self.label_1=Label(self.frame3,text="Não foi(ram) encontrada(s) \n Reunião(ões) Organizada por você",font=self.fonteGrande)
            self.label_1.pack()

    def selectParticipantesNovo(self):
        #self.limparTela()

        if self.idcoordenador:
            self.organizador=self.idcoordenador
        elif self.idusuario:
            self.organizador=self.idusuario

        self.mensagem=Label(self.frame4,text="Selecione o(s) participante(s) para a reunião",font=self.fonteVermelho,height=1)
        self.mensagem.pack()

        self.valores = StringVar()
        self.idreuniao=self.listareuniao.get().split('-')
        self.valores.set(part.Participantes().buscarParticipantesAdicionar(self.idreuniao[0],str(self.organizador)))
        #print(reuniao[0],str(self.idcoordenador))

        #print(reuniao[0])

        self.lstbox = Listbox(self.frame5, listvariable=self.valores, selectmode=MULTIPLE, width=20, height=5)
        self.lstbox.grid(column=0, row=0, columnspan=2)

        self.btn = Button(self.frame6, text="Inserir")
        self.btn["command"]=self.insereParticipanteNovo
        self.btn.grid(column=1, row=1)

        self.label=Label(self.frame7,text="",font=self.fonteGrande)
        self.label.pack()
    ####################################
    ####################################
    ####################################

    def insereParticipanteNovo(self):
        reslist = list()
        seleccion = self.lstbox.curselection()
        self.frame4.destroy()
        for i in seleccion:
            entrada = self.lstbox.get(i)
            reslist.append(entrada)
        for val in reslist:
            val=val.split('-',2)
            if part.Participantes(val[0],self.idreuniao[0],"0").insereParticipante()==True:
                self.frame3.destroy()
                self.label["text"]="Participante cadastrado com sucesso!"
            else:
                self.label["text"]="Erro ao cadastrar participante!"
        self.frame5.destroy()
        self.frame6.destroy()


    def verReuniao(self):
        self.limparTela()


        #Formulário

        self.nomePubpriva=Label(self.frame1,text="Reunião pública/privada",font=self.fontePadrao,width=35)
        self.nomePubpriva.pack(side=LEFT,expand=True)

        self.var1 = IntVar()
        self.pubpriv=Radiobutton(self.frame1,text="Publica",value=0,padx=1,variable=self.var1,width=20)
        self.pubpriv.pack(side=RIGHT,expand=True)
        self.pubpriv=Radiobutton(self.frame1,text="Privada",value=1,padx=1,variable=self.var1,width=15)
        self.pubpriv.pack(side=RIGHT,expand=True)

        self.encerra=Label(self.frame2,text="Reunião concluida/futura",font=self.fontePadrao,width=35)
        self.encerra.pack(side=LEFT,expand=True)

        self.var2 = IntVar()
        self.encfut=Radiobutton(self.frame2,text="Concluida",value=0,padx=1,variable=self.var2,width=20)
        self.encfut.pack(side=RIGHT,expand=True)
        self.encfut=Radiobutton(self.frame2,text="Futura",value=1,padx=1,variable=self.var2,width=15)
        self.encfut.pack(side=RIGHT,expand=True)

        self.ativa=Label(self.frame3,text="Selecione o status de aprovação pelo Gestor",font=self.fontePadrao,width=35)
        self.ativa.pack(side=LEFT,expand=True)

        self.var3 = IntVar()
        self.aguardaprov=Radiobutton(self.frame3,text="Aguardando aprovação",value=0,padx=1,variable=self.var3,width=20)
        self.aguardaprov.pack(side=RIGHT,expand=True)
        self.aguardaprov=Radiobutton(self.frame3,text="Aprovada",value=1,padx=1,variable=self.var3,width=15)
        self.aguardaprov.pack(side=RIGHT,expand=True)

        self.organizador=Label(self.frame4,text="Selecione Organizador/Participante",font=self.fontePadrao,width=35)
        self.organizador.pack(side=LEFT,expand=True)

        self.var4 = IntVar()
        self.orgpart=Radiobutton(self.frame4,text="Organizador",value=0,padx=1,variable=self.var4,width=20)
        self.orgpart.pack(side=RIGHT,expand=True)
        self.orgpart=Radiobutton(self.frame4,text="Participante",value=1,padx=1,variable=self.var4,width=15)
        self.orgpart.pack(side=RIGHT,expand=True)

        self.finaliza=Button(self.frame5)
        self.finaliza["text"]="Ver reuniões"
        self.finaliza["font"]=("Calibri","8")
        self.finaliza["width"]=30
        self.finaliza["command"]=self.listarReuniao
        self.finaliza.pack()

        self.label_1=Label(self.frame6,text="",font=self.fonteGrande)
        self.label_1.pack()

    def listarReuniao(self):
        self.pubpriv=self.var1.get()
        self.encfut=self.var2.get()
        self.aguardaprov=self.var3.get()
        self.orgpart=self.var4.get()

        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame5.destroy()
        #verifica se é coordenador ou usuário
        if self.idcoordenador:
            self.organizador=self.idcoordenador
        elif self.idusuario:
            self.organizador=self.idusuario

        #filtraReuniao(self,pubpriva,concfut,orgpart,idorganizador):
        listreun=Reuniao()

        self.barraRolagem()
        text = Text(self.frame6,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        text.insert(INSERT, listreun.filtraReuniao(self.pubpriv,self.encfut,self.orgpart,self.aguardaprov,self.organizador)) #
        text.pack(side=LEFT,padx=20,pady=20)
        self.barraRolagemPack(text)

        self.label_1["text"]="Lista de Reuniões"

    def listaReuniaoAprovar(self):
        self.limparTela()
        listreun=Reuniao()

        self.label=Label(self.frame1,text="Lista de Reuniões para aprovar",font=self.fonteGrande)
        self.label.pack()
        self.labe2=Label(self.frame2,text="Atenção! Ao aprovar uma Reunião, as outras do mesmo periodo serão descartadas",font=self.fonteBold,fg="#e60000")
        self.labe2.pack(side=LEFT)

        listreun.reunioesParaAprovar()
        self.selectReunioes=StringVar()
        self.listareuniao=ttk.Combobox(self.frame3,width=15,textvariable=self.selectReunioes,values=listreun.printSelectReunioes(),height=2)
        self.listareuniao["width"]=40
        self.listareuniao.pack(side=LEFT)

        self.finaliza=Button(self.frame4)
        self.finaliza["text"]="Aprovar Reunião"
        self.finaliza["font"]=("Calibri","8")
        self.finaliza["width"]=30
        self.finaliza["command"]=self.aprovarReuniao
        self.finaliza.pack()

        self.barraRolagem()
        self.text = Text(self.frame5,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        self.text.insert(INSERT, listreun.reunioesParaAprovar()) #
        self.text.pack(side=LEFT,padx=20,pady=20)
        self.barraRolagemPack(self.text)

        self.label=Label(self.frame6,text="",font=self.fonteBold,fg="#006600")
        self.label.pack()

    def aprovarReuniao(self):
        reuniao=self.listareuniao.get().split('-')
        listreun=Reuniao()
        listreun.alterarStatusReuniao(reuniao[0],"1")
        self.label["text"]=listreun.printMensagem()
        self.frame4.destroy()
        self.frame5.destroy()

    def selectSelect(self):
        reslist = list()
        seleccion = self.lstbox.curselection()
        for i in seleccion:
            entrada = self.lstbox.get(i)
            reslist.append(entrada)
        for val in reslist:
            val=val.split('-',2)
            if part.Participantes(val[0],self.idultimareuniao,"0").insereParticipante()==True:
                self.frame3.destroy()
                self.label["text"]="Participante cadastrado com sucesso!"
            else:
                self.label["text"]="Erro ao cadastrar participante!"

    def listagemSalas(self):
        self.limparTela()

        salalista=Salas()
        self.lista=Label(self.frame1,text="Salas",font=self.fonteVermelho)
        self.barraRolagem()
        text = Text(self.frame2,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        text.insert(INSERT, salalista.listaSalasTodas())
        text.pack(side=LEFT,padx=20,pady=20)
        self.barraRolagemPack(text)
        self.lista.pack()

    def formConfirmaPresenca(self):
        self.limparTela()
        listreun=Reuniao()
        self.lista=Label(self.frame1,text="Salas",font=self.fonteVermelho)


        self.selectReunioes=StringVar()
        listreun.reunioesAprovadaPendente(self.idusuario)
        if listreun.printQtdReuniao()>0:
            self.listareuniao=ttk.Combobox(self.frame1,width=15,textvariable=self.selectReunioes,values=listreun.printSelectReunioes(),height=2)
            self.listareuniao["width"]=40
            self.listareuniao.pack(side=LEFT)

            self.finaliza=Button(self.frame2)
            self.finaliza["text"]="Confirmar presença"
            self.finaliza["font"]=("Calibri","8")
            self.finaliza["width"]=30
            self.finaliza["command"]=self.confirmarPresenca
            self.finaliza.pack()

            self.barraRolagem()
            text = Text(self.frame3,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
            text.insert(INSERT, listreun.reunioesAprovadaPendente(self.idusuario)) #
            text.pack(side=LEFT,padx=20,pady=20)
            self.barraRolagemPack(text)

            self.label=Label(self.frame4,text="",font=self.fonteBold,fg="#006600")
            self.label.pack()
        else:
            self.label=Label(self.frame4,text="\n\n Nenhuma reunião pendente de aprovação para o seu perfil",font=self.fonteBold,fg="#e60000")
            self.label.pack()

    def confirmarPresenca(self):
        reuniao=self.listareuniao.get().split('-')
        part.Participantes().updateParticipante(reuniao[0],"1")
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.label["text"]="Presença confirmada com sucesso!"

    def selecionaAtaReuniao(self):
        self.limparTela()
        listreun=Reuniao()
        #verifica se é coordenador ou usuário
        if self.idcoordenador:
            self.organizador=self.idcoordenador
        elif self.idusuario:
            self.organizador=self.idusuario

        self.selectReunioes=StringVar()
        listreun.reunioesOrganizadorFinalizada(self.organizador)
        if listreun.printQtdReuniao()>0:
            self.listareuniao=ttk.Combobox(self.frame1,width=15,textvariable=self.selectReunioes,values=listreun.printSelectReunioes(),height=2)
            self.listareuniao["width"]=40
            self.listareuniao.pack(side=LEFT)

            self.finaliza=Button(self.frame2)
            self.finaliza["text"]="Abrir Ata"
            self.finaliza["font"]=("Calibri","8")
            self.finaliza["width"]=30
            self.finaliza["command"]=self.cadastraAtaReuniao
            self.finaliza.pack()
        else:
            self.label=Label(self.frame4,text="\n\n Nenhuma ata disponivel para gerar",font=self.fonteBold,fg="#e60000")
            self.label.pack()

    def cadastraAtaReuniao(self):
        self.idreuniao=self.listareuniao.get().split('-')
        listreun=Reuniao()

        self.barraRolagem()
        self.text = Text(self.frame3,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        self.text.insert(INSERT, listreun.gerarAtaReuniao(self.idreuniao[0]))
        self.text.pack(side=LEFT,padx=30,pady=20)
        self.barraRolagemPack(self.text)

        self.autenticar=Button(self.frame4)
        self.autenticar["text"]="Gerar Arquivo"
        self.autenticar["font"]=("Calibri","8")
        self.autenticar["width"]=12
        self.autenticar["command"]=self.imprimeAta
        self.autenticar.pack()

    def selecionaAtaAlterar(self):
        self.limparTela()
        listreun=Reuniao()
        #verifica se é coordenador ou usuário
        if self.idcoordenador:
            self.organizador=self.idcoordenador
        elif self.idusuario:
            self.organizador=self.idusuario

        self.selectReunioes=StringVar()
        listreun.reunioesOrganizadorFinalizada(self.organizador,"1")
        if listreun.printQtdReuniao()>0:
            self.listareuniao=ttk.Combobox(self.frame1,width=15,textvariable=self.selectReunioes,values=listreun.printSelectReunioes(),height=2)
            self.listareuniao["width"]=40
            self.listareuniao.pack(side=LEFT)

            self.finaliza=Button(self.frame2)
            self.finaliza["text"]="Abrir Ata"
            self.finaliza["font"]=("Calibri","8")
            self.finaliza["width"]=30
            self.finaliza["command"]=self.alteraAtaReuniao
            self.finaliza.pack()
        else:
            self.label=Label(self.frame4,text="\n\n Nenhuma ata disponivel para gerar",font=self.fonteBold,fg="#e60000")
            self.label.pack()

    def alteraAtaReuniao(self):
        self.idreuniao=self.listareuniao.get().split('-')
        listreun=Reuniao()

        idreuniao=str(self.idreuniao[0])
        nomearquivo=idreuniao+"-arquivo-reuniao.txt"
        nomepasta=idreuniao+"-arquivo-reuniao"

        caminho = 'arquivo/'+nomepasta
        if not os.path.exists(caminho):
            self.label=Label(self.frame4,text="\n\n ERRO! Ata não encontrada",font=self.fonteBold,fg="#e60000")
            self.label.pack()

        arquivo = open(caminho+"/"+nomearquivo, 'r', encoding="utf8")

        self.barraRolagem()
        self.text = Text(self.frame3,wrap="word",xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        self.text.insert(INSERT, arquivo.read())
        self.text.pack(side=LEFT,padx=30,pady=20)
        self.barraRolagemPack(self.text)

        self.autenticar=Button(self.frame4)
        self.autenticar["text"]="Atualizar Ata"
        self.autenticar["font"]=("Calibri","8")
        self.autenticar["width"]=12
        self.autenticar["command"]=self.imprimeAta
        self.autenticar.pack()

    def imprimeAta(self):
        listreun=Reuniao()
        textoimprime=self.text.get(1.0, END)
        idreuniao=str(self.idreuniao[0])
        nomearquivo=idreuniao+"-arquivo-reuniao.txt"
        nomepasta=idreuniao+"-arquivo-reuniao"

        caminho = 'arquivo/'+nomepasta
        if not os.path.exists(caminho):
            os.makedirs(caminho)
            listreun.atualizaAtaGerada(idreuniao)

        arquivo = open(caminho+"/"+nomearquivo, 'w', encoding="utf8")
        arquivo.write(textoimprime)
        arquivo.close()

        self.label=Label(self.frame5,text="Ata de Reunião gerada com sucesso!",font=self.fonteGrande,fg="#006600", height="4")
        self.label.pack()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.yscrollbar.destroy()
        self.xscrollbar.destroy()

    def selecionaAtaEnvioArquivo(self):
        self.limparTela()
        listreun=Reuniao()
        #verifica se é coordenador ou usuário
        if self.idcoordenador:
            self.organizador=self.idcoordenador
        elif self.idusuario:
            self.organizador=self.idusuario

        self.selectReunioes=StringVar()
        listreun.reunioesOrganizadorFinalizada(self.organizador,"1")
        if listreun.printQtdReuniao()>0:
            self.listareuniao=ttk.Combobox(self.frame1,width=15,textvariable=self.selectReunioes,values=listreun.printSelectReunioes(),height=2)
            self.listareuniao["width"]=40
            self.listareuniao.pack(side=LEFT)

            self.finaliza = Button(self.frame2)
            self.finaliza["text"]="Abrir Arquivo"
            self.finaliza["font"]=("Calibri","8")
            self.finaliza["width"]=30
            self.finaliza["command"]=self.envioArquivoReuniao
            self.finaliza.pack()
        else:
            self.label=Label(self.frame3,text="\n\n Nenhuma ata disponivel para gerar",font=self.fonteBold,fg="#e60000")
            self.label.pack()

    def envioArquivoReuniao(self):
        self.idreuniao=self.listareuniao.get().split('-')
        idreuniao=str(self.idreuniao[0])
        nomepasta=idreuniao+"-arquivo-reuniao"

        caminho = 'arquivo/'+nomepasta

        filename = filedialog.askopenfilename()
        nomearquivo=filename.split('/')
        tamanho=len(nomearquivo)
        #caminho = 'arquivo'
        if not os.path.exists(caminho):
            os.makedirs(caminho)

        if shutil.copyfile(filename, os.path.join(caminho+"/"+nomearquivo[tamanho-1])):
            self.label=Label(self.frame3,text="Arquivo enviado com sucesso!",font=self.fonteGrande,fg="#006600", height="4")
            self.label.pack()
        else:
            self.label=Label(self.frame3,text="Erro! Arquivo não enviado",font=self.fonteGrande,fg="#006600", height="4")
            self.label.pack()

        self.frame1.destroy()
        self.frame2.destroy()

    def selectSalaRelocar(self):
        self.limparTela()
        if self.idcoordenador:
            self.organizador=self.idcoordenador
        elif self.idusuario:
            self.organizador=self.idusuario

        listreun=Reuniao()
        listreun.reunioesOrganizadorAtiva(self.organizador)
        if listreun.printQtdReuniao()>0:
            self.label_1=Label(self.frame1,text="Lista de Reuniões para relocar sala",font=self.fonteGrande)
            self.label_1.pack()

            self.selectReunioes=StringVar()
            self.listareuniao=ttk.Combobox(self.frame2,width=15,textvariable=self.selectReunioes,values=listreun.printSelectReunioes(),height=2)
            self.listareuniao["width"]=40
            self.listareuniao.pack(side=LEFT)

            self.btn = Button(self.frame3, text="Inserir")
            self.btn["command"]=self.formRelocarSala
            self.btn.grid(column=1, row=1)
        else:
            self.label_1=Label(self.frame3,text="Não foi(ram) encontrada(s) \n Reunião(ões) Organizada por você",font=self.fonteGrande)
            self.label_1.pack()

    def formRelocarSala(self):
        listreun=Reuniao()
        if self.idcoordenador:
            self.menuCoordenador()
        elif self.idusuario:
            self.menuUsuario()

        self.idreuniao=self.listareuniao.get().split('-')
        self.idreuniao=str(self.idreuniao[0])
        #print(idreuniao)

        self.titulo=Label(self.frame4,text="Defina o periodo ou mantenha",height=2)
        self.titulo["font"]=("Arial","14","bold")
        self.titulo.pack()

        listreun.pegaDetalhesReuniao(self.idreuniao,self.organizador)
        dataini=listreun.getDataIni().split('-')
        #print(dataini[0])
        datafim=listreun.getDataFim().split('-')
        listreun.getIdSala()

        self.datainiLabel=Label(self.frame5,text="Data de Inicio (dd/mm/aaaa): ",font=self.fontePadrao,height=3)
        self.datainiLabel.pack(side=LEFT)

        listagem.inputDia()
        self.selectDia=StringVar()
        dia=listagem.printDia()
        self.dia=ttk.Combobox(self.frame5,width=15,textvariable=self.selectDia,values=dia,height=1)
        self.dia.set(dataini[2])
        self.dia["width"]=2
        #self.dia.grid(column=1,row=0)
        self.dia.pack(side=LEFT)

        self.barra=Label(self.frame5,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectMes=StringVar()
        mes=listagem.inputMes()
        self.mes=ttk.Combobox(self.frame5,width=15,textvariable=self.selectMes,values=mes,height=1)
        self.mes.set(dataini[1])
        self.mes["width"]=2
        self.mes.pack(side=LEFT)

        self.barra=Label(self.frame5,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectAno=StringVar()
        ano=listagem.inputAno()
        self.ano=ttk.Combobox(self.frame5,width=15,textvariable=self.selectAno,values=ano,height=1)
        self.ano.set(dataini[0])
        self.ano["width"]=4
        self.ano.pack(side=LEFT)


        self.datafimLabel=Label(self.frame6,text="Data Fim (dd/mm/aaaa): ",font=self.fontePadrao,height=3)
        self.datafimLabel.pack(side=LEFT)

        self.selectDiaFim=StringVar()
        dia=listagem.printDia()
        self.diafim=ttk.Combobox(self.frame6,width=15,textvariable=self.selectDiaFim,values=dia,height=1)
        self.diafim.set(datafim[2])
        self.diafim["width"]=2
        self.diafim.pack(side=LEFT)

        self.barra=Label(self.frame6,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectMesFim=StringVar()
        mes=listagem.inputMes()
        self.mesfim=ttk.Combobox(self.frame6,width=15,textvariable=self.selectMesFim,values=mes,height=1)
        self.mesfim.set(datafim[1])
        self.mesfim["width"]=2
        self.mesfim.pack(side=LEFT)

        self.barra=Label(self.frame6,text="/",font=self.fontePadrao,height=1)
        self.barra.pack(side=LEFT)

        self.selectAnoFim=StringVar()
        ano=listagem.inputAno()
        self.anofim=ttk.Combobox(self.frame6,width=15,textvariable=self.selectAnoFim,values=ano,height=1)
        self.anofim.set(datafim[0])
        self.anofim["width"]=4
        self.anofim.pack(side=LEFT)

        self.periodo=Button(self.frame7)
        self.periodo["text"]="Buscar Salas"
        self.periodo["font"]=("Calibri","8")
        self.periodo["width"]=30
        self.periodo["command"]=self.listaSalasRelocar
        self.periodo.pack()

        self.mensagem=Label(self.frame8,text="",font=self.fontePadrao,height=1)
        self.mensagem.pack()

    def listaSalasRelocar(self):
        self.dataini=self.ano.get()+"-"+self.mes.get()+"-"+self.dia.get()
        self.datafim=self.anofim.get()+"-"+self.mesfim.get()+"-"+self.diafim.get()

        if Datas.Datas().validaDatas(self.dataini,self.datafim)==True:
            self.selectSalas=StringVar()
            self.arraylista=Reuniao().buscarReuniaoDatas(self.dataini,self.datafim)
            self.listas1=Label(self.frame9,text=self.arraylista[0],font=self.fontePadrao)
            self.listas1.pack(side=LEFT)

            self.salas=ttk.Combobox(self.frame9,textvariable=self.selectSalas,values=self.arraylista)
            self.salas["width"]=22
            self.salas.pack(side=LEFT)

            self.finaliza=Button(self.frame10)
            self.finaliza["text"]="Relocar"
            self.finaliza["font"]=("Calibri","8")
            self.finaliza["width"]=30
            self.finaliza["command"]=self.relocaSala
            self.finaliza.pack()

            self.mensagemFim=Label(self.frame11,text="",font=self.fonteVermelho, height=5)
            self.mensagemFim.pack()
        else:
            self.mensagemFim=Label(self.frame11,text="Erro! Tente novamente com o periodo correto",font=self.fonteVermelho, height=5)
            self.mensagemFim.pack()

    def relocaSala(self):
        self.mensagemFim["text"]=Reuniao().atualizaReuniao(self.idreuniao,self.salas.get(),self.dataini,self.datafim)

    def sobre(self):
        self.limparTela()

        self.photo=PhotoImage(file="img\MoraesCorporation.png")
        self.label=Label(self.frame1, image=self.photo)
        self.label.pack()

        self.label_1=Label(self.frame2,text="Disciplina: Estrutura de dados \n\n Projeto 2019.2 \n\n Alunos:\n Diomar Victor \n Edson Ferreira \n Italo Matheus \n Leonardo Hiago",font=self.fonteGrande)
        self.label_1.pack()

        self.label_2=Label(self.frame3,text="\n\n 2019 - Desenvolvido em Python 3.7 - Interface nativa Tkinter - Sqlite3 nativo",font=self.fontePadrao)
        self.label_2.pack()

    def limitarTamanhoDia(self,tam):
        if len(tam) > 2:
            return False
        return True

    def limitarTamanhoAno(self,tam):
        if len(tam) > 4:
            return False
        return True

    def limparTela(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame5.destroy()
        self.frame6.destroy()
        self.frame7.destroy()
        self.frame8.destroy()
        self.frame9.destroy()
        self.frame10.destroy()
        self.frame11.destroy()
        if self.yscrollbar and self.xscrollbar:
            self.yscrollbar.destroy()
            self.xscrollbar.destroy()

        self.frame1=Frame()
        self.frame2=Frame()
        self.frame3=Frame()
        self.frame4=Frame()
        self.frame5=Frame()
        self.frame6=Frame()
        self.frame7=Frame()
        self.frame8=Frame()
        self.frame9=Frame()
        self.frame10=Frame()
        self.frame11=Frame()

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.frame9.pack()
        self.frame10.pack()
        self.frame11.pack()

    def barraRolagem(self):
        self.yscrollbar = Scrollbar(self.frame6,orient=VERTICAL)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.xscrollbar = Scrollbar(self.frame6,orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)

    def barraRolagemPack(self,text):
        self.xscrollbar.config(command=text.xview)
        self.yscrollbar.config(command=text.yview)

    def segundoMenu(self,menu):
        segundomenu=Menu(menu)
        segundomenu.add_command(label="Sobre", command=self.sobre)
        segundomenu.add_command(label="Sair", command=self.Sair)
        menu.add_cascade(label="Opções",menu=segundomenu)

    def Sair(self):
        root.destroy()

def main():
    root.geometry("600x550+500+150")

    App()
    root.title("Sistema e-meeting")

    root.mainloop()
if __name__ == '__main__':
    main()