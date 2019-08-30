#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import time
import pymysql
import datetime
from config.config import Config

class Tools:

    @staticmethod
    def getTime():
        # nowTime = str(datetime.datetime.now())
        # nowTime = re.sub('[^0-9]', '_', nowTime)
        return datetime.datetime.now()

    @staticmethod
    def getData():
        return time.strftime('%Y-%m-%d', time.localtime())

    @staticmethod
    def writeFile(grade, outFile, info):
        if grade == 1:
            f = open(outFile, 'a+')
            f.write(info + '\n')
            f.close()
        elif grade == 2:
            f = open(outFile, 'w+')
            f.write(info + '\n')
            f.close()

    @staticmethod
    def printInfo(logFile, grade, info):
        if grade == 1:
            info = info
        elif grade == 2:
            info = "\033[0;31m%s\033[0m" % "Error: {0} : {1} : {2}".format(
                str(info),
                str(info.__traceback__.tb_frame.f_globals['__file__']),
                str(info.__traceback__.tb_lineno))
        elif grade == 3:
            info = "\033[0;31m%s\033[0m" % "Error: {0}".format(str(info))
        print(info)
        Tools.writeFile(1, logFile, str(Tools.getTime()) + ':' + str(info))

    @staticmethod
    def connect_db(func):
        def wrapper(args):

            dbConnect = pymysql.connect(
                host = args['host'],
                port = int(args['port']),
                user = args['user'],
                password = args['password'],
                database = args['database']
            )
            args['dbConnect'] = dbConnect

            output = func(args)

            dbConnect.close()

            return output
        return wrapper