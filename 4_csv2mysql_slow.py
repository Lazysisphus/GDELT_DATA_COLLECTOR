'''
@Descripttion: 
@version: 
@Author: pigZhang
@Date: 2018-07-23 08:54:12
@LastEditors: Please set LastEditors
@LastEditTime: 2020-03-14 12:55:06
'''


import pymysql # 导入mysql数据库的python接口pymysql
import csv     # 读取csv文件的包


# 建表语句是一个字符串，每一行的格式是（列名，存储类型）
event = '''create table event(
            GLOBALEVENTID varchar(255),
            SQLDATE varchar(255),
            MonthYear varchar(255),
            Year varchar(255),
            FractionDate varchar(255),
            Actor1Code varchar(255),
            Actor1Name varchar(255),
            Actor1CountryCode varchar(255),
            Actor1KnownGroupCode varchar(255),
            Actor1EthnicCode varchar(255),
            Actor1Religion1Code varchar(255),
            Actor1Religion2Code varchar(255),
            Actor1Type1Code varchar(255),
            Actor1Type2Code varchar(255),
            Actor1Type3Code varchar(255),
            Actor2Code varchar(255),
            Actor2Name varchar(255),
            Actor2CountryCode varchar(255),
            Actor2KnownGroupCode varchar(255),
            Actor2EthnicCode varchar(255),
            Actor2Religion1Code varchar(255),
            Actor2Religion2Code varchar(255),
            Actor2Type1Code varchar(255),
            Actor2Type2Code varchar(255),
            Actor2Type3Code varchar(255),
            IsRootEvent varchar(255),
            EventCode varchar(255),
            EventBaseCode varchar(255),
            EventRootCode varchar(255),
            QuadClass varchar(255),
            GoldsteinScale varchar(255),
            NumMentions varchar(255),
            NumSources varchar(255),
            NumArticles varchar(255),
            AvgTone varchar(255),
            Actor1Geo_Type varchar(255),
            Actor1Geo_FullName varchar(255),
            Actor1Geo_CountryCode varchar(255),
            Actor1Geo_ADM1Code varchar(255),
            Actor1Geo_ADM2Code varchar(255),
            Actor1Geo_Lat varchar(255),
            Actor1Geo_Long varchar(255),
            Actor1Geo_FeatureID varchar(255),
            Actor2Geo_Type varchar(255),
            Actor2Geo_FullName varchar(255),
            Actor2Geo_CountryCode varchar(255),
            Actor2Geo_ADM1Code varchar(255),
            Actor2Geo_ADM2Code varchar(255),
            Actor2Geo_Lat varchar(255),
            Actor2Geo_Long varchar(255),
            Actor2Geo_FeatureID varchar(255),
            ActionGeo_Type varchar(255),
            ActionGeo_FullName varchar(255),
            ActionGeo_CountryCode varchar(255),
            ActionGeo_ADM1Code varchar(255),
            ActionGeo_ADM2Code varchar(255),
            ActionGeo_Lat varchar(255),
            ActionGeo_Long varchar(255),
            ActionGeo_FeatureID varchar(255),
            DATEADDED varchar(255),
            SOURCEURL varchar(255),
            Title MEDIUMTEXT,
            Content MEDIUMTEXT
        )CHARSET=utf8mb4 COLLATE=utf8mb4_bin;'''


# 与数据库建立连接，返回连接以及连接的指针
# 输入的参数分别是：ip地址、端口号、用户名、密码、数据库名称、字符编码
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='5991', db='gdelt', charset='utf8')
    cur = conn.cursor()
    return conn, cur


# 在数据库表格中插入一条数据
def insert(cur, sql, args):
    cur.execute(sql, args)


# 将表格导入数据库表格
def csv_to_db(csvname):
    reader = csv.reader(open(csvname, encoding='utf-8'), delimiter='\t') # 读取当前csv文件
    conn,cur = get_conn() # 建立和数据库的连接，相当于登陆了数据库
    sql = 'insert into event values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
                                    %s,%s,%s)'
	# 将csv文件中的每一行更新到数据库的表格中
    for i, row in enumerate(reader):
        if i == 0:
            continue
        else:
            row = row[1:]
            if row[0] is None or row[0] == '': # item[0]作为唯一键,不能为null
                continue
            args = tuple(row) # 每个arg现在是一个元组，元组中元素的个数等于表格的列数。
            # print(args) # ('', '', ... , '')的形式
            # print(len(args)) # 61，表格有61列
            insert(cur, sql=sql, args=args)
    conn.commit() # 和数据库通信，更新数据库信息
    print('表格' + csvname + '数据添加成功!')
    # 关闭数据库连接
    cur.close()
    conn.close()


if __name__ == '__main__':
    pymysql.charset = 'utf-8'
    csv_list = ['test.csv']
	# 更新多个csv文件的数据到数据库的表格中
    for csv_name in csv_list:
        csv_to_db(csv_name)