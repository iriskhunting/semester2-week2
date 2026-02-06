import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    return conn

def orders_per_category(db):

    query = '''
            SELECT category, COUNT(oi.order_id) as num_orders FROM 
            products p LEFT JOIN order_items oi
            GROUP BY category
            ORDER BY num_orders DESC
            '''

    cursor = db.execute(query)

    x = []
    y = []
    for c in cursor:
        x.append(c[0])
        y.append(c[1])
    
    plt.bar(x, y)
    plt.title("Orders per Category")
    plt.xlabel('Category')
    plt.ylabel('Orders')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("orders_per_category.png")
    plt.close()

def total_spent(db):

    query = """
            SELECT c.customer_id, first_name, last_name, SUM(total_amount) AS total_spent FROM
            customers c LEFT JOIN orders o
            ON c.customer_id = o.customer_id
            GROUP BY c.customer_id
            ORDER BY total_spent DESC LIMIT 5
            """

    cursor = db.execute(query)

    for c in cursor:
        print(f"ID: {c[0]}\tName: {c[1]} {c[2]}\tTotal Spent: {c[3]}")
    

def main():

    db = get_connection()

    total_spent(db)

    orders_per_category(db)

    db.close()


if __name__=="__main__":
    main()
