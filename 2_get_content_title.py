'''
@Descripttion: 
@version: 
@Author: pigZhang
@Date: 2019-07-20 20:27:12
@LastEditors: Please set LastEditors
@LastEditTime: 2020-02-27 14:06:37
'''

import os
import re
import argparse
import pandas as pd
from newspaper import Article
from tqdm import tqdm


def get_title_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
    except:
        title = 'None'
        content = 'None'
    else:
        title = article.title
        content = article.text
    return title, content


def produce_Newcsv(csv_file_path, new_file_path, csv_file):
    print('开始爬取文件：', csv_file)
    full_path = csv_file_path + csv_file
    df_org = pd.read_csv(full_path, header=None, sep='\t')
    url_list = df_org[60].tolist() # 获取csv文件的URL列表
    
    title_list = []
    content_list = []
    temp_save = {} # 暂时存储一个csv文件包含新闻的title、content
    count = 0 # 记录爬取率
    total_num = len(df_org)
    for url in tqdm(url_list):
        if url not in temp_save.keys():
            title, content = get_title_content(url)
            content = re.sub('\n\n', '\n', content)
            temp_save[url] = {'title' : title, 'content' : content}
        else:
            title = temp_save[url]['title']
            content = temp_save[url]['content']
        title_list.append(title)
        content_list.append(content)

        if content != 'None':
            count += 1
    success_rate = float(count) / total_num
    print('新闻原文的爬取成功率是：', success_rate)
    
    # 输出新的csv文件
    df_title = pd.DataFrame({'title' : title_list})
    df_content = pd.DataFrame({'content' : content_list})
    df = pd.concat([df_org, df_title, df_content], axis=1, join_axes=[df_org.index])
    df.to_csv(new_file_path + csv_file, sep='\t')


if __name__ == "__main__":
    # 在命令行中输入要爬取新闻标题和正文的日期
    # 如 nohup python get_content_title --date 20200101
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', default=None, type=str)
    args = parser.parse_args()

    csv_file_path = './csv_file/' + args.date + '/'
    new_file_path = './new_file/' + args.date + '/'

    # create path
    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)

    csv_list = os.listdir(csv_file_path)
    for csv_file in csv_list:
        produce_Newcsv(csv_file_path, new_file_path, csv_file)