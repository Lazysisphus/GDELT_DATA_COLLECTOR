'''
@Descripttion: 
@version: 
@Author: pigZhang
@Date: 2018-07-23 08:54:12
@LastEditors: Please set LastEditors
@LastEditTime: 2020-02-27 14:25:29
'''


import os
import datetime
import requests
import zipfile
from tqdm import tqdm


def get_url_list(start_date, end_date):
    url_list = []
    begin_date = datetime.datetime.strptime(start_date, "%Y%m%d%H%M")
    end_date = datetime.datetime.strptime(end_date, "%Y%m%d%H%M")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m%d%H%M%S")
        date_str = 'http://data.gdeltproject.org/gdeltv2/' + date_str + '.export.CSV.zip'
        url_list.append(date_str)
        begin_date += datetime.timedelta(minutes=15)
    return url_list


def download(zip_file_path, url_list):
    for url in tqdm(url_list):
        zip_doc = requests.get(url)
        zip_fname = zip_file_path + '/' + url[37:52] + 'zip'
        if os.path.exists(zip_fname):
            print(zip_fname + ' existed!')
        else:
            with open(zip_fname, "wb") as fp:
                fp.write(zip_doc.content)
    print('Downloaded!')


def un_zip(csv_file_path, zip_file_path):
    zip_names = os.listdir(zip_file_path)
    for name in zip_names:
        name = zip_file_path + '/' + name
        fz = zipfile.ZipFile(name, 'r')
        for name in fz.namelist():
            fz.extract(name, csv_file_path)
    print('Unzip!')


if __name__ == '__main__':
    date_list = []
    # 在此输入需要下载文件的开始、结束时间（是一个闭区间）
    begin_date = datetime.datetime.strptime('20200128', "%Y%m%d")
    end_date = datetime.datetime.strptime('20200220', "%Y%m%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)

    for date in date_list:
        begin_time = date + '0000'
        end_time = date + '2345'

        zip_file_path = './zip_file/' + date
        csv_file_path = './csv_file/' + date

        # create path
        if not os.path.exists(zip_file_path):
            os.makedirs(zip_file_path)
        if not os.path.exists(csv_file_path):
            os.makedirs(csv_file_path)

        # get URL list
        url_list = get_url_list(begin_time, end_time)

        # download zips
        download(zip_file_path, url_list)
        
        # unzip files
        un_zip(csv_file_path, zip_file_path)