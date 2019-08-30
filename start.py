#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
from tools.tools import Tools
from config.config import Config
from dbOperation.mysql_select import Select

logFile = os.path.dirname(os.path.abspath(__file__)) + '/log/' + Tools.getData() + '.log'
Config.SetLogFile(logFile)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--select", help="select", action="store_true")
        parser.add_argument("--update", help="update", action="store_true")
        parser.add_argument("--insert", help="insert", action="store_true")
        parser.add_argument("--delete", help="delete", action="store_true")
        parser.add_argument("--host", help="ip", type=str)
        parser.add_argument("--user", help="user", type=str)
        parser.add_argument("--database", help="db name", type=str)
        parser.add_argument("--password", help="password", type=str)
        parser.add_argument("--port", help="port", type=str)
        parser.add_argument("--sql", help="sql code", type=str)
        parser.add_argument("--outPath", help="out file Path", type=str)

        args = parser.parse_args()
        runConfig = args.__dict__

        if all(runConfig[i] is not None for i in ['host', 'user', 'database', 'password', 'port', 'sql']):
            if runConfig['select'] is True:
                result = Select.select(runConfig)
                runConfig.pop('dbConnect')
                if runConfig['outPath'] is not None:
                    Tools.writeFile(2, os.path.abspath(runConfig['outPath']), json.dumps(result))
                else:
                    Tools.printInfo(
                        Config.logFile,
                        1,
                        json.dumps(result, sort_keys=True, indent=4, separators=(', ', ': ')))
            elif runConfig['update'] is True:
                pass
            elif runConfig['insert'] is True:
                pass
            elif runConfig['delete'] is True:
                pass
        elif len(sys.argv) == 1:
            parser.print_help()
        else:
            Tools.printInfo(Config.logFile, 3, "mysql info is None")

    except Exception as msg:
        Tools.printInfo(Config.logFile, 2, msg)