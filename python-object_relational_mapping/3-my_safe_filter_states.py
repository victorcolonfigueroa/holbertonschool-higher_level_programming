#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name=%s ORDER BY id ASC;"
    cur.execute(query, (state_name,))
    # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
