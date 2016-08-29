import MySQLdb
try:
    conn = MySQLdb.connect(host='ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn', user='moji',
                           passwd='BigDataMoji', db='tblu', port=3306, charset="utf8")
    cursor = conn.cursor()
    content = [(1, 12, 12)]
    sql = """insert into feed_access_click(click_num,date) values(%s,%s)"""
    cursor.executemany(sql, content)
    conn.commit()
except:
    print "Mysql Error %d: %s"
finally:
    cursor.close()
    conn.close()
