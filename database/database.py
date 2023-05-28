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
            # result = self.cursor.execute("SELECT `tg_id` FROM `drop_accs` WHERE `tg_id` = ?",(user_id,)).fetchone()
            sql = "SELECT `tg_id` FROM `drop_accs` WHERE `tg_id` = ?"
            result = self.cursor.execute(sql, (user_id,)).fetchone()
            # result = self.cursor.fetchone()
            # print(result)
            if (result is None):
                return 0
            else:
                return 1

    def user_registered(self, user_id):
        with self.connection:
            sql = "SELECT `tg_id` FROM `drop_accs` WHERE `tg_id` = ? AND `user_status` != 'new'"
            result = self.cursor.execute(sql, (user_id,)).fetchone()
            # result = self.cursor.fetchone()
            if (result is None):
                return 0
            else:
                return 1

    def phone_exists(self, phonenumber):
        with self.connection:
            sql = "SELECT `phone_number` FROM `drop_accs` WHERE `phone_number` = ?"
            result = self.cursor.execute(sql, (phonenumber,)).fetchone()
            # result = self.cursor.fetchone()
            if (result is None):
                return 0
            else:
                return bool(len(result))

    def add_user_empty(self, tg_id, tg_username, referral_id, user_status="new"):
        with self.connection:
            sql = "INSERT INTO `drop_accs` (`tg_id`,`tg_username`,`referral_id`,`user_status`) VALUES (?, ?, ?, ?)"
            result = self.cursor.execute(
                sql, (tg_id, tg_username, referral_id, user_status)).fetchall()
            self.connection.commit()
            #result = self.cursor.fetchall()
            if (result is None):
                return 0
            else:
                return bool(len(result))

    def add_user_account(self, tg_id, tg_username, country, region, city, first_name, middle_name, surname, address, postcode, date_of_birth, document_id, phone_number, user_status="filled"):
        with self.connection:
            sql = "UPDATE `drop_accs` SET `country` = ?, `region` = ?, `city` = ?, `first_name` = ?, `middle_name` = ?, `surname` = ?, `address` = ?, `postcode`= ?, `date_of_birth` = ?, `document_id` = ?, `phone_number` = ?, `user_status` = ? WHERE `tg_id` = ?"
            result = self.cursor.execute(
                sql, (country, region, city, first_name, middle_name, surname, address, postcode, date_of_birth, document_id, phone_number, user_status, tg_id)).fetchall()
            self.connection.commit()
            #result = self.cursor.fetchall()
            if (result is None):
                return 0
            else:
                return bool(len(result))

    def get_user_language(self, user_id):
        with self.connection:
            sql = "SELECT `language` FROM `drop_accs` WHERE `tg_id` = ?"
            result = self.cursor.execute(sql, (user_id,)).fetchone()
            # result = self.cursor.fetchone()
            if (result is None):
                return "ru"
            else:
                return result[0]

    def get_user_referral(self, user_id):
        with self.connection:
            sql = "SELECT `referral_id` FROM `drop_accs` WHERE `tg_id` = ?"
            result = self.cursor.execute(sql, (user_id,)).fetchone()
            # result = self.cursor.fetchone()
            if (result is None):
                return ""
            else:
                return result[0]

    def change_user_language(self, user_id, new_language):
        with self.connection:
            sql = "UPDATE `drop_accs` set `language` = ? WHERE `tg_id` = ?"
            self.cursor.execute(sql, (new_language, user_id,))
            return True

    def is_user_manager(self, user_id):
        with self.connection:
            sql = "SELECT `dm_tg_username` FROM `drop_manager` WHERE `dm_tg_id` = ?"
            result = self.cursor.execute(sql, (user_id,)).fetchone()
            #result = self.cursor.fetchone()
            #print(result)
            if (result is None):
                return 0
            else:
                return 1
            
    def get_manager_invites(self, user_id, user_status="new"):
        with self.connection:
            sql = "SELECT COUNT(`referral_id`) FROM `drop_accs` WHERE `referral_id` = ? AND `user_status` = ?"
            result = self.cursor.execute(sql, (user_id, user_status,)).fetchone()
            # result = self.cursor.fetchone()
            if (result is None):
                return 0
            else:
                return result[0]
            
    def get_top_managers(self):
        with self.connection:
            sql = "SELECT `tg_id_top_manager` FROM `top_manager`"
            result = self.cursor.execute(sql, ()).fetchall()
            # result = self.cursor.fetchone()
            #print(result)
            if (result is None):
                return None
            else:
                return result

