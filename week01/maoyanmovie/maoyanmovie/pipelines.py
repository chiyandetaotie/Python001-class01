# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import os


DIC_INFO = {'电影名称': [], '电影类型': [], '上映时间': []}
file_path = 'scrapy_XPath_maoyan_top10.csv'


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        DIC_INFO['电影名称'] = [item['name']]
        DIC_INFO['电影类型'] = [item['genra']]
        DIC_INFO['上映时间'] = [item['release_date']]

        if file_path not in os.listdir():
            pd.DataFrame(DIC_INFO).to_csv(file_path,
                                          mode='a',
                                          index=False,
                                          encoding='utf-8-sig')
        else:
            pd.DataFrame(DIC_INFO).to_csv(file_path,
                                          mode='a',
                                          index=False,
                                          header=False,
                                          encoding='utf-8-sig')
        return item
