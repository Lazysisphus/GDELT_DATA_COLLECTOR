'''
@Descripttion: 
@version: 
@Author: Zhang Xiaozhu
@Date: 2020-03-26 20:06:30
@LastEditors: Zhang Xiaozhu
@LastEditTime: 2020-04-07 23:40:42
'''


'''
在已经导入数据库的表格上建立索引
'''


import pymysql


table_name_list = [
    'week14'
]


# 创建连接
conn = pymysql.connect(user='root', password='5991', database='gdelt', charset='utf8mb4')


for table in table_name_list:
    with conn.cursor() as cursor:
        # event_fulltext、title_fulltext
        sql = "create fulltext index event_fulltext on " + table + " (Actor1Name, Actor2Name, Actor1Geo_FullName, Actor2Geo_FullName, ActionGeo_FullName, Title, Content);"
        cursor.execute(sql)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    conn.commit()
    print(table + "的索引建立完成！")