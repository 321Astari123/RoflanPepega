import sqlite3

# Подключение к базе данных (или создание, если она не существует)
conn = sqlite3.connect('products.db')
c = conn.cursor()

# Создание таблицы
c.execute('''CREATE TABLE products
             (id INTEGER PRIMARY KEY, name TEXT, amount INT, price REAL, image_path TEXT)''')

# Вставка тестовых данных
products = [
    (1, 'Бибиэски', 15, 60, 'images/bbslm.jpg'),
    (2, 'Всмпошки', 15, 50, 'images/ellada.jpg'),
    (3, 'Энкеи', 15, 70, 'images/enkei.jpg'),
    (4, 'Кёниг', 15, 80, 'images/konig.jpg'),
    (5, 'ВиеннаSSR', 15, 50, 'images/vienna.jpg'),
    (6, '5зиген', 0, 70, 'images/zigen5.jpg'),
]

c.executemany('INSERT INTO products VALUES (?,?,?,?,?)', products)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных успешно создана и заполнена!")
