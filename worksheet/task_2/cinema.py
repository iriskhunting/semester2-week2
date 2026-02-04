"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    
    query = """
            SELECT title AS film_title, screen, price FROM
            tickets t JOIN screenings s
            ON t.screening_id = s.screening_id
            JOIN films f
            ON s.film_id = f.film_id
            WHERE t.customer_id = ?
            ORDER BY film_title;
            """

    cursor = conn.execute(query, (customer_id,))

    return cursor.fetchall()




def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    
    query = """
            SELECT s.screening_id, title AS film_title, COUNT(ticket_id) AS tickets_sold FROM
            screenings s LEFT JOIN tickets t
            ON s.screening_id = t.screening_id
            JOIN films f
            ON s.film_id = f.film_id
            GROUP BY s.screening_id
            ORDER BY tickets_sold DESC;
            """

    cursor = conn.execute(query)

    return cursor.fetchall()



def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """

    query = """
            SELECT customer_name, SUM(price) AS total_spent FROM 
            customers c JOIN tickets t
            ON c.customer_id = t.customer_id
            GROUP BY customer_name
            ORDER BY total_spent DESC LIMIT ?;
            """
    
    cursor = conn.execute(query, (limit,))

    return cursor.fetchall()
