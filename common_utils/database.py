import configparser

import pymysql


class DataBase(object):

    def excute_sql(self, db_filepath, db_item, sql):
        config = configparser.RawConfigParser()
        config.read(db_filepath, encoding="utf-8")
        dbconfig=dict(config.items(db_item))
        connect = pymysql.Connect(
            host=dbconfig['host'],
            port=int(dbconfig['port']),
            user=dbconfig['mysql_username'],
            passwd=dbconfig['mysql_root_password'],
            db=dbconfig['db_name'],
            charset="utf8"
        )
        # 获得游标
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行sql语句
        cursor.execute(sql)
        connect.commit()
        # 获取所有记录列表
        results = cursor.fetchall()
        cursor.close()
        connect.close()
        return results
