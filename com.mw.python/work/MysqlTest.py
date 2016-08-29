import traceback

import MySQLdb

def mysqlExe(sql):
    try:
        conn = MySQLdb.connect(host='ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn', user='moji',passwd='BigDataMoji', db='userinfo', port=3306, charset="utf8")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()
