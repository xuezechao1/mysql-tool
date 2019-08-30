1.0 mysql查询导出json工具
===
# 功能
## 1 查询功能
    可自定义mysql数据库，自定义sql语句，可指定输出结果文件
```
./start.py --select --host 10.208.255.64 --user iot_firmware --database iot_firmware --password 13d3bbfe08f11857 --port 13824 
--sql 'select f.firmware_name,f.firmware_id, m.manufacturer_name, d.device_name, d.device_type, d.model from fp_firmware f, fp_manufacturer m, fp_device d 
where f.manufacturer_id=m.manufacturer_id and f.device_id=d.device_id 
and f.firmware_id in (39790, 39792)' --outPath ../tmp.json
```