# import mysql.connector
# from mysql.connector import errorcode
# import mariadb
import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        if (self.connection):
            print("DB Connected!")

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("DB connection closed!")

    def user_exists(self, user_id):
        with self.connection:
            #result = self.cursor.execute("SELECT `tg_id` FROM `drop_accs` WHERE `tg_id` = ?",(user_id,)).fetchone()
            sql = "SELECT `tg_id` FROM `drop_accs` WHERE `tg_id` = ?"
            self.cursor.execute(sql, (user_id,))
            result = self.cursor.fetchone()
            #print(result)
            if result != None:
                return 1
            else:
                return 0

    def user_registered(self, user_id):
        with self.connection:
            sql = "SELECT `tg_id` FROM `drop_accs` WHERE `tg_id` = ? AND `user_status` != 'new'"
            self.cursor.execute(sql, (user_id,))
            result = self.cursor.fetchone()
            if result != None:
                return 1
            else:
                return 0

    def phone_exists(self, phonenumber):
        with self.connection:
            sql = "SELECT `phone_number` FROM `drop_accs` WHERE `phone_number` = ?"
            self.cursor.execute(sql, (phonenumber,))
            result = self.cursor.fetchone()
            if result != None:
                return bool(len(result))
            else:
                return 0

    def add_user_empty(self, tg_id, tg_username, referral_id, user_status="new"):
        with self.connection:
            sql = "INSERT INTO `drop_accs` (`tg_id`,`tg_username`,`referral_id`,`user_status`) VALUES (?, ?, ?, ?)"
            self.cursor.execute(
                sql, (tg_id, tg_username, referral_id, user_status))
            self.connection.commit()
            result = self.cursor.fetchall()
            if result != None:
                return bool(len(result))
            else:
                return 0

    def add_user_account(self, tg_id, tg_username, country, region, city, full_name, address, date_of_birth, document_id, phone_number, user_status="filled"):
        with self.connection:
            sql = "UPDATE `drop_accs` SET `country` = ?, `region` = ?, `city` = ?, `full_name` = ?, `address` = ?, `date_of_birth` = ?,`document_id` = ?,`phone_number` = ?,`user_status` = ? WHERE `tg_id` = ?"
            self.cursor.execute(
                sql, (country, region, city, full_name, address, date_of_birth, document_id, phone_number, user_status, tg_id))
            self.connection.commit()
            result = self.cursor.fetchall()
            if result != None:
                return bool(len(result))
            else:
                return 0

    def get_user_language(self, user_id):
        with self.connection:
            sql = "SELECT `language` FROM `drop_accs` WHERE `tg_id` = ?"
            self.cursor.execute(sql, (user_id,))
            result = self.cursor.fetchone()[0]
            if result != None:
                return result
            else:
                return 'en'

    def change_user_language(self, user_id, new_language):
        with self.connection:
            sql = "UPDATE `drop_accs` set `language` = ? WHERE `tg_id` = ?"
            self.cursor.execute(sql, (new_language, user_id,))
            return True

    def is_user_manager(self, user_id):
        with self.connection:
            sql = "SELECT `dm_tg_username` FROM `drop_manager` WHERE `dm_tg_id` = ?"
            self.cursor.execute(sql, (user_id,))
            result = self.cursor.fetchone()
            print(result)
            if result != None:
                return result
            else:
                return 0
