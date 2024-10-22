import sqlite3
class Planta:
    def conexao(self):
        conexao = sqlite3.connect("horta.db")
        consulta = conexao.cursor()
        tabela = """
        CREATE TABLE IF NOT EXISTS planta(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        id VARCHAR(100),
        data_plantio DATE,
        tipo VARCHAR(100),
        quantidade VARCHAR(100)
        );
        """

        consulta.execute(tabela)
        return conexao

    def cadastrarPlanta(self, nome,  id, data_plantio, tipo, quantidade):
        conexao = self.conexao()

        sql = "INSERT INTO planta VALUES (?,?,?,?,?,?)"

        campos = (None, nome , id, data_plantio, tipo, quantidade)

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "Linha(s) inserido(s) com sucesso")

        conexao.close()
    
    def consultarPlantaIndividual(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()

      
        sql = "SELECT * FROM planta WHERE id = ?"

        campos = (id,)
        consulta.execute(sql,campos)

        resultado = consulta.fetchall()

        for itens in resultado:
            print(f"Nome: {itens [1]}")
            print(f"Id: {itens [2]}")
            print(f"Tipo: {itens [3]}")
            print(f"Data Plantio {itens[4]}")
            print(f"Quantidade: {itens [5]}")
            print(f"-"*40) # criando um separador entre cada registro
            
        conexao.close()

    def deletarPlanta(self,id):
        conexao = self.conexao()
        consultar = conexao.cursor()
        

        sql = "DELETE FROM planta WHERE id = ?"


        campos = (id,)
        consultar.execute(sql, campos)

        conexao.commit()

        print(consultar.rowcount, " linha(s) deletada(s) com sucesso")

        conexao.close()

    def atualizarPlanta(self,nome, id):
        conexao = self.conexao()
        consultar = conexao.cursor()

        

        sql = "UPDATE planta SET nome = ? WHERE id = ?"

        campos = (nome,id )

        consultar.execute(sql, campos)

        conexao.commit()

        print(consultar.rowcount, " linha(s) atualizada (s) com sucesso")

        conexao.close()

    def consultarPlanta(self):
        conexao = self.conexao()
        consultar = conexao.cursor()

        sql = "SELECT * FROM planta"
        consultar.execute(sql)

        resultado = consultar.fetchall()#Fetchall() irá trazer todos os registros que existem na tabela do banco de dados
        
        for itens in resultado:
            print(f"Nome: {itens [1]}")
            print(f"id: {itens [2]}")
            print(f"Data de plantio: {itens [3]}")
            print(f"tipo: {itens [4]}")
            print(f"quantidade: {itens [5]}")
            print(f"-"*40) # criando um separador entre cada registro
        
        conexao.close()
        
    