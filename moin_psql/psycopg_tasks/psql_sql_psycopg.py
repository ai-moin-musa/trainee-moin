import psycopg2

conn=psycopg2.connect(
dbname="test",
user="odoo",
password="odoo",
host="127.0.0.1",
port="5432")
cursor = conn.cursor()
conn.autocommit = True
print(cursor)

cursor.execute('''
select c.name,SUM(COALESCE(o.quantity*p.price,0)) as Total_Order_Value 
from customers as c 
LEFT JOIN orders as o ON c.id = o.customer_id 
LEFT JOIN products as p ON o.product_id = p.id 
GROUP BY c.name;
''')

result = cursor.fetchall()
print("--first query output--")
for row in result:
	print(row)
	
	
cursor.execute('''
select p.id, p.name, p.price from products as p LEFT JOIN orders as o ON p.id = o.product_id where o.id is null;
''')

result = cursor.fetchall()
print("\n\n\n--second query output--")
for row in result:
	print(row)
	

	
cursor.execute('''
select c.name, (p.price*o.quantity) as total_value from orders as o INNER JOIN customers as c ON o.customer_id = c.id INNER JOIN products as p ON o.product_id = p.id where p.price > 50;
''')

result = cursor.fetchall()
print("\n\n\n--third query output--")
for row in result:
	print(row)

conn.commit()
conn.close()
