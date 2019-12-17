# -*- coding: UTF-8 -*-
import requests
import csv
import xlsxwriter
import json
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def shopee_scraper(keyword, limit='50', conditions=None, price_min=None, price_max=None):
    # url = 'https://shopee.tw/search?keyword=' + keyword + '&page=' + n_page + '&sortBy=relevancy'
    url = 'https://shopee.tw/api/v2/search_items/?by=price&keyword=' + keyword + '&limit=' + limit
    if conditions:
        url += '&conditions=' + conditions
    if price_min:
        url += '&price_min=' + str(price_min)
    if price_max:
        url += '&price_max=' + str(price_max)

    # print (url)
    headers = {
        'User-Agent': 'Googlebot',
    }

    r = requests.get(url, headers=headers)

    api1_data = json.loads(r.text)
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('shopee.xlsx')
    worksheet = workbook.add_worksheet()
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    titles = ['名稱', '價格', '螢幕尺寸', '年份', 'RAM', 'ROM', 'CPU', '商品連結']
    for title in (titles):
        worksheet.write(row, col, title)
        col += 1
    workbook.close()


    # row += 1
    # for data in api1_data['items']:
    #     url2 = 'https://shopee.tw/api/v2/item/get?itemid=' + str(data['itemid']) + '&shopid=' + str(data['shopid'])
    #     r = requests.get(url2, headers=headers)
    #     api2_data = json.loads(r.text)
    #     name = data['name'].encode('utf-8')
    #     # 用name去分析出 螢幕尺寸 年份 RAM ROM CPU
    #     screenSizeArr = ['12"', '13"', '13.3"', '15"', '16"',
    #                      '12″', '13″', '13.3″', '15″', '16″',
    #                      '12吋', '13吋', '13.3吋', '15吋', '16吋',
    #                      '12寸', '13寸', '13.3寸', '15寸', '16寸',
    #                      '12', '13', '13.3', '15', '16']
    #     yearArr = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    #     RAMArr = ['8g', '16g', '32g', '8G', '16G', '32G', '8', '16', '32']
    #     ROMArr = ['128G', '256G', '512G', '1T', '128g', '256g', '512g', '1t', '128', '256', '512']
    #     CPUArr = ['i5', 'i7', 'i9']
    #     macScreenSize = macYear = macRAM = macROM = macCPU = ''
    #     for screenSize in screenSizeArr:
    #         if name.find(screenSize) != -1:
    #             macScreenSize = screenSize
    #     for year in yearArr:
    #         if name.find(year) != -1:
    #             macYear = year
    #     for RAM in RAMArr:
    #         if name.find(RAM) != -1:
    #             macRAM = RAM
    #     for ROM in ROMArr:
    #         if name.find(ROM) != -1:
    #             macROM = ROM
    #     for CPU in CPUArr:
    #         if name.find(CPU) != -1:
    #             macCPU = CPU
    #
    #     price = str(api2_data['item']['price'] / 100000)
    #     shopUrl = 'https://shopee.tw/' + name + '-i.' + str(data['shopid']) + '.' + str(data['itemid'])
    #
    #     itemInfo = [name, price, macScreenSize, macYear, macRAM, macROM, macCPU, shopUrl]
    #     for itemInfo in (itemInfo):
    #         worksheet.write(row, col, itemInfo)
    #         col += 1
    #
    #     row += 1
    #     time.sleep(0.1)

# shopee_scraper(keyword,limit,conditions,price_min,price_max)
shopee_scraper('macbook pro', '1', None, '20000', '40000')




# -*- coding: UTF-8 -*-
import requests
import csv
import json
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def shopee_scraper(keyword, limit='50', conditions=None, price_min=None, price_max=None):
    # url = 'https://shopee.tw/search?keyword=' + keyword + '&page=' + n_page + '&sortBy=relevancy'
    url = 'https://shopee.tw/api/v2/search_items/?by=price&keyword=' + keyword + '&limit=' + limit
    if conditions:
        url += '&conditions=' + conditions
    if price_min:
        url += '&price_min=' + str(price_min)
    if price_max:
        url += '&price_max=' + str(price_max)

    # print (url)
    headers = {
        'User-Agent': 'Googlebot',
    }

    r = requests.get(url, headers=headers)

    api1_data = json.loads(r.text)
    with open('shpee.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['名稱', '價格', '螢幕尺寸', '年份', 'RAM', 'ROM', 'CPU', '商品連結'])
        for data in api1_data['items']:
            url2 = 'https://shopee.tw/api/v2/item/get?itemid=' + str(data['itemid']) + '&shopid=' + str(data['shopid'])
            r = requests.get(url2, headers=headers)
            api2_data = json.loads(r.text)
            name = data['name'].encode('utf-8')
            # 用name去分析出 螢幕尺寸 年份 RAM ROM CPU
            screenSizeArr = ['12"', '13"', '13.3"', '15"', '16"',
                             '12″', '13″', '13.3″', '15″', '16″',
                             '12吋', '13吋', '13.3吋', '15吋', '16吋',
                             '12寸', '13寸', '13.3寸', '15寸', '16寸',
                             '12', '13', '13.3', '15', '16']
            yearArr = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
            RAMArr = ['8g', '16g', '32g', '8G', '16G', '32G', '8', '16', '32']
            ROMArr = ['128G', '256G', '512G', '1T', '128g', '256g', '512g', '1t', '128', '256', '512']
            CPUArr = ['i5', 'i7', 'i9']
            macScreenSize = macYear = macRAM = macROM = macCPU = ''
            for screenSize in screenSizeArr:
                if name.find(screenSize) != -1:
                    macScreenSize = screenSize
            for year in yearArr:
                if name.find(year) != -1:
                    macYear = year
            for RAM in RAMArr:
                if name.find(RAM) != -1:
                    macRAM = RAM
            for ROM in ROMArr:
                if name.find(ROM) != -1:
                    macROM = ROM
            for CPU in CPUArr:
                if name.find(CPU) != -1:
                    macCPU = CPU

            price = str(api2_data['item']['price'] / 100000)
            shopUrl = 'https://shopee.tw/' + name + '-i.' + str(data['shopid']) + '.' + str(data['itemid'])

            filewriter.writerow([name, price, macScreenSize, macYear, macRAM, macROM, macCPU, shopUrl])
            time.sleep(0.1)


# shopee_scraper(keyword,limit,conditions,price_min,price_max)
shopee_scraper('macbook pro', '100', None, '20000', '40000')
