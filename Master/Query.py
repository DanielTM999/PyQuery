import mysql.connector
from time import sleep
import os
import dotenv

class Masterclass:
    def __init__(self, host, user, password, showemsg=True):
        self.host = host
        self.user = user
        self.password = password
        self.database = ""
        self.showemsg = showemsg

    def createDB(self, database):
        if(self.showemsg):
            print("*"*10+"CRINDO DB"+"*"*10)
            print('procurando por erros...')
            sleep(2)
        if(len(database.strip()) == 0):
            print("\033[31merro: ->nome do banco em branco\033[0m")
            database = str(input('informe o nome do banco para continuar(-1 p/ cancelar):'))
            if(database == "-1"):
                exit()
        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
            if(self.showemsg):
                print("\033[32mPreparando query...\033[0;0m")
                sleep(1)
            sql = f"CREATE DATABASE IF NOT EXISTS {database}"
            if(self.showemsg):
                print("\033[32mcriando conexão com o banco...\033[0;0m")
                sleep(1)
            act = self.connexao()
            if(self.showemsg):
                print("\033[32mexecutando query...\033[0;0m")
                sleep(1)
            act[1].execute(sql)
            if(self.showemsg):
                print("\033[32mvalidando...\033[0;0m")
                sleep(1)
            act[0].commit()
            self.useDB(database)
            if(self.showemsg):
                print(f"\033[32mdatabase '{database.upper()}' criada com secesso\033[0;0m")
            return True
        except:
            return False
        finally:
            act[0].close()
            act[1].close()

    def dropDB(self, database):
        if(self.showemsg):
            print("*"*10+"EXCLUINDO DB"+"*"*10)
            print('procurando por erros...')
            sleep(2)
        if(len(database.strip()) == 0):
            print("\033[31merro: ->nome do banco em branco\033[0m")
            database = str(input('informe o nome do banco para continuar(-1 p/ cancelar):'))
            if(database == "-1"):
                exit()
        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
                sleep(1)
            sql = f"DROP DATABASE {database}"
            if(self.showemsg):
                print("\033[32mcriando conexão com o banco...\033[0;0m")
                sleep(1)
            act = self.connexao()
            if(self.showemsg):
                print("\033[32mexecutando query...\033[0;0m")
                sleep(1)
            act[1].execute(sql)
            if(self.showemsg):
                print("\033[32mvalidando...\033[0;0m")
                sleep(1)
            act[0].commit()
            if(self.showemsg):
                print(f"\033[32mdatabase '{database.upper()}' deletada com secesso\033[0;0m")
            return True
        except:
            return False
        finally:
            act[0].close()
            act[1].close()

    def dropTable(self, NameTable):
        if(self.showemsg):
            print("*"*10+"EXCLUINDO TABELA"+"*"*10)
            print('procurando por erros...')
            sleep(2)
        if(len(NameTable.strip()) == 0):
            print("\033[31merro: ->nome do banco em branco\033[0m")
            NameTable = str(input('informe o nome do banco para continuar(-1 p/ cancelar):'))
            if(NameTable == "-1"):
                exit()
        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
                sleep(1)
            sql = f"DROP TABLE {NameTable}"
            if(self.showemsg):
                print("\033[32mcriando conexão com o banco...\033[0;0m")
                sleep(1)
            act = self.connexao()
            if(self.showemsg):
                print("\033[32mexecutando query...\033[0;0m")
                sleep(1)
            act[1].execute(sql)
            if(self.showemsg):
                print("\033[32mvalidando...\033[0;0m")
                sleep(1)
            act[0].commit()
            if(self.showemsg):
                print(f"\033[32mTabela '{NameTable.upper()}' deletada com secesso\033[0;0m")
            return True
        except:
            return False
        finally:
            act[0].close()
            act[1].close()

    def connexao(self):
        try:
            conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
            )
            cursor = conexao.cursor()
            return conexao, cursor
        except:
            print("Erro de coneção com o banco de dados")

    def useDB(self, database):
        self.database = database

    def createTable(self, tableName, colluns = list, type= list, tamanho = list):
        if(self.showemsg):
            print("*"*10+"CRINDO TABELA"+"*"*10)
            print('procurando por erros...')
            sleep(2)
        pste = ""

        if(len(colluns) != len(type) or (len(colluns) + len(type) == 0) or len(tamanho) != len(colluns)):
            err = abs(len(type) - len(colluns))
            if(len(colluns) < len(type)):
                for i in range(0, err):
                    colluns += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}\033[0;0m"\033[0m')
            elif(len(colluns) + len(type) == 0):
                colluns += ["args, ..."]
                type += ['args, ...']
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}/{type}\033[0;0m"\033[0m')
            else:
                for i in range(0, err):
                    type += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{type}\033[0;0m"\033[0m')
            exit()

        for i in range(0, len(colluns)):
            if(len(colluns[i].strip()) == 0):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
                colluns[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(colluns[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
            if(len(type[i].strip()) == 0):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{type}Type\033[0;0m"\033[0m')
                type[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(type[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{type}Type\033[0;0m"\033[0m')


        for i in type:
            i = str(i).lower()
            if((i != "varchar") and (i != "int")):
                print('\033[31m->Erro: tipos de colunas \033[0;0m'+ f'\033[1m"\033[32m{i}\033[0;0m"\033[0m')
                exit()

        for i in range(0, len(colluns)):
            tamanho[i] = str(tamanho[i])
            type[i] = str(type[i]).lower()
            if(type[i] == "varchar"):
                pste+= f"{colluns[i]} {type[i]}({tamanho[i]}) NOT NULL,"
            elif(type[i] == "int"):
                pste+= f"{colluns[i]} {type[i]} NOT NULL,"

        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
                sleep(1)
            sql = f"CREATE TABLE IF NOT EXISTS {tableName}(id{tableName} INT NOT NULL AUTO_INCREMENT,{pste} PRIMARY KEY (`id{tableName}`))"
            if(self.showemsg):
                print("\033[32mcriando conexão com o banco...\033[0;0m")
                sleep(1)
            act = self.connexao()
            if(self.showemsg):
                print("\033[32mexecutando query...\033[0;0m")
                sleep(1)
            act[1].execute(sql)
            if(self.showemsg):
                print("\033[32mvalidando...\033[0;0m")
                sleep(1)
            act[0].commit()
            if(self.showemsg):
                print(f"\033[32mtabela '{tableName.upper()}' criada com secesso\033[0;0m")
            return True
        except:
            print('erro')
            return False
        finally:
            act[0].close()
            act[1].close()

    def insertDB(self, tableName, colluns = list, values = list):
        if(self.showemsg):
            print("*"*10+"INSERINDO VALORES"+"*"*10)
            print('procurando por erros...')
            sleep(2)
        banco = self.database
        pste_itens = ""
        pste_values = ""
        mos = ""
        if(len(colluns) != len(values) or (len(colluns) + len(values) == 0)):
            err = abs(len(values) - len(colluns))
            if(len(colluns) < len(values)):
                for i in range(0, err):
                    colluns += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}colluns\033[0;0m"\033[0m')
            elif(len(colluns) + len(values) == 0):
                colluns += ["args, ..."]
                values += ['args, ...']
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}/{values}colluns/values\033[0;0m"\033[0m')
            else:
                for i in range(0, err):
                    values += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{values}values\033[0;0m"\033[0m')
            exit()

        for i in range(0, len(colluns)):
            values[i] = str(values[i])
            if(len(colluns[i].strip()) == 0):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
                colluns[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(colluns[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
            if((len(values[i].strip()) == 0)):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{values}Value\033[0;0m"\033[0m')
                values[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(values[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{values}Value\033[0;0m"\033[0m')

        for i in range(0, len(values)):
            if(values[i].isnumeric()):
                pste_itens += f"{colluns[i]},"
                pste_values += f"{int(values[i])},"
                mos += f"{values[i]},"
            else:
                pste_itens += f"{colluns[i]},"
                pste_values += "'"+values[i]+"',"
                mos += f"{values[i]},"

        pste_itens = pste_itens[0:(len(pste_itens) - 1)]
        pste_values = pste_values[0:(len(pste_values) - 1)]
        mos = mos[0:(len(mos) - 1)]
        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
            sql = f"INSERT INTO {banco}.{tableName}({pste_itens}) VALUES ({pste_values})"
            if(self.showemsg):
                sleep(1)
                print("\033[32mcriando conexão com o banco...\033[0;0m")
            act = self.connexao()
            if(self.showemsg):
                sleep(1)
                print("\033[32mexecutando query...\033[0;0m")
            act[1].execute(sql)
            if(self.showemsg):
                sleep(1)
                print("\033[32mvalidando...\033[0;0m")
            act[0].commit()
            if(self.showemsg):
                sleep(1)
                print(f"\033[32mvalores '{mos.upper()}' inseridos com secesso\033[0;0m")
            return True
        except:
            print('fatal error')
            return False
        finally:
            act[0].close()
            act[1].close()

    def getAllDB(self, TableName):
        banco = self.database
        if(len(TableName.strip()) == 0):
            print("\033[31merro: ->nome do banco em branco\033[0m")
            TableName = str(input('informe o nome do banco para continuar(-1 p/ cancelar):'))
            if(TableName == "-1"):
                exit()
        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
            sql = f"SELECT * FROM {banco}.{TableName}"
            if(self.showemsg):
                sleep(1)
                print("\033[32mcriando conexão com o banco...\033[0;0m")
            act = self.connexao()
            if(self.showemsg):
                sleep(1)
                print("\033[32mvalidando...\033[0;0m")
            act[1].execute(sql)
            if(self.showemsg):
                print(f"\033[32mRetornando valores em array...\033[0;0m")
            linhas  = act[1].fetchall()
            if(self.showemsg):
                sleep(1)
                print(f"\033[32mSucesso\033[0;0m")
            return linhas
        except Exception as e:
            print("fatal error, não foi possivel acessa o mysql")
            print(e)
        finally:
            act[0].close()
            act[1].close()

    def getUniqIdDB(self, TableName, colluns = list, itens = list, elementos = ""):
        pste_elemento = ""
        pste_itens = ""
        banco = self.database
        if(len(elementos) == 0):
            pste_elemento = "*"
        else:
            for i in elementos:
                pste_elemento += f"{i},"
            pste_elemento = pste_elemento[0:(len(pste_elemento)-1)]

        if(len(colluns) != len(itens) or (len(colluns) + len(itens) == 0)):
            err = abs(len(itens) - len(colluns))
            if(len(colluns) < len(itens)):
                for i in range(0, err):
                    colluns += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}\033[0;0m"\033[0m')
            elif(len(colluns) + len(itens) == 0):
                colluns += ["args, ..."]
                itens += ['args, ...']
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}/{itens}\033[0;0m"\033[0m')
            else:
                for i in range(0, err):
                    itens += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{itens}\033[0;0m"\033[0m')
            exit()
        for i in range(0, len(colluns)):
            if(len(colluns[i].strip()) == 0):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
                colluns[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(colluns[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
            if(len(itens[i].strip()) == 0):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{itens}itens\033[0;0m"\033[0m')
                itens[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(itens[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{itens}itens\033[0;0m"\033[0m')
        for i in range(0, len(itens)):
            pste_itens += f"{colluns[i]}='{itens[i]}' AND "
        pste_itens = pste_itens[0:(len(pste_itens)-5)]

        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
            sql = f"SELECT {pste_elemento} FROM {banco}.{TableName} WHERE {pste_itens}"
            if(self.showemsg):
                sleep(1)
                print("\033[32mcriando conexão com o banco...\033[0;0m")
            act = self.connexao()
            if(self.showemsg):
                sleep(1)
                print("\033[32mvalidando...\033[0;0m")
            act[1].execute(sql)
            if(self.showemsg):
                print(f"\033[32mRetornando valores em array...\033[0;0m")
            linhas  = act[1].fetchone()
            if(self.showemsg):
                sleep(1)
                print(f"\033[32mSucesso\033[0;0m")
            return linhas
        except Exception as e:
            print("fatal error, não foi possivel acessa o mysql")
            print(e)
        finally:
            act[0].close()
            act[1].close()

    def AlterElement(self, NameTable, colluns = list, newValue = list, Condition = list):
        banco = self.database

        if((len(colluns) != len(newValue)) or (len(colluns) + len(newValue) == 0)):
            err = abs(len(newValue) - len(colluns))
            if(len(colluns) < len(newValue)):
                for i in range(0, err):
                    colluns += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}\033[0;0m"\033[0m')
            elif(len(colluns) + len(newValue) == 0):
                colluns += ["args, ..."]
                newValue += ['args, ...']
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}/{type}\033[0;0m"\033[0m')
            else:
                for i in range(0, err):
                    newValue += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{newValue}\033[0;0m"\033[0m')
            exit()

        pste = ''
        for i in range(len(colluns)):
            pste += f"{colluns[i]}='{newValue[i]}',"
        pste = pste[0:(len(pste)-1)]

        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
                sleep(1)
            sql = f"UPDATE `{banco}`.`{NameTable}` SET {pste} WHERE {Condition[0]}='{Condition[1]}'"
            if(self.showemsg):
                print("\033[32mcriando conexão com o banco...\033[0;0m")
                sleep(1)
            act = self.connexao()
            if(self.showemsg):
                print("\033[32mexecutando query...\033[0;0m")
                sleep(1)
            act[1].execute(sql)
            if(self.showemsg):
                print("\033[32mvalidando...\033[0;0m")
                sleep(1)
            act[0].commit()
            if(self.showemsg):
                print(f"\033[32mValor da tabela '{NameTable.upper()}' alterada com secesso\033[0;0m")
            return True
        except:
            print('erro')
            return False
        finally:
            act[0].close()
            act[1].close()

        pass

    def AlterElementcollun(self, NameTable, collum = list, notn = bool(True),type = list, value = list, newName = [""]):
        banco = self.database
        pste = ''
        for i in range(len(collum)):
            type[i] = str(type[i]).upper()
            value[i] = str(value[i])
            if(type[i] == "INT"):
                if((newName != None) or (newName[i].strip() != "")):
                    if(notn == True):
                        pste += f"CHANGE COLUMN `{newName[i]}` {type[i]} NOT NULL, "
                    else:
                        pste += f"CHANGE COLUMN `{newName[i]}` {type[i]} NULL, "
                else:
                    if(notn == True):
                        pste += f"CHANGE COLUMN `{collum[i]}` `{collum[i]}` {type[i]} NOT NULL, "
                    else:
                        pste += f"CHANGE COLUMN `{collum[i]}` `{collum[i]}` {type[i]} NULL, "
            else:
                if((newName[0] != "")):
                    if(notn == True):
                        pste += f"CHANGE COLUMN `{collum[i]}` `{newName[i]}` {type[i]}({value[i]}) NOT NULL, "
                    else:
                        pste += f"CHANGE COLUMN `{collum[i]}` `{newName[i]}` {type[i]}({value[i]}) NULL, "
                else:
                    if(notn == True):
                        pste += f"CHANGE COLUMN `{collum[i]}` `{collum[i]}` {type[i]}({value[i]}) NOT NULL, "
                    else:
                        pste += f"CHANGE COLUMN `{collum[i]}` `{collum[i]}` {type[i]}({value[i]}) NULL, "
        pste = pste[0:(len(pste) - 2)]

        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
                sleep(1)
            sql = f"ALTER TABLE `{banco}`.`{NameTable}` {pste}"
            if(self.showemsg):
                print("\033[32mcriando conexão com o banco...\033[0;0m")
                sleep(1)
            act = self.connexao()
            if(self.showemsg):
                print("\033[32mexecutando query...\033[0;0m")
                sleep(1)
            act[1].execute(sql)
            if(self.showemsg):
                print("\033[32mvalidando...\033[0;0m")
                sleep(1)
            act[0].commit()
            if(self.showemsg):
                print(f"\033[32mNOme da coluna da tabela '{NameTable.upper()}'coluna alterada com secesso\033[0;0m")
            return True
        except Exception as e:
            print('erro:', e)
            return False
        finally:
            act[0].close()
            act[1].close()

    def getnumDB(self, TableName, colluns = list, itens = list, elementos = ""):
        pste_elemento = ""
        pste_itens = ""
        banco = self.database
        if(len(elementos) == 0):
            pste_elemento = "*"
        else:
            for i in elementos:
                pste_elemento += f"{i},"
            pste_elemento = pste_elemento[0:(len(pste_elemento)-1)]

        if(len(colluns) != len(itens) or (len(colluns) + len(itens) == 0)):
            err = abs(len(itens) - len(colluns))
            if(len(colluns) < len(itens)):
                for i in range(0, err):
                    colluns += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}\033[0;0m"\033[0m')
            elif(len(colluns) + len(itens) == 0):
                colluns += ["args, ..."]
                itens += ['args, ...']
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{colluns}/{itens}\033[0;0m"\033[0m')
            else:
                for i in range(0, err):
                    itens += ["args"]
                print('\033[31m->Erro: Faltando elemento \033[0;0m'+ f'\033[1m"\033[32m{itens}\033[0;0m"\033[0m')
            exit()
        for i in range(0, len(colluns)):
            if(len(colluns[i].strip()) == 0):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
                colluns[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(colluns[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{colluns}Collun\033[0;0m"\033[0m')
            if(len(itens[i].strip()) == 0):
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{itens}itens\033[0;0m"\033[0m')
                itens[i] = str(input("informe o elemento em branco para continuar[-1 p/ cancelar]:"))
                if(itens[i] == "-1"):
                    exit()
                print('\033[31m->Erro: elemento em branco \033[0;0m'+ f'\033[1m"\033[32m{itens}itens\033[0;0m"\033[0m')
        for i in range(0, len(itens)):
            pste_itens += f"{colluns[i]}='{itens[i]}' AND "
        pste_itens = pste_itens[0:(len(pste_itens)-5)]

        try:
            if(self.showemsg):
                print("\033[32mErros: 0\033[0;0m")
                sleep(1)
                print("\033[32mPreparando query...\033[0;0m")
            sql = f"SELECT {pste_elemento} FROM {banco}.{TableName} WHERE {pste_itens}"
            if(self.showemsg):
                sleep(1)
                print("\033[32mcriando conexão com o banco...\033[0;0m")
            act = self.connexao()
            if(self.showemsg):
                sleep(1)
                print("\033[32mvalidando...\033[0;0m")
            act[1].execute(sql)
            if(self.showemsg):
                print(f"\033[32mRetornando valores em array...\033[0;0m")
            act[1].fetchone()
            linhas  = act[1].rowcount
            if(self.showemsg):
                sleep(1)
                print(f"\033[32mSucesso\033[0;0m")
            return linhas
        except Exception as e:
            print("fatal error, não foi possivel acessa o mysql")
            print(e)
        finally:
            act[0].close()
            act[1].close()

class DotEnv:
    def GetDotenv(env = list):
        dotenv.load_dotenv(dotenv.find_dotenv())
        dic = []
        for i in env:
            dic.append(os.getenv(i))

        return dic

class MasterclassAuth(Masterclass):
    #em desenvolvimento
    pass
