import sqlite3
import random
from datetime import datetime, timedelta

db='examples/text2sql/demo_users.db'
# 连接到SQLite数据库（如果不存在则创建）
conn = sqlite3.connect(db)
cursor = conn.cursor()

# 创建用户表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE,
    registration_date DATE,
    last_login DATETIME
)
''')

# 生成示例数据
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]

for i in range(50):  # 创建50个用户记录
    name = random.choice(names)
    age = random.randint(18, 70)
    email = f"{name.lower()}{random.randint(1, 100)}@{random.choice(domains)}"
    registration_date = datetime.now() - timedelta(days=random.randint(1, 1000))
    last_login = registration_date + timedelta(days=random.randint(1, 500))

    cursor.execute('''
    INSERT INTO users (name, age, email, registration_date, last_login)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, age, email, registration_date.date(), last_login))

# 提交更改并关闭连接
conn.commit()
conn.close()

print("Demo database 'demo_users.db' created successfully with sample data.")

# 函数用于显示表格内容
def display_table_contents():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT 5")
    rows = cursor.fetchall()

    print("\nSample data from the users table:")
    for row in rows:
        print(row)

    conn.close()

display_table_contents()