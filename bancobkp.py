import sqlite3
import csv
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT rowid, * FROM inventory")
columns = [column[0] for column in c.description]
results = []
for row in c.fetchall():
    results.append(dict(zip(columns, row)))
with open("output.csv", "w", newline='') as new_file:
    fieldnames = columns
    writer = csv.DictWriter(new_file,fieldnames=fieldnames)
    writer.writeheader()
    for line in results:
        writer.writerow(line)
conn.close()