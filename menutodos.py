import limpeza,crudusuarios,crudsalas,crudreuniao,verificaarquivo

class menu(object):
    def __init__(self, login=''):
        self.login = login
    # ------------------------------------------------------------
    #                     Menu Coordenador
    # ------------------------------------------------------------
    def menuCoord(self,returnopcao=False):
        print("  =====================================================")
        print("   Coordenador {} , bem vindo(a) ao E - M E E T I N G  ".format(self.login))
        print("  1 - Visualizar minhas reunioes")
        print("  2 - Confirmar/Negar presenca em reuniao")
        print("  3 - Criar reuniao")
        print("  4 - Editar atas")
        print("  5 - Realocar reunioes de sala")
        print("  6 - Adicionar participantes em lista de reuniao")
        print("  x - Sair")
        print("  =====================================================")
        if (returnopcao==False):
            self.inputcoord=''
            self.inputcoord=str(input("  Escolha a opcao 1-6 ou 'x' para sair: "))
            whileCoord(self.inputcoord,self.login)

    # ------------------------------------------------------------
    #                     Menu Usuario Comum
    # ------------------------------------------------------------
    def menuUsu(self,returnopcao=False):
        print("  =====================================================")
        print("   Usuario {} , bem vindo(a) ao E - M E E T I N G  ".format(self.login))
        print("  1 - Visualizar minhas reunioes")
        print("  2 - Confirmar/Negar presenca em reuniao")
        print("  3 - Visualizar atas")
        print("  4 -  Reuniao - criar")
        print("  5 -  Reuniao - adicionar participantes")
        print("  6 -  Reuniao - redigir atas")
        print("  6 -  Reuniao - editar atas")
        print("  7 -  Reuniao - sugerir local")
        print("  8 -  Reuniao - baixar atas")
        print("  x - Sair")
        print("  =====================================================")
        if (returnopcao==False):
            self.inputcoord=''
            self.inputcoord=str(input("  Escolha a opcao 1-6 ou 'x' para sair: "))
            whileCoord(self.inputcoord,self.login)

    # ------------------------------------------------------------
    #                      Menu Principal
    # ------------------------------------------------------------
    def menuLogin(self,returnopcao=False):
        print("=======================================")
        print("  Bem vindo ao E - M E E T I N G")
        print("  1 - Visualizar Reunioes Publicas")
        print("  2 - Login Usuario")
        print("  3 - Login Coordenador")
        print("  4 - Login Gestor de Recursos")
        print("  5 - Cadastro Usuario")
        print("  x - Sair")
        print("=======================================")
        if (returnopcao==False):
            self.inputopcao = input("  Escolha a opcao 1-5 ou 'x' para sair: ")
            whilePrincipal(self.inputopcao,self.login)

    # ------------------------------------------------------------
    #                      Menu Gestor
    # ------------------------------------------------------------
    def menuGestor(self,returnopcao=False):
        print("======================================================")
        print("  Gestor de Recursos - Bem vindo ao E - M E E T I N G")
        print("  1 - Confirmar sala de reunioes")
        print("  2 - Cadastrar salas")
        print("  x - Sair")
        print("======================================================")
        if (returnopcao==False):
            self.inputopcao = input("  Escolha a opcao 1-2 ou 'x' para sair: ")
            whileGestor(self.inputopcao,self.login)

# ------------------------------------------------------------
#           Função para varrer o menu Coordenador
# ------------------------------------------------------------
def whileCoord(inputcoord='',login=''):
    login=login
    if inputcoord == "1":
        limpeza.LimpaTela()
        print("======================================================")
        print("      Listagem de reunioes - E - M E E T I N G")
        print("======================================================")
        crudreuniao.reuniaoLista().listaReuniaoUsuario(login)
        print("======================================================")
        limpeza.voltar()
        menu(login).menuCoord()
    if inputcoord == "3":
        limpeza.LimpaTela()
        valida=False
        print("======================================================")
        print("  Cadastro de Reuniao - E - M E E T I N G")
        while valida==False:
            dataini=input('  Informe a data de inicio (dd/mm/aaa): ')
            valida=verificaarquivo.manipulaData().validaInputData(dataini)
            if valida==False:
                print('   Erro! Favor inserir a data no formato correto')
        valida=False
        while valida==False:
            datafim=input('  Informe a data do encerramento (dd/mm/aaa): ')
            valida=verificaarquivo.manipulaData().validaInputData(datafim)
            if valida==False:
                print('   Erro! Favor inserir a data no formato correto')
        if crudreuniao.reuniaoLista().salaDisponivel(dataini,datafim):
            print('------------ Sala(s) disponivel(is) ------------')
            print('  {}'.format(crudreuniao.reuniaoLista().salaDisponivel(dataini,datafim)))
            sala=input('  Informe a sala: ')
            assunto=input('  Informe o assunto: ')
            status='0'
            visibilidade=input('Informe a visibilidade (0=Publico,1=Privado): ')
            print("======================================================")
            crudreuniao.reuniaoClass(login,dataini,datafim,sala,assunto,status,visibilidade)
            print('  Reuniao cadastrada com sucesso!')
        else:
            print('  Nenhuma sala disponivel')
            limpeza.voltar()
            menu(login).menuCoord()
        limpeza.voltar()
        menu(login).menuCoord()

    if inputcoord == "x":
        limpeza.LimpaTela()
        menu(login).menuLogin()

# ------------------------------------------------------------
#           Função para varrer o menu Principal
# ------------------------------------------------------------
def whilePrincipal(inputopcao='',inputlogin=''):
    if inputopcao!='x':
        if inputopcao == "1":
            limpeza.LimpaTela()
            print("======================================================")
            print("  Listagem de Reunioes Publicas - E - M E E T I N G")
            print("======================================================\n")
            crudreuniao.reuniaoLista().listaReuniaoPublica()
            print("\n======================================================")
            limpeza.voltar()
            menu(inputlogin).menuLogin()
        if inputopcao == "2":
            limpeza.LimpaTela()
            print("======================================================")
            print("  Login Usuario - E - M E E T I N G")
            print("======================================================")
            login=input(' Login: ')
            senha=input(' Senha: ') #getpass.getpass(prompt="Senha: ")
            nivel=str('3')
            if crudusuarios.usuarioLista().buscarUsuario(login, senha, nivel):
                print(' Usuario Logado com sucesso!')
            else:
                print(' Erro! Usuario nao localizado')
            print("======================================================")
            limpeza.voltar()
            menu(inputlogin).menuLogin()
        if inputopcao == "3":
            limpeza.LimpaTela()
            print("======================================================")
            print("  Login Coordenador - E - M E E T I N G")
            print("======================================================")
            login=input(' Login: ')
            senha=input(' Senha: ') #getpass.getpass(prompt="Senha: ")
            nivel=str('1')
            print("======================================================")
            if crudusuarios.usuarioLista().buscarUsuario(login, senha, nivel):
                limpeza.LimpaTela()
                menu(login).menuCoord()
                limpeza.LimpaTela()
                whileCoord(menu(inputlogin).menuCoord())
            else:
                print('  Erro! Usuario nao localizado')
            limpeza.voltar()
            menu(inputlogin).menuLogin()
        if inputopcao == "4":
            limpeza.LimpaTela()
            print("======================================================")
            print("  Login Gestor de Recursos - E - M E E T I N G")
            print("======================================================")
            login=input(' Login: ')
            senha=input(' Senha: ') #getpass.getpass(prompt="Senha: ")
            nivel=str('2')
            print("======================================================")
            if crudusuarios.usuarioLista().buscarUsuario(login, senha, nivel):
                limpeza.LimpaTela()
                menu(login).menuGestor()
                limpeza.LimpaTela()
                whileGestor(menu(inputlogin).menuGestor())
            else:
                print('  Erro! Usuario nao localizado')
            limpeza.voltar()
            menu(inputlogin).menuLogin()
        if inputopcao == "5":
            limpeza.LimpaTela()
            print("======================================================")
            print("  Cadastro de Usuarios - E - M E E T I N G")
            print("======================================================")
            nome=input(' Nome: ')
            login=input(' Login: ')
            senha=input(' Senha: ')

            if (nome and login and senha):
                if (crudusuarios.Comandos().validaLogin(login,'3')==False):
                    print(' Login ja cadastrado anteriormente, tente outro')
                else:
                    if (crudusuarios.Comandos(login,senha,nome,'3').cadastraUsuario()==True):
                        print('  Cadastro efetuado com sucesso!')
                    else:
                        print('  Erro no cadastro!')
            else:
                print('  Erro ao inserir os dados, tente novamente!')
            print("======================================================")
            limpeza.voltar()
            menu(inputlogin).menuLogin()
        if inputopcao == "x":
            limpeza.LimpaTela()
    else:
        limpeza.LimpaTela()

# ------------------------------------------------------------
#           Função para varrer o menu Gestor
# ------------------------------------------------------------
def whileGestor(inputopcao='',login=''):
    login=login
    if inputopcao == "1":
        limpeza.LimpaTela()
        print('confirma sala de reunioes')
        limpeza.voltar()
        menu(login).menuGestor()
    if inputopcao == "2":
        limpeza.LimpaTela()
        print("======================================================")
        print("      Cadastro de Salas - E - M E E T I N G")
        print("======================================================")
        if (crudsalas.Comandos().listarSalas()==None):
            print(' Ainda nao existem salas cadastradas, cadastre uma nova agora!')
        else:
            print("  ======== Sala(s) cadastrada(s) ========")
            print(crudsalas.Comandos().listarSalas())
            print("  =======================================")

        parar=False
        while (parar==False):
            numsala=input(' Entre com o numero da sala: ')
            if crudsalas.Comandos().salaExiste(numsala)==True:
                print('  Sala ja cadastrada, tente outra!')
            else:
                crudsalas.Comandos().cadastraSala(numsala)
                continua=input(' \n Cadastrar outra sala (s/n)?')
                if (continua!="s"):
                    parar=True
        print("======================================================")
        limpeza.voltar()
        menu(login).menuGestor()
    if inputopcao == "x":
        limpeza.LimpaTela()
        menu(login).menuLogin()
