import sqlite3
import os

DB_NAME = "study-dashboard.db"

def get_db():
    try:
        # Conecta ao banco de dados ou cria um novo se não existir
        conn = sqlite3.connect(DB_NAME)
        
        # Cria as tabelas
        create_tables(conn)

        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def create_tables(conn):
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tasks (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       description TEXT,
                       done BOOLEAN NOT NULL CHECK (done IN (0, 1))
                   )
            """)
    
    conn.commit()
    print("Tabelas criadas com sucesso!")

# Testando a função
conn = get_db()
if conn:
    print("Banco de dados está pronto para uso.")
    # Não se esqueça de fechar a conexão quando terminar de usá-la
    conn.close()
