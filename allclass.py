#D:\anaconda\Scripts\activate.bat
from nghe import *
from noichonhe import  *
import os,io
import sqlite3
conn = sqlite3.connect('./datamayhoc.db')
c = conn.cursor()
class use_os_data:
    def __init__(self,listdir_s = ",".join(os.listdir())):
        self.listdir = listdir_s
        self.data_file = None
        self.create_file = None
        self.so = 0
        self.data_read_s = None
    def in_all_data(self):
        print(self.listdir)
