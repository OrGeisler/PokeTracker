import pymysql

class db_proxy:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                                                host='localhost',
                                                user='root',
                                                password="",
                                                db="poke_tracker",
                                                charset="utf8",
                                                cursorclass=pymysql.cursors.DictCursor
                                            )
        except pymysql.Error as e:
            print("Error while connecting to MySQL", e)

    def execute_insert_query(self, sql_query, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params)
                self.connection.commit()
                print(f'{params} inserted successfully')

        except pymysql.Error as e:
            print("Failed to insert into MySQL table {}".format(e))
    
    def execute_delete_query(self, sql_query, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params)
                self.connection.commit()
                print(f'{params} deleted successfully')

        except pymysql.Error as e:
            print("Failed to delete from MySQL table {}".format(e))

    def execute_select_one_query(self, sql_query, params = None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params) if params else cursor.execute(sql_query)
                result = cursor.fetchone()
                print(f'selected {result} successfully')
                return result
        except pymysql.Error as e:
            print("Failed to select one from MySQL table {}".format(e))

    def execute_select_all_query(self, sql_query, params = None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params) if params else cursor.execute(sql_query)
                result = cursor.fetchall()
                print(f'selected {result} successfully')
                return result
        except pymysql.Error as e:
            print("Failed to select all from MySQL table {}".format(e))