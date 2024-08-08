import sqlite3
import csv

try:
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id_funcionario INTEGER PRIMARY KEY,
            nome TEXT,
            cargo TEXT,
            departamento TEXT,
            salario REAL,
            data_contratacao TEXT,
            cargo_confianca INTEGER
        )
    ''')

    with open('data/data.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            cursor.execute('''
                INSERT INTO funcionarios (id_funcionario, nome, cargo, departamento, salario, data_contratacao, cargo_confianca)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                int(row[0]),
                row[1],
                row[2],
                row[3],
                float(row[4]),
                row[5],
                int(row[6])
            ))

    conn.commit()

    # Exemplo
    cursor.execute('SELECT * FROM funcionarios')
    resultados = cursor.fetchall()
    for row in resultados:
        print(row)

except sqlite3.Error as e:
    print(f"Ocorreu um erro ao trabalhar com SQLite: {e}")
except FileNotFoundError:
    print("O arquivo CSV não foi encontrado. Verifique o caminho e o nome do arquivo.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    if conn:
        conn.close()
        print("Conexão com o banco de dados fechada.")
