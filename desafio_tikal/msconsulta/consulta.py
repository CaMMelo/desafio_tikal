import re

from sqlalchemy import text

from desafio_tikal.msconsulta.database import engine

QUERY_STRING = "SELECT c.* FROM crud_cliente c {} WHERE {}"
CLAUSE_JOIN_EMAIL = "LEFT JOIN crud_email e ON e.cliente_id = c.id"
CLAUSE_WHERE_EMAIL = "e.email LIKE '%{}%'"
CLAUSE_JOIN_TELEFONE = "LEFT JOIN crud_telefone t ON t.cliente_id = c.id"
CLAUSE_WHERE_DDD = "t.ddd = '{}'"
CLAUSE_WHERE_NUMERO = "t.numero LIKE '%{}%'"
CLAUSE_WHERE_NUMERO_DDD = "t.numero LIKE '{}%'"


def format_query(query_val):
    clause_join = ""
    clause_where = ""
    if re.search(r"^[0-9]+$", query_val):
        clause_join = f"{CLAUSE_JOIN_TELEFONE} {CLAUSE_JOIN_EMAIL}"
        clause_where = f"{CLAUSE_WHERE_EMAIL.format(query_val)}"
        if 1 <= len(query_val) <= 8:
            clause_where += f" OR {CLAUSE_WHERE_NUMERO.format(query_val)}"
        if len(query_val) >= 2:
            ddd = query_val[:2]
            clause_where += f" OR {CLAUSE_WHERE_DDD.format(ddd)}"
        if 3 <= len(query_val) <= 11:
            numero = query_val[2:]
            if 1 <= len(numero) <= 8:
                clause_where += f" OR {CLAUSE_WHERE_NUMERO_DDD.format(numero)}"
            if numero[0] == "9" and (1 <= len(numero[1:]) <= 8):
                clause_where += f" OR {CLAUSE_WHERE_NUMERO_DDD.format(numero[1:])}"
    elif re.search(r"^([0-9]{2})9?[0-9]*$", query_val):
        clause_join = f"{CLAUSE_JOIN_TELEFONE}"
        ddd = query_val[1:3]
        numero = query_val[3:]
        clause_where = f"{CLAUSE_WHERE_DDD.format(ddd)}"
        if 1 <= len(numero) <= 8:
            clause_where += f" OR {CLAUSE_WHERE_NUMERO_DDD.format(numero)}"
        if numero[0] == "9" and (1 <= len(numero[1:]) <= 8):
            clause_where += f" OR {CLAUSE_WHERE_NUMERO_DDD.format(numero[1:])}"
    else:
        clause_join = f"{CLAUSE_JOIN_EMAIL}"
        clause_where = f"{CLAUSE_WHERE_EMAIL.format(query_val)}"
    return QUERY_STRING.format(clause_join, clause_where)


def consulta(query_val):
    with engine.connect() as conn:
        result = conn.execute(text(format_query(query_val)))
        return result.all()
