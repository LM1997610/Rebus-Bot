

import sqlite3


class DBHelper:

    def __init__(self, dbname="dabatabase.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS user_data (chiave integer, nome text, date integer, numero integer)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_users(self, item_text, nome, date, numero):
        stmt = "INSERT INTO user_data  (chiave, nome, date, numero) VALUES (?,?,?,?)"
        args = (item_text, nome, date, numero)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users(self):
        stmt = "SELECT chiave, nome, date, numero FROM user_data"
        res = [x for x in self.conn.execute(stmt)]
        output = dict([(k[0],k[1:]) for k in res ])
        return output

    def get_number(self,chiave):
        stmt = "SELECT numero FROM user_data  WHERE chiave=(?) "
        res = self.conn.execute(stmt, (chiave,))
        res = res.fetchall()

        return res[0][0]

    def get_date(self,chiave):
        stmt = "SELECT date FROM user_data  WHERE chiave=(?) "
        res = self.conn.execute(stmt, (chiave,))
        res = res.fetchall()

        return res[0][0]

    def update_number(self, chiave, numero):
        stmt = "Update user_data set numero = (?) WHERE chiave = (?)"
        args = (numero, chiave )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def update_date(self, chiave, data):
        stmt = "Update user_data set date = (?) WHERE chiave = (?)"
        args = (data, chiave)
        self.conn.execute(stmt, args)
        self.conn.commit()



