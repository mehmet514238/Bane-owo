import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect('owo_bot.db')
cursor = conn.cursor()

# Veritabanı tablosu oluşturma
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS balances (
            id INTEGER PRIMARY KEY,
            user_id TEXT,
            balance INTEGER
        )
    ''')
    conn.commit()

# Balance güncelleme/loglama fonksiyonu
def log_balance(user_id, balance):
    cursor.execute('INSERT INTO balances (user_id, balance) VALUES (?, ?)', (user_id, balance))
    conn.commit()

# Veritabanı kapatma işlemi
def close_db():
    conn.close()
