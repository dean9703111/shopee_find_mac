# shopee_find_mac
這是我個人為了方便在蝦皮上找到符合自己需求的mac時所寫的python程式

### 事前安裝
python 2.7
```
https://www.python.org/downloads/release/python-2717/
```
相關套件
```
pip install xlsxwriter
```
如果你想要製作出來給大家用，打包 .py 檔

Windows
```
pip install pyinstaller
pyinstaller -F shopee.py
```
Mac
```
sudo pip install pyinstaller --upgrade --ignore-installed
pyinstaller -F shopee.py
```
#### 執行dist資料夾裡面的執行檔，檔案會直接跑到桌面

#### 或是你可以直接下指令如下
```
python shopee.py --keyword='macbook pro' --totalCount=1000 --conditions --price_min=32000 --price_max=45000 --start_year=2015 --min_RAM=16
```

### 參數說明
```
|  參數   | 型態  | 說明  | 預設值  |
|  ----  | ----  | ----  | ----  |
| keyword  | 字串 |  搜尋關鍵字 | 'macbook pro' |
| search_limit  | 數字整數 |  要搜尋多少筆資訊，50倍數為佳 | 100 |
| conditions  | 字串 |  used(二手)/new(全新) | None |
| price_min  | 數字整數 |  最低價格 | 32000 |
| price_max  | 數字整數 |  最高價格 | 45000 |
| start_year  | 數字整數 |  mac開始年份 | 2015 |
| min_RAM  | 數字整數 |  最小RAM接受度 | 16 |
```