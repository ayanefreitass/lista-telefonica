import mysql.connector
import mysql.connector.errors

class BD:
    _connection = None

    def connect(self):
        try:
            if self._connection is not None:
                return self._connection
            else:
                self._connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password="",
                database="telefone"
                    
                )
                return self._connection
        except mysql.connector.erros.ProgrammingError as error:
            print("Error:", error)
            return{"Error:", error}
        
    def close(self):
        self._connection.close()
        self._connection = None
        
    def buscarContatos(self):
        self.criarConexão()
        cursor = self._connection.cursor
        
        cursor.execute("select * from lista")
        result = cursor.fetchall()
        
        contatos = []
        
        if len(result) > 0:
            for contato in result:
                contatos.append(
                    {
                    "nome": contato[0],
                    "numero":contato[1],
                    "cidade":[2]
                    }
                )

    def adicionarcontato()
bd = BD()

print(bd.buscarContatos())
