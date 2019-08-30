#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Config:
    logFile = ''

    @staticmethod
    def SetLogFile(logFileInfo):
        Config.logFile = logFileInfo