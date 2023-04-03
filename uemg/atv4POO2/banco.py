import sqlite3  #import the sqlite3 module to be used.
import traceback

class Banco():
    def __init__(self):
        self.conn = sqlite3.connect("meubanco.db")

    def __del__(self):
        self.conn.close()

    def select(self, sqlstatement):
        """Seleciona registros do banco de dados a partir de um parâmetro"""
        self.__cursor = self.conn.cursor()

        try:
            self.__cursor.execute(sqlstatement)
            
        except sqlite3.OperationalError:
            print ("Erro. Verifique seu SQL")

        self.dados = self.__cursor.fetchall()

    def select_one(self, id):
        self.__cursor = self.conn.cursor()

        sqlstatement = "Select * from produto where id=?"

        try:
            self.__cursor.execute(sqlstatement,id)
        except sqlite3.OperationalError:
            print ("Erro. Verifique seu SQL")

        self.dados = self.__cursor.fetchall()


    def create(self):
        self.__cursor = self.conn.cursor()
        try:
            sqlstatement = "drop table if exists produto"
            self.__cursor.execute(sqlstatement)
            sqlstatement = "CREATE TABLE produto             (id   INTEGER PRIMARY KEY AUTOINCREMENT, Nome_do_Produto TEXT (255),             Quantidade TEXT (10), Valor TEXT (10)            );"
            self.__cursor.execute(sqlstatement)   
            
        except sqlite3.OperationalError:
            #print Exception.
            print ("Erro. Verifique seu SQL")

        self.conn.commit()


    def insert(self,dados):
        self.__cursor = self.conn.cursor()
        sqlstatement = "INSERT INTO produto (Nome_do_Produto, Quantidade, Valor) VALUES (?,?,?)"
        try:
            self.__cursor.execute(sqlstatement, dados)

        except sqlite3.OperationalError:
            print ("Erro. Verifique seu SQL")

        self.conn.commit()

    def update(self,dados):
        self.__cursor = self.conn.cursor()
        sqlstatement = """UPDATE produto 
        SET Nome_do_Produto=?, Quantidade=?, Valor=? 
        WHERE id=?
        """

        try:
            self.__cursor.execute(sqlstatement, dados)

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))

        self.conn.commit()


    def delete(self,id):
        self.__cursor = self.conn.cursor()
        sqlstatement = "DELETE FROM produto where ID=?"
        try:
            self.__cursor.execute(sqlstatement, id)

        except sqlite3.OperationalError:
            print ("Erro. Verifique seu SQL")

        self.conn.commit()