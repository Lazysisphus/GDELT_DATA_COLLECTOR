'''
@Author: your name
@Date: 2020-03-14 11:17:48
@LastEditTime: 2020-04-07 23:16:12
@LastEditors: Zhang Xiaozhu
@Description: In User Settings Edit
@FilePath: \Gdelt_Spring\new_csv2mysql.py
'''


'''
调用pandas包将csv文件导入数据库
与文件4功能相同，但是调包导入速度更快，因此建议使用文件3
'''

import os
import pandas as pd

from tqdm import tqdm
from header import header
from sqlalchemy import create_engine


if __name__ == "__main__":
    # 初始化数据库连接，使用pymysql模块
    db_info = {'user': 'root',
                'password': '5991',
                'host': 'localhost',
                'port': 3306,
                'database': 'gdelt'
                }
    # charset必须使用utf8mb4，因为传统的utf8与emoji不兼容
    engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8mb4' % db_info, encoding='utf8')
    
    # 列表，存储爬取到标题和内容后的新文件路径
    week1 = [
        'E:/GDELT_DATA/new_csv_files/20200101/',
        'E:/GDELT_DATA/new_csv_files/20200102/',
        'E:/GDELT_DATA/new_csv_files/20200103/',
        'E:/GDELT_DATA/new_csv_files/20200104/',
        'E:/GDELT_DATA/new_csv_files/20200105/'
    ]
    week2 = [
        'E:/GDELT_DATA/new_csv_files/20200106/',
        'E:/GDELT_DATA/new_csv_files/20200107/',
        'E:/GDELT_DATA/new_csv_files/20200108/',
        'E:/GDELT_DATA/new_csv_files/20200109/',
        'E:/GDELT_DATA/new_csv_files/20200110/',
        'E:/GDELT_DATA/new_csv_files/20200111/',
        'E:/GDELT_DATA/new_csv_files/20200112/'
    ]
    week3 = [
        'E:/GDELT_DATA/new_csv_files/20200113/',
        'E:/GDELT_DATA/new_csv_files/20200114/',
        'E:/GDELT_DATA/new_csv_files/20200115/',
        'E:/GDELT_DATA/new_csv_files/20200116/',
        'E:/GDELT_DATA/new_csv_files/20200117/',
        'E:/GDELT_DATA/new_csv_files/20200118/',
        'E:/GDELT_DATA/new_csv_files/20200119/'
    ]
    week4 = [
        'E:/GDELT_DATA/new_csv_files/20200120/',
        'E:/GDELT_DATA/new_csv_files/20200121/',
        'E:/GDELT_DATA/new_csv_files/20200122/',
        'E:/GDELT_DATA/new_csv_files/20200123/',
        'E:/GDELT_DATA/new_csv_files/20200124/',
        'E:/GDELT_DATA/new_csv_files/20200125/',
        'E:/GDELT_DATA/new_csv_files/20200126/'
    ]
    week5 = [
        'E:/GDELT_DATA/new_csv_files/20200127/',
        'E:/GDELT_DATA/new_csv_files/20200128/',
        'E:/GDELT_DATA/new_csv_files/20200129/',
        'E:/GDELT_DATA/new_csv_files/20200130/',
        'E:/GDELT_DATA/new_csv_files/20200131/',
        'E:/GDELT_DATA/new_csv_files/20200201/',
        'E:/GDELT_DATA/new_csv_files/20200202/'
    ]  
    week6 = [
        'E:/GDELT_DATA/new_csv_files/20200203/',
        'E:/GDELT_DATA/new_csv_files/20200204/',
        'E:/GDELT_DATA/new_csv_files/20200205/',
        'E:/GDELT_DATA/new_csv_files/20200206/',
        'E:/GDELT_DATA/new_csv_files/20200207/',
        'E:/GDELT_DATA/new_csv_files/20200208/',
        'E:/GDELT_DATA/new_csv_files/20200209/'
    ]
    week7 = [
        'E:/GDELT_DATA/new_csv_files/20200210/',
        'E:/GDELT_DATA/new_csv_files/20200211/',
        'E:/GDELT_DATA/new_csv_files/20200212/',
        'E:/GDELT_DATA/new_csv_files/20200213/',
        'E:/GDELT_DATA/new_csv_files/20200214/',
        'E:/GDELT_DATA/new_csv_files/20200215/',
        'E:/GDELT_DATA/new_csv_files/20200216/'
    ]
    week8 = [
        'E:/GDELT_DATA/new_csv_files/20200217/',
        'E:/GDELT_DATA/new_csv_files/20200218/',
        'E:/GDELT_DATA/new_csv_files/20200219/',
        'E:/GDELT_DATA/new_csv_files/20200220/',
        'E:/GDELT_DATA/new_csv_files/20200221/',
        'E:/GDELT_DATA/new_csv_files/20200222/',
        'E:/GDELT_DATA/new_csv_files/20200223/'
    ]
    week9 = [
        'E:/GDELT_DATA/new_csv_files/20200224/',
        'E:/GDELT_DATA/new_csv_files/20200225/',
        'E:/GDELT_DATA/new_csv_files/20200226/',
        'E:/GDELT_DATA/new_csv_files/20200227/',
        'E:/GDELT_DATA/new_csv_files/20200228/',
        'E:/GDELT_DATA/new_csv_files/20200229/',
        'E:/GDELT_DATA/new_csv_files/20200301/'
    ]
    week10 = [
        'E:/GDELT_DATA/new_csv_files/20200302/',
        'E:/GDELT_DATA/new_csv_files/20200303/',
        'E:/GDELT_DATA/new_csv_files/20200304/',
        'E:/GDELT_DATA/new_csv_files/20200305/',
        'E:/GDELT_DATA/new_csv_files/20200306/',
        'E:/GDELT_DATA/new_csv_files/20200307/',
        'E:/GDELT_DATA/new_csv_files/20200308/',
    ]
    week11 = [
        'E:/GDELT_DATA/new_csv_files/20200309/',
        'E:/GDELT_DATA/new_csv_files/20200310/',
        'E:/GDELT_DATA/new_csv_files/20200311/',
        'E:/GDELT_DATA/new_csv_files/20200312/',
        'E:/GDELT_DATA/new_csv_files/20200313/',
        'E:/GDELT_DATA/new_csv_files/20200314/',
        'E:/GDELT_DATA/new_csv_files/20200315/'
    ]
    week12 = [
        'E:/GDELT_DATA/new_csv_files/20200316/',
        'E:/GDELT_DATA/new_csv_files/20200317/',
        'E:/GDELT_DATA/new_csv_files/20200318/',
        'E:/GDELT_DATA/new_csv_files/20200319/',
        'E:/GDELT_DATA/new_csv_files/20200320/',
        'E:/GDELT_DATA/new_csv_files/20200321/',
        'E:/GDELT_DATA/new_csv_files/20200322/'
    ]
    week13 = [
        'E:/GDELT_DATA/new_csv_files/20200323/',
        'E:/GDELT_DATA/new_csv_files/20200324/',
        'E:/GDELT_DATA/new_csv_files/20200325/',
        'E:/GDELT_DATA/new_csv_files/20200326/',
        'E:/GDELT_DATA/new_csv_files/20200327/',
        'E:/GDELT_DATA/new_csv_files/20200328/',
        'E:/GDELT_DATA/new_csv_files/20200329/'
    ]
    week14 = [
        'E:/GDELT_DATA/new_csv_files/20200330/',
        'E:/GDELT_DATA/new_csv_files/20200331/',
        'E:/GDELT_DATA/new_csv_files/20200401/',
        'E:/GDELT_DATA/new_csv_files/20200402/',
        'E:/GDELT_DATA/new_csv_files/20200403/',
        'E:/GDELT_DATA/new_csv_files/20200404/',
        'E:/GDELT_DATA/new_csv_files/20200405/'
    ]
    # 字典，存储要放入
    week_dict = {
        'week14' : week14 
        }

    for name, week in week_dict.items():
        csv_list = []
        for day in week:
            tmp = os.listdir(day)
            tmp = [day + x for x in tmp]
            csv_list.extend(tmp)

        for csv_file in tqdm(csv_list):
            # 读取本地CSV文件
            data = pd.read_csv(csv_file, sep='\t', index_col=0)
            data.columns = header

            # 将新建的DataFrame储存为MySQL中的数据表，不储存index列(index=False)
            # if_exists:
            # 1.fail:如果表存在，啥也不做
            # 2.replace:如果表存在，删了表，再建立一个新表，把数据插入
            # 3.append:如果表存在，把数据插入，如果表不存在创建一个表！！
            pd.io.sql.to_sql(data, name, con=engine, index=False, if_exists='append')
        
        print(name + 'finished!')