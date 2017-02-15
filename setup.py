#-*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pip

def install(package):
    pip.main(['install', package])

install('git+git://github.com/ernw/python-wcfbin.git')

setup(
    name='openair',
    version='0.1.17',
    keywords = ('aqi', 'air', 'china'),
    description='This project is to fetch data from the official Silverlight application of Ministry of Environmental Protection of China (http://106.37.208.233:20035/), which publish realtime air quality. 本项目旨在方便地获取官方发布的中国空气质量数据。',
    license='MIT',
    author='hebingchang',
    author_email='hebingchang@sjtu.edu.cn',
    url='https://ovo.qaq.ac.cn',
    platforms = 'any',
    packages = ['openair', 'openair.data'],
    install_requires = ["xmltodict", "wcf-binary-parser==0.5.3"],
    dependency_links = ['http://github.com/ernw/python-wcfbin/tarball/master#egg=wcf-binary-parser-0.5.3']
)

