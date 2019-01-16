import sqlite3

database: sqlite3.Connection

TABLE_ID="TABLE_ID"
TABLE_NAME="BOOKS"
BOOK_NAME="BOOK_NAME"
BOOK_PRICE="BOOK_PRICE"
BOOK_AVAILABAL="BOOK_AVAILABLE"

def connection_start():
    global database
    database=sqlite3.connect('book.db')
    print("database created successfully")
    create_table()
    return database
def create_table():
    CREATE_TABLE_QUERY=" CREATE TABLE IF NOT EXISTS "+TABLE_NAME+"("+TABLE_ID+" INTEGER PRIMARY  KEY AUTOINCREMENT ,\
                        "+BOOK_NAME+" TEXT, "+BOOK_PRICE+" INTEGER ,"+BOOK_AVAILABAL+" TEXT);"
    database.execute(CREATE_TABLE_QUERY)
    print("table created")

def save_data(name,price,availability):
    sava_book="INSERT INTO  "+TABLE_NAME+"( " +BOOK_NAME+","+BOOK_PRICE+","+BOOK_AVAILABAL+" " \
                                        ")VALUES ('"+name+ "','"+price+"','"+availability+"');"
    database.execute(sava_book)


def read_data():
    database = connection_start()
    RETRIVE_DATA="SELECT * FROM WebScrapTable;  "
    data = database.execute(RETRIVE_DATA)
    return data
