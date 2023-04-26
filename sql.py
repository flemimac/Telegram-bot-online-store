import sqlite3 as sl

con = sl.connect('database.db')
try:
    with con:
        con.execute("""
            CREATE TABLE database (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255),
                stock VARCHAR(2),
                description TEXT
            );
        """)    
except sl.OperationalError:
    print('База данных уже создана. Пропускаем этот этап')

# Записываем в базу какие-то записи
sql = 'INSERT INTO database (name, stock, description) values( ?, ?, ?)'
data = [ 
    ('1 кг', '1', 'Клей ПВА Момент столяр 1 кг'),
]  # data Может быть любыми вашими записями, как вы их запишите, это лишь ваше дело
with con:
    con.executemany(sql, data)