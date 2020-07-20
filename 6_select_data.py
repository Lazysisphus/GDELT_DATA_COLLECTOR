'''
@Author: your name
@Date: 2020-03-14 21:23:37
@LastEditTime: 2020-04-16 10:07:31
@LastEditors: Zhang Xiaozhu
@Description: In User Settings Edit
@FilePath: \Gdelt_Spring\mysql2csv.py
'''

import pymysql
import pandas as pd
 

'''
在建立好索引的表格上检索特定关键字的内容
'''


table_name_list = [
    'week1',
    'week2',
    'week3',
    'week4',
    'week5',
    'week6',
    'week7',
    'week8',
    'week9',
    'week10',
    'week11',
    'week12',
    'week13',
    'week14'
]


for table in table_name_list:
    conn = pymysql.connect(
                        host='localhost', 
                        user='root', 
                        passwd='5991',
                        db='gdelt',
                        charset='utf8mb4')
    # sql_query = "select SQLDATE, Actor1Name, Actor2Name, Actor1Geo_FullName, Actor2Geo_FullName, ActionGeo_FullName, NumMentions, GoldsteinScale, AvgTone, Title, Content, SOURCEURL from " + table + " where \
    #             match(Actor1Name, Actor2Name, Actor1Geo_FullName, Actor2Geo_FullName, ActionGeo_FullName, Title, Content) \
    #             against('" + word + "');"
    sql_query = "select SQLDATE, Actor1Name, Actor2Name, Actor1Geo_FullName, Actor2Geo_FullName, ActionGeo_FullName, NumMentions, GoldsteinScale, AvgTone, Title, Content, SOURCEURL from " + table + " where \
                    match(Actor1Name, Actor2Name, Actor1Geo_FullName, Actor2Geo_FullName, ActionGeo_FullName, Title, Content) \
                    against('united states america');"
    df = pd.read_sql(sql_query, con=conn)
    conn.close() # 使用完后记得关掉

    df.to_csv(table + '_America.csv', sep='\t')