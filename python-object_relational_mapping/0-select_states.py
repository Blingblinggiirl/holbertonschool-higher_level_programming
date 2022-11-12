#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mysql_dbname = sys.argv[3]

    # connect target db
    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_pwd,
        # db
        db=mysql_dbname)

    # execute the query 
    qry_cursor = my_db.cursor()

    sql_request = "SELECT * FROM states ORDER BY id ASC"
    qry_cursor.execute(sql_request)

    # selects all data from the table:
    records = qry_cursor.fetchall()

    # print records:
    for element in records:
        print(element)

    my_db.close()
