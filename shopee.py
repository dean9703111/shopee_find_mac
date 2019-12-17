# -*- coding: UTF-8 -*-
import requests
import xlsxwriter
import json
import sys
import time
import math
import os
import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--keyword', type=str, default = 'macbook pro')
parser.add_argument('--search_limit', type=int, default=100)
parser.add_argument('--conditions', type=str, default=None)
parser.add_argument('--price_min', type=int, default=32000)
parser.add_argument('--price_max', type=int, default=45000)
parser.add_argument('--start_year', type=int, default=2015)
parser.add_argument('--min_RAM', type=int, default=16)
args = parser.parse_args()


reload(sys)
sys.setdefaultencoding('utf8')
os.chdir(os.path.expanduser("~/Desktop"))

def excel_title(worksheet):
    col = row = 0
    titles = ['名稱', '價格', '螢幕尺寸', '年份', 'RAM', 'ROM', 'CPU', '商品連結']
    # titles = ['RAM', 'ROM', 'CPU']
    for title in titles:
        worksheet.write(row, col, title)
        col += 1


def excel_content(worksheet, data, headers, row, start_year, min_RAM):
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
    soldOutArr = ['已售出', '售出']
    macScreenSize = macYear = macRAM = macROM = macCPU = ''
    jumpItem = False
    
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
    # 過濾掉已經販賣出去的
    for soldOut in soldOutArr:
        if name.find(soldOut) != -1:
            jumpItem = True
    # 確認符合需求才能放入
    if min_RAM:
        if macRAM == '':
            jumpItem = True
        elif int(min_RAM) > int(filter(str.isdigit, macRAM)):
            jumpItem = True
    if start_year:
        if macYear == '':
            jumpItem = True
        elif int(start_year) > int(macYear):
            jumpItem = True

    if jumpItem == False:
        price = str(api2_data['item']['price'] / 100000)
        shopUrl = 'https://shopee.tw/' + name + '-i.' + str(data['shopid']) + '.' + str(data['itemid'])

        itemInfo = [name, price, macScreenSize, macYear, macRAM, macROM, macCPU, shopUrl]
        col = 0
        for info in (itemInfo):
            worksheet.write(row, col, info)
            col += 1
        return True
    else:
        return False

def shopee_scraper(keyword, search_limit=50, conditions=None, price_min=None, price_max=None, start_year=None, RAM=None):
    # url = 'https://shopee.tw/search?keyword=' + keyword + '&page=' + n_page + '&sortBy=relevancy'
    # 確認要跑多少次
    row = 0
    runTimes = int(math.ceil(search_limit / 50))
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('shopee.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column("A:A", 70)  # 設定A列列寬為40
    # Start from the first cell. Rows and columns are zero indexed.
    excel_title(worksheet)
    row += 1
    for runTime in range(0, runTimes):
        url = 'https://shopee.tw/api/v2/search_items/?by=price&keyword=' + keyword + '&limit=50&newest=' + str(
            50 * runTime)
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

        if len(api1_data['items']) == 0:
            break
        for data in api1_data['items']:
            is_insert = excel_content(worksheet, data, headers, row, str(start_year), str(RAM))
            if is_insert:
                row += 1
            # 因為本身內部運算時間也不少，所以似乎不用這個間隔了...
            # time.sleep(0.01)
    workbook.close()


# shopee_scraper(keyword,search_limit,conditions,price_min,price_max,start_year,min_RAM)
shopee_scraper(args.keyword, args.search_limit, args.conditions, args.price_min, args.price_max, args.start_year, args.min_RAM)
