

# API接口

## 1 登录

### 1.1 登出

##### 功能描述

对admin类型用户执行登出动作，登出后不能访问admin类型的资源。

##### 接口

http://mobile.router/api.cgi?path=account&method=logout

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明                  |
| ------ | ---- | --------------------- |
| result | 数字 | 0：成功<br>-1:   失败 |

##### 特别说明

登出后UI还可以访问SD卡资源

##### 示例

###### response

```json
{
    "result": 0
}
```



### 1.2 更新后端超时计数

##### 功能描述

更新后端超时计数，ui长时间不更新后端超时计数会导致admin类型用户登出。

##### 接口

http://mobile.router/api.cgi?path=account&method=reset_time

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明                  |
| ------ | ---- | --------------------- |
| result | 数字 | 0：成功<br>-1:   失败 |

##### 特别说明

使用该接口需要admin权限.还有另一种更新计数的方法，在请求头后面增加reset_time=1参数。

##### 示例

###### response

```json
{
    "result": 0
}
```



### 1.3 获取随机数

##### 功能描述

对admin或sdcard类型用户登入时随机数的获取。

##### 接口

http://mobile.router/api.cgi?path=account&method=get_rand

##### 请求参数

| 字段    | 类型   | 说明                                           |
| ------- | ------ | ---------------------------------------------- |
| type    | 字符串 | admin: admin用户登入<br>sdcard: sdcard用户登入 |
| user_id | 字符串 | 前端随机生成8字符的字符串                      |

##### 响应结果

| 字段   | 类型   | 说明                 |
| ------ | ------ | -------------------- |
| result | 数字   | 0：成功<br>4:   失败 |
| rand   | 字符串 | 8字符的随机字符串    |

##### 特别说明

get_rand接口和login接口按随机数在先，登录在后的顺序调用，请求参数的user_id为前端随机生成8字符的字符串，两接口下发的此参数请保证一致。

##### 示例

###### request

```json
{
	"type": "admin",
	"user_id": "abcdefgh"
}
```

###### response

```json
{
	"result": 0,
	"rand": "5qy1BdRJ"
}
```



### 1.4 登录

##### 功能描述

对admin和sdcard类型用户的登录用户名和密码验证。

##### 接口

http://mobile.router/api.cgi?path=account&method=login

##### 请求参数

| 字段     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| type     | 字符串 | admin: admin用户登入<br>sdcard: sdcard用户登入               |
| usrename | 字符串 | 用户名：默认admin<br>sdcard用户名：默认sdcard                |
| password | 字符串 | 密码：get_rand接口获取的随机数+“admin”后转换成的MD5码<br>sdcard密码：get_rand接口获取的随机数+“sdcard”后转换成的MD5码 |
| user_id  | 字符串 | 前端随机生成8字符的字符串                                    |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0：用户名和密码均不正确<br>1: 用户名正确但密码错误<br>2: 用户名错误但密码正确<br>3: 用户名和密码均正确，登陆成功<br>4: 随机数不正确<br>5: 随机数为空<br>6: 超过最大尝试登陆的次数 |

##### 特别说明

get_rand接口和login接口按随机数在先，登录在后的顺序调用，请求参数的user_id为前端随机生成8字符的字符串，两接口下发的此参数请保证一致。

##### 示例

###### request

```json
{
	"type": "admin",
    "username": "admin",
	"password": "f1d870370af1a0ffad793610905d61ba",
    "user_id": "abcdefgh"
}
```

###### 

###### response

```json
{
	"result": 3
}
```



### 1.5 获取登录信息

##### 功能描述

获取admin或sdcard类型用户的登录信息。

##### 接口

http://mobile.router/api.cgi?path=account&method=get_info

##### 请求参数

| 字段       | 类型   | 说明                                                   |
| ---------- | ------ | ------------------------------------------------------ |
| type       | 字符串 | admin: 获取admin用户信息<br>sdcard: 获取sdcard用户信息 |
| session_id | 字符串 | 当前获取到的session_id                                 |

##### 响应结果

| 字段           | 类型   | 说明                                     |
| -------------- | ------ | ---------------------------------------- |
| result         | 数字   | 0：成功<br>4:   失败                     |
| username       | 字符串 | 用户名                                   |
| password       | 字符串 | 密码                                     |
| modified       | 数字   | 0：未更改默认密码<br>1: 已更改过默认密码 |
| status         | 字符串 | login:登陆<br>logout：登出               |
| total_time     | 字符串 | 设置的自动登出的时间（时间单位：秒）     |
| remaining_time | 字符串 | 自动登出剩余时间（时间单位：秒）         |

##### 特别说明

无。

##### 示例

###### request

```json
{
	"type": "admin",
    "session_id": "fMHFD9n7lG6zHSpgdj9pjWBJ9vLAsyBGdjeSlBQEiOcSE"
}
```

###### 

###### response

```json
{
	"result": 0,
	"username": "admin",
	"password": "admin",
	"modified": 0,
	"status": "login",
	"total_time": "300",
	"remaining_time": "277"
}
```



### 1.6 设置登录信息

##### 功能描述

设置admin或sdcard类型用户的登录信息。

##### 接口

http://mobile.router/api.cgi?path=account&method=set_info

##### 请求参数

| 字段       | 类型   | 说明                                                   |
| ---------- | ------ | ------------------------------------------------------ |
| type       | 字符串 | admin: 获取admin用户信息<br>sdcard: 获取sdcard用户信息 |
| username   | 字符串 | 设置用户名                                             |
| password   | 字符串 | 设置密码                                               |
| total_time | 字符串 | 设置自动登出的时间                                     |

##### 响应结果

| 字段   | 类型 | 说明                 |
| ------ | ---- | -------------------- |
| result | 数字 | 0：成功<br>4:   失败 |

##### 特别说明

无。

##### 示例

###### request

```json
{
    "type":"admin",
 	"username":"admin",
 	"password":"admin",
 	"total_time":"300"
}
```

###### 

###### response

```json
{
	"result": 0
}
```

### 1.7 获取登陆剩余尝试次数和超出次数的锁定时间

##### 功能描述

获取登陆剩余尝试次数和超出次数的锁定时间。

##### 接口

http://mobile.router/api.cgi?path=account&method=get_retrytimes_and_time

##### 请求参数

| 字段 | 类型   | 说明                                                   |
| ---- | ------ | ------------------------------------------------------ |
| type | 字符串 | admin: 获取admin用户信息<br>sdcard: 获取sdcard用户信息 |

##### 响应结果

| 字段        | 类型 | 说明                                                         |
| ----------- | ---- | ------------------------------------------------------------ |
| result      | 数字 | 0：成功<br>4:   失败                                         |
| retry_times | 数字 | 登陆验证失败时，剩余的尝试登陆次数                           |
| remain_time | 数字 | 登陆锁定后的剩余时间，时间清零后可继续尝试登陆（时间单位：秒） |

##### 特别说明

无。

##### 示例

###### request

```json
{
    "type":"admin"
}
```

###### 

###### response

```json
{
	"result": 0,
	"retry_times": 5,
	"remain_time": 0
}
```



### 1.8 单独获取登录状态

##### 功能描述

单独获取admin登录状态。

##### 接口

http://mobile.router/api.cgi?path=account&method=get_login_status

##### 请求参数

| 字段       | 类型   | 说明                                          |
| ---------- | ------ | --------------------------------------------- |
| session_id | 字符串 | web拿到的session值，如果拿不到session值则传空 |

##### 响应结果

| 字段         | 类型 | 说明                     |
| ------------ | ---- | ------------------------ |
| result       | 数字 | 0：成功<br>4:   失败     |
| login_status | 数字 | 0：未登录<br>1:   已登录 |

##### 特别说明

无。

##### 示例

###### request

```json
{
        "session_id":"fMHFD9n7lG6zHSpgdj9pjWBJ9vLAsyBGdjeSlBQEiOcSE"
}
```

###### response

```json
{
	"result": 0,
	"login_status": 1
}
```





## 2 状态

### 2.1 用户列表

#### 2.1.1 get_conn_clients_info

##### 功能描述

获取连接到设备的客户端信息，包括MAC，IP，名字，类型

##### 接口

http://mobile.router/api.cgi?path=statistics&method=get_conn_clients_info

##### 请求参数

无

##### 响应结果

| 字段         | 类型 | 说明                         |
| ------------ | ---- | ---------------------------- |
| clients_info | 数组 | 数组元素为对象，详细定义见后 |

###### clients_info元素对象

| 字段          | 类型   | 说明                             |
| ------------- | ------ | -------------------------------- |
| mac           | 字符串 | MAC地址                          |
| ip            | 字符串 | IP地址                           |
| name          | 字符串 | 名字                             |
| type          | 字符串 | 类型，USB或WIFI                  |
| cur_conn_time | 字符串 | 当前连接时长，单位秒，目前未使用 |

##### 特别说明

cur_conn_time目前没有使用

##### 示例

###### response

```json
{
    "clients_info": [
        {
            "mac": "C2:0C:99:52:5D:3B",
            "ip": "192.168.8.165",
            "name": "Truman",
            "type": "USB",
            "cur_conn_time": "77885"
        }
    ]
}
```

### 2.2 流量统计

#### 2.2.1 获取设备流量消耗和联网时间

##### 功能描述

获取设备本次开机后访问网络的时间及上下行流量和设备访问网络的总时间及总上下行流量

##### 接口

http://mobile.router/api.cgi?path=statistics&method=stat_get_common_data

##### 请求参数

无

##### 响应结果

| 字段              | 类型 | 说明                          |
| :---------------- | ---- | ----------------------------- |
| duration          | 数字 | 本次开机联网时间（单位：秒）  |
| total_duration    | 数字 | 设备总联网时间（单位：秒）    |
| rx_bytes          | 数字 | 下行流量 （单位：bytes）      |
| tx_bytes          | 数字 | 上行流量（单位：bytes）       |
| rx_tx_bytes       | 数字 | 上下行总流量（单位：bytes）   |
| error_bytes       | 数字 | 错误流量（单位：bytes）       |
| total_rx_bytes    | 数字 | 总下行流量（单位：bytes）     |
| total_tx_bytes    | 数字 | 总上行流量（单位：bytes）     |
| total_rx_tx_bytes | 数字 | 总上下行总流量（单位：bytes） |
| total_error_bytes | 数字 | 总错误流量（单位：bytes）     |

##### 特别说明

无

##### 示例

###### response

```json
{
    "statistics": {
        "duration": 157,
        "total_duration": 157,
        "rx_bytes": 226468,
        "tx_bytes": 79744,
        "rx_tx_bytes": 306212,
        "error_bytes": 0,
        "total_rx_bytes": 226468,
        "total_tx_bytes": 79744,
        "total_rx_tx_bytes": 306212,
        "total_error_bytes": 0
    }
}
```

#### 2.2.2 清除设备流量消耗和联网时间

##### 功能描述

清除设备本次开机后访问网络的时间及上下行流量和设备访问网络的总时间及总上下行流量

##### 接口

http://mobile.router/api.cgi?path=statistics&method=stat_clear_common_data

##### 请求参数

无

##### 响应结果

| 字段             | 类型   | 说明                                    |
| :--------------- | ------ | --------------------------------------- |
| setting_response | 字符串 | “OK”代表清除成功    “ERROR”代表清除失败 |

##### 特别说明

无

##### 示例

###### response

```json
{
	"statistics": {
		"setting_response": "OK"
	}
}
```

### 2.3 流量使用状态

#### 2.3.1 获取设备流量上行和下行状态

##### 功能描述

获取设备当前流量的上行和下行状态

##### 接口

http://mobile.router/api.cgi?path=statistics&method=stat_get_traffic_transport_status

##### 请求参数

无

##### 响应结果

| 字段      | 类型 | 说明                                   |
| :-------- | ---- | -------------------------------------- |
| tx_status | 数字 | 为0代表无上行流量；大于0代表有上行流量 |
| rx_status | 数字 | 为0代表无下行流量；大于0代表有下行流量 |

##### 特别说明

无

##### 示例

###### response

```json
{
	"traffic_transport_status": {
		"tx_status": 48,
		"rx_status": 98
	}
}
```

### 2.4 电池信息

#### 2.4.1 get_bat_info

##### 功能描述

获取电池信息

##### 接口

http://mobile.router/api.cgi?path=aoc&method=get_bat_info

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| capacity | 数字 | 电量百分比，0~100                                            |
| status   | 数字 | 0：电池不在位<br>1：充电中<br>2：未在充电中<br>4：已充满<br> |
| ind      | 数字 | 1/2/3为电量格数                                              |

##### 特别说明

无

##### 示例

###### response

```json
{
    "capacity": 100,
    "status": 2,
    "ind": 3
}
```

### 2.5 wifi基本信息

#### 2.5.1 wifi_get_basic_info

##### 功能描述

获取wifi基本信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_get_basic_info

##### 请求参数

| 字段    | 类型   | 说明                      |
| ------- | ------ | ------------------------- |
| sw_only | 字符串 | 为”1“，仅获取wifi开关状态 |

##### 响应结果

| 字段   | 类型   | 说明                |
| ------ | ------ | ------------------- |
| switch | 字符串 | ”on“为开，”off“为关 |

##### 特别说明

目前此结果仅用于获取wifi开关状态，即sw_only为”1“

##### 示例

###### request

```json
{
    "sw_only": "1"
}
```

###### response

```json
{
    "switch": "on"
}
```

### 2.6 版本信息

#### 2.6.1 get_ww_version

##### 功能描述

获取版本信息

##### 接口

http://mobile.router/api.cgi?path=version&method=get_ww_version

##### 请求参数

无

##### 响应结果

| 字段   | 类型   | 说明                         |
| ------ | ------ | ---------------------------- |
| result | 数字   | 0为成功，非0为失败           |
| sw_ver | 字符串 | 软件版本号，result为0时有效  |
| hw_ver | 字符串 | 硬件版本号，result为0时有效  |
| ww_ver | 字符串 | webui版本号，result为0时有效 |
| ow_ver | 字符串 | 内核版本号，result为0时有效  |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
	"sw_ver": "Mobile.Router.B01",
	"hw_ver": "Mobile.Router.H01",
	"ww_ver": "Mobile.Router.W01",
	"ow_ver": "Linux version 3.10.33"
}
```

### 2.7 设备信息

#### 2.7.1 get_feature_list

##### 功能描述

获取设备支持的功能列表

##### 接口

http://mobile.router/api.cgi?path=router&method=get_feature_list

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明                                        |
| -------- | ---- | ------------------------------------------- |
| result   | 数字 | 0为成功，非0为失败                          |
| features | 对象 | 设备功能信息，详细定义见后，result为0时有效 |

###### features对象

| 字段          | 类型   | 说明                        |
| ------------- | ------ | --------------------------- |
| device_type   | 字符串 | mifi，wingle，dongle，cpe等 |
| sdcard        | 数字   | 0为不支持，1为支持          |
| ussd          | 数字   | 0为不支持，1为支持          |
| sms           | 数字   | 0为不支持，1为支持          |
| phonebook     | 数字   | 0为不支持，1为支持          |
| wifi_extender | 数字   | 0为不支持，1为支持          |
| wds           | 数字   | 0为不支持，1为支持          |
| wps           | 数字   | 0为不支持，1为支持          |
| local_update  | 数字   | 0为不支持，1为支持          |

##### 特别说明

所有产品都支持的功能不用放在里边

##### 示例

###### response

```json
{
    "result": 0,
    "features": {
        "device_type": "mifi",
        "sdcard": 1,
        "ussd": 0,
        "sms": 1,
        "phonebook": 1,
        "wifi_extender": 1,
        "wds": 0,
        "wps": 1,
        "local_update": 1
    }
}
```

#### 2.7.2 get_mac_info

##### 功能描述

获取设备MAC地址信息

##### 接口

http://mobile.router/api.cgi?path=router&method=get_mac_info

##### 请求参数

无

##### 响应结果

| 字段      | 类型   | 说明                                |
| --------- | ------ | ----------------------------------- |
| result    | 数字   | 0为成功，非0为失败                  |
| wifi_mac  | 字符串 | wifi的MAC地址，result为0时有效      |
| rndis_mac | 字符串 | 可选，rndis主机MAC，result为0时有效 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
    "wifi_mac": "00:c7:7f:e4:77:77",
    "rndis_mac": "fc:de:56:ff:01:06"
}
```

#### 2.7.3 get_device_info

##### 功能描述

获取设备信息

##### 接口

http://mobile.router/api.cgi?path=router&method=get_device_info

##### 请求参数

无

##### 响应结果

| 字段   | 类型   | 说明                    |
| ------ | ------ | ----------------------- |
| result | 数字   | 0为成功，非0为失败      |
| sn     | 字符串 | 序列号，result为0时有效 |
| IMEI   | 字符串 | IMEI                    |
| IMSI   | 字符串 | IMSI                    |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
    "sn": "0123456789",
    "IMEI": "352099001761481",
    "IMSI": "460019894025417"
}
```

## 3 连接管理

### 3.1 连接管理

#### 3.1.1 connect

##### 功能描述

建立连接

##### 接口

http://mobile.router/api.cgi?path=cm&method=connect

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明               |
| :----- | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0
}
```

#### 3.1.2 disconnect

##### 功能描述

断开连接

##### 接口

http://mobile.router/api.cgi?path=cm&method=disconnect

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明               |
| :----- | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0
}
```

### 3.2 连接信息

#### 3.2.1 get_link_context

##### 功能描述

##### 接口

http://mobile.router/api.cgi?path=cm&method=get_link_context

##### 请求参数

无

##### 响应结果

| 字段               | 类型 | 说明                           |
| :----------------- | ---- | ------------------------------ |
| celluar_basic_info | 对象 | 蜂窝网络基本信息，详细定义见后 |
| signal_info        | 对象 | 蜂窝信号强度信息，详细定义见后 |
| contextlist        | 数组 | 数组元素为对象，详细定义见后   |

###### celluar_basic_info对象

| 字段                 | 类型   | 说明                                                         |
| :------------------- | ------ | ------------------------------------------------------------ |
| sys_mode             | 数字   | 0: 无服务<br>1: 2G/3G<br>2: LTE<br>3: LTEP                   |
| data_mode            | 数字   | 定义如下：<br>RADIO_TECH_UNKNOWN = 0,<br/>RADIO_TECH_GPRS = 1,<br/>RADIO_TECH_EDGE = 2,<br/>RADIO_TECH_UMTS = 3,<br/>RADIO_TECH_IS95A = 4,<br/>RADIO_TECH_IS95B = 5,<br/>RADIO_TECH_1xRTT =  6,<br/>RADIO_TECH_EVDO_0 = 7,<br/>RADIO_TECH_EVDO_A = 8,<br/>RADIO_TECH_HSDPA = 9,<br/>RADIO_TECH_HSUPA = 10,<br/>RADIO_TECH_HSPA = 11,<br/>RADIO_TECH_EVDO_B = 12,<br/>RADIO_TECH_EHRPD = 13,<br/>RADIO_TECH_LTE = 14,<br/>RADIO_TECH_HSPAP = 15, // HSPA+<br/>RADIO_TECH_GSM = 16, // Only supports voice<br/>RADIO_TECH_TD_SCDMA = 17,<br/>RADIO_TECH_IWLAN = 18,<br/>RADIO_TECH_LTEP = 19,<br/>RADIO_TECH_DC_HSPA = 20 |
| IMEI                 | 字符串 | IMEI                                                         |
| IMSI                 | 字符串 | IMSI                                                         |
| network_name         | 字符串 | 网络名称                                                     |
| roaming_network_name | 字符串 | 漫游网络名称                                                 |
| roaming              | 数字   | 0：普通   1：漫游                                            |

###### signal_info对象

| 字段  | 类型   | 说明                   |
| ----- | ------ | ---------------------- |
| rat   | 字符串 | 无线接入技术，4g/3g/2g/no service |
| level | 数字   | 信号格数，0~5          |

###### contextlist元素对象

| 字段              | 类型   | 说明                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| connection_status | 数字   | 连接状态<br>#define CM_CONNECT_DISCON				0<br/>#define CM_CONNECT_CONSUCCESS			1<br/>#define CM_CONNECT_CONNING				2<br/>#define CM_CONNECT_REDIAL				3<br/>#define CM_CONNECT_DIAL_IMMEDIATELY  	4<br/>#define CM_CONNECT_ROAM                        	5<br/>#define CM_CONNECT_WAIT_NWCHANGE		6<br/>#define CM_CONNECT_GET_GLOBALIP_ERR 	7<br/>#define CM_CONNECT_DEACTIVATED   8<br/>#define CM_CONNECT_WAIT_PS_ATTACH   9 |
| ipv4_ip           | 字符串 | ipv4地址                                                     |
| ipv4_dns1         | 字符串 | ipv4 dns1地址                                                |
| ipv4_dns2         | 字符串 | ipv4 dns2地址                                                |
| ipv6_ip           | 字符串 | ipv6地址                                                     |
| ipv6_dns1         | 字符串 | ipv6 dns1地址                                                |
| ipv6_dns2         | 字符串 | ipv6 dns2地址                                                |

##### 特别说明

##### 示例

###### response

```json
{
    "celluar_basic_info": {
        "sys_mode": 1,
        "data_mode": 15,
        "IMEI": "352099001761481",
        "IMSI": "460016427527520",
        "network_name": "UNICOM",
        "roaming_network_name": "UNICOM",
        "roaming": 0
    },
    "signal_info": {
        "rat": "3g",
        "level": 5
    },
    "contextlist": [
        {
            "connection_status": 1,
            "ipv4_ip": "10.147.246.136",
            "ipv4_dns1": "120.80.80.80",
            "ipv4_dns2": "221.5.88.88",
            "ipv4_gateway": "10.147.246.136",
            "ipv4_submask": "255.255.255.255"
        }
    ]
}
```

## 4 电话本

### 4.1 组管理

#### 4.1.1 query_group

##### 功能描述

查询电话本组信息

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=query_group

##### 请求参数

无

##### 响应结果

| 字段      | 类型 | 说明                                              |
| --------- | ---- | ------------------------------------------------- |
| result    | 数字 | 0为成功，非0为失败                                |
| grouplist | 数组 | 数组元素为对象，result为0的时候有效，详细定义见后 |

###### grouplist元素对象

| 字段         | 类型   | 说明                                        |
| ------------ | ------ | ------------------------------------------- |
| index        | 数字   | 0~10的整数，其中0表示"未分组"，1~10为组索引 |
| valid        | 数字   | 为1表示有效；为0表示无效                    |
| name         | 字符串 | 组的名称，只有valid为1时才有                |
| contactcount | 数字   | 组内联系人数量，只有valid为1时才有          |

##### 特别说明

索引为0的组表示"未分组"

##### 示例

###### response

```json
{
    "result": 0,
    "grouplist": [
        {
            "index": 0,
            "valid": 1,
            "name": "",
            "contactcount": 0
        },
        {
            "index": 1,
            "valid": 0
        },
        {
            "index": 2,
            "valid": 1,
            "name": "Group 1",
            "contactcount": 5
        },
        {
            "index": 3,
            "valid": 1,
            "name": "Group 2",
            "contactcount": 0
        },
        {
            "index": 4,
            "valid": 0
        },
        {
            "index": 5,
            "valid": 0
        },
        {
            "index": 6,
            "valid": 0
        },
        {
            "index": 7,
            "valid": 0
        },
        {
            "index": 8,
            "valid": 0
        },
        {
            "index": 9,
            "valid": 0
        },
        {
            "index": 10,
            "valid": 0
        }
    ]
}
```

#### 4.1.2 addnew_group

##### 功能描述

在电话本中添加新的组

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=addnew_group

##### 请求参数

| 字段 | 类型   | 说明 |
| ---- | ------ | ---- |
| name | 字符串 | 组名 |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0为成功，非0为失败<br>典型错误值：<br/>-2：文件错误<br/>-5：参数错误<br/>-9：名称太长<br/>-100：组已存在<br/>-102：组数量超过限制 |
| index  | 数字 | 组索引，result为0的时候有效                                  |

##### 特别说明

无

##### 示例

###### request

```json
{
        "name": "g3"
}
```

###### response

```json
{
        "result": 0,
        "index": 1
}
```

#### 4.1.3 delete_group

##### 功能描述

从电话本中删除组

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=delete_group

##### 请求参数

| 字段  | 类型   | 说明           |
| ----- | ------ | -------------- |
| index | 字符串 | 要删除的组索引 |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0为成功，非0为失败<br>典型错误值<br>-2：文件错误<br>-5：参数错误<br>-101：组不存在 |
| index  | 数字 | 组索引号，result为0的时候有效                                |

##### 特别说明

索引为0的组，不允许删除

##### 示例

###### request

```json
{
        "index":"10"
}
```

###### response

```json
{
        "result": 0,
        "index": 10
}
```

#### 4.1.4 update_group

##### 功能描述

更新电话本中的组的名称

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=update_group

##### 请求参数

| 字段  | 类型   | 说明   |
| ----- | ------ | ------ |
| index | 字符串 | 组索引 |
| name  | 字符串 | 新名称 |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0为成功，非0为失败<br>典型错误值<br>-2：文件错误<br/>-5：参数错误<br/>-9：名称太长<br/>-101：组不存在 |

##### 特别说明

索引为0的组，不允许更新

##### 示例

###### request

```json
{
        "index":"3",
        "name":"gg3"
}
```

###### response

```json
{
        "result": 0,
        "index": 3
}
```

### 4.2 联系人管理

#### 4.2.1 addnew_pb

##### 功能描述

添加联系人

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=addnew_pb

##### 请求参数

| 字段      | 类型 | 说明         |
| --------- | ---- | ------------ |
| addnew_pb | 对象 | 详细定义见后 |

###### addnew_pb对象

| 字段     | 类型   | 说明                                    |
| -------- | ------ | --------------------------------------- |
| location | 字符串 | 储存位置，0：device                     |
| name     | 字符串 | 联系人名称，需要编码（UniEncode，见后） |
| mobile   | 字符串 | 联系人号码                              |
| group    | 字符串 | 联系人分组编号                          |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0为成功，非0为失败<br>典型错误值：<br>-1：失败<br>-2：文件错误<br>-5：参数错误<br>-10：名称为空<br>-11：名称太长<br>-12：号码太长<br>-14：空间已满 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "addnew_pb": {
        "location": "0",
        "name": "004a00610063006b",
        "mobile": "12345678901",
        "group": "1"
    }
}
```

###### response

```json
{
    "result": 0
}
```

#### 4.2.2 delete_pb

##### 功能描述

删除联系人，可以一次删除多个联系人

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=delete_pb

##### 请求参数

| 字段      | 类型 | 说明         |
| --------- | ---- | ------------ |
| delete_pb | 对象 | 详细定义见后 |

###### delete_pb对象

| 字段       | 类型   | 说明                    |
| ---------- | ------ | ----------------------- |
| location   | 字符串 | 储存位置，0：device     |
| count      | 字符串 | 数量                    |
| indexarray | 字符串 | 联系人索引号，以`,`分隔 |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0为成功，非0为失败<br>典型错误值：<br>-1：失败<br>-2：文件错误<br>-5：参数错误 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "delete_pb": {
        "location": "0",
        "count": "2",
        "indexarray": "0,1,"
    }
}
```

###### response

```json
{
    "result": 0
}
```

#### 4.2.3 update_pb

##### 功能描述

更新联系人信息

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=update_pb

##### 请求参数

| 字段      | 类型 | 说明         |
| --------- | ---- | ------------ |
| update_pb | 对象 | 详细定义见后 |

###### update_pb对象

| 字段     | 类型   | 说明                                    |
| -------- | ------ | --------------------------------------- |
| location | 字符串 | 储存位置，0：device                     |
| index    | 字符串 | 联系人索引                              |
| name     | 字符串 | 联系人名称，需要编码（UniEncode，见后） |
| mobile   | 字符串 | 联系人号码                              |
| group    | 字符串 | 联系人分组编号                          |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0为成功，非0为失败<br/>典型错误值：<br/>-1：失败<br/>-2：文件错误<br/>-5：参数错误<br/>-10：名称为空<br/>-11：名称太长<br/>-12：号码太长<br/>-14：空间已满 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "update_pb": {
        "location": "0",
        "index": "0",
        "name": "004a00610063006b",
        "mobile": "12345678901",
        "group": "0"
    }
}
```

###### response

```json
{
    "result": 0
}
```

#### 4.2.4 getcontactbylocation

##### 功能描述

按存储位置获取联系人信息，支持分页

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=getcontactbylocation

##### 请求参数

| 字段                 | 类型 | 说明         |
| -------------------- | ---- | ------------ |
| getcontactbylocation | 对象 | 详细定义如下 |

###### getcontactbylocation对象

| 字段      | 类型   | 说明                |
| --------- | ------ | ------------------- |
| pagecap   | 字符串 | 每页联系人数量      |
| pageindex | 字符串 | 页索引号，从0开始   |
| location  | 字符串 | 储存位置，0：device |

##### 响应结果

| 字段         | 类型 | 说明                         |
| ------------ | ---- | ---------------------------- |
| contactcount | 数字 | 联系人数量                   |
| contactlist  | 数组 | 数组元素为对象，详细定义见后 |

###### contactlist元素对象

| 字段     | 类型   | 说明                |
| -------- | ------ | ------------------- |
| location | 数字   | 储存位置，0：device |
| index    | 数字   | 联系人索引          |
| name     | 字符串 | 联系人名称          |
| mobile   | 字符串 | 联系人号码          |
| group    | 数字   | 联系人分组编号      |

##### 特别说明

无

##### 示例

###### request

```json
{
    "getcontactbylocation": {
        "pagecap": "100",
        "pageindex": "0",
        "location": "0"
    }
}
```

###### response

```json
{
    "contactcount": 3,
    "contactlist": [
        {
            "location": 0,
            "index": 0,
            "name": "004a00610063006b",
            "mobile": "12345678901",
            "group": 0
        },
        {
            "location": 0,
            "index": 1,
            "name": "00750034",
            "mobile": "123",
            "group": 2
        },
        {
            "location": 0,
            "index": 2,
            "name": "00750035",
            "mobile": "123",
            "group": 3
        }
    ]
}
```

#### 4.2.5 getcontactbygroup

##### 功能描述

按分组获取联系人信息，支持分页

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=getcontactbygroup

##### 请求参数

| 字段              | 类型 | 说明         |
| ----------------- | ---- | ------------ |
| getcontactbygroup | 对象 | 详细定义见后 |

###### getcontactbygroup对象

| 字段      | 类型   | 说明              |
| --------- | ------ | ----------------- |
| pagecap   | 字符串 | 每页联系人数量    |
| pageindex | 字符串 | 页索引号，从0开始 |
| group     | 字符串 | 联系人分组编号    |

##### 响应结果

| 字段         | 类型 | 说明                         |
| ------------ | ---- | ---------------------------- |
| contactcount | 数字 | 联系人数量                   |
| contactlist  | 数组 | 数组元素为对象，详细定义见后 |

###### contactlist元素对象

| 字段     | 类型   | 说明                |
| -------- | ------ | ------------------- |
| location | 数字   | 储存位置，0：device |
| index    | 数字   | 联系人索引          |
| name     | 字符串 | 联系人名称          |
| mobile   | 字符串 | 联系人号码          |
| group    | 数字   | 联系人分组编号      |

##### 特别说明

无

##### 示例

###### request

```json
{
    "getcontactbygroup": {
        "pagecap": "100",
        "pageindex": "0",
        "group": "2"
    }
}
```

###### response

```json
{
    "contactcount": 3,
    "contactlist": [
        {
            "location": 0,
            "index": 1,
            "name": "00750034",
            "mobile": "123",
            "group": 2
        },
        {
            "location": 0,
            "index": 3,
            "name": "00750075",
            "mobile": "345",
            "group": 2
        },
        {
            "location": 0,
            "index": 4,
            "name": "0075007500750075",
            "mobile": "234234234",
            "group": 2
        }
    ]
}
```



#### 4.2.6 move_contacts_to_group

##### 功能描述

将联系人移至分组，可以一次移动多个联系人

##### 接口

http://mobile.router/api.cgi?path=phonebook&method=move_contacts_to_group

##### 请求参数

| 字段     | 类型   | 说明                        |
| -------- | ------ | --------------------------- |
| newgroup | 字符串 | 目标分组索引                |
| contacts | 字符串 | 联系人索引号，多个以`,`分隔 |

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | 数字 | 0为成功，非0为失败<br>典型错误值<br>-1：失败<br>-2：文件错误<br>-5：参数错误<br>-101：分组不存在 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "newgroup": "1",
    "contacts": "1,3,4"
}
```

###### response

```json
{
    "result": 0
}
```

## 5 短消息

### 5.1 查询

#### 5.1.1 sms.list_by_type

##### 功能描述

根据类型，按页查询短消息详细信息

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms.list_by_type

##### 请求参数

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段       | 类型   | 说明                              |
| ---------- | ------ | --------------------------------- |
| list_type  | 字符串 | 0：INBOX<br>1：OUTBOX<br>2：DRAFT |
| page_index | 字符串 | 页号，从1开始                     |

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段       | 类型   | 说明                 |
| ---------- | ------ | -------------------- |
| resp       | 字符串 | 0为成功，非0为失败   |
| count      | 字符串 | 当前页内短消息数量   |
| total      | 字符串 | 指定类型短消息总数量 |
| page_count | 字符串 | 指定类型短消息页数   |
| node_list  | 对象   | 详细定义见后         |

###### node_list对象

| 字段 | 类型 | 说明                                      |
| ---- | ---- | ----------------------------------------- |
| s[n] | 对象 | 本页内第n条短消息，n为1到10，详细定义见后 |

###### s[n]对象

| 字段     | 类型   | 说明                                |
| -------- | ------ | ----------------------------------- |
| id       | 字符串 | 短消息编号                          |
| address  | 字符串 | 号码                                |
| date     | 字符串 | 时间                                |
| protocol | 字符串 | 协议                                |
| type     | 字符串 | 0：INBOX<br/>1：OUTBOX<br/>2：DRAFT |
| read     | 字符串 | 0：unread<br>1：read                |
| status   | 字符串 | 0为成功，1为失败                    |
| location | 字符串 | 0为设备                             |
| body     | 字符串 | 经过编码的短消息内容                |

##### 特别说明

无

##### 示例

###### request

```json
{
    "sms": {
        "page_index": "1",
        "list_type": "0"
    }
}
```

###### response

```json
{
    "sms": {
        "resp": "0",
        "count": "6",
        "total": "6",
        "page_count": "1",
        "node_list": {
            "s1": {
                "id": "505",
                "address": "1001001260",
                "contact_id": "0",
                "date": "21,11,24,09,15,39,+8",
                "protocol": "0",
                "type": "0",
                "read": "1",
                "status": "0",
                "location": "0",
                "body": "30108d345fc3670d52a1518d53477ea70020975e51e14f539a8c57288eab8fb930115c0a656c76845ba26237ff0c611f8c224f7f75284e2d56fd8054901a4e1a"
            },
            "s2": {
                "id": "504",
                "address": "1065599799",
                "contact_id": "0",
                "date": "21,11,21,10,55,59,+8",
                "protocol": "0",
                "type": "0",
                "read": "1",
                "status": "0",
                "location": "0",
                "body": "30106d3b52a853c24e0e901a77e5301160a85df283b75f974e004e2a5fae4fe173b091d17ea25305ff0c965065f6965091cf798f5229ff0c70b951fb00200068"
            },
            "s3": {
                "id": "503",
                "address": "10010",
                "contact_id": "0",
                "date": "21,11,20,10,15,59,+8",
                "protocol": "0",
                "type": "0",
                "read": "1",
                "status": "0",
                "location": "0",
                "body": "6df157335e025e9460257ba174065c4030015e026c148c615c4063d0919260a8ff1a53d75f3a51b77a7a6c145f7154cdff0c0032003265e551cc66688d776211"
            },
            "s4": {
                "id": "502",
                "address": "10010",
                "contact_id": "0",
                "date": "21,11,17,10,36,38,+8",
                "protocol": "0",
                "type": "0",
                "read": "1",
                "status": "0",
                "location": "0",
                "body": "5c0a656c768475286237ff0c622a6b62523000320030003200315e740031003167080031003765e5000d000a0020672c67085df24f7f75286d4191cfff084e0d"
            },
            "s5": {
                "id": "501",
                "address": "10010",
                "contact_id": "0",
                "date": "21,11,16,10,24,23,+8",
                "protocol": "0",
                "type": "0",
                "read": "1",
                "status": "0",
                "location": "0",
                "body": "5c0a656c768475286237ff0c622a6b62523000320030003200315e740031003167080031003665e5000d000a0020672c67085df24f7f75286d4191cfff084e0d"
            },
            "s6": {
                "id": "500",
                "address": "10010",
                "contact_id": "0",
                "date": "21,11,16,10,24,11,+8",
                "protocol": "0",
                "type": "0",
                "read": "1",
                "status": "0",
                "location": "0",
                "body": "5c0a656c768475286237ff0c8bf756de590d4ee54e0b7f167801529e74064e1a52a1ff1a000d000a0020003500390039ff1a67e58be275ab60c5000d000a0020"
            }
        }
    }
}
```

#### 5.1.2 sms.query

##### 功能描述

查询符合条件的短消息编号列表

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms.query

##### 请求参数

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段     | 类型   | 说明                                |
| -------- | ------ | ----------------------------------- |
| type     | 字符串 | 0：INBOX<br/>1：OUTBOX<br/>2：DRAFT |
| read     | 字符串 | 0为未读，1为已读，2为未读及已读     |
| location | 字符串 | 0为设备                             |

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段 | 类型   | 说明                  |
| ---- | ------ | --------------------- |
| resp | 字符串 | 0未成功，非0为失败    |
| ids  | 字符串 | 短消息编号，以`,`分隔 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "sms": {
        "type": "0",
        "read": "2",
        "location": "0"
    }
}
```

###### response

```json
{
    "sms": {
        "resp": "0",
        "ids": "505,504,503,502,501,500"
    }
}
```

#### 5.1.3 sms.get_by_id

##### 功能描述

根据编号获取短消息详细信息

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms.get_by_id

##### 请求参数

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段 | 类型   | 说明       |
| ---- | ------ | ---------- |
| id   | 字符串 | 短消息编号 |

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段     | 类型   | 说明                                |
| -------- | ------ | ----------------------------------- |
| resp     | 字符串 | 0为成功，非0为失败                  |
| id       | 字符串 | 短消息编号                          |
| address  | 字符串 | 号码                                |
| date     | 字符串 | 时间                                |
| protocol | 字符串 | 协议                                |
| type     | 字符串 | 0：INBOX<br/>1：OUTBOX<br/>2：DRAFT |
| read     | 字符串 | 0：unread<br>1：read                |
| status   | 字符串 | 0为成功，1为失败                    |
| location | 字符串 | 0为设备                             |
| body     | 字符串 | 经过编码的短消息内容                |

##### 特别说明

未读会变为已读

##### 示例

###### request

```json
{
    "sms": {
        "id": "505"
    }
}
```

###### response

```json
{
    "sms": {
        "resp": "0",
        "id": "505",
        "address": "1001001260",
        "contact_id": "0",
        "date": "21,11,24,09,15,39,+8",
        "protocol": "0",
        "type": "0",
        "read": "1",
        "status": "0",
        "location": "0",
        "body": "30108d345fc3670d52a1518d53477ea70020975e51e14f539a8c57288eab8fb930115c0a656c76845ba26237ff0c611f8c224f7f75284e2d56fd8054901a4e1a52a1ff0c8bf775280031003052300031520676844efb610f4e004e2a657465708bc44ef762114eec76840020624b673a7f517edc0020ff0c003100304e3a975e5e386ee1610fff0c00314e3a975e5e384e0d6ee1610f3002ff0856de590d514d8d39ff09000a"
    }
}
```

#### 5.1.4 sms.get_brief_info

##### 功能描述

获取短消息基本信息

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms.get_brief_info

##### 请求参数

无

##### 响应结果

| 字段          | 类型 | 说明                                 |
| ------------- | ---- | ------------------------------------ |
| new_num       | 数字 | 新短信数量，调用一次后自动清0        |
| unread_num    | 数字 | 未读短信数量                         |
| memory_full   | 数字 | 0为未满；1为满，即短信总条数达到上限 |
| flash_msg_ids | 数组 | 数组元素为数字，flash短信的id        |

##### 特别说明

新短信数目，用于通知用户，调用一次后自动清0

##### 示例

###### response

```json
{
        "new_num": 0,
        "unread_num": 9,
        "memory_full": 1,
        "flash_msg_ids": [
                19,
                4
        ]
}
```



#### 5.1.5 sms_import_from_sim_to_device

##### 功能描述

将SIM卡中的短信导入到设备中

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms_import_from_sim_to_device

##### 请求参数

无

##### 响应结果

| 字段                 | 类型 | 说明                                                         |
| -------------------- | ---- | ------------------------------------------------------------ |
| resp                 | 数字 | 0：导入成功 <br>1:从SIM卡获取短信失败 <br>2:设备的剩余空间不足 <br>3:未知原因<br>4:SIM卡无短信 |
| sim_unbroken_sms_num | 数字 | SIM卡中整条短信数量，不是分段短信数量                        |
| success              | 数字 | 从SIM卡导入短信到设备成功的条数                              |
| fail                 | 数字 | 从SIM卡导入短信到设备失败的条数                              |
| del_num              | 数字 | 从SIM卡导入短信到设备，设备存储空间不够时，提示要删除设备短信数量 |

##### 特别说明



##### 示例

###### response

```json
{
        "resp": 0,
        "sim_unbroken_sms_num": 7,
        "success": 7,
        "fail": 0
}


```

### 5.2 编辑

#### 5.2.1 sms.delete

##### 功能描述

删除指定编号的短消息

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms.delete

##### 请求参数

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段 | 类型   | 说明       |
| ---- | ------ | ---------- |
| id   | 字符串 | 短消息编号 |

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段 | 类型   | 说明               |
| ---- | ------ | ------------------ |
| resp | 字符串 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "sms": {
        "id": "503"
    }
}
```

###### response

```json
{
    "sms": {
        "resp": "0"
    }
}
```

#### 5.2.2 sms.save

##### 功能描述

新建或者编辑已有短消息后保存，可以是群发短消息

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms.save

##### 请求参数

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段     | 类型   | 说明                           |
| -------- | ------ | ------------------------------ |
| id       | 字符串 | -1为新建，其他为编辑已有短消息 |
| gsm7     | 字符串 | 1为gsm7，0为非gsm7             |
| address  | 字符串 | 1到5个号码，每个号码以`,`结束  |
| body     | 字符串 | 编码后的短消息内容             |
| date     | 字符串 | 时间                           |
| type     | 字符串 | 2：DRAFT                       |
| protocol | 字符串 | 协议                           |

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段        | 类型   | 说明               |
| ----------- | ------ | ------------------ |
| resp        | 字符串 | 0为成功，非0为失败 |
| smsSaveSucc | 字符串 | 保存成功条数       |
| smsSaveFail | 字符串 | 保存失败条数       |

##### 特别说明

多个收件人会保存为多条

##### 示例

###### request

```json
{
    "sms": {
        "id": "24",
        "gsm7": "1",
        "address": "18620351080,10010,10011,",
        "body": "0074006500730074",
        "date": "21,11,24,15,37,45,%2B8",
        "type": "2",
        "protocol": "0"
    }
}
```

###### response

```json
{
    "sms": {
        "resp": "0",
        "smsid": "27",
        "smsSaveSucc": "3",
        "smsSaveFail": "0"
    }
}
```

### 5.3 发送

#### 5.3.1 sms.send

##### 功能描述

发送短消息

##### 接口

http://mobile.router/api.cgi?path=sms&method=sms.send

##### 请求参数

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段     | 类型   | 说明                           |
| -------- | ------ | ------------------------------ |
| id       | 字符串 | -1为新建，其他为编辑已有短消息 |
| gsm7     | 字符串 | 1为gsm7，0为非gsm7             |
| address  | 字符串 | 1到5个号码，每个号码以`,`结束  |
| body     | 字符串 | 编码后的短消息内容             |
| date     | 字符串 | 时间                           |
| protocol | 字符串 | 协议                           |

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| sms  | 对象 | 详细定义见后 |

###### sms对象

| 字段        | 类型   | 说明               |
| ----------- | ------ | ------------------ |
| resp        | 字符串 | 0为成功，非0为失败 |
| smsSendSucc | 字符串 | 发送成功条数       |
| smsSendFail | 字符串 | 发送失败条数       |

##### 特别说明

多个收件人会保存为多条

##### 示例

###### request

```json
{
    "sms": {
        "id": "-1",
        "gsm7": "1",
        "address": "17688890470,18620351080,",
        "body": "00740077006f",
        "date": "21,11,24,16,12,18,%2B8",
        "protocol": "0"
    }
}
```

###### response

```json
{
    "sms": {
        "resp": "0",
        "smsid": "32",
        "smsRef": "69",
        "smsSendSucc": "2",
        "smsSendFail": "0"
    }
}
```

## 6 固件升级

### 6.1 在线升级

#### 6.1.1 new_query

##### 功能描述

检查新版本，及详细信息

##### 接口

http://mobile.router/api.cgi?path=ota&method=new_query

##### 请求参数

| 字段 | 类型   | 说明                                                |
| ---- | ------ | --------------------------------------------------- |
| type | 字符串 | 可选，有此字段且为1表示查询详细信息，否则只查询状态 |

##### 响应结果

| 字段         | 类型   | 说明                                                         |
| ------------ | ------ | ------------------------------------------------------------ |
| response     | 字符串 | 固件升级状态，包括`idle`：空闲<br>`checking`：检测新版本中<br/>`checked`：检测到新版本<br/>`updating,local`：本地升级中<br/>`updating,auto_fota`：在线自动升级中<br/>`updating,manual_fota`：在线手动升级中<br/>`success`：下载成功但此时未重启升级<br/>`failed`：失败 |
| release_note | 字符串 | 新固件版本说明。请求中type为1，并且response为checked时有效   |
| version      | 字符串 | 新固件版本号。请求中type为1，并且response为checked时有效     |
| date         | 字符串 | 新固件发布时间。请求中type为1，并且response为checked时有效   |
| size         | 字符串 | 新固件大小，单位为字节。请求中type为1，并且response为checked时有效 |
| progress     | 字符串 | fota进度百分比。请求中type为1，并且response为`updating,manual_fota`时有效 |

##### 特别说明

不同的状态下，详细信息包含的内容不同

查询到状态为success，调用router_call_reboot重启设备

此接口也用于本地升级

##### 示例

###### request

```json
{
    "type": "1"
}
```

###### response

```json
{
    "release_note": "1)Please update your device to enjoy new user interface for better experience.",
    "version": "Mobile.Router.B01",
    "date": "2020-05-07T15:00:10.000Z",
    "size": "11386880",
    "response": "checked"
}
```

#### 6.1.2 manual_check_update

##### 功能描述

手动检查更新

##### 接口

http://mobile.router/api.cgi?path=ota&method=manual_check_update

##### 请求参数

无

##### 响应结果

| 字段   | 类型   | 说明               |
| ------ | ------ | ------------------ |
| result | 字符串 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": "0"
}
```

#### 6.1.3 abandon_checked

##### 功能描述

丢弃检查结果

##### 接口

http://mobile.router/api.cgi?path=ota&method=abandon_checked

##### 请求参数

无

##### 响应结果

| 字段     | 类型   | 说明                                       |
| -------- | ------ | ------------------------------------------ |
| result   | 字符串 | 0为成功，非0为失败                         |
| response | 字符串 | 失败原因，如`not checked`，result非0时有效 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": "-1",
    "response": "not checked"
}
```

#### 6.1.4 download_update

##### 功能描述

下载新固件

##### 接口

http://mobile.router/api.cgi?path=ota&method=download_update

##### 请求参数

无

##### 响应结果

| 字段     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| result   | 字符串 | 0为成功，非0为失败，-1为未检测到新版本 ，-2为电量低于45%不允许下载升级 |
| response | 字符串 | 失败原因，如`not checked`，result非0时有效                   |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": "-1",
    "response": "not checked"
}
```

###### 或

###### response

```json
{
    "result": "-2",
    "response": "battery low power"
}
```





#### 6.1.5 abandon_download_update

##### 功能描述

取消下载

##### 接口

http://mobile.router/api.cgi?path=ota&method=abandon_download_update

##### 请求参数

无

##### 响应结果

| 字段     | 类型   | 说明                                        |
| -------- | ------ | ------------------------------------------- |
| result   | 字符串 | 0为成功，非0为失败                          |
| response | 字符串 | 失败原因，如`not updating`，result非0时有效 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": "-1",
    "response": "not updating"
}
```

#### 6.1.6 clear_failed_state

##### 功能描述

清除失败状态

##### 接口

http://mobile.router/api.cgi?path=ota&method=clear_failed_state

##### 请求参数

无

##### 响应结果

| 字段     | 类型   | 说明                                      |
| -------- | ------ | ----------------------------------------- |
| result   | 字符串 | 0为成功，非0为失败                        |
| response | 字符串 | 失败原因，如`not failed`，result非0时有效 |

##### 特别说明

失败后，调用此接口回到idle状态

此接口也用于本地升级

##### 示例

###### response

```json
{
    "result": "-1",
    "response": "not failed"
}
```



#### 6.1.7 get_updated_status

##### 功能描述

获取当前是否为版本升级后的状态

##### 接口

http://mobile.router/api.cgi?path=ota&method=get_updated_status

##### 请求参数

无

##### 响应结果

| 字段                     | 类型   | 说明                                             |
| ------------------------ | ------ | ------------------------------------------------ |
| result                   | 数字   | 0为获取成功，非0为失败                           |
| fota_auto_upgrade_status | 字符串 | “0”：当前未升级新版本；  “1”：当前升级新版本成功 |

##### 特别说明

此接口进入webUI时调用，如果字段fota_auto_upgrade_status为“1”，说明是升级重启之后的新版本状态，弹窗提示用户已经升级到新版本。弹窗上客户点击确定时，调用6.1.8的接口（http://mobile.router/api.cgi?path=ota&method=clear_updated_status）,清除升级到了新版本的状态标志。

##### 示例

###### response

```json
{
    "result": 0,
    "fota_auto_upgrade_status": "1"
}
```



#### 6.1.8 clear_updated_status

##### 功能描述

清除升级到新版本标志

##### 接口

http://mobile.router/api.cgi?path=ota&method=clear_updated_status

##### 请求参数

| 字段           | 类型   | 说明                |
| -------------- | ------ | ------------------- |
| updated_status | 字符串 | "0"：清除新版本标志 |

##### 响应结果

| 字段   | 类型 | 说明                   |
| ------ | ---- | ---------------------- |
| result | 数字 | 0为获取成功，非0为失败 |

##### 特别说明

调用此接口请求字段updated_status始终为“0”。

##### 示例

###### request

```json
{
   "updated_status":"0"
}
```



###### response

```json
{
    "result": "0",
}
```





### 6.2 本地升级

本地升级使用的ota new_query，router_call_reboot，clear_failed_state，定义和在线升级一样

#### 6.2.1 上传固件

##### 功能描述

将固件上传到设备，可以分多个包上传

##### 接口

http://mobile.router/file.cgi?Action=Upload&file=upgrade

##### 请求参数

| http头       | 取值                                                         | 说明                                                   |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| Content-Type | application/octet-stream, 11386880<br>application/octet-stream | 第一个包携带文件大小，单位字节；后续包不能携带文件大小 |

##### 响应结果

http状态码为200 OK为成功，否则为失败

##### 特殊说明

接口调用者计算并展示进度

##### 示例

N/A

## 7 SIM卡

### 7.1 状态

#### 7.1.1 get_sim_status

##### 功能描述

获取SIM卡状态信息

##### 接口

http://mobile.router/api.cgi?path=sim&method=get_sim_status

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| pin_puk  | 对象 | 详细定义见后 |
| response | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段         | 类型 | 说明                                                         |
| ------------ | ---- | ------------------------------------------------------------ |
| sim_status   | 数字 | 0：卡不在位<br>1：卡在位<br>2：错误                          |
| pin_status   | 数字 | 0：未知<br>2：需要PIN<br/>3：需要PUK<br/>4:   Invalid SIM  无效SIM卡<br/>5：READY |
| pin_attempts | 数字 | PIN剩余次数                                                  |
| puk_attempts | 数字 | PUK剩余次数                                                  |
| pin_enabled  | 数字 | PIN使能                                                      |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

##### 示例

###### response

```json
{
    "pin_puk": {
        "sim_status": 1,
        "pin_status": 5,
        "pin_attempts": 3,
        "puk_attempts": 10,
        "mep_sim_attempts": 10,
        "mep_nw_attempts": 10,
        "mep_subnw_attempts": 10,
        "mep_sp_attempts": 10,
        "mep_corp_attempts": 10,
        "pin_enabled": 0,
        "pn_status": 1,
        "pu_status": 4,
        "pp_status": 7,
        "pc_status": 10,
        "ps_status": 13
    },
    "response": {
        "setting_response": "OK"
    }
}
```

### 7.2 PIN & PUK

#### 7.2.1 provide_pin

##### 功能描述

提供PIN

##### 接口

http://mobile.router/api.cgi?path=sim&method=provide_pin

##### 请求参数

| 字段    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pin_puk | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段 | 类型   | 说明  |
| ---- | ------ | ----- |
| pin  | 字符串 | PIN码 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| pin_puk  | 对象 | 详细定义见后 |
| response | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段         | 类型 | 说明        |
| ------------ | ---- | ----------- |
| pin_attempts | 数字 | PIN剩余次数 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

是否输入PIN错误，需要根据剩余次数判断

##### 示例

###### request

```json
{
    "pin_puk": {
        "pin": "1233"
    }
}
```

###### response

```json
{
    "pin_puk": {
        "pin_attempts": 2
    },
    "response": {
        "setting_response": "OK"
    }
}
```

#### 7.2.2 enable_pin

##### 功能描述

使能PIN

##### 接口

http://mobile.router/api.cgi?path=sim&method=enable_pin

##### 请求参数

| 字段    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pin_puk | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段 | 类型   | 说明  |
| ---- | ------ | ----- |
| pin  | 字符串 | PIN码 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| pin_puk  | 对象 | 详细定义见后 |
| response | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段         | 类型 | 说明        |
| ------------ | ---- | ----------- |
| pin_attempts | 数字 | PIN剩余次数 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

是否输入PIN错误，需要根据剩余次数判断

##### 示例

###### response

```json
{
    "pin_puk": {
        "pin": "1234"
    }
}
```

###### response

```json
{
    "pin_puk": {
        "pin_attempts": 3
    },
    "response": {
        "setting_response": "OK"
    }
}
```

#### 7.2.3 disable_pin

##### 功能描述

禁用PIN

##### 接口

http://mobile.router/api.cgi?path=sim&method=disable_pin

##### 请求参数

| 字段    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pin_puk | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段 | 类型   | 说明  |
| ---- | ------ | ----- |
| pin  | 字符串 | PIN码 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| pin_puk  | 对象 | 详细定义见后 |
| response | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段         | 类型 | 说明        |
| ------------ | ---- | ----------- |
| pin_attempts | 数字 | PIN剩余次数 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

是否输入PIN错误，需要根据剩余次数判断

##### 示例

###### request

```json
{
    "pin_puk": {
        "pin": "1233"
    }
}
```

###### response

```json
{
    "pin_puk": {
        "pin_attempts": 2
    },
    "response": {
        "setting_response": "OK"
    }
}
```

#### 7.2.4 change_pin 

##### 功能描述

修改PIN码

##### 接口

http://mobile.router/api.cgi?path=sim&method=change_pin

##### 请求参数

| 字段    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pin_puk | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段    | 类型   | 说明    |
| ------- | ------ | ------- |
| pin     | 字符串 | PIN码   |
| new_pin | 字符串 | 新PIN码 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| pin_puk  | 对象 | 详细定义见后 |
| response | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段         | 类型 | 说明        |
| ------------ | ---- | ----------- |
| pin_attempts | 数字 | PIN剩余次数 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

是否输入PIN错误，需要根据剩余次数判断

##### 示例

###### request

```json
{
    "pin_puk": {
        "pin": "1234",
        "new_pin": "1233"
    }
}
```

###### response

```json
{
    "pin_puk": {
        "pin_attempts": 3
    },
    "response": {
        "setting_response": "OK"
    }
}
```

#### 7.2.5 reset_pin_using_puk

##### 功能描述

使用PUK重置PIN

##### 接口

http://mobile.router/api.cgi?path=sim&method=reset_pin_using_puk

##### 请求参数

| 字段    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pin_puk | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段    | 类型   | 说明    |
| ------- | ------ | ------- |
| puk     | 字符串 | PUK码   |
| new_pin | 字符串 | 新PIN码 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| pin_puk  | 对象 | 详细定义见后 |
| response | 对象 | 详细定义见后 |

###### pin_puk对象

| 字段         | 类型 | 说明        |
| ------------ | ---- | ----------- |
| puk_attempts | 数字 | PUK剩余次数 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

##### 示例

###### request

```json
{
    "pin_puk": {
        "puk": "12345678",
        "new_pin": "1234"
    }
}
```

###### response

```json
{
    "pin_puk": {
        "puk_attempts": 9
    },
    "response": {
        "setting_response": "OK"
    }
}
```

#### 7.2.6 获取电话号码get_phone_no

##### 功能描述

获取电话号码

##### 接口

http://mobile.router/api.cgi?path=router&method=get_phone_no

##### 请求参数

无

##### 响应结果

| 字段     | 类型   | 说明                                                     |
| -------- | ------ | -------------------------------------------------------- |
| result   | 数字   | 0：获取成功<br>1：获取成功但sim卡里没号码<br>4：执行失败 |
| phone_no | 字符串 | 获得的电话号码                                           |



##### 特别说明

无

##### 示例

###### response

```json
{
	"result": 0,
	"phone_no": "+8618681227035"
}
```



#### 7.2.7 获取电话号码ww_get_phone_no  （Mobilink M403使用）

##### 功能描述

获取电话号码

##### 接口

http://mobile.router/api.cgi?path=ussd&method=ww_get_phone_no

##### 请求参数

无

##### 响应结果

| 字段     | 类型   | 说明                         |
| -------- | ------ | ---------------------------- |
| result   | 数字   | 0：获取成功<br>非0：获取失败 |
| phone_no | 字符串 | 获得的电话号码               |

##### 特别说明

该接口调用会通过ussd发送*99#，如果获取到结果立即返回，获取不到结果显示为unknown。

##### 示例

###### response

```json
{
	"result": 0,
	"phone_no": "923237972175"
}
```



## 8 SD卡

### 8.1 卡操作

#### 8.1.1 status

##### 功能描述

获取SD卡状态

##### 接口

http://mobile.router/api.cgi?path=sdcard&method=status

##### 请求参数

无

##### 响应结果

| 字段   | 类型   | 说明                                                         |
| ------ | ------ | ------------------------------------------------------------ |
| status | 字符串 | not present：卡不在位<br>not mount：卡在位但未挂载<br>mount：卡已挂载 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "status": "mount"
}
```

#### 8.1.2 format

##### 功能描述

格式化SD卡

##### 接口

http://mobile.router/api.cgi?path=sdcard&method=format

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 0    | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0
}
```

#### 8.1.3 capacity

##### 功能描述

获取SD卡容量

##### 接口

http://mobile.router/api.cgi?path=sdcard&method=capacity

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明       |
| -------- | ---- | ---------- |
| capacity | 数字 | 单位MBytes |

##### 特别说明

结果展示为2的整数次幂GB

##### 示例

###### response

```json
{
    "capacity": 7439
}
```

#### 8.1.4 free

##### 功能描述

获取SD卡剩余容量

##### 接口

http://mobile.router/api.cgi?path=sdcard&method=free

##### 请求参数

无

##### 响应结果

| 字段 | 类型 | 说明       |
| ---- | ---- | ---------- |
| free | 数字 | 单位MBytes |

##### 特别说明

无

##### 示例

###### response

```json
{
    "free": 7423
}
```

#### 8.1.5 set_sd_mode

##### 功能描述

设置SD卡模式

##### 接口

http://mobile.router/api.cgi?path=sdcard&method=set_sd_mode

##### 请求参数

| 字段 | 类型   | 说明                                            |
| ---- | ------ | ----------------------------------------------- |
| mode | 字符串 | 0：wifi存储<br/>1：本地存储<br/>2：internet存储 |

##### 响应结果

| 字段   | 类型 | 说明                |
| ------ | ---- | ------------------- |
| result | 数字 | 0为成功， 非0为失败 |

##### 特别说明

修改模式需要重启设备才能生效

##### 示例

###### request

```json
{
    "mode": "1"
}
```

###### response

```json
{
    "result": 0
}
```

#### 8.1.6 sd_mode

##### 功能描述

获取SD卡模式

##### 接口

http://mobile.router/api.cgi?path=sdcard&method=sd_mode

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明                                          |
| ------ | ---- | --------------------------------------------- |
| result | 数字 | 0：wifi存储<br>1：本地存储<br>2：internet存储 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0
}
```

### 8.2 内容操作

webdav扩展

## 9 设置

### 9.1 wifi设置

#### 9.1.1 wifi_get_detail（将要过期）

##### 功能描述

获取wifi详细参数

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_get_detail

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段         | 类型 | 说明         |
| ------------ | ---- | ------------ |
| wireless_num | 数字 | wifi设备数量 |
| AP0          | 对象 | 详细定义见后 |

###### APx对象

| 字段        | 类型 | 说明         |
| ----------- | ---- | ------------ |
| wifi_if_24G | 对象 | 详细定义见后 |

###### wifi_if_24G对象

| 字段          | 类型   | 说明         |
| ------------- | ------ | ------------ |
| switch        | 字符串 | on/off       |
| net_mode      | 字符串 |              |
| bandwidth     | 字符串 |              |
| channel       | 字符串 |              |
| first_channel | 字符串 |              |
| last_channel  | 字符串 |              |
| n_ssid        | 数字   |              |
| ssid0         | 对象   | 详细定义见后 |

###### ssid0对象

| 字段            | 类型   | 说明       |
| --------------- | ------ | ---------- |
| ssid            | 字符串 | SSID       |
| hidden          | 字符串 |            |
| isolate         | 字符串 |            |
| maxassoc        | 字符串 | 最大连接数 |
| encryption      | 字符串 | 加密方式   |
| key             | 字符串 | 密码       |
| wpa_group_rekey | 字符串 |            |

##### 特别说明

此接口将要过期，使用wifi_get_ap_config替代

##### 示例

###### response

```json
{
    "wireless": {
        "wireless_num": 1,
        "AP0": {
            "wifi_if_24G": {
                "switch": "on",
                "net_mode": "11ng",
                "bandwidth": "HT40",
                "channel": "0",
                "first_channel": "1",
                "last_channel": "13",
                "n_ssid": 1,
                "ssid0": {
                    "ssid": "ww-c77fe47777cf15e3",
                    "hidden": "0",
                    "isolate": "0",
                    "maxassoc": "10",
                    "encryption": "mixed-psk",
                    "key": "12345678",
                    "wpa_group_rekey": "600"
                }
            }
        }
    }
}
```

#### 9.1.2 wifi_set_2.4g（将要过期）

##### 功能描述

设置2.4g wifi参数

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_set_2.4g

##### 请求参数

| 字段        | 类型   | 说明         |
| ----------- | ------ | ------------ |
| wifi_device | 字符串 | 设备索引号   |
| wifi_if_24G | 对象   | 详细定义见后 |

###### wifi_if_24G对象

| 字段       | 类型   | 说明       |
| ---------- | ------ | ---------- |
| ssid       | 字符串 | SSID       |
| channel    | 字符串 | wifi信道   |
| encryption | 字符串 | 加密方式   |
| switch     | 字符串 | 开关       |
| hidden     | 字符串 |            |
| net_mode   | 字符串 |            |
| bandwidth  | 字符串 | 带宽       |
| maxassoc   | 字符串 | 最大连接数 |
| key        | 字符串 | 密码       |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

此接口将要过期，使用wifi_set_ap_config替代

##### 示例

###### request

```json
{
    "wifi_device": "0",
    "wifi_if_24G": {
        "ssid": "Openwrt_SSV_2G#f065",
        "channel": "11",
        "encryption": "mixed-psk",
        "switch": "on",
        "hidden": "0",
        "net_mode": "11ng",
        "bandwidth": "HT40",
        "maxassoc": "10",
        "key": "12345678"
    }
}
```

###### response

```json
{
    "wireless": {
        "setting_response": "OK"
    }
}
```

#### 9.1.3 wifi_get_ap_config

##### 功能描述

获取wifi热点配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_get_ap_config

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明                                            |
| ------ | ---- | ----------------------------------------------- |
| result | 数字 | 0为成功，非0为失败                              |
| config | 对象 | wifi热点配置参数，详细定义见后，result为0时有效 |

###### config对象

| 字段          | 类型   | 说明                                                         |
| ------------- | ------ | ------------------------------------------------------------ |
| switch        | 字符串 | on为打开，off为关闭                                          |
| maxassoc      | 字符串 | 最大连接数                                                   |
| mode          | 字符串 | 工作模式，`2.4G`，`5G`，`GUEST`，`DUAL`这几项的组合，空格分开 |
| wifi_if_24G   | 对象   | 可选，2.4G配置参数，详细定义见后，mode包含2.4G时有效         |
| wifi_if_5G    | 对象   | 可选，5G配置参数，详细定义见后，mode包含5G时有效             |
| wifi_if_DUAL  | 对象   | 可选，双频合一配置参数，详细定义见后，mode包含DUAL时有效     |
| wifi_if_GUEST | 对象   | 可选，访客wifi配置参数，详细定义见后，mode包含GUEST时有效    |

###### wifi_if_24G对象

| 字段          | 类型   | 说明                                 |
| ------------- | ------ | ------------------------------------ |
| net_mode      | 字符串 | 硬件模式，如11ng，具体取值和芯片有关 |
| bandwidth     | 字符串 | 带宽，如HT40，详细定义见后           |
| channel       | 字符串 | 0为自动，1~13为wifi信道号            |
| first_channel | 字符串 | 第一个wifi信道号                     |
| last_channel  | 字符串 | 最后一个wifi信道号                   |
| ssid          | 字符串 | SSID                                 |
| hidden        | 字符串 | 0为开启广播，1为关闭广播             |
| isolate       | 字符串 | 0为关闭isolate，1为打开isolate       |
| encryption    | 字符串 | 加密方式，详细定义见后               |
| key           | 字符串 | 密码                                 |

###### bandwidth

```
HT20 High Throughput 20MHz, 802.11n
HT40 High Throughput 40MHz, 802.11n
HT40- High Throughput 40MHz, 802.11n, control channel is below extension channel.
HT40+ High Throughput 40MHz, 802.11n, control channel is above extension channel.
VHT20 Very High Throughput 20MHz, Supported by 802.11ac
VHT40 Very High Throughput 40MHz, Supported by 802.11ac
VHT80 Very High Throughput 80MHz, Supported by 802.11ac
VHT160 Very High Throughput 160MHz, Supported by 802.11ac
NOHT disables 11n
```

###### encryption

| value          | Security Mode     | WPA Option    | 说明           |
| -------------- | ----------------- | ------------- | -------------- |
| psk            | WPA-PSK           | TKIP          |                |
| psk+ccmp       | WPA-PSK           | AES-CCMP      |                |
| psk+tkip+ccmp  | WPA-PSK           | TKIP/AES-CCMP |                |
| psk2           | WPA2-PSK          | AES-CCMP      |                |
| psk2+tkip+ccmp | WPA2-PSK          | TKIP/AES-CCMP |                |
| mixed-psk+aes  | WPA/WPA2-PSK      | AES-CCMP      |                |
| mixed-psk      | WPA/WPA2-PSK      | TKIP/AES-CCMP |                |
| wep+shared     | WEP               |               |                |
| none           | NONE              |               |                |
| sae            | WPA3-SAE          |               | 支持wpa3才有效 |
| sae-mixed      | WPA2-PSK/WPA3-SAE |               | 支持wpa3才有效 |

###### wifi_if_5G对象

| 字段         | 类型   | 说明                                            |
| ------------ | ------ | ----------------------------------------------- |
| net_mode     | 字符串 | 硬件模式，如11ng，具体取值和芯片有关            |
| bandwidth    | 字符串 | 带宽，如HT40，详细定义见后                      |
| channel      | 字符串 | 0为自动，36-165为wifi 5G信道号                  |
| channel_list | 对象   | 支持的信道列表，详细定义见后                    |
| ssid         | 字符串 | SSID                                            |
| hidden       | 字符串 | 0为开启广播，1为关闭广播                        |
| isolate      | 字符串 | 0为关闭isolate，1为打开isolate                  |
| encryption   | 字符串 | 加密方式，详细定义同wifi_if_24G对象的encryption |
| key          | 字符串 | 密码                                            |

channel_list数组元素

| 字段          | 类型   | 说明               |
| ------------- | ------ | ------------------ |
| dfs           | 字符串 | 信道号，以空格分隔 |
| non_dfs       | 字符串 | 信道号，以空格分隔 |
| indoor        | 字符串 | 信道号，以空格分隔 |
| indoor_or_dfs | 字符串 | 信道号，以空格分隔 |

###### wifi_if_DUAL对象

| 字段       | 类型   | 说明                                            |
| ---------- | ------ | ----------------------------------------------- |
| ssid       | 字符串 | SSID                                            |
| hidden     | 字符串 | 0为开启广播，1为关闭广播                        |
| encryption | 字符串 | 加密方式，详细定义同wifi_if_24G对象的encryption |
| key        | 字符串 | 密码                                            |

###### wifi_if_GUEST对象

| 字段       | 类型   | 说明                                            |
| ---------- | ------ | ----------------------------------------------- |
| maxassoc   | 字符串 | guest热点最大连接数                             |
| ssid       | 字符串 | SSID                                            |
| hidden     | 字符串 | 0为开启广播，1为关闭广播                        |
| isolate    | 字符串 | 0为关闭isolate，1为打开isolate                  |
| encryption | 字符串 | 加密方式，详细定义同wifi_if_24G对象的encryption |
| key        | 字符串 | 密码                                            |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
    "config": {
        "switch": "on",
        "maxassoc": "10",
        "mode": "2.4G 5G GUEST DUAL",
        "wifi_if_24G": {
            "net_mode": "11ng",
            "bandwidth": "HT40",
            "channel": "11",
            "first_channel": "1",
            "last_channel": "11",
            "ssid": "Openwrt_SSV_2G#f065",
            "hidden": "0",
            "isolate": "0",
            "encryption": "mixed-psk",
            "key": "12345678",
        },
        "wifi_if_5G": {
            "net_mode": "11a",
            "bandwidth": "HT20",
            "channel": "36",
            "channel_list": {
                "dfs": "52 56",
                "non_dfs": "36 40",
                "indoor": "60",
                "indoor_or_dfs": "68"
            },
            "ssid": "Openwrt_SSV_5G",
            "hidden": "0",
            "isolate": "0",
            "encryption": "psk2",
            "key": "12345678",
        },
        "wifi_if_DUAL": {
            "ssid": "Openwrt_SSV_2G#f065",
            "hidden": "0",
            "encryption": "mixed-psk",
            "key": "12345678",
        },
        "wifi_if_GUEST": {
            "maxassoc": "10",
            "ssid": "Openwrt_SSV_5G",
            "hidden": "0",
            "isolate": "0",
            "encryption": "psk2",
            "key": "12345678",
        }
    }
}
```

#### 9.1.4 wifi_set_ap_config

##### 功能描述

设置wifi热点配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_set_ap_config

##### 请求参数

| 字段          | 类型   | 说明                                                         |
| ------------- | ------ | ------------------------------------------------------------ |
| switch        | 字符串 | on为打开，off为关闭                                          |
| maxassoc      | 字符串 | 最大连接数                                                   |
| mode          | 字符串 | 工作模式，`2.4G`，`5G`，`GUEST`，`DUAL`这几项的组合，空格分开 |
| wifi_if_24G   | 对象   | 可选，2.4G配置参数，详细定义见后，mode包含2.4G时有效         |
| wifi_if_5G    | 对象   | 可选，5G配置参数，详细定义见后，mode包含5G时有效             |
| wifi_if_DUAL  | 对象   | 可选，双频合一配置参数，详细定义见后，mode包含DUAL时有效     |
| wifi_if_GUEST | 对象   | 可选，访客wifi配置参数，详细定义见后，mode包含GUEST时有效    |

###### wifi_if_24G对象

| 字段       | 类型   | 说明                                                 |
| ---------- | ------ | ---------------------------------------------------- |
| net_mode   | 字符串 | 硬件模式，如11ng，具体取值和芯片有关                 |
| bandwidth  | 字符串 | 带宽，如HT40，详细定义同wifi_get_ap_config中相应字段 |
| channel    | 字符串 | 0为自动，1~13为wifi信道号                            |
| ssid       | 字符串 | SSID                                                 |
| hidden     | 字符串 | 0为开启广播，1为关闭广播                             |
| isolate    | 字符串 | 0为关闭isolate，1为打开isolate                       |
| encryption | 字符串 | 加密方式，详细定义同wifi_get_ap_config中相应字段     |
| key        | 字符串 | 密码                                                 |

###### wifi_if_5G对象

| 字段       | 类型   | 说明                                                 |
| ---------- | ------ | ---------------------------------------------------- |
| net_mode   | 字符串 | 硬件模式，如11ng，具体取值和芯片有关                 |
| bandwidth  | 字符串 | 带宽，如HT40，详细定义同wifi_get_ap_config中相应字段 |
| channel    | 字符串 | 0为自动，36~165为wifi信道号                          |
| ssid       | 字符串 | SSID                                                 |
| hidden     | 字符串 | 0为开启广播，1为关闭广播                             |
| isolate    | 字符串 | 0为关闭isolate，1为打开isolate                       |
| encryption | 字符串 | 加密方式，详细定义同wifi_if_24G对象的encryption      |
| key        | 字符串 | 密码                                                 |

###### wifi_if_DUAL对象

| 字段       | 类型   | 说明                                            |
| ---------- | ------ | ----------------------------------------------- |
| ssid       | 字符串 | SSID                                            |
| hidden     | 字符串 | 0为开启广播，1为关闭广播                        |
| encryption | 字符串 | 加密方式，详细定义同wifi_if_24G对象的encryption |
| key        | 字符串 | 密码                                            |

###### wifi_if_GUEST对象

| 字段       | 类型   | 说明                                            |
| ---------- | ------ | ----------------------------------------------- |
| maxassoc   | 字符串 | guest热点最大连接数                             |
| ssid       | 字符串 | SSID                                            |
| hidden     | 字符串 | 0为开启广播，1为关闭广播                        |
| isolate    | 字符串 | 0为关闭isolate，1为打开isolate                  |
| encryption | 字符串 | 加密方式，详细定义同wifi_if_24G对象的encryption |
| key        | 字符串 | 密码                                            |

##### 响应结果

| 字段   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "switch": "on",
    "maxassoc": "20",
    "mode": "2.4G 5G GUEST DUAL",
    "wifi_if_24G": {
        "net_mode": "11ng",
        "bandwidth": "HT40",
        "channel": "11",
        "ssid": "Openwrt_SSV_2G#f065",
        "hidden": "0",
        "isolate": "0",
        "encryption": "mixed-psk",
        "key": "12345678",
    },
    "wifi_if_5G": {
        "net_mode": "11a",
        "bandwidth": "HT20",
        "channel": "36",
        "ssid": "Openwrt_SSV_5G",
        "hidden": "0",
        "isolate": "0",
        "encryption": "psk2",
        "key": "12345678",
    },
    "wifi_if_DUAL": {
        "ssid": "Openwrt_SSV_2G#f065",
        "hidden": "0",
        "encryption": "mixed-psk",
        "key": "12345678",
    },
    "wifi_if_GUEST": {
        "maxassoc": "10",
        "ssid": "Openwrt_SSV_5G",
        "hidden": "0",
        "isolate": "0",
        "encryption": "psk2",
        "key": "12345678",
    }
}
```

###### response

```json
{
    "result": 0
}
```

#### 9.1.5 wifi_get_station_config

##### 功能描述

获取wifi extender配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=get_station_config

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明                               |
| ------ | ---- | ---------------------------------- |
| result | 数字 | 0为成功，非0为失败                 |
| config | 对象 | wifi station配置信息，详细定义见后 |

###### config对象

| 字段 | 类型   | 说明 |
| ---- | ------ | ---- |
| ssid | 字符串 | SSID |
| key  | 字符串 | 密码 |

##### 特别说明

##### 示例

###### response

```json
{
    "result": 0,
    "config": {
        "ssid": "Openwrt_SSV_5G",
		"key": "12345678"
    }
}
```

#### 9.1.6 wifi_set_station_config

##### 功能描述

设置wifi extender配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_set_station_config

##### 请求参数

| 字段 | 类型   | 说明 |
| ---- | ------ | ---- |
| ssid | 字符串 | SSID |
| key  | 字符串 | 密码 |

##### 响应结果

| 字段   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "ssid": "Openwrt_SSV_5G",
    "key": "12345678"
}
```

###### response

```json
{
    "result": 0
}
```



#### 9.1.7 wifi_scan

##### 功能描述

获取可用的wifi列表信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_scan

##### 请求参数

无

##### 响应结果

| 字段      | 类型 | 说明                         |
| --------- | ---- | ---------------------------- |
| scan_list | 数组 | 数据元素为对象，详见后面定义 |

###### scan_list数组中的对象

| 字段    | 类型   | 说明      |
| ------- | ------ | --------- |
| ssid    | 字符串 | WIFI SSID |
| ch      | 字符串 | 信道      |
| sig     | 数字   | 信号      |
| encrypt | 字符串 | 加密方式  |

##### 特别说明

无

##### 示例

###### response

```json
{
	"scan_list": [
		{
			"ssid": "Leonardo_ZE",
			"ch": 1,
			"sig": -45,
			"encrypt": "WPA2"
		},
		{
			"ssid": "KNDL",
			"ch": 1,
			"sig": -70,
			"encrypt": "WPA2"
		},
		{
			"ssid": "ww-8b7680e57a5e60ae",
			"ch": 6,
			"sig": -69,
			"encrypt": "WPA\/WPA2"
		}，
		{
			"ssid": "ww-80ec53917a0e086e",
			"ch": 6,
			"sig": -52,
			"encrypt": "WPA\/WPA2"
		},
		{
			"ssid": "ww-31ebd7e6",
			"ch": 10,
			"sig": -50,
			"encrypt": "WPA2"
		}
	]
}
```



#### 9.1.8  get_extender_status

##### 功能描述

获取WIFI extender的连接状态信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=get_extender_status

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| status | 数字 | 0:未连接<br/>1:WIFI密码错误<br/>2:搜索WIFI网络中<br/>3:网络连接中<br/>4:等待获取网络IP<br/>5:已连接 |



##### 特别说明

无

##### 示例

###### response

```json
{
	"status": 0
}
```



#### 9.1.9  get_extender_config

##### 功能描述

获取WIFI extender的配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=get_extender_config

##### 请求参数

无

##### 响应结果

| 字段   | 类型   | 说明              |
| ------ | ------ | ----------------- |
| enable | 数字   | 0:关闭<br/>1:打开 |
| ssid   | 字符串 | WIFI SSID         |
| key    | 字符串 | WIFI 密码         |



##### 特别说明

无

##### 示例

###### response

```json
{
	"enable": 1,
	"ssid": "cd_wewins",
	"key": "cdww-2021"
}
```



#### 9.1.10  set_extender_config

##### 功能描述

设置 WIFI extender的配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=set_extender_config

##### 请求参数

| 字段   | 类型   | 说明              |
| ------ | ------ | ----------------- |
| enable | 数字   | 0:关闭<br/>1:打开 |
| ssid   | 字符串 | WIFI SSID         |
| key    | 字符串 | WIFI 密码         |

##### 响应结果

| 字段   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 数字 | -1:失败<br/>0:成功 |

##### 特别说明

无

##### 示例

###### request

```json
{
	"enable": 1,
	"ssid": "cd_wewins",
	"key": "cdww-2021"
}
```



###### response

```json
{
	"result": 0,
}
```



### 9.2 网络设置

#### 9.2.1 get_available_network_mode

##### 功能描述

获取可用的网络模式

##### 接口

http://mobile.router/api.cgi?path=cm&method=get_available_network_mode

##### 请求参数

无

##### 响应结果

| 字段          | 类型 | 说明                          |
| ------------- | ---- | ----------------------------- |
| result        | 数字 | 0为成功，非0为失败            |
| network_modes | 数组 | 元素为字符串，auto/4g/3g/2g等 |

##### 特别说明

用于产品定制

##### 示例

###### response

```json
{
    "result": 0,
    "network_modes": [
        "auto",
        "4g",
        "3g",
        "2g"
    ]
}
```

#### 9.2.2 get_network_settings

##### 功能描述

获取蜂窝网络参数

##### 接口

http://mobile.router/api.cgi?path=cm&method=get_network_settings

##### 请求参数

无

##### 响应结果

| 字段             | 类型 | 说明                          |
| ---------------- | ---- | ----------------------------- |
| result           | 数字 | 0为成功，非0为失败            |
| network_settings | 对象 | result为0时有效，详细定义见后 |

###### network_settings对象

| 字段         | 类型   | 说明                                           |
| ------------ | ------ | ---------------------------------------------- |
| network_mode | 字符串 | auto/4g/3g/2g                                  |
| profile_mode | 字符串 | auto/manual                                    |
| connect_mode | 字符串 | auto/manual                                    |
| data_roaming | 字符串 | 1：漫游下使能数据业务<br>0：漫游下关闭数据业务 |
| profile      | 对象   | 详细定义见后                                   |

###### profile对象

| 字段         | 类型 | 说明                                                         |
| ------------ | ---- | ------------------------------------------------------------ |
| active_index | 数字 | profile_mode为auto时为0，profile_mode为manual时为1/2/3       |
| data         | 数组 | 元素为对象，共三个，分别为index为1/2/3的profile的参数，详细定义见后 |

###### data元素对象

| 字段      | 类型   | 说明                            |
| --------- | ------ | ------------------------------- |
| name      | 字符串 | profile名称                     |
| apn       | 字符串 | apn名称                         |
| username  | 字符串 | 用户名                          |
| password  | 字符串 | 密码                            |
| ip_type   | 字符串 | 0：ipv4v6<br>1：ipv4<br>2：ipv6 |
| auth_type | 字符串 | NONE/PAP/CHAP                   |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
    "network_settings": {
        "network_mode": "auto",
        "profile_mode": "auto",
        "connect_mode": "auto",
        "data_roaming": "1",
        "profile": {
            "active_index": 0,
            "data": [
                {
                    "name": "Internet",
                    "apn": "Internet",
                    "username": "Internet",
                    "password": "Internet",
                    "ip_type": "0",
                    "auth_type": "NONE"
                },
                {
                    "name": "APN1",
                    "apn": "any",
                    "username": "any",
                    "password": "any",
                    "ip_type": "0",
                    "auth_type": "NONE"
                },
                {
                    "name": "APN2",
                    "apn": "any",
                    "username": "any",
                    "password": "any",
                    "ip_type": "0",
                    "auth_type": "NONE"
                }
            ]
        }
    }
}
```

#### 9.2.3 set_network_settings

##### 功能描述

设置蜂窝网络参数

##### 接口

http://mobile.router/api.cgi?path=cm&method=set_network_settings

##### 请求参数

| 字段         | 类型   | 说明                                            |
| ------------ | ------ | ----------------------------------------------- |
| connect_mode | 字符串 | auto/manual                                     |
| network_mode | 字符串 | auto/4g/3g/2g                                   |
| data_roaming | 字符串 | 1：漫游下使能数据业务<br/>0：漫游下关闭数据业务 |
| profile_mode | 字符串 | auto/manual                                     |
| profile      | 对象   | profile信息，详细定义见后                       |

###### profile对象

| 字段  | 类型   | 说明                      |
| ----- | ------ | ------------------------- |
| index | 字符串 | 1/2/3                     |
| data  | 对象   | profile参数，详细定义见后 |

###### data对象

| 字段      | 类型   | 说明                              |
| --------- | ------ | --------------------------------- |
| name      | 字符串 | profile名称                       |
| apn       | 字符串 | apn名称                           |
| username  | 字符串 | 用户名                            |
| password  | 字符串 | 密码                              |
| ip_type   | 字符串 | 0：ipv4v6<br/>1：ipv4<br/>2：ipv6 |
| auth_type | 字符串 | NONE/PAP/CHAP                     |

##### 响应结果

| 字段   | 类型 | 说明             |
| ------ | ---- | ---------------- |
| result | 梳子 | 0未成功，1为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "connect_mode": "auto",
    "network_mode": "auto",
    "data_roaming": "1",
    "profile_mode": "manual",
    "profile": {
        "index": "2",
        "data": {
            "name": "cmcc",
            "apn": "cmnet",
            "username": "any",
            "password": "any",
            "ip_type": "2",
            "auth_type": "NONE"
        }
    }
}
```

###### response

```json
{
    "result": 0
}
```

### 9.3 网络搜索

#### 9.3.1 get_network_select_mode

##### 功能描述

获取网络选择模式

##### 接口

http://mobile.router/api.cgi?path=util_wan&method=get_network_select_mode

##### 请求参数

无

##### 响应结果

| 字段        | 类型   | 说明                       |
| ----------- | ------ | -------------------------- |
| result      | 数字   | 0为成功，非0为失败         |
| nw_sel_mode | 字符串 | manual：手动<br>auto：自动 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
    "nw_sel_mode": "manual"
}
```

#### 9.3.2 search_network

##### 功能描述

手动搜网

##### 接口

http://mobile.router/api.cgi?path=util_wan&method=search_network&timeout=100

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| response | 对象 | 详细定义见后 |
| wan      | 对象 | 详细定义见后 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

###### wan对象

| 字段         | 类型 | 说明                         |
| ------------ | ---- | ---------------------------- |
| network_list | 数组 | 数组元素为对象，详细定义见后 |

###### network_list数组元素对象

| 字段     | 类型   | 说明                                     |
| -------- | ------ | ---------------------------------------- |
| isp_name | 字符串 | 运营商名称                               |
| plmn     | 字符串 | PLMN                                     |
| status   | 字符串 | 状态，unkown/current/available/forbidden |
| act      | 字符串 | 接入技术，GSM/UTRAN/E_UTRAN              |

##### 特别说明

手动搜网之前断开连接

搜网时间较长，通常大于30s，需要设置timeout

##### 示例

###### response

```json
{
    "wan": {
        "network_list": [
            {
                "isp_name": "UNICOM",
                "plmn": "46001",
                "status": "current",
                "act": "E_UTRAN"
            },
            {
                "isp_name": "UNICOM",
                "plmn": "46001",
                "status": "available",
                "act": "UTRAN"
            },
            {
                "isp_name": "CMCC",
                "plmn": "46000",
                "status": "forbidden",
                "act": "GSM"
            },
            {
                "isp_name": "CT",
                "plmn": "46011",
                "status": "forbidden",
                "act": "E_UTRAN"
            },
            {
                "isp_name": "CMCC",
                "plmn": "46000",
                "status": "forbidden",
                "act": "E_UTRAN"
            }
        ]
    },
    "response": {
        "setting_response": "OK"
    }
}
```

#### 9.3.3 select_network

##### 功能描述

选择网络，包括手动和自动

##### 接口

http://mobile.router/api.cgi?path=util_wan&method=select_network

##### 请求参数

| 字段          | 类型   | 说明                         |
| ------------- | ------ | ---------------------------- |
| network_param | 字符串 | auto：自动<br>act%plmn：手动 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| response | 对象 | 详细定义见后 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "network_param": "UTRAN%46001"
}
```

###### response

```json
{
    "response": {
        "setting_response": "OK"
    }
}
```



### 9.4 admin设置



### 9.5 storage设置



### 9.6 DHCP&DNS

#### 9.6.1 router_get_lan_ip

##### 功能描述

获取局域网IP地址和掩码

##### 接口

http://mobile.router/api.cgi?path=router&method=router_get_lan_ip

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明         |
| ------ | ---- | ------------ |
| router | 对象 | 详细定义见后 |

###### router对象

| 字段        | 类型   | 说明     |
| ----------- | ------ | -------- |
| lan_ip      | 字符串 | IP地址   |
| lan_netmask | 字符串 | 子网掩码 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "router": {
        "lan_ip": "192.168.8.1",
        "lan_netmask": "255.255.255.0"
    }
}
```

#### 9.6.2 router_set_lan_ip

##### 功能描述

设置局域网IP地址

##### 接口

http://mobile.router/api.cgi?path=router&method=router_set_lan_ip

##### 请求参数

| 字段   | 类型   | 说明         |
| ------ | ------ | ------------ |
| lan_ip | 字符串 | 局域网IP地址 |

##### 响应结果

| 字段   | 类型 | 说明         |
| ------ | ---- | ------------ |
| router | 对象 | 详细定义见后 |

###### router对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

连接会断开

##### 示例

###### request

```json
{
    "lan_ip": "192.168.8.1"
}
```

###### response

```json
{
    "router": {
        "setting_response": "OK"
    }
}
```

#### 9.6.3 router_get_dhcp_settings

##### 功能描述

获取DHCP/DNS参数

##### 接口

http://mobile.router/api.cgi?path=router&method=router_get_dhcp_settings

##### 请求参数

无

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| dhcp | 对象 | 详细定义见后 |

###### dhcp对象

| 字段      | 类型   | 说明                                  |
| --------- | ------ | ------------------------------------- |
| disabled  | 字符串 | DHCP开关，0为使能，1为禁用            |
| start     | 字符串 | IP地址池起始值                        |
| limit     | 字符串 | IP地址池可用数量                      |
| leasetime | 字符串 | 租约时间                              |
| dnsmode   | 字符串 | DNS模式，auto或manual                 |
| dns1      | 字符串 | DNS服务器1地址，DNS模式为manual时有效 |
| dns2      | 字符串 | DNS服务器2地址，DNS模式为manual时有效 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "dhcp": {
        "disabled": "0",
        "start": "100",
        "limit": "150",
        "leasetime": "7200",
        "dnsmode": "manual",
        "dns1": "7.7.7.7",
        "dns2": "8.8.8.8"
    }
}
```

#### 9.6.4 router_set_dhcp_settings

##### 功能描述

设置DHCP/DNS参数

##### 接口

http://mobile.router/api.cgi?path=router&method=router_set_dhcp_settings

##### 请求参数

| 字段      | 类型   | 说明                                  |
| --------- | ------ | ------------------------------------- |
| disabled  | 字符串 | DHCP开关，0为使能，1为禁用            |
| start     | 字符串 | IP地址池起始值                        |
| limit     | 字符串 | IP地址池可用数量                      |
| leasetime | 字符串 | 租约时间                              |
| dnsmode   | 字符串 | DNS模式，auto或manual                 |
| dns1      | 字符串 | DNS服务器1地址，DNS模式为manual时有效 |
| dns2      | 字符串 | DNS服务器2地址，DNS模式为manual时有效 |

##### 响应结果

| 字段 | 类型 | 说明         |
| ---- | ---- | ------------ |
| dhcp | 对象 | 详细定义见后 |

###### dhcp对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "disabled": "0",
    "start": "100",
    "limit": "150",
    "leasetime": "7200",
    "dnsmode": "auto",
    "dns1": "",
    "dns2": ""
}
```

###### response

```json
{
    "dhcp": {
        "setting_response": "OK"
    }
}
```

### 9.7 整机休眠设置

#### 9.7.1 sleep_wait_time

##### 功能描述

获取整机休眠等待时间

##### 接口

http://mobile.router/api.cgi?path=aoc&method=sleep_wait_time

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明                                 |
| ------ | ---- | ------------------------------------ |
| result | 数字 | 0表示不休眠；10/20/30/40，单位为分钟 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 40
}
```

#### 9.7.2 set_sleep_wait_time

##### 功能描述

设置整机休眠等待时间

##### 接口

http://mobile.router/api.cgi?path=aoc&method=set_sleep_wait_time

##### 请求参数

| 字段 | 类型 | 说明                                       |
| ---- | ---- | ------------------------------------------ |
| time | 数字 | 0表示不休眠；有效值10/20/30/40，单位为分钟 |

##### 响应结果

| 字段   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "time" : 40
}
```

###### response

```json
{
    "result": 0
}
```

### 9.8 WPS

#### 9.8.1 wifi_get_wps_disable

##### 功能描述

获取wps开关状态

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_get_wps_disable

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段       | 类型   | 说明             |
| ---------- | ------ | ---------------- |
| wps_enable | 字符串 | 0为关闭，1为开启 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "wireless": {
        "wps_enable": "1"
    }
}
```

#### 9.8.2 wifi_set_wps_disable

##### 功能描述

设置wps开关状态

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_set_wps_disable

##### 请求参数

| 字段       | 类型   | 说明             |
| ---------- | ------ | ---------------- |
| wps_enable | 字符串 | 0为关闭，1为开启 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "wps_enable": "1"
}
```

###### response

```json
{
    "wireless": {
        "setting_response": "OK"
    }
}
```

#### 9.8.3 wifi_call_wps_pbc

##### 功能描述

开始PBC

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_call_wps_pbc

##### 请求参数

| 字段             | 类型   | 说明                |
| ---------------- | ------ | ------------------- |
| wifi_iface_index | 字符串 | wifi接口索引，0开始 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段                | 类型   | 说明                 |
| ------------------- | ------ | -------------------- |
| wps_call_pbc_result | 字符串 | OK为成功，FAIL为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "wifi_iface_index": "0"
}
```

###### response

```json
{
    "wireless": {
        "wps_call_pbc_result": "OK"
    }
}
```

#### 9.8.4 wifi_call_wps_pin

##### 功能描述

开始PIN

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_call_wps_pin

##### 请求参数

| 字段             | 类型   | 说明                |
| ---------------- | ------ | ------------------- |
| wps_pin          | 字符串 | PIN码               |
| wifi_iface_index | 字符串 | wifi接口索引，0开始 |

##### 响应结果

| 字段     | 类型   | 说明         |
| -------- | ------ | ------------ |
| wireless | 字符串 | 详细定义见后 |

###### wireless对象

| 字段                | 类型   | 说明                 |
| ------------------- | ------ | -------------------- |
| wps_call_pin_result | 字符串 | OK为成功，FAIL为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "wps_pin": "53477712",
    "wifi_iface_index": "0"
}
```

###### response

```json
{
    "wireless": {
        "wps_call_pin_result": "OK"
    }
}
```

#### 9.8.5 wps_status

##### 功能描述

获取wps状态，当前只关心是否为Active

##### 接口

http://mobile.router/api.cgi?path=hostapd.uap0&method=wps_status

##### 请求参数

无

##### 响应结果

| 字段       | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| pbc_status | 字符串 | Active表示正在进行WPS，其他值有Disabled/Timed-out/Overlap/Unknown |

##### 特别说明

path跟平台或wifi方案有关

##### 示例

###### response

```json
{
    "pbc_status": "Disabled"
}
```

#### 9.8.6 wifi_call_wps_cancel

##### 功能描述

取消wps

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_call_wps_cancel

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段                   | 类型   | 说明                 |
| ---------------------- | ------ | -------------------- |
| wps_call_cancel_result | 字符串 | OK为成功，FAIL为失败 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "wireless": {
        "wps_call_cancel_result": "OK"
    }
}
```

### 9.9 设备

#### 9.9.1 router_call_reboot

##### 功能描述

重启设备

##### 接口

http://mobile.router/api.cgi?path=router&method=router_call_reboot

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明         |
| ------ | ---- | ------------ |
| router | 对象 | 详细说明见后 |

###### router对象

| 字段             | 类型   | 说明                 |
| ---------------- | ------ | -------------------- |
| setting_response | 字符串 | OK为成功，否则为失败 |

##### 特别说明

修改SD卡模式、本地升级或FOTA的时候需要调用此接口重启设备

##### 示例

###### response

```json
{
    "router": {
        "setting_response": "OK"
    }
}
```

#### 9.9.2 router_call_rst_factory

##### 功能描述

恢复出厂设置

##### 接口

http://mobile.router/api.cgi?path=router&method=router_call_rst_factory

##### 请求参数

无

##### 响应结果

| 字段   | 类型 | 说明         |
| ------ | ---- | ------------ |
| router | 对象 | 详细说明见后 |

###### router对象

| 字段             | 类型   | 说明                 |
| ---------------- | ------ | -------------------- |
| setting_response | 字符串 | OK为成功，否则为失败 |

##### 特别说明

调用此接口，可能收不到响应，当作成功处理

##### 示例

###### response

```json
{
    "router": {
            "setting_response": "OK"
    }
}
```

#### 9.9.3 get_ui_language

##### 功能描述

获取UI语言

##### 接口

http://mobile.router/api.cgi?path=router&method=get_ui_language

##### 请求参数

无

##### 响应结果

| 参数     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| result   | 数字   | 0为成功，非0为失败                                           |
| language | 字符串 | ISO 639-1 语言代码，参考https://www.w3school.com.cn/tags/html_ref_language_codes.asp |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
    "language": "en"
}
```

#### 9.9.4 set_ui_language

##### 功能描述

设置UI语言

##### 接口

http://mobile.router/api.cgi?path=router&method=set_ui_language

##### 请求参数

| 参数     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| language | 字符串 | ISO 639-1 语言代码，参考https://www.w3school.com.cn/tags/html_ref_language_codes.asp |

##### 响应结果

| 参数   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "language": "en"
}
```

###### response

```json
{
    "result": 0
}
```

## 10 防火墙

### 10.1 DMZ

#### 10.1.1 获取DMZ 开关状态

##### 功能描述

获取DMZ功能状态。

##### 接口

http://mobile.router/api.cgi?path=firewall&method=fw_get_disable_info

##### 请求参数

无

##### 响应结果

| 字段        | 类型   | 说明                                      |
| ----------- | ------ | ----------------------------------------- |
| dmz_disable | 字符串 | "0"：DMZ功能已开启<br/>"1"：DMZ功能已关闭 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "firewall": {
        "dmz_disable": "0"
    }
}
```

#### 10.1.2 开启关闭DMZ 功能

##### 功能描述

开启关闭DMZ功能。

##### 接口

http://mobile.router/api.cgi?path=firewall&method=fw_set_disable_info

##### 请求参数

| 字段        | 类型   | 说明                                  |
| ----------- | ------ | ------------------------------------- |
| dmz_disable | 字符串 | “0”：开启DMZ功能<br/>”1“：关闭DMZ功能 |

##### 响应结果

| 字段             | 类型   | 说明                             |
| ---------------- | ------ | -------------------------------- |
| setting_response | 字符串 | OK：开启成功<br/>ERROR：开启失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "dmz_disable": "0"
}
```

###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```

#### 10.1.3 获取DMZ配置信息

##### 功能描述

获取DMZ配置信息。

##### 接口

http://mobile.router/api.cgi?path=firewall&method=fw_get_dmz_info

##### 请求参数

无

##### 响应结果

| 字段        | 类型   | 说明            |
| ----------- | ------ | --------------- |
| dmz_dest_ip | 字符串 | DMZ主机的IP地址 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "firewall": {
        "dmz_dest_ip": "192.168.8.199"
    }
}
```

#### 10.1.4 编辑DMZ配置信息

编辑已设置的DMZ 主机ip地址

##### 接口

http://mobile.router/api.cgi?path=firewall&method=fw_edit_dmz_entry

##### 请求参数

| 字段        | 类型   | 说明            |
| ----------- | ------ | --------------- |
| dmz_dest_ip | 字符串 | DMZ主机的IP地址 |

##### 响应结果

| 字段             | 类型   | 说明                                                         |
| ---------------- | ------ | ------------------------------------------------------------ |
| setting_response | 字符串 | OK：设置成功<br/>ERROR：设置失败<br/>no exist：无配置信息，无法修改 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "dmz_dest_ip":"192.168.8.188"
}
```

###### response

```json
{
	"firewall": {
		"setting_response": "OK"
	}
}
```

#### 10.1.5 新增DMZ配置信息

新增DMZ 主机ip地址

##### 接口

http://mobile.router/api.cgi?path=firewall&method=fw_add_dmz_entry

##### 请求参数

| 字段        | 类型   | 说明            |
| ----------- | ------ | --------------- |
| dmz_dest_ip | 字符串 | DMZ主机的IP地址 |

##### 响应结果

| 字段             | 类型   | 说明                                                         |
| ---------------- | ------ | ------------------------------------------------------------ |
| setting_response | 字符串 | OK：新增成功<br/>ERROR：新增失败<br/>exist：配置信息已存在不能再新增 |

##### 特别说明

只允许新增一个DMZ主机ip地址

##### 示例

###### request

```json
{
    "dmz_dest_ip":"192.168.8.192"
}
```

###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```

#### 10.1.6 删除DMZ配置信息

##### 功能描述

删除DMZ 主机ip地址。

##### 接口

http://mobile.router/api.cgi?path=firewall&method=delete_dmz

##### 请求参数

无

##### 响应结果

| 字段             | 类型   | 说明                                                         |
| ---------------- | ------ | ------------------------------------------------------------ |
| setting_response | 字符串 | OK：删除成功<br/>ERROR：删除失败<br/>no exist：无配置信息，无法删除 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```

### 10.2 IP 过滤

#### 10.2.1 开启IP过滤功能

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_fw_set_disable_info

##### 请求参数

| 字段              | 类型   | 说明                                        |
| ----------------- | ------ | ------------------------------------------- |
| ip_filter_disable | 字符串 | “1”:关闭IP过滤功能。<br/>"0":开启IP过滤功能 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

开启、关闭时会让所有的防火墙规则立即生效。设备的初始开关状态为关闭。只能在开启IP过滤功能后才能更改IP过滤表。

##### 示例

###### request

```json
{
    "ww_ip_filter":
    {
        "ip_filter_disable":"1"
    }
}
```



###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```





#### 10.2.2 设置默认IP过滤模式

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_set_ip_filter_default_pol

##### 请求参数

| 字段           | 类型   | 说明                                                         |
| -------------- | ------ | ------------------------------------------------------------ |
| default_policy | 字符串 | ACCEPT:默认允许所有的ip设备上网，拒绝名单中的所有ip指向的设备上网。<br/>REJECT:默认拒绝所有的ip设备上网，允许名单中的所有ip指向的设备上网 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

包含两种模式，”ACCEPT”和”REJECT”；”ACCEPT”代表防火墙默认允许所有的IP包转发，”REJECT”代表防火墙默认拒绝所有的ip转发。在默认为”ACCEPT”情况下，增加的ip代表需要过滤掉，并且该ip不能访问局域网的webui；在默认为”REJECT”情况下，增加的ip代表允许转发。每次切换模式后，后端的IP过滤规则自动转换成相应的模式。设备的初始状态为”ACCEPT”。

##### 示例

###### request

```json
{
    "ww_ip_filter":
    {
        "default_policy":"REJECT"
    }
}
```



###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```



#### 10.2.3 读取ip过滤开关、模式状态

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_read_switch_mode_state

##### 请求参数

无

##### 响应结果

| 字段              | 类型   | 说明                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| setting_response  | 字符串 | OK：成功<br/>ERROR：失败<br/>                                |
| default_policy    | 字符串 | ACCEPT:默认允许所有的ip设备上网，拒绝名单中的所有ip指向的设备上网。<br/>REJECT:默认拒绝所有的ip设备上网，允许名单中的所有ip指向的设备上网 |
| ip_filter_disable | 字符串 | “1”:关闭IP过滤功能。<br/>"0":开启IP过滤功能                  |

##### 特别说明

无

##### 示例

###### request

无

###### response

```json
{
    "firewall": {
        "ip_filter_disable": "1",
        "default_policy": "REJECT",
        "setting_response": "OK"
    }
}
```



#### 10.2.4 编辑ip过滤表单项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_edit_ip_filter

##### 请求参数

| 字段 | 类型 | 说明               |
| ---- | ---- | ------------------ |
| list | 数组 | 数组元素类型为对象 |

###### list数组元素对象

| 字段  | 类型   | 说明                     |
| ----- | ------ | ------------------------ |
| ip    | 字符串 | IP地址字符串             |
| index | 字符串 | 为0到9范围的数字字符串。 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

Webui将序号和该序号修改后的ip地址下发给后端，后端自动更新防火墙配置文件。如果没有该序号对应规则，则新增该规则。ip值为"0"则删除该规则。

##### 示例

###### request

```json
{
    "ww_ip_filter": {
        "list": [
            {
                "ip": "192.168.8.199",
                "index": "9",
            },
            {
                "ip": "192.168.8.196",
                "index": "6",
            },
        ],
    }
}
```



###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```

#### 10.2.5 读取ip过滤表项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_read_ip_filter

##### 请求参数

| 字段 | 类型 | 说明                                           |
| ---- | ---- | ---------------------------------------------- |
| list | 数组 | 数组值范围：0~9对应的数字字符串以及字符串all。 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |
| list             | 对象   |                               |

###### list对象

| 字段 | 类型   | 说明                                         |
| ---- | ------ | -------------------------------------------- |
| 0    | 字符串 | 序号0对应的IP地址                            |
| n    | 字符串 | 序号n对应的IP地址，n为1到8范围的数字字符串。 |
| 9    | 字符串 | 序号9对应的IP地址                            |

##### 特别说明

可以通过序号读取一项或者几项，另外以all的形式读取表单内的所有ip地址。如果该序号对应的ip不存在则list内无返回。

##### 示例

###### request1

```json
{
    "ww_ip_filter":{
        "list":["8"]
    }
}
```



###### request2

```json
{
    "ww_ip_filter":{
        "list":["all"]
    }
}
```



###### response

```json
{
    "firewall": {
        "list": [
            {
                "index": "8",
                "ip": "192.168.8.199"
            }
        ],
        "setting_response": "OK"
    }
}
```

#### 10.2.6 删除ip过滤表项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_delete_ip_filter

##### 请求参数

| 字段 | 类型 | 说明                                           |
| ---- | ---- | ---------------------------------------------- |
| list | 数组 | 数组值范围：0~9对应的数字字符串以及字符串all。 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

可以通过序号删除一项或者几项，另外以all的形式删除表单内的所有ip地址。

##### 示例

###### request1

```json
{
    "ww_ip_filter":{
        "list":["6","8"]
    }
}
```

###### request2

```json
{
    "ww_ip_filter":{
        "list":["all"]
    }
}
```



###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```
### 10.3 PORT 过滤

#### 10.3.1 开启PORT过滤功能

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_fw_set_port_disable_info 

##### 请求参数

| 字段              | 类型   | 说明                                        |
| ----------------- | ------ | ------------------------------------------- |
| port_filter_disable | 字符串 | “1”:关闭port过滤功能。<br/>"0":开启port过滤功能 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

开启、关闭时会让所有的防火墙规则立即生效。设备的初始开关状态为关闭。只能在开启port过滤功能后才能更改port过滤表。

##### 示例

###### request

```json
{
    "ww_port_filter":
    {
        "port_filter_disable":"1"
    }
}
```



###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```


#### 10.3.2 读取PORT开关、模式状态

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_read_switch_port_mode_state

##### 请求参数

无

##### 响应结果

| 字段              | 类型   | 说明                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| setting_response  | 字符串 | OK：成功<br/>ERROR：失败<br/>                                |
| default_policy    | 字符串 | ACCEPT:拒绝名单中的所有port访问。							|
| port_filter_disable | 字符串 | “1”:关闭port过滤功能。<br/>"0":开启port过滤功能              |

##### 特别说明

无

##### 示例

###### request

无

###### response

```json
{
    "firewall": {
        "port_filter_disable": "1",
        "default_policy": "ACCEPT",
        "setting_response": "OK"
    }
}
```


#### 10.3.3编辑PORT过滤表单项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_edit_port_filter

##### 请求参数

| 字段 | 类型 | 说明               |
| ---- | ---- | ------------------ |
| list | 数组 | 数组元素类型为对象 |

###### list数组元素对象

| 字段  | 类型   | 说明                     |
| ----- | ------ | ------------------------ |
| port    | 字符串 | PORT范围字符串             |
| index | 字符串 | 为0到9范围的数字字符串。 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

Webui将序号和该序号修改后的port下发给后端，后端自动更新防火墙配置文件。如果没有该序号对应规则，则新增该规则。port值为"0"则删除该规则。

##### 示例

###### request

```json
{
    "ww_port_filter": {
        "list": [
            {
                "port": "100:200",
                "index": "9",
            },
            {
                "port": "200:400",
                "index": "6",
            },
        ],
    }
}
```



###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```

#### 10.3.4 读取PORT过滤表项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_read_port_filter

##### 请求参数

| 字段 | 类型 | 说明                                           |
| ---- | ---- | ---------------------------------------------- |
| list | 数组 | 数组值范围：0~9对应的数字字符串以及字符串all。 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |
| list             | 对象   |                               |

###### list对象

| 字段 | 类型   | 说明                                         |
| ---- | ------ | -------------------------------------------- |
| 0    | 字符串 | 序号0对应的PORT                            |
| n    | 字符串 | 序号n对应的PORT，n为1到8范围的数字字符串。 |
| 9    | 字符串 | 序号9对应的PORT                            |

##### 特别说明

可以通过序号读取一项或者几项，另外以all的形式读取表单内的所有port。如果该序号对应的port不存在则list内无返回。

##### 示例

###### request1

```json
{
    "ww_port_filter":{
        "list":["8"]
    }
}
```



###### request2

```json
{
    "ww_port_filter":{
        "list":["all"]
    }
}
```



###### response

```json
{
    "firewall": {
        "list": [
            {
                "index": "8",
                "port": "100:200"
            }
        ],
        "setting_response": "OK"
    }
}
```

#### 10.3.5 删除PORT过滤表项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_delete_port_filter

##### 请求参数

| 字段 | 类型 | 说明                                           |
| ---- | ---- | ---------------------------------------------- |
| list | 数组 | 数组值范围：0~9对应的数字字符串以及字符串all。 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

可以通过序号删除一项或者几项，另外以all的形式删除表单内的所有ip地址。

##### 示例

###### request1

```json
{
    "ww_port_filter":{
        "list":["6","8"]
    }
}
```

###### request2

```json
{
    "ww_port_filter":{
        "list":["all"]
    }
}
```



###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```



### 10.4 upnp

#### 10.4.1 开启/关闭upnp功能

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_upnp_open_close

##### 请求参数

| 字段        | 类型   | 说明                |
| ----------- | ------ | ------------------- |
| upnp_enable | 字符串 | 0：关闭<br/>1：开启 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

无。

##### 示例

###### request

```json
{
    "ww_upnp":{
        "upnp_enable":"1"
    }
}
```

###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```



#### 10.4.2 获取upnp功能开关状态

##### 接口

http://mobile.router/api.cgi?path=firewall&method=ww_upnp_open_close_state

##### 请求参数

无

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |
| upnp_enable      | 字符串 | 0：关闭<br/>1：开启           |

##### 特别说明

无。

##### 示例

###### request

无

###### response

```json
{
    "firewall": {
        "setting_response": "OK",
        "upnp_enable":"1"
    }
}

```

### 10.5 ping from wan

#### 10.5.1 开启/关闭ping from wan功能

##### 接口

http://mobile.router/api.cgi?path=firewall&method=set_ping_from_wan

##### 请求参数

| 字段                 | 类型   | 说明                |
| -------------------- | ------ | ------------------- |
| ping_from_wan_enable | 字符串 | 0：关闭<br/>1：开启 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

无。

##### 示例

###### request

```json
{
    "ping_from_wan":{
        "ping_from_wan_enable":"1"
    }
}
```

###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```



#### 10.5.2 获取ping from wan功能开关状态

##### 接口

http://mobile.router/api.cgi?path=firewall&method=get_ping_from_wan

##### 请求参数

无

##### 响应结果

| 字段                 | 类型   | 说明                          |
| -------------------- | ------ | ----------------------------- |
| setting_response     | 字符串 | OK：成功<br/>ERROR：失败<br/> |
| ping_from_wan_enable | 字符串 | 0：关闭<br/>1：开启           |

##### 特别说明

无。

##### 示例

###### request

无

###### response

```json
{
	"firewall": {
		"ping_from_wan_enable": "1",
		"setting_response": "OK"
	}
}
```



### 10.6 admin from wan

#### 10.6.1 开启/关闭admin from wan功能

##### 接口

http://mobile.router/api.cgi?path=firewall&method=set_admin_from_wan

##### 请求参数

| 字段                  | 类型   | 说明                |
| --------------------- | ------ | ------------------- |
| admin_from_wan_enable | 字符串 | 0：关闭<br/>1：开启 |

##### 响应结果

| 字段             | 类型   | 说明                          |
| ---------------- | ------ | ----------------------------- |
| setting_response | 字符串 | OK：成功<br/>ERROR：失败<br/> |

##### 特别说明

无。

##### 示例

###### request

```json
{
    "admin_from_wan":{
        "admin_from_wan_enable":"1"
    }
}
```

###### response

```json
{
    "firewall": {
        "setting_response": "OK"
    }
}
```



#### 10.6.2 获取admin from wan功能开关状态

##### 接口

http://mobile.router/api.cgi?path=firewall&method=get_admin_from_wan

##### 请求参数

无

##### 响应结果

| 字段                  | 类型   | 说明                     |
| --------------------- | ------ | ------------------------ |
| setting_response      | 字符串 | OK：成功<br/>ERROR：失败 |
| admin_from_wan_enable | 字符串 | 0：关闭<br/>1：开启      |

##### 特别说明

无。

##### 示例

###### request

无

###### response

```json
{
	"firewall": {
		"admin_from_wan_enable": "0",
		"setting_response": "OK"
	}
}
```

### 10.7 URL过滤

#### 10.7.1 获取URL过滤配置

##### 功能描述

获取URL过滤配置，包括开关和过滤项，最大支持10个过滤项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=get_url_filter

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明                          |
| -------- | ---- | ----------------------------- |
| result   | 数字 | 0为成功，非0为失败            |
| settings | 对象 | result为0时有效，详细定义见后 |

###### settings对象

| 字段        | 类型   | 说明                                                        |
| ----------- | ------ | ----------------------------------------------------------- |
| mode        | 字符串 | disable为关闭，blacklist为开启黑名单，whitelist为开启白名单 |
| black_items | 数组   | 数组元素为对象，详细定义见后                                |
| white_items | 数组   | 数组元素为对象，详细定义见后                                |

###### black_items/white_items元素对象

| 字段  | 类型   | 说明       |
| ----- | ------ | ---------- |
| index | 数字   | 0-9        |
| value | 字符串 | 过滤关键字 |

##### 特别说明

无

##### 示例

###### response

```json
{
        "result": 0,
        "settings": {
                "mode": "disable",
                "black_items": [
                        {
                                "index": 0,
                                "value": "baidu"
                        },
                        {
                                "index": 3,
                                "value": "sohu"
                        }
                ],
            	"white_items": [
                        {
                                "index": 0,
                                "value": "baidu"
                        },
                        {
                                "index": 3,
                                "value": "sohu"
                        }
                ]
        }
}
```

#### 10.7.2 设置URL过滤配置

##### 功能描述

设置URL过滤配置，包括开关和过滤项，最大支持10个过滤项

##### 接口

http://mobile.router/api.cgi?path=firewall&method=set_url_filter

##### 请求参数

| 字段        | 类型   | 说明                                                        |
| ----------- | ------ | ----------------------------------------------------------- |
| mode        | 字符串 | disable为关闭，blacklist为开启黑名单，whitelist为开启白名单 |
| black_items | 数组   | 可选，数组元素为对象，详细定义见后                          |
| white_items | 数组   | 可选，数组元素为对象，详细定义见后                          |

###### black_items/white_items元素对象

| 字段  | 类型   | 说明       |
| ----- | ------ | ---------- |
| index | 数字   | 0-9        |
| value | 字符串 | 过滤关键字 |

##### 响应结果

| 字段   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

black_items和white_items为可选

不带black_items和white_items时，只修改模式

带black_items时，清空已有的black_items，保存新设置的black_items

带white_items时，清空已有的white_items，保存新设置的white_items

##### 示例

###### request

```json
{
    "mode": "blacklist",
    "black_items": [
        {
            "index": 3,
            "value": "baidu"
        },
        {
            "index": 2,
            "value": "sohu"
        }
    ]
}
```

###### response

```json
{
    "result": 0
}
```

### 10.8 MAC过滤

#### 10.8.1 wifi_get_mac_filter

##### 功能描述

获取wifi mac过滤配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_get_mac_filter

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段         | 类型 | 说明                                  |
| ------------ | ---- | ------------------------------------- |
| wireless_num | 数字 | 热点数量                              |
| APx          | 对象 | x从0开始，如AP0，AP1...，详细定义见后 |

APx对象

| 字段          | 类型   | 说明                                              |
| ------------- | ------ | ------------------------------------------------- |
| macfilter     | 字符串 | disable为关闭mac过滤，deny为黑名单，allow为白名单 |
| maclist_deny  | 字符串 | 黑名单mac列表，以空格分隔，没此字段表示黑名单为空 |
| maclist_allow | 字符串 | 白名单mac列表，以空格分隔，没此字段表示白名单为空 |

##### 特别说明

无

##### 示例

###### response

```json
{
    "wireless": {
        "wireless_num": 1,
        "AP0": {
            "macfilter": "allow",
            "maclist_allow": "11:22:33:44:55:64  11:22:33:44:55:68       ",
            "maclist_deny": "11:22:33:44:55:66  11:22:33:44:55:67       ",
            "host_name_allow": "adfg  123  456     "
        }
    }
}
```

#### 10.8.2 wifi_set_mac_filter

##### 功能描述

设置wifi MAC过滤配置信息

##### 接口

http://mobile.router/api.cgi?path=wireless&method=wifi_set_mac_filter

##### 请求参数

| 字段            | 类型   | 说明                                              |
| --------------- | ------ | ------------------------------------------------- |
| wifi_device     | 字符串 | 0为第一个，1为第二个...                           |
| macfilter       | 字符串 | disable为关闭mac过滤，deny为黑名单，allow为白名单 |
| maclist_allow   | 字符串 | 白名单mac列表，以空格分隔                         |
| maclist_deny    | 字符串 | 黑名单mac列表，以空格分隔                         |
| host_name_allow | 字符串 | 白名单host_name_allow列表，以空格分隔             |
| host_name_deny  | 字符串 | 黑名单host_name_deny列表，以空格分隔              |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| wireless | 对象 | 详细定义见后 |

###### wireless对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "wifi_device": "0",
    "macfilter": "allow",
    "maclist_allow": "11:22:33:44:55:64  11:22:33:44:55:68  11:22:33:44:55:67     ",
    "host_name_allow":"adfg  123  456     "
}
```

###### response

```json
{
    "wireless": {
        "setting_response": "OK"
    }
}
```



### 10.9 port forward

#### 10.9.1 获取port_forward配置

##### 功能描述

获取port forward配置，包括开关和端口绑定项，最大支持10个port forward规则。

##### 接口

http://mobile.router/api.cgi?path=firewall&method=get_port_forward

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明                          |
| -------- | ---- | ----------------------------- |
| result   | 数字 | 0为成功，非0为失败            |
| settings | 对象 | result为0时有效，详细定义见后 |

###### settings对象

| 字段   | 类型 | 说明                         |
| ------ | ---- | ---------------------------- |
| enable | 数字 | 0为关闭，1为开启             |
| items  | 数组 | 数组元素为对象，详细定义见后 |



###### items元素对象

| 字段       | 类型   | 说明                        |
| ---------- | ------ | --------------------------- |
| index      | 数字   | 0-9                         |
| name       | 字符串 | 配置名称                    |
| mac        | 字符串 | 需要配端口转发的设备MAC地址 |
| local_port | 字符串 | 局域网端口                  |
| wan_port   | 字符串 | WAN口端口                   |

##### 特别说明

无

##### 示例

###### response

```json
{
    "result": 0,
    "settings": {
        "enable": 1,
        "items": [
            {
                "index": 0,
                "mac": "b2:ba:b3:02:33:ac",
                "name": "jxdteset",
                "local_port": "200",
                "wan_port": "300"
            }
        ]
    }
}
```

#### 10.9.2 设置port_forward配置

##### 功能描述

获取port forward配置，包括开关和端口绑定项，最大支持10个port forward规则。

##### 接口

http://mobile.router/api.cgi?path=firewall&method=set_port_forward

##### 请求参数



| 字段   | 类型 | 说明                               |
| ------ | ---- | ---------------------------------- |
| enable | 数字 | 0为关闭，1为开启                   |
| items  | 数组 | 可选，数组元素为对象，详细定义见后 |

###### items元素对象

| 字段       | 类型   | 说明                        |
| ---------- | ------ | --------------------------- |
| index      | 数字   | 0-9                         |
| name       | 字符串 | 配置名称                    |
| mac        | 字符串 | 需要配端口转发的设备MAC地址 |
| local_port | 字符串 | 局域网端口                  |
| wan_port   | 字符串 | WAN端口                     |

##### 响应结果

| 字段   | 类型 | 说明               |
| ------ | ---- | ------------------ |
| result | 数字 | 0为成功，非0为失败 |

##### 特别说明

items为可选

不带items时，只修改开关；带items时，清空已有的items，保存新设置的items

##### 示例

###### request

```json
{
    "enable":1,
    "items":[
        {
            "index":0,
            "mac":"b2:ba:b3:02:33:ac",
            "name":"jxdteset",
            "local_port":"200",
            "wan_port":"300"
        }
    ]
}
```

###### response

```json
{
        "result": 0
}
```





## 11 DDNS

### 11.1 设置DDNS参数

##### 功能描述

设置DDNS参数保存配置。

##### 接口

http://mobile.router/api.cgi?path=ddns&method=set_ddns

##### 请求参数

| 字段            | 类型   | 说明                                                         |
| --------------- | ------ | ------------------------------------------------------------ |
| enabled         | 字符串 | 0：关闭使能<br>1：打开使能                                   |
| service_name    | 字符串 | 服务器网址，支持下发以下四种：<br>oray.com<br>dyndns.com<br>no-ip.com<br>ipv6.dynv6.com |
| domain          | 字符串 | 申请的域名地址                                               |
| username        | 字符串 | 服务器网址中注册的用户名                                     |
| password或token | 字符串 | 服务器网址中注册的用户名密码或生成的token                    |

##### 响应结果

| 字段   | 类型 | 说明                         |
| ------ | ---- | ---------------------------- |
| result | 整数 | 0：设置成功<br>4:   设置失败 |

##### 特别说明

service_name固定为以下四个：oray.com；dyndns.com；no-ip.com；ipv6.dynv6.com，当service_name为ipv6.dynv6.com时，请求字段的password字段变为下发token。当service_name为其余三个时使用password字段。

##### 示例

###### request

```json
{
	"enabled":"1",
    "service_name":"oray.com",
    "domain":"xxxxxxxx.qicp.vip",
    "username":"xxxxxxxx",
    "password":"xxxxxxxx"
}
```

###### 或

###### 当service_name为ipv6.dynv6.com时，请求字段的password字段变为下发token。

###### request

```json
{
	"enabled":"1",
    "service_name":"ipv6.dynv6.com",
    "domain":"xxxxxxxx.xxx",
    "username":"xxxxxxxx",
    "token":"xxxxxxxx"
}
```

###### 

###### response

```json
{
	"result": 0
}
```



### 11.2 读取DDNS参数

##### 功能描述

获取配置文件中的DDNS配置信息。

##### 接口

http://mobile.router/api.cgi?path=ddns&method=get_ddns

##### 请求参数

无

##### 响应结果

| 字段         | 类型   | 说明                                                         |
| ------------ | ------ | ------------------------------------------------------------ |
| result       | 数字   | 0：读取成功<br>4:   未找到DDNS配置文件                       |
| enabled      | 字符串 | 0：未使能<br>1：使能                                         |
| service_name | 字符串 | DDNS服务器网址                                               |
| domain       | 字符串 | 申请的域名地址                                               |
| username     | 字符串 | 服务器网址中注册的用户名                                     |
| password     | 字符串 | 服务器网址中注册的用户名密码                                 |
| token        | 字符串 | 服务器网址中注册生成的token                                  |
| ddns_ipaddr  | 字符串 | 获取当前IP地址                                               |
| ddns_state   | 字符串 | 当前DDNS状态<br> 0： Idle<br> 1： Updating<br> 3 ：OK<br> 4 ：Block |

##### 特别说明

service_name固定为四个oray.com；dyndns.com；no-ip.com；ipv6.dynv6.com，当service_name为ipv6.dynv6.com时，响应结果的返回的password字段变为返回token字段。

##### 示例

###### response

```json
{
	"enabled": "1",
	"service_name": "oray.com",
	"domain": "domain_example.qicp.vip",
	"username": "username_example",
	"ddns_ipaddr": "172.31.151.252",
	"password": "password_example",
    "ddns_state": "3",
	"result": 0
}
或
{
	"enabled": "1",
	"service_name": "ipv6.dynv6.com",
	"domain": "domain_example.qicp.vip",
	"username": "username_example",
	"ddns_ipaddr": "2409:8962:337:b36:1:0:9191:67b3",
	"token": "password_example",
    "ddns_state": "0",
	"result": 0
}
```



## 12 其他

### 12.1 UniEncode

## 13 内部接口

### 13.1 安全

#### 13.1.1 get_magicnumber

##### 功能描述

获取magicnumber

##### 接口

http://mobile.router/api.cgi?path=version&method=get_magicnumber

##### 请求参数

无

##### 响应结果

| 字段   | 类型   | 说明                         |
| ------ | ------ | ---------------------------- |
| result | 数字   | 0为成功，非0为失败           |
| magic  | 字符串 | magicnumber，result为0时有效 |

##### 特别说明

此接口不需要登录

##### 示例

###### response

```json
{
    "result": 0,
    "magic": "c77fe47777cf15e3570e218f21abaf42"
}
```

#### 13.1.1 router_restart_adb

##### 功能描述

开启/重启adb服务，密码正确的情况下，如果未启动adbd则启动，如果已经启动adbd则重启

##### 接口

http://mobile.router/api.cgi?path=router&method=router_restart_adb

##### 请求参数

| 字段   | 类型   | 说明    |
| ------ | ------ | ------- |
| adbkey | 字符串 | adb密码 |

##### 响应结果

| 字段   | 类型 | 说明                |
| ------ | ---- | ------------------- |
| result | 数字 | 1为成功，否则为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "adbkey": "dffd46e47d16f169c4558039d2f86663"
}
```

###### response

```json
{
    "result": 1
}
```

### 13.2 工程信息

#### 13.2.1 set_eng_mode

##### 功能描述

设置工程模式

##### 接口

http://mobile.router/api.cgi?path=cm&method=set_eng_mode

##### 请求参数

| 字段 | 类型   | 说明                       |
| ---- | ------ | -------------------------- |
| mode | 字符串 | 工程模式，0为关闭，1为开启 |

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| response | 对象 | 详细定义见后 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "mode": "1"
}
```

###### response

```json
{
    "response": {
        "setting_response": "OK"
    }
}
```



#### 13.2.2 query_eng_info

##### 功能描述

查询工程信息

##### 接口

http://mobile.router/api.cgi?path=cm&method=query_eng_info

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明                          |
| -------- | ---- | ----------------------------- |
| result   | 数字 | 0为成功，非0为失败            |
| eng_info | 对象 | 详细定义见后，result为0时有效 |

###### eng_info对象

| 字段 | 类型   | 说明                                |
| ---- | ------ | ----------------------------------- |
| rat  | 字符串 | 2g/3g/4g                            |
| data | 对象   | 根据rat不同，内容不同，详细定义见后 |

###### data（rat为4g）

| 字段           | 类型   | 说明     |
| -------------- | ------ | -------- |
| plmn           | 字符串 |          |
| cell_id        | 数字   |          |
| pci            | 数字   |          |
| ecgi           | 字符串 |          |
| band           | 数字   |          |
| operation_mode | 字符串 | FDD或TDD |
| dl_earfcn      | 数字   |          |
| ul_earfcn数字  | 数字   |          |
| dl_freq        | 字符串 |          |
| ul_freq        | 字符串 |          |
| dl_bandwidth   | 字符串 |          |
| rsrp           | 字符串 |          |
| rsrq           | 字符串 |          |
| sinr           | 字符串 |          |
| rssi           | 字符串 |          |

###### data（rat为3g）

| 字段    | 类型   | 说明 |
| ------- | ------ | ---- |
| plmn    | 字符串 |      |
| lac     | 数字   |      |
| cell_id | 数字   |      |
| uarfcn  | 数字   |      |
| rscp    | 字符串 |      |
| ecio    | 字符串 |      |
| rssi    | 字符串 |      |

###### data（rat为2g）

| 字段    | 类型   | 说明 |
| ------- | ------ | ---- |
| plmn    | 字符串 |      |
| lac     | 数字   |      |
| cell_id | 数字   |      |
| arfcn   | 数字   |      |
| bsic    | 数字   |      |
| rx_lev  | 字符串 |      |

##### 特别说明

获取之前需要先设置为工程模式

##### 示例

###### response

```json
{
    "eng_info": {
        "rat": "4g",
        "data": {
            "plmn": "46001",
            "cell_id": 101792260,
            "pci": 203,
            "ecgi": "46001252f6113a04",
            "band": 3,
            "operation_mode": "FDD",
            "dl_earfcn": 1650,
            "ul_earfcn": 19650,
            "dl_freq": "1850 MHz",
            "ul_freq": "1755 MHz",
            "dl_bandwidth": "20 MHz",
            "rsrp": "-105 dBm",
            "rsrq": "-13.50 dB",
            "sinr": "127 dB",
            "rssi": "-111 dBm"
        }
    },
    "result": 0
}
```
### 13.3 工具接口

#### 13.3.1 factory命令

##### 功能描述

通过web调用生产接口

##### 接口

http://mobile.router/api.cgi?path=factory&method=commands

##### 请求参数

参见《工厂工具通用接口详细设计》中"使用json指令文件输入"

##### 响应结果

参见《工厂工具通用接口详细设计》中"使用json指令文件输入"

##### 特别说明

admin登录有才能访问

##### 示例

###### request

```json
{
    "wwfac_get_imei": [],
    "wwfac_get_wifi_mac": []
}
```

###### response

```json
{
    "status": 0,
    "wwfac_get_imei": {
        "status": 0,
        "result": {
            "code": 0,
            "data": [
                "352099001761482"
            ]
        }
    },
    "wwfac_get_wifi_mac": {
        "status": 0,
        "result": {
            "code": 0,
            "data": [
                "00c77fe47777"
            ]
        }
    }
}
```

## 14 USSD

### 14.1 USSD发送

##### 功能描述

ussd发送操作。

##### 接口

http://mobile.router/api.cgi?path=ussd&method=send_ussd

##### 请求参数

| 字段   | 类型   | 说明                                                         |
| ------ | ------ | ------------------------------------------------------------ |
| action | 字符串 | "0"：不需要回复<br>"1"：需要回复<br>"2":   结束会话          |
| param  | 字符串 | 发送的内容（操作码）：Mobilink M403定义见下表<br/>Check Balance:    \*6363*3#<br/>Check Bundle Usage:    \*6363\*4#<br/>Show My MBB Number :   \*6363\*2#<br/>Add/Change MBB Contact No :  \*6363\*6#<br/>流量均发送 :   \*6363\*3# |



##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| response | 对象 | 详细定义见后 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明

无

##### 示例

###### request

```json
{
    "action":"1",
    "param":"*6363*3#"
}
```

###### response

```json
{
    "response": {
        "setting_response": "OK"
    }
}
```



### 14.2 USSD获取

##### 功能描述

获取USSD信息。

##### 接口

http://mobile.router/api.cgi?path=ussd&method=ww_get_ussd_ind

##### 请求参数

无

##### 响应结果

| 字段     | 类型 | 说明         |
| -------- | ---- | ------------ |
| ussd     | 对象 | 详细定义见后 |
| response | 对象 | 详细定义见后 |

###### ussd对象

| 字段      | 类型   | 说明                                                     |
| --------- | ------ | -------------------------------------------------------- |
| ussd_type | 字符串 | 1：交互式USSD，会话继续。<br>2:   非交互式USSD, 回话结束 |
| ussd_str  | 字符串 | 返回内容，如果为空则继续; 超过40次即失败; 有内容则为成功 |

###### response对象

| 字段             | 类型   | 说明                  |
| ---------------- | ------ | --------------------- |
| setting_response | 字符串 | OK为成功，ERROR为失败 |

##### 特别说明



##### 示例

###### response

```json
{
	"ussd": {
		"ussd_type": "2",
		"ussd_str": ""
	},
	"response": {
		"setting_response": "OK"
	}
}
```

