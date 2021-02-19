'''
Instructions
If you don't already have it, install the SQLite Browser from
http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table
in the database called "Ages":

CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously
inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Kiza', 37);
INSERT INTO Ages (name, age) VALUES ('Ruth', 13);
INSERT INTO Ages (name, age) VALUES ('Darcey', 16);
INSERT INTO Ages (name, age) VALUES ('Hadasah', 17);


Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X

