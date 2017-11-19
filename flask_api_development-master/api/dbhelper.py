import psycopg2  # define database connection parameters


def GetData(strsql):
    con = psycopg2.connect(host="localhost",
                           user="postgres",
                           password="Esrigis01",
                           database="weather",
                           port=5433)

    cur = con.cursor()
    cur.execute(strsql)
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows