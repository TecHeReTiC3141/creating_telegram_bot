import sqlite3

db = sqlite3.connect(r'../databases/testDB2.db')
cur = db.cursor()
cur.execute('''INSERT INTO users (name, chat_id, exp)
                VALUES ("Tec", 1000, 0)''')
print(*cur.execute('''SELECT * FROM users'''), sep='\n')
db.commit()