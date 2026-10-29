import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))


def executar_sql(sql, parametros=()):
    conexao = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

    cursor = None

    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql, parametros)
        return cursor.fetchall()

    finally:
        if cursor is not None:
            cursor.close()
        conexao.close()