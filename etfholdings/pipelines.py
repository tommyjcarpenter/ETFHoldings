# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from os import path

from scrapy.xlib.pydispatch import dispatcher
from scrapy import  signals

class EtfholdingsPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item

#this code is from https://github.com/feiskyer/scrapy-examples/blob/master/blog_crawl/blog_crawl/pipelines.py
class SQLiteStorePipeline(object):
    filename = 'data.sqlite'
 
    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
 
    def process_item(self, item, domain):
        try:
            self.conn.execute('insert into holdings values(?,?,?,?)', 
                          (item['fund'], item['symbol'], item['long_name'], item['percentage_allocation']))
        except:
            print('Failed to insert item: ' + item['url'])
        return item
 
    def initialize(self):
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)
 
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
 
    def create_table(self, filename):
        conn = sqlite3.connect(filename)
        conn.execute("""create table holdings
                     (fund text, symbol text primary key, long_name text, percentage_allocation text)""")
        conn.commit()
        return conn
