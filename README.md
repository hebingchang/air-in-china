# air in China / Openair
This project is to fetch data from the official Silverlight application of Ministry of Environmental Protection of China (http://106.37.208.233:20035/), which publish realtime air quality.

本项目旨在从国家官方空气质量发布平台(http://106.37.208.233:20035/) 的Silverlight程序中获取空气质量数据，便于处理后进行二次开发。

## Install
via pip (recommanded):

    pip install openair

手动安装:

    git clone https://github.com/hebingchang/air-in-china
    cd air-in-china
    python setup.py install

## Usage

    #-*- encoding: utf-8 -*-
    from openair import air_class
    air = air_class.airChina()
    
    # 获取所有气象站点详细数据
    print air.getAllStationsData()
    
    # 获取省内所有站点数据, 其中:
    # 至少提供一个参数, 即省/直辖市. type参数可选, 当不提供时默认为0.
    # type = 0:按省id查找(如'9'), 1:按省名称查找(如'上海'), 2:按省拼音查找(如'shanghai')
    # 按拼音查找时需注意: 山西=shanxi, 陕西=shan_xi
    print air.getProvinceStationsData("shanghai", type=2) 
    
    # 获取所有省/直辖市
    print air.getAllProvinceName()
    
    # 获取某省所有城市
    # 必须提供1个参数: 省id; 可以通过getAllProvinceName()方法查找省id
    air.getProvinceAllCityName(12)
    
    # 获取某省所有站点信息
    # 必须提供1个参数: 省id
    air.getProvinceAllStationInfo(10)
    
    # 获取某市所有站点信息
    # 必须提供2个参数: 省id, 市名(unicode)
    # 市名可以通过getProvinceAllCityName()方法获取
    air.getCityAllStationInfo(10, u"苏州市")
    
    # 获取某市历史AQI
    # 必须提供1个参数: 市id / 市名
    # 如下例, 传递310000与传递u'上海市'的效果是相同的.
    air.getCityHistory(310000)

### Return values
    
    # 为方便观察数据结构, 所有返回的JSON数据均经过格式化.
    
    # 所有气象站点详细数据
    [{
        "Area": "北京市",
        "CO_24h": "3.1",
        "Latitude": "39.8673",
        "O3": "64",
        "PM10_24h": "—",
        "NO2": "160",
        "O3_24h": "2",
        "Unheathful": "健康人运动耐受力降低，有明显强烈症状，提前出现某些疾病",
        "SO2_24h": "41",
        "PM2_5_24h": "247",
        "AQI": "329",
        "ProvinceId": "1",
        "PM2_5": "279",
        "CO": "4.3",
        "O3_8h": "39",
        "Longitude": "116.366",
        "O3_8h_24h": "29",
        "SO2": "53",
        "TimePoint": "2017-02-15T22:00:00",
        "StationCode": "1001A",
        "OrderId": "1",
        "CityCode": "110000",
        "PositionName": "万寿西宫",
        "PM10": "—",
        "PrimaryPollutant": "细颗粒物(PM2.5)",
        "NO2_24h": "120",
        "Measure": "老年人和病人应当留在室内，避免体力消耗，一般人群应避免户外活动",
        "IsPublish": "true",
        "Quality": "严重污染"
    }
    ......
    ]
    
    # 获取所有省/直辖市
    {
        "1": [
            "北京",
            "beijing"
        ],
        "2": [
            "天津",
            "tianjin"
        ],
        
        ...
        
        "31": [
            "新疆",
            "xinjiang"
        ]
    }
    
    # 获取某省所有城市
    [
        "滁州市",
        "黄山市",
        ......
        
        "池州市"
    ]
    
    # 获取某市所有站点信息
    [
        {
            "Latitude": "31.2472",
            "StationCode": "1160A",
            "PositionName": "上方山",
            "Longitude": "120.561"
        },
        {
            "Latitude": "31.2864",
            "StationCode": "1161A",
            "PositionName": "南门",
            "Longitude": "120.628"
        },
        ......
        
        {
            "Latitude": "31.3708",
            "StationCode": "1167A",
            "PositionName": "相城区",
            "Longitude": "120.641"
        }
    ]
    
    # 获取某市历史AQI
    [
        {
            "CityCode": "310000",
            "Area": "上海市",
            "Unheathful": "空气质量令人满意，基本无空气污染",
            "Quality": "优",
            "PM2_5_24h": "31",
            "PrimaryPollutant": "—",
            "TimePoint": "2017-02-01T00:00:00",
            "CO_24h": "0.7",
            "PM10_24h": "37",
            "NO2_24h": "20",
            "SO2_24h": "12",
            "Measure": "各类人群可正常活动",
            "O3_8h_24h": "90",
            "AQI": "45",
            "Id": "386477"
        },
        {
            "CityCode": "310000",
            "Area": "上海市",
            "Unheathful": "空气质量令人满意，基本无空气污染",
            "Quality": "优",
            "PM2_5_24h": "21",
            "PrimaryPollutant": "—",
            "TimePoint": "2017-02-02T00:00:00",
            "CO_24h": "0.6",
            "PM10_24h": "27",
            "NO2_24h": "23",
            "SO2_24h": "11",
            "Measure": "各类人群可正常活动",
            "O3_8h_24h": "87",
            "AQI": "44",
            "Id": "386876"
        },
        ......
    ]

## Thanks to
python-wcfbin (https://github.com/ernw/python-wcfbin)

## License
This project is under [the MIT License](https://mit-license.org).

Copyright © 2017

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Afterword
由于国情，我国在数据公开方面的工作的确乏善可陈。

但是，每个国民都应有获知数据的权利，所以我将此项目开源，提供一个从官方渠道获取空气质量数据的途径。