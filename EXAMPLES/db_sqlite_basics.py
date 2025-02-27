import sqlite3

# conn = sqlite3.Connection(...)
with sqlite3.connect("../DATA/presidents.db") as conn:  # connect to the database

    s3_cursor = conn.cursor()  # get a cursor object

    # select specified columns from all presidents
    s3_cursor.execute('''
        select *
        from presidents
    ''')  # execute a SQL statement

    for row in s3_cursor.fetchall():
        print(row)
    # for term, firstname, lastname, party in s3_cursor.fetchall():
    #     print(f"{term:2d} {firstname:25} {lastname:20} {party}")
    # print()
    # print(f"{s3_cursor = }")
    
    # print(dir(s3_cursor))