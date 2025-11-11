from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        self._db = DBConnect().get_connection()

    def get_artefatti_filtrati(self, museo:str, epoca:str):
        cursor = self._db.cursor()
        query = """
        SELECT a.id, a.nome, a.epoca, m.nome AS museo_nome
        FROM artefatto a
        JOIN museo m ON a.museo_id = m.id
        WHERE (%s IS NULL OR m.nome = %s)
          AND (%s IS NULL OR a.epoca = %s)
        ORDER BY a.nome;
        """

        cursor.execute(query, (museo, museo, epoca, epoca))
        artefatti = [Artefatto(r["id"], r["nome"], r["epoca"], r["museo_nome"]) for r in cursor.fetchall()]
        cursor.close()
        return artefatti


