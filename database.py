import sqlite3

DB_FILE = "sales.db"

def create_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            selling_price REAL NOT NULL,
            expenses REAL NOT NULL,
            status TEXT NOT NULL default 'confirmed'     
        )
    ''')
    connection.commit()
    connection.close()


##CREATE / ADD A NEW EVENT
def add_sale(client_name, category, date, selling_price, expenses):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO sales (client_name, category, date, selling_price, expenses)
        VALUES (?, ?, ?, ?, ?)
    ''', (client_name, category, date, selling_price, expenses))
    connection.commit()
    connection.close()
    
##READ / VIEW ALL EVENTS
def get_all_sales():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    connection.close()
    
    sales_list = []
    for sale in sales:
        sales_list.append({
            "id": sale[0],
            "client_name": sale[1],
            "category": sale[2],
            "date": sale[3],
            "selling_price": sale[4],
            "expenses": sale[5],
            "status": sale[6]
        })
    return sales_list

###UPDATE / EDIT AN EVENT
def update_sale(sale_id, client_name, category, date, selling_price, expenses):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE sales
        SET client_name = ?, category = ?, date = ?, selling_price = ?, expenses = ?
        WHERE id = ?
    ''', (client_name, category, date, selling_price, expenses, sale_id))
    connection.commit()
    connection.close()
    
###DELETE AN EVENT
def delete_sale(sale_id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM sales WHERE id = ?', (sale_id,))
    connection.commit()
    connection.close()