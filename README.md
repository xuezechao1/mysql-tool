1.0 mysql查询导出json工具
===
# 功能
## 1 查询功能
    可自定义mysql数据库，自定义sql语句，可指定输出结果文件
```
./start.py --select --host 10.208.255.64 --user iot_firmware --database iot_firmware --password 13d3bbfe08f11857 --port 13824 
--sql '[sql语句]' --outPath ../tmp.json
```
