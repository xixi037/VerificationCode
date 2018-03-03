import os
import pymysql

# base_path = os.path.join(os.getcwd(),"static")
# dir_path = os.path.join(base_path,"pic")
# print(dir_path)
#
# for root,dirs,files in os.walk(dir_path):
#     for filename in files:
#         path = "/pic/" + str(filename)
#         print(path)
#
#         db = pymysql.connect("localhost","root","1234","verificationcode")
#         cursor = db.cursor()
#         sql = "INSERT INTO verify(path,status) VALUES ('%s',0)" %(path)
#         print(sql)
#         try:
#             cursor.execute(sql)
#             db.commit()
#         except:
#             db.rollback()
#         db.close()

import sqlite3

base_path = os.path.join(os.getcwd(),"static")
dir_path = os.path.join(base_path,"pic")
print(dir_path)

for root,dirs,files in os.walk(dir_path):
    for filename in files:
        path = "/pic/" + str(filename)
        print(path)
        sq = sqlite3.connect('VerificationCode.db')
        cursor = sq.cursor()
        # cursor.execute('''
        # CREATE TABLE verify (
        # path VARCHAR(255) PRIMARY KEY,
        # status VARCHAR(255),
        # tab VARCHAR(255),
        # verify VARCHAR(255),
        # uptime VARCHAR(255),
        # operator VARCHAR(255)
        # );
        # ''')
        sql = "INSERT INTO verify(path,status) VALUES ('%s',0)" %(path)
        cursor.execute(sql)
        sq.commit()
        cursor.close()
        sq.close()