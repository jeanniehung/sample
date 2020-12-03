# import pymysql
# from data.dir_data import Mysql
#
#
# class PyMysql(object):
#
#     def db(self):
#         db = pymysql.connect(host=Mysql.host, user=Mysql.user, password=Mysql.password, db=Mysql.db)
#         return db
#
#     def option(self, sql):
#         db = self.db()
#         cursor = db.cursor()
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         cursor.close()
#         db.close()
#         return result
#
#     def db_close(self, db):
#         db.close()




