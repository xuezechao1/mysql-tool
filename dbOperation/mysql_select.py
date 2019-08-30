#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from tools.tools import Tools
from config.config import Config

class Select:

    @staticmethod
    @Tools.connect_db
    def select(runConfig):
        try:
            print(runConfig)
            cursor = runConfig['dbConnect'].cursor()

            cursor.execute(runConfig['sql'])

            # 获取结果字段名
            colList = []
            cols = cursor.description
            for col in cols:
                colList.append(col[0])

            # 获取结果信息
            resultDict = {}
            num = 1
            selectResult = cursor.fetchall()
            for row in selectResult:
                for i in range(0, len(colList)):
                    resultDict.setdefault(num, {})[colList[i]] = row[i]
                num += 1

            return resultDict

        except Exception as msg:
            Tools.printInfo(Config.logFile, 2, msg)
            return {}