import mysql.connector
class Dal:
    def __init__(self,host,data_base,user,password,port):
        self.data = mysql.connector.connect(
            host=host,
            database=data_base,
            user=user,
            password=password,
            port=port)


    #Select all table
    def select_all(self):
        try:
            my_cursor = self.data.cursor()
            my_cursor.execute(f"SELECT * FROM {self.data}")
            all_rows = my_cursor.fetchall()
            return all_rows
        except Exception as ex:
            print(f"The error is: {ex}")