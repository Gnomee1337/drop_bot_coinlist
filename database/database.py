import mysql.connector
from mysql.connector import errorcode


class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="reg_bot"
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your DB user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cursor = self.connection.cursor()
            print("DB connection established!")

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("DB connection closed!")

    def user_exists(self, user_id):
        with self.connection:
            sql = "SELECT `tg_id` FROM `drop_accs` WHERE `tg_id` = %s LIMIT 1"
            self.cursor.execute(sql, (user_id,))
            result = self.cursor.fetchone()
            if result != None:
                return 1
            else:
                return 0

    def phone_exists(self, phonenumber):
        with self.connection:
            sql = "SELECT `phone_number` FROM `drop_accs` WHERE `phone_number` = %s LIMIT 1"
            self.cursor.execute(sql, (phonenumber,))
            result = self.cursor.fetchone()
            if result != None:
                return bool(len(result))
            else:
                return 0
            
    def add_user_account(self, tg_id, tg_username, country, full_name, phone_number, address, postal_code):
        with self.connection:
                sql = "INSERT INTO `drop_accs` (`tg_id`,`tg_username`,`country`,`full_name`,`phone_number`,`address`,`postal_code`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql, (tg_id, tg_username, country, full_name, phone_number, address, postal_code))
                self.connection.commit()
                result = self.cursor.fetchall()
                if result != None:
                  return bool(len(result))
                else:
                  return 0
