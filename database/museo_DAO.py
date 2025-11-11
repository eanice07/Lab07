from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self._db = DBConnect().get_connection()

    def get_musei(self):
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM museo ORDER BY nome")
        musei = [Museo(row["id"], row["nome"]) for row in cursor.fetchall()]
        cursor.close()
        return musei

