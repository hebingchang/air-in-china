#-*- encoding: utf-8 -*-
import StringIO, requests, re, base64, zlib, xmltodict, json
from io import BytesIO
from wcf.records import *
from wcf.xml2records import XMLParser
import function.station_data

# https://github.com/ernw/python-wcfbin

class airChina():
    def __init__(self):
        self.provinceList = json.loads(function.station_data.provinceList_json)

    def pListSearch(self, fromform, value):
        if fromform == 0:
            return {value: self.provinceList[str(value)]}
        else:
            for i in self.provinceList:
                if self.provinceList[i][fromform-1].lower() == value.lower():
                    return {i: self.provinceList[str(i)]}
        return None

    def getResponse(self, action, data):
        output = StringIO.StringIO()
        output.write('<'+action+' xmlns="http://tempuri.org/">'+data+'</'+action+'>')
        output.seek(0)

        r = XMLParser.parse(output)
        req = dump_records(r)

        r = requests.post(url='http://106.37.208.233:20035/ClientBin/Env-CnemcPublish-RiaServices-EnvCnemcPublishDomainService.svc/binary/'+action,
            data=req,
            headers={'Content-Type': 'application/msbin1'})
        res = r.content

        buf = BytesIO(res)
        r = Record.parse(buf)

        print_records(r, fp=output)
        output.seek(0)

        pat = re.compile('<[^>]+>')
        enc = pat.sub('', output.readlines()[1][1:])[:-1]

        enc = base64.b64decode(enc)
        enc = zlib.decompress(enc)

        convertedDict = xmltodict.parse(enc)
        return json.dumps(convertedDict)

    #getInfo("GetProvincePublishLives", "<pid>9</pid>")
    #getInfo("GetAreaIaqiPublishLive", "<area>上海市</area>")
    #getInfo("GetCityDayAqiHistoryByCondition", "<cityCode>310000</cityCode>")
    def getAllStationsData(self):
        return json.loads(self.getResponse("GetAllAQIPublishLive", ""))["ArrayOfAQIDataPublishLive"]["AQIDataPublishLive"]

    def getProvinceStationsData(self, province, type=0):
        # 0: pid
        # 1: Chinese name
        # 2: Pinyin

        if type == 0:
            return json.loads(self.getResponse("GetProvincePublishLives", "<pid>"+str(province)+"</pid>"))["ArrayOfAQIDataPublishLive"]["AQIDataPublishLive"]
        else:
            pinfo = self.pListSearch(type, province)
            if pinfo != None:
                return json.loads(self.getResponse("GetProvincePublishLives", "<pid>"+str(pinfo.keys()[0])+"</pid>"))["ArrayOfAQIDataPublishLive"]["AQIDataPublishLive"]
            else:
                return None

    def getAllProvinceName(self):
        return json.loads(function.station_data.provinceList_json)

    def getProvinceAllCityName(self, pid):
        pjson = json.loads(function.station_data.stationList_json)
        ret = []
        for c in pjson[str(pid)]:
            ret.append(c)

        return ret

    def getProvinceAllStationInfo(self, pid):
        pjson = json.loads(function.station_data.stationList_json)
        ret = []
        for c in pjson[str(pid)]:
            for s in pjson[str(pid)][c]:
                ret.append(s)

        return ret

    def getCityAllStationInfo(self, pid, cityname):
        pjson = json.loads(function.station_data.stationList_json)
        try:
            return pjson[str(pid)][cityname]
        except:
            return None

    def searchCity(self, city):
        sjson = json.loads(function.station_data.cityList_json)
        city = str(city)
        if sjson.has_key(city):
            return {city: sjson[city]}
        else:
            for c in sjson:
                if sjson[c] == city:
                    return {c: sjson[c]}

        return None

    def getCityHistory(self, city):
        return json.loads(self.getResponse("GetCityDayAqiHistoryByCondition", "<cityCode>"+self.searchCity(city).keys()[0]+"</cityCode>"))["ArrayOfCityDayAQIPublishHistory"]["CityDayAQIPublishHistory"]

    #def getAreaAQI(self):
        # return json.loads(self.getResponse("ArrayOfIAQIDataPublishLive", u"<area>上海市</area>"))

