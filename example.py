#-*- encoding: utf-8 -*-
import json
from openair import air_class

air = air_class.airChina()

# Get data of all air matters from each station in China
allData = air.getAllStationsData()
print json.dumps(allData[0])

# Get data of all substations in one province
# type      search by
# 0         pid
# 1         Chinese name
# 2         Chinese pinyin

provinceData = air.getProvinceStationsData("shanghai", type=2)
print json.dumps(provinceData)

# Get all province names
AllProvince = air.getAllProvinceName()
print json.dumps(AllProvince)

# Get all cities of the province(pid)
AllCity = air.getProvinceAllCityName(12)
print json.dumps(AllCity)

# Get all stations of the province(pid)
AllProvinceStation = air.getProvinceAllStationInfo(10)
print json.dumps(AllProvinceStation)

# Get all stations of the city(pid & city name)
AllCityStation = air.getCityAllStationInfo(10, u"苏州市")
print json.dumps(AllCityStation)

# Get city AQI history
# param: city name or city code
cityHistory = air.getCityHistory(u"上海市")
print json.dumps(cityHistory)
