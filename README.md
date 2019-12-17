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
python shopee.spec
```