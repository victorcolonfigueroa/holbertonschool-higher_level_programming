import MySQLdb
import sys

def list_states_with_n(username, password, dbname):
    """
    Connects to a MySQL database and lists all states with names starting with N, sorted by id in ascending order
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
    
if __name__ == "__main__":
    list_states_with_n(sys.argv[1], sys.argv[2], sysargv[3])
