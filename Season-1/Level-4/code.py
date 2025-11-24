import sqlite3
import os

class Connect(object):

    def create_connection(self, path):
        try:
            return sqlite3.connect(path)
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
            return None


class Create(object):

    def __init__(self):
        con = Connect()
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, "level-4.db")
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()

            table_fetch = cur.execute(
                """
                SELECT name
                FROM sqlite_master
                WHERE type='table' AND name='stocks';
                """).fetchall()

            if table_fetch == []:
                cur.execute("""
                    CREATE TABLE stocks (
                        date TEXT,
                        symbol TEXT,
                        price REAL
                    )
                """)

                cur.execute(
                    "INSERT INTO stocks VALUES ('2022-01-06','MSFT',300.00)"
                )
                db_con.commit()

        except sqlite3.Error as e:
            print(f"ERROR: {e}")

        finally:
            db_con.close()


class DB_CRUD_ops(object):

    # (1) SAFE get_stock_info
    def get_stock_info(self, stock_symbol):
        Create()
        con = Connect()

        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, "level-4.db")
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()

            query = "SELECT * FROM stocks WHERE symbol = ?"

            cur.execute(query, (stock_symbol,))
            rows = cur.fetchall()

            res = "[METHOD EXECUTED] get_stock_info\n"
            res += "[QUERY] " + query + "\n"

            for row in rows:
                res += "[RESULT] " + str(row)

            return res

        finally:
            db_con.close()

    # (2) SAFE get_stock_price
    def get_stock_price(self, stock_symbol):
        Create()
        con = Connect()

        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, "level-4.db")
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()

            query = "SELECT price FROM stocks WHERE symbol = ?"

            cur.execute(query, (stock_symbol,))
            rows = cur.fetchall()

            res = "[METHOD EXECUTED] get_stock_price\n"
            res += "[QUERY] " + query + "\n"

            for row in rows:
                res += "[RESULT] " + str(row) + "\n"

            return res

        finally:
            db_con.close()

    # (3) SAFE update_stock_price
    def update_stock_price(self, stock_symbol, price):
        if not isinstance(price, (int, float)):
            raise ValueError("ERROR: stock price provided is not numeric")

        Create()
        con = Connect()

        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, "level-4.db")
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()

            query = "UPDATE stocks SET price = ? WHERE symbol = ?"

            cur.execute(query, (float(price), stock_symbol))
            db_con.commit()

            res = "[METHOD EXECUTED] update_stock_price\n"
            res += "[QUERY] " + query + "\n"

            return res

        finally:
            db_con.close()