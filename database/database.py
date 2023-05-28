import logging
import mysql.connector
from mysql.connector import errorcode

# import mariadb
# import sqlite3

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE


class Database:
    def __init__(self):
        self.host = DB_HOST
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.database = DB_DATABASE

        try:
            logging.info("DB starting Test-Connection")
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
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
            logging.info("DB Test-Connection established!")
            self.__disconnect__()

    def __connect__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        logging.debug("DB connection established!")

    def __disconnect__(self):
        self.cursor.close()
        self.connection.close()
        logging.debug("DB cursor and connection closed!")

    def user_exists(self, user_id):
        self.__connect__()
        sql = "SELECT `tg_id` FROM drop_accs WHERE `tg_id` = %s"
        self.cursor.execute(sql, (user_id,))
        result = self.cursor.fetchone()
        self.__disconnect__()
        if result is None:
            return 0
        else:
            return 1

    def user_registered(self, user_id):
        self.__connect__()
        sql = "SELECT `tg_id` FROM drop_accs WHERE `tg_id` = %s AND `user_status` != 'new'"
        self.cursor.execute(sql, (user_id,))
        result = self.cursor.fetchone()
        self.__disconnect__()
        if result is None:
            return 0
        else:
            return 1

    def phone_exists(self, phonenumber):
        self.__connect__()
        sql = "SELECT `phone_number` FROM drop_accs WHERE `phone_number` = %s"
        self.cursor.execute(sql, (phonenumber,))
        result = self.cursor.fetchone()
        self.__disconnect__()
        if result is None:
            return 0
        else:
            return bool(len(result))

    def add_user_empty(self, tg_id, tg_username, referral_id, user_status="new"):
        self.__connect__()
        sql = "INSERT INTO drop_accs (`tg_id`,`tg_username`,`referral_id`,`user_status`) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (tg_id, tg_username, referral_id, user_status))
        self.connection.commit()
        result = self.cursor.fetchall()
        self.__disconnect__()
        if result is None:
            return 0
        else:
            return bool(len(result))

    def add_user_account(
        self,
        tg_id,
        tg_username,
        country,
        region,
        city,
        first_name,
        middle_name,
        surname,
        address,
        postcode,
        date_of_birth,
        document_id,
        phone_number,
        user_status="filled",
    ):
        self.__connect__()
        sql = "UPDATE drop_accs SET `country` = %s, `region` = %s, `city` = %s, `first_name` = %s, `middle_name` = %s, `surname` = %s, `address` = %s, `postcode`= %s, `date_of_birth` = %s, `document_id` = %s, `phone_number` = %s, `user_status` = %s WHERE `tg_id` = %s"
        self.cursor.execute(
            sql,
            (
                country,
                region,
                city,
                first_name,
                middle_name,
                surname,
                address,
                postcode,
                date_of_birth,
                document_id,
                phone_number,
                user_status,
                tg_id,
            ),
        )
        self.connection.commit()
        result = self.cursor.fetchall()
        self.__disconnect__()
        if result is None:
            return 0
        else:
            return bool(len(result))

    def get_user_language(self, user_id):
        self.__connect__()
        sql = "SELECT `language` FROM drop_accs WHERE `tg_id` = %s"
        self.cursor.execute(sql, (user_id,))
        result = self.cursor.fetchone()
        self.__disconnect__()
        if result is None:
            return "ru"
        else:
            return result[0]

    def get_user_referral(self, user_id):
        self.__connect__()
        sql = "SELECT `referral_id` FROM drop_accs WHERE `tg_id` = %s"
        self.cursor.execute(sql, (user_id,))
        result = self.cursor.fetchone()
        self.__disconnect__()
        if result is None:
            return ""
        else:
            return result[0]

    def change_user_language(self, user_id, new_language):
        self.__connect__()
        sql = "UPDATE drop_accs SET `language` = %s WHERE `tg_id` = %s"
        self.cursor.execute(
            sql,
            (
                new_language,
                user_id,
            ),
        )
        self.connection.commit()
        self.__disconnect__()
        return True

    def is_user_manager(self, user_id):
        self.__connect__()
        sql = "SELECT `dm_tg_username` FROM drop_manager WHERE `dm_tg_id` = %s"
        self.cursor.execute(sql, (user_id,))
        result = self.cursor.fetchone()
        self.__disconnect__()
        if result is None:
            return 0
        else:
            return 1

    def get_manager_invites(self, user_id, user_status):
        self.__connect__()
        if(user_status != ""):
            sql = "SELECT COUNT(`referral_id`) FROM drop_accs WHERE `referral_id` = %s AND `user_status` = %s"
            self.cursor.execute(
                sql,
                (
                    user_id,
                    user_status,
                ),
            )
            result = self.cursor.fetchone()
        else:
            sql = "SELECT COUNT(`referral_id`) FROM drop_accs WHERE `referral_id` = %s"
            self.cursor.execute(
                sql,
                (
                    user_id,
                ),
            )
            result = self.cursor.fetchone()
        self.__disconnect__()
        if result is None:
            return 0
        else:
            return result[0]

    def get_top_managers(self):
        self.__connect__()
        sql = "SELECT `tg_id_top_manager` FROM top_manager"
        self.cursor.execute(sql, ())
        result = self.cursor.fetchall()
        self.__disconnect__()
        if result is None:
            return None
        else:
            return result
        
    def update_manager_invites(self, user_id, invited_users):
        self.__connect__()
        sql = "UPDATE drop_manager SET `invited_users` = %s WHERE `dm_tg_id` = %s"
        self.cursor.execute(sql, (invited_users, user_id, ))
        self.connection.commit()
        result = self.cursor.fetchone()
        if (result is None):
            return 0
        else:
            return result[0]
