# repo.py
from typing import Tuple, List, Any
import sqlite3

def _filters(search: str, type_filter: str) -> Tuple[str, list]:
    where = ["name LIKE ?"]
    params = [f"%{search}%"]
    if type_filter and type_filter != "all":
        where.append("(type1 = ? OR type2 = ?)")
        params += [type_filter, type_filter]
    return " AND ".join(where), params

def fetch_pokemon_list(conn: sqlite3.Connection, search: str, type_filter: str):
    where, params = _filters(search, type_filter)
    sql = f"SELECT * FROM pokemon WHERE {where} ORDER BY id"
    cur = conn.execute(sql, params)
    return cur.fetchall()

def fetch_stats(conn: sqlite3.Connection, search: str, type_filter: str):
    where, params = _filters(search, type_filter)
    sql = f"""
        SELECT 
            COUNT(*)             AS total_count,
            ROUND(AVG(hp), 1)    AS avg_hp,
            ROUND(AVG(attack),1) AS avg_attack,
            ROUND(AVG(defense),1)AS avg_defense,
            MAX(attack)          AS max_attack
        FROM pokemon
        WHERE {where}
    """
    cur = conn.execute(sql, params)
    return cur.fetchone()

def fetch_strongest(conn: sqlite3.Connection, search: str, type_filter: str) -> str:
    where, params = _filters(search, type_filter)
    sql = f"""
        SELECT name
        FROM pokemon
        WHERE {where}
        ORDER BY (hp + attack + defense + sp_attack + sp_defense + speed) DESC
        LIMIT 1
    """
    row = conn.execute(sql, params).fetchone()
    return row["name"] if row else "N/A"
