import sqlite3
conn = sqlite3.connect('AnimalKingdom.db')
cursor = conn.cursor()
cursor.execute("")
animals = [
    ('Лев', 'Ссавець'),
    ('Крокодил', 'Плазун'),
    ('Орел', 'Птах'),
    ('Морська черепаха', 'Плазун'),
    ('Мавпа', 'Ссавець')
]
cursor.executemany('INSERT INTO Animals (Назва_звіра, Тип_звіра) VALUES (?, ?)', animals)

conn.commit()
cursor.execute('SELECT * FROM Animals')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()