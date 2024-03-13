# 胃食道逆流判讀系統建置
## 問題描述
此資料集為蒐集24小時胃食道相關數據，由於醫師於診斷方面需要查看24小時的連續數據並找出有發生胃食道逆流的區段，但發生時機短，同時需要2位醫師進行審查，因此整個判讀過程十分繁複。
由於目前使用系統判讀效率不佳，醫院方想透過重新建置一套判讀系統，此專案為系統前端建置及串接後端判讀系統。
## 使用工具
* Adobe XD: 介面繪製及使用者經驗設計
* Pycharm: 撰寫程式編譯器
* Python: 撰寫程式
  * 使用套件: PyQt, Tensorflow, Plotly, numpy, pandas
## 程式說明
1. 主要分為執行檔及UI設計檔，由於是使用Python進行程式撰寫，因此需要將UI檔(html & css) 轉換為py執行檔。
2. 第2頁作為轉換檔案程式，需要透過程式呼叫本機的傳換檔案程式。
3. 後續第3頁為分析頁面，作為串街後段判讀演算法
4. 最後於第4頁顯示圖表於使用者，並根據使用者需求可以調整範圍及長度。
5. 增加額外更新模型的地方。
## 示範影片
<https://www.youtube.com/watch?v=sRtgTmftVCw>
## 程式流程
* 主程式: Main.py
* 副頁面:
  * secondUI_First_page.py
  * secondUI_DataExtract_page.py
  * secondUI_Analysis_1_page.py
  * secondUI_show_picture_page.py
  * secondUI_Back_login_page.py
  * secondUI_Back_updata_page.py
  * secondUI_Back_Success_page.py
  * secondUI_login_failed_page.py
* 環境: Main.spec
* 資源庫: XD_2_rc.py
