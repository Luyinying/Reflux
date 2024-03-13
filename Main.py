import numpy as np
from scipy.signal import find_peaks
import os
import pandas as pd
import time
import tensorflow as tf
from sklearn import preprocessing
import logging
tf.get_logger().setLevel(logging.ERROR) # 刪除會跑出warring的句子
import win32process
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from secondUI_First_page import Ui_Form
from secondUI_DataExtract_page import Ui_Ui_Page2
from secondUI_Analysis_1_page import Ui_Ui_Page3
from secondUI_Back_login_page import Ui_Ui_back_1
from secondUI_Back_updata_page import Ui_Ui_back_2
from secondUI_show_picture_page import Ui_Ui_show_picture
from secondUI_Back_Success_page import Ui_Ui_Back_3
from secondUI_login_failed_page import Ui_Ui_B_04
import dash
import dash_html_components as html
import dash_core_components as dcc
from os.path import isfile, isdir, join
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import sys
import webbrowser



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
class Dialog_Back_04(QMainWindow, Ui_Ui_B_04):
    def __init__(self):
        super(Dialog_Back_04, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.home_btn_02.clicked.connect(self.homepage_b4)
        self.exit_btn_02.clicked.connect(self.leave_b4)
        self.OK_btn_02.clicked.connect(self.OK_b4)

    def homepage_b4(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

    def leave_b4(self):
        app = QApplication.instance()
        app.quit()

    def OK_b4(self):
        self.hide()
        self.dialog_B_01 = Dialog_Back_01()
        self.dialog_B_01.show()
        self.dialog_B_01.raise_()

class Dialog_Back_03(QMainWindow, Ui_Ui_Back_3):
    def __init__(self):
        super(Dialog_Back_03, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.home_B_3.clicked.connect(self.homepage_b3)
        self.exit_B_3.clicked.connect(self.leave_b3)
        self.Leave_btn.clicked.connect(self.Leave_F)

    def homepage_b3(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

    def leave_b3(self):
        app = QApplication.instance()
        app.quit()

    def Leave_F(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

#更新模型介面
class Dialog_Back_02(QMainWindow, Ui_Ui_back_2):
    global all_modol #儲存模型路徑
    all_modol = []
    def __init__(self):
        super(Dialog_Back_02, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.home_b_2.clicked.connect(self.homepage_b2)
        self.exit_b_2.clicked.connect(self.leave_b2)
        self.update_btn.clicked.connect(self.update_02)
        self.more_btn_6s.clicked.connect(self.more_01)
        self.more_btn_11s.clicked.connect(self.more_02)
        self.more_btn_21s.clicked.connect(self.more_03)

    def homepage_b2(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

    def leave_b2(self):
        app = QApplication.instance()
        app.quit()

    def more_01(self):
        global modol_6s_add  # 宣告區域變數
        modol_6s_add = QtWidgets.QFileDialog.getOpenFileName(self,"標題",".","*.h5") #讀單個資料
        print(modol_6s_add)
        self.modol_6s_lab.setText(modol_6s_add[0])
        modol_6s_add = modol_6s_add[0] #僅寫入路徑
        print(modol_6s_add)
        all_modol.append(modol_6s_add) #更新模型路徑

    def more_02(self):
        global modol_11s_add  # 宣告區域變數
        modol_11s_add = QtWidgets.QFileDialog.getOpenFileName(self,"標題",".","*.h5")
        self.modol_11s_lab.setText(modol_11s_add[0])
        modol_11s_add = modol_11s_add[0]
        all_modol.append(modol_11s_add)


    def more_03(self):
        global modol_21s_add  # 宣告區域變數
        modol_21s_add = QtWidgets.QFileDialog.getOpenFileName(self,"標題",".","*.h5")
        self.modol_21s_lab.setText(modol_21s_add[0])
        modol_21s_add = modol_21s_add[0]
        all_modol.append(modol_21s_add)


    def update_02(self):
        self.hide()
        self.dialog_B_03 = Dialog_Back_03()
        self.dialog_B_03.show()
        self.dialog_B_03.raise_()
        print(all_modol)

        #轉成陣列、並存成CSV
        a = pd.DataFrame(all_modol)
        aa = a.T
        aa.columns = ['6s','11s','21s']
        aa.to_csv('D:/Lab2022/modolTest/'+'modol_new.csv')


class Dialog_Back_01(QMainWindow, Ui_Ui_back_1):
    def __init__(self):
        super(Dialog_Back_01, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.home_b_1.clicked.connect(self.homepage_b1)
        self.exit_b_1.clicked.connect(self.leave_b1)
        self.login_btn.clicked.connect(self.login_01)
        self.account_lab.setText('e')
        self.password_lab.setText('l')


    def homepage_b1(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

    def leave_b1(self):
        app = QApplication.instance()
        app.quit()

    def login_01(self):
        val_username = self.account_txt.text()
        val_pass = self.password_txt.text()
        #驗證帳號密碼
        if val_username == 'User' and val_pass == '0000':
            self.hide()
            self.dialog_back2 = Dialog_Back_02()
            self.dialog_back2.show()
            self.dialog_back2.raise_()
        else:
            self.hide()
            self.dialog_B_04 = Dialog_Back_04()
            self.dialog_B_04.show()
            self.dialog_B_04.raise_()

class Dialog_04(QMainWindow, Ui_Ui_show_picture):
    def __init__(self):
        super(Dialog_04, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.home_btn_5.clicked.connect(self.homepage_5)
        self.exit_btn_5.clicked.connect(self.Leave_05)
        self.OK_btn.clicked.connect(self.show_picture)

    def homepage_5(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

    def Leave_05(self):
        app = QApplication.instance()
        app.quit()

    def show_picture(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

        csvsave = []  # 設定空集合(檔案CSV)
        # # 找到儲存的檔案路徑
        os.chdir('D:/Lab2022/csv_iloc/')
        path = 'D:/Lab2022/csv_iloc/CSV_iloc/'
        dirs = os.listdir(path)
        dirs.sort()
        dirs.sort(key=lambda x: str(x[:-4]))  # 排序
        
        savedir = []  # 設定空集合(資料夾)
        # 讀取當按路徑下的所有資料夾
        for i in dirs:
            a = join(path, i)
            if isdir(a):
                savedir.append(a + '/')
                print('目錄:', i, '路徑:', a)
        print(savedir)
        
        # csvsave = []   # 設定空集合(檔案CSV)
        # 讀取資料夾下的所有CSV
        for j in range(len(savedir)):
            b = savedir[j]
            dir_1 = os.listdir(b)
            dir_1.sort()
            dir_1.sort(key=lambda x: str(x[:-6]))
            for z in dir_1:
                c = join(b, z)
                if isfile(c):
                    csvsave.append(c)
                    print('檔案:', z, '路徑', c)
        
        app = dash.Dash(
            __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
        )
        app.title = 'Plotly for reflux'
        server = app.server
        app.config.suppress_callback_exceptions = True
        
        def description_card():
            return html.Div(
                id="description-card",
                children=[
                    html.H3("Relux Plot"),
                    html.H5("Welcome to the Relux Plot"),
                ],
            )
        
        def generate_control_card():
            global csv_select
            return html.Div(
                id="control-card",
                children=[
                    html.P("Select CSV"),
                    dcc.Dropdown(
                        id="csv_select",
                        options=[{"label": i, "value": i} for i in csvsave],
                        value=csvsave[0],
                    ),
                    # html.Br(),
                    # html.Div(
                    #     id="reset-btn-outer",
                    #     children=html.Button(id="reset-btn", children="Reset", n_clicks=0),
                    # ),
                ],
            )
        
        app.layout = html.Div(
            id="app-container",
            children=[
                # Banner
                html.Div(
                    id="banner",
                    className="banner",
                ),
                # Left column
                html.Div(
                    id="left-column",
                    className="four columns",
                    children=[description_card(), generate_control_card()]
                             + [
                                 html.Div(
                                     ["initial child"], id="output-clientside", style={"display": "none"}
                                 )
                             ],
                ),
                # # Right column
                # html.Div(
                #     id="right-columns",
                #     children=[generate_patient_plotly()]
                # ),
                dcc.Graph(id='plotly_try')
            ],
        )
        
        @app.callback(
            Output("plotly_try", "figure"),
            [Input('csv_select', 'value')]
        )
        def generate_patient_plotly(csv_select):
            df = pd.read_csv(csv_select)
            if csv_select == ('D:/Lab2022/csv_iloc/CSV_iloc/2413/2413_15.csv'):
                path_3 = r'D:\Lab2022\TRY\Raw_Data\Subject_test_data\2413\6s'
                dirs = os.listdir(path_3)
                dirs.sort()
                dirs.sort(key=lambda x: str(x[:-4]))
                checkcsv_2 = []  # 設定空集合(資料夾)
                # 讀取當按路徑下的所有資料夾
                aa = '.csv'
                for i in dirs:
                    a = join(path_3, i)
                    if isfile(a):
                        b = i
                        b = ''.join(i for i in b if i not in aa)  # 刪除.csv名字 以方便後續查找
                        checkcsv_2.append(b)
                        print('目錄:', i, '路徑:', a)
                print(checkcsv_2)
                finalcsv = []
                df_2 = pd.read_csv(r'D:\Lab2022\TRY\predict_result\part1\2413_pred_LPR.csv')
                df_2.columns = ['No', "Time", "Singal"]
                print(df_2)
                for i in df_2['No']:
                    if i in checkcsv_2:
                        finalcsv.append(path_3 + '/' + i + ".csv")
                print(finalcsv)
                Beforetime = []
                Aftertime = []
        
                for k in finalcsv:
                    df_3 = pd.read_csv(f'{k}')
                    df_3_list = list(df_3['Time'])  # 以list的方式儲存
                    time_F = df_3_list[0]  # 取第一個值
                    time_A = df_3_list[-1]  # 取最後一個值
                    Beforetime.append(time_F)
                    Aftertime.append(time_A)
                    fig = go.Figure()
        
                    # Add traces
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_1), name='Channel_1', marker={'color': '#008080'},
                                   yaxis='y8'))
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_2), name='Channel_2', marker={'color': '#778899'},
                                   yaxis='y7'))
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_3), name='Channel_3', marker={'color': '#778899'},
                                   yaxis='y6'))
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_4), name='Channel_4', marker={'color': '#778899'},
                                   yaxis='y5'))
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_5), name='Channel_5', marker={'color': '#778899'},
                                   yaxis='y4'))
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_6), name='Channel_6', marker={'color': '#778899'},
                                   yaxis='y3'))
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_7), name='Channel_7', marker={'color': '#778899'},
                                   yaxis='y2'))
                    fig.add_trace(
                        go.Scatter(x=list(df.Time), y=list(df.Channel_8), name='Channel_8', marker={'color': '#ff7f50'},
                                   yaxis='y1'))
                    # Update axes
                    fig.update_layout(
                        yaxis1=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0, 0.115],
                            linecolor="#ff7f50",
                            mirror=True,
                            range=[0, 8],
                            showline=True,
                            side="right",
                            tickfont={"color": "#ff7f50"},
                            tickmode="auto",
                            ticks="",
                            title="ph",
                            titlefont={"color": "#ff7f50"},
                            type="linear",
                            zeroline=False
                        ),
                        yaxis2=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0.125, 0.24],
                            linecolor="#778899",
                            mirror=True,
                            range=[0, 10000],
                            showline=True,
                            side="right",
                            tickfont={"color": "#778899"},
                            tickmode="auto",
                            ticks="",
                            titlefont={"color": "#778899"},
                            type="linear",
                            zeroline=False
                        ),
                        yaxis3=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0.25, 0.365],
                            linecolor="#778800",
                            mirror=True,
                            range=[0, 10000],
                            showline=True,
                            side="right",
                            tickfont={"color": "#778800"},
                            tickmode="auto",
                            ticks="",
                            titlefont={"color": "#778800"},
                            type="linear",
                            zeroline=False
                        ),
                        yaxis4=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0.375, 0.49],
                            linecolor="#778665",
                            mirror=True,
                            range=[0, 10000],
                            showline=True,
                            side="right",
                            tickfont={"color": "#778665"},
                            tickmode="auto",
                            ticks="",
                            titlefont={"color": "#778665"},
                            type="linear",
                            zeroline=False
                        ),
                        yaxis5=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0.5, 0.615],
                            linecolor="#776666",
                            mirror=True,
                            range=[0, 10000],
                            showline=True,
                            side="right",
                            tickfont={"color": "#776666"},
                            tickmode="auto",
                            ticks="",
                            titlefont={"color": "#776666"},
                            type="linear",
                            zeroline=False
                        ),
                        yaxis6=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0.626, 0.74],
                            linecolor="#755576",
                            mirror=True,
                            range=[0, 10000],
                            showline=True,
                            side="right",
                            tickfont={"color": "#755576"},
                            tickmode="auto",
                            ticks="",
                            titlefont={"color": "#755576"},
                            type="linear",
                            zeroline=False
                        ),
                        yaxis7=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0.75, 0.865],
                            linecolor="#700099",
                            mirror=True,
                            range=[0, 10000],
                            showline=True,
                            side="right",
                            tickfont={"color": "#700099"},
                            tickmode="auto",
                            ticks="",
                            titlefont={"color": "#700099"},
                            type="linear",
                            zeroline=False
                        ),
                        yaxis8=dict(
                            anchor="x",
                            autorange=True,
                            domain=[0.875, 1],
                            linecolor="#ff7f50",
                            mirror=True,
                            range=[0, 8],
                            showline=True,
                            side="right",
                            tickfont={"color": "#ff7f50"},
                            tickmode="auto",
                            ticks="",
                            title="ph",
                            titlefont={"color": "#ff7f50"},
                            type="linear",
                            zeroline=False
                        )
                    )
        
                    fig.update_layout(
                        shapes=[
                            dict(fillcolor="rgba(250, 250, 0, 0.5)", line={"width": 0}, type='rect',
                                 x0=time_F,
                                 x1=time_A,
                                 xref='x',
                                 y0=0,
                                 y1=1,
                                 yref='paper'
                                 )
                        ]
                    )
                # # 秒、分
                fig.update_xaxes(
                    rangeslider_visible=False,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1s", step="second", stepmode="backward"),
                            dict(count=5, label="5s", step="second", stepmode="backward"),
                            dict(count=1, label="1m", step="minute", stepmode="backward"),
                            dict(step="all")
                        ])
        
                    ),
                    # 滑輪
                    rangeslider=dict(
                        visible=True
                    )
                )
                # Update layout
                fig.update_layout(
                    dragmode="zoom",
                    hovermode="x",
                    legend=dict(traceorder="reversed"),
                    height=600,
                    template="plotly_white",
                    margin=dict(
                        t=100,
                        b=100
                    ),
                )
        
                return fig
            else:
                path_2 = r'D:\Lab2022\TRY\Raw_Data\Subject_test_data\2413\6s'
                dirs = os.listdir(path_2)
                dirs.sort()
                dirs.sort(key=lambda x: str(x[:-4]))  # 排序
        
                checkcsv = []  # 設定空集合(資料夾)
                # 讀取當按路徑下的所有資料夾
                gg = '.csv'
                for i in dirs:
                    a = join(path_2, i)
                    if isfile(a):
                        b = i
                        b = ''.join(i for i in b if i not in gg)  # 刪除.csv名字 以方便後續查找
                        checkcsv.append(b)
                        print('目錄:', i, '路徑:', a)
                print(checkcsv)
        
                fig = go.Figure()
        
                # Add traces
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_1), name='Channel_1', marker={'color': '#008080'},
                               yaxis='y8'))
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_2), name='Channel_2', marker={'color': '#778899'},
                               yaxis='y7'))
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_3), name='Channel_3', marker={'color': '#778899'},
                               yaxis='y6'))
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_4), name='Channel_4', marker={'color': '#778899'},
                               yaxis='y5'))
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_5), name='Channel_5', marker={'color': '#778899'},
                               yaxis='y4'))
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_6), name='Channel_6', marker={'color': '#778899'},
                               yaxis='y3'))
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_7), name='Channel_7', marker={'color': '#778899'},
                               yaxis='y2'))
                fig.add_trace(
                    go.Scatter(x=list(df.Time), y=list(df.Channel_8), name='Channel_8', marker={'color': '#ff7f50'},
                               yaxis='y1'))
                # Update axes
                fig.update_layout(
                    yaxis1=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0, 0.115],
                        linecolor="#ff7f50",
                        mirror=True,
                        range=[0, 8],
                        showline=True,
                        side="right",
                        tickfont={"color": "#ff7f50"},
                        tickmode="auto",
                        ticks="",
                        title="ph",
                        titlefont={"color": "#ff7f50"},
                        type="linear",
                        zeroline=False
                    ),
                    yaxis2=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0.125, 0.24],
                        linecolor="#778899",
                        mirror=True,
                        range=[0, 10000],
                        showline=True,
                        side="right",
                        tickfont={"color": "#778899"},
                        tickmode="auto",
                        ticks="",
                        titlefont={"color": "#778899"},
                        type="linear",
                        zeroline=False
                    ),
                    yaxis3=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0.25, 0.365],
                        linecolor="#778800",
                        mirror=True,
                        range=[0, 10000],
                        showline=True,
                        side="right",
                        tickfont={"color": "#778800"},
                        tickmode="auto",
                        ticks="",
                        titlefont={"color": "#778800"},
                        type="linear",
                        zeroline=False
                    ),
                    yaxis4=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0.375, 0.49],
                        linecolor="#778665",
                        mirror=True,
                        range=[0, 10000],
                        showline=True,
                        side="right",
                        tickfont={"color": "#778665"},
                        tickmode="auto",
                        ticks="",
                        titlefont={"color": "#778665"},
                        type="linear",
                        zeroline=False
                    ),
                    yaxis5=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0.5, 0.615],
                        linecolor="#776666",
                        mirror=True,
                        range=[0, 10000],
                        showline=True,
                        side="right",
                        tickfont={"color": "#776666"},
                        tickmode="auto",
                        ticks="",
                        titlefont={"color": "#776666"},
                        type="linear",
                        zeroline=False
                    ),
                    yaxis6=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0.626, 0.74],
                        linecolor="#755576",
                        mirror=True,
                        range=[0, 10000],
                        showline=True,
                        side="right",
                        tickfont={"color": "#755576"},
                        tickmode="auto",
                        ticks="",
                        titlefont={"color": "#755576"},
                        type="linear",
                        zeroline=False
                    ),
                    yaxis7=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0.75, 0.865],
                        linecolor="#700099",
                        mirror=True,
                        range=[0, 10000],
                        showline=True,
                        side="right",
                        tickfont={"color": "#700099"},
                        tickmode="auto",
                        ticks="",
                        titlefont={"color": "#700099"},
                        type="linear",
                        zeroline=False
                    ),
                    yaxis8=dict(
                        anchor="x",
                        autorange=True,
                        domain=[0.875, 1],
                        linecolor="#ff7f50",
                        mirror=True,
                        range=[0, 8],
                        showline=True,
                        side="right",
                        tickfont={"color": "#ff7f50"},
                        tickmode="auto",
                        ticks="",
                        title="ph",
                        titlefont={"color": "#ff7f50"},
                        type="linear",
                        zeroline=False
                    )
                )
                fig.update_xaxes(
                    rangeslider_visible=False,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1s", step="second", stepmode="backward"),
                            dict(count=5, label="5s", step="second", stepmode="backward"),
                            dict(count=1, label="1m", step="minute", stepmode="backward"),
                            dict(step="all")
                        ])
        
                    ),
                    # 滑輪
                    rangeslider=dict(
                        visible=True
                    )
                )
                # Update layout
                fig.update_layout(
                    dragmode="zoom",
                    hovermode="x",
                    legend=dict(traceorder="reversed"),
                    height=600,
                    template="plotly_white",
                    margin=dict(
                        t=100,
                        b=100
                    ),
                )
                return fig
        
        app.run_server(debug=True)


        webbrowser.open("http://127.0.0.1:8050/")

# 第三頁-輸入檔案
class Dialog_03(QMainWindow, Ui_Ui_Page3):
    def __init__(self):
        super(Dialog_03, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.home_btn_3.clicked.connect(self.homepage_3)
        self.Exit_btn_3.clicked.connect(self.leave_3)
        self.more_btn_1.clicked.connect(self.csv_1)
        self.more_btn_2.clicked.connect(self.save_1)
        self.Analysis_btn_3.clicked.connect(self.Analysis_3)

    def homepage_3(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

    def leave_3(self):
        app = QApplication.instance()
        app.quit()

    def csv_1(self):
        global csv_address # 宣告區域變數
        global path # 宣告區域變數
        csv_address = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.csv_lab.setText(csv_address)

        path = csv_address + "/"
        print(path)


    def save_1(self):
        global save_address # 宣告區域變數
        global save_path # 宣告區域變數
        save_address = QFileDialog.getExistingDirectory(self, "open folder", "/")
        self.save_lab.setText(save_address)

        save_path = save_address + "/"
        print(save_path)


    def Analysis_3(self):
        global modol_address
        modol_address = pd.read_csv('D:/Lab2022/modolTest/modol_new.csv')
        self.hide()
        self.dialog_04 = Dialog_04()
        self.dialog_04.show()
        self.dialog_04.raise_()

        os.chdir(save_path)

        dirs = os.listdir(path)

        ''' 原資料 '''
        dirs.sort()
        dirs.sort(key=lambda x: str(x[:-4]))
        df_path = pd.DataFrame(dirs)
        df_path.columns = ['path']
        df_path['path'] = path + df_path['path']
        ''' 創建資料夾 '''

        def creat_file():
            path_test = "./Raw_Data/Subject_test_data/"
            # 如果沒有資料夾則創建
            if not os.path.isdir(path_test):
                os.makedirs(path_test)
            dirs = os.listdir(path_test)
            if dirs == []:
                os.mkdir(path_test + df_path['path'][0][len(path) + 4:len(path) + 8])
                os.mkdir(path_test + df_path['path'][0][len(path) + 4:len(path) + 8] + "/6s")
                os.mkdir(path_test + df_path['path'][0][len(path) + 4:len(path) + 8] + "/11s")
                os.mkdir(path_test + df_path['path'][0][len(path) + 4:len(path) + 8] + "/21s")
                dirs = os.listdir(path_test)
            dirs.sort()
            dirs.sort(key=lambda x: str(x[:-4]))
            df_path_test = pd.DataFrame(dirs)
            df_path_test.columns = ['path']
            df_path_test['path'] = path_test + df_path_test['path']

            for j in range(len(df_path)):
                count = 0
                for i in range(len(df_path_test)):
                    if df_path_test['path'][i][len(path_test):len(path_test) + 4] != df_path['path'][j][
                                                                                     len(path) + 4:len(path) + 8]:
                        count += 1
                    else:
                        break
                if count == len(df_path_test):
                    os.mkdir(path_test + df_path['path'][j][len(path) + 4:len(path) + 8])
                    os.mkdir(path_test + df_path['path'][j][len(path) + 4:len(path) + 8] + "/6s")
                    os.mkdir(path_test + df_path['path'][j][len(path) + 4:len(path) + 8] + "/11s")
                    os.mkdir(path_test + df_path['path'][j][len(path) + 4:len(path) + 8] + "/21s")


        creat_file()

        path_test = "./Raw_Data/Subject_test_data/"

        def creat_singal_df():
            LPRD = df.set_index(['Time'])
            print('####################################')
            print('############## creat data ##############')
            print('####################################')
            for indx_5 in range(len(data_final)):
                timeString = data_final['Date'][indx_5] + ' ' + data_final['Time'][indx_5]  # 時間格式為字串
                struct_time = time.strptime(timeString, "%Y-%m-%d %H:%M:%S")  # 轉成時間元組
                time_stamp = int(time.mktime(struct_time))  # 轉成時間戳
                time_stamp_before_6s = time_stamp - 5
                time_stamp_after_6s = time_stamp + 1
                time_stamp_before_11s = time_stamp - 10
                time_stamp_after_11s = time_stamp + 1
                time_stamp_before_21s = time_stamp - 20
                time_stamp_after_21s = time_stamp + 1
                struct_time_before_6s = time.localtime(time_stamp_before_6s)  # 轉成時間元組
                struct_time_after_6s = time.localtime(time_stamp_after_6s)  # 轉成時間元組
                struct_time_before_11s = time.localtime(time_stamp_before_11s)  # 轉成時間元組
                struct_time_after_11s = time.localtime(time_stamp_after_11s)  # 轉成時間元組
                struct_time_before_21s = time.localtime(time_stamp_before_21s)  # 轉成時間元組
                struct_time_after_21s = time.localtime(time_stamp_after_21s)  # 轉成時間元組
                timeString_before_6s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time_before_6s)  # 轉成字串
                timeString_after_6s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time_after_6s)  # 轉成字串
                timeString_before_11s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time_before_11s)  # 轉成字串
                timeString_after_11s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time_after_11s)  # 轉成字串
                timeString_before_21s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time_before_21s)  # 轉成字串
                timeString_after_21s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time_after_21s)  # 轉成字串

                data_6s = path_test + df_path['path'][i][len(path) + 4:len(path) + 8] + "/6s/" + df_path['path'][i][
                                                                                                 len(path) + 4:len(
                                                                                                     path) + 8] + "_" + f"{indx_5}".zfill(
                    3)
                LPR = LPRD[f'{timeString_before_6s}':f'{timeString_after_6s}']
                LPR.to_csv(data_6s + '.csv')

                data_11s = path_test + df_path['path'][i][len(path) + 4:len(path) + 8] + "/11s/" + df_path['path'][i][
                                                                                                   len(path) + 4:len(
                                                                                                       path) + 8] + "_" + f"{indx_5}".zfill(
                    4)
                LPR = LPRD[f'{timeString_before_11s}':f'{timeString_after_11s}']
                LPR.to_csv(data_11s + '.csv')

                data_21s = path_test + df_path['path'][i][len(path) + 4:len(path) + 8] + "/21s/" + df_path['path'][i][
                                                                                                   len(path) + 4:len(
                                                                                                       path) + 8] + "_" + f"{indx_5}".zfill(
                    5)
                LPR = LPRD[f'{timeString_before_21s}':f'{timeString_after_21s}']
                LPR.to_csv(data_21s + '.csv')

            print(df_path['path'][i][len(path) + 4:len(path) + 8], "Finsh")
            print('################ end ####################')
            print()

        ''' 創建訊號 '''
        auto_patient_record = {}
        result_pred_path = './predict_result/part1/'
        if not os.path.isdir(result_pred_path):
            os.makedirs(result_pred_path)
        start = time.time()
        for i in range(len(df_path)):
            df = pd.read_csv(df_path['path'].values[i])
            ########## 高峰 ##########

            ####### 抓取Ch1數值 #########
            answer = df.set_index(['Time'])  # 讓Time 當index
            answer_data = answer.drop(
                ['Channel_2', 'Channel_3', 'Channel_4', 'Channel_5', 'Channel_6', 'Channel_7', 'Channel_8'],
                axis=1)  # 去掉不要的欄位
            answer_data = answer_data[0: answer_data.shape[0] - 30000]  # 去掉後面雜訊
            Ch1_data = answer_data
            Ch1_data.loc['new', :] = 8
            ########## 抓取Ch1 CH1_peaks ##########
            inputSignal = np.array(Ch1_data)
            Ch1_Signal = np.reshape(inputSignal, (inputSignal.shape[0],))
            CH1_H_peaks, CH1_properties = find_peaks(Ch1_Signal, prominence=(1.0, None), distance=3,
                                                     height=(0.05, None))  # (1,10) 1最低要1以上   10-->最高不超過10
            ######## 抓取Ch8數值 #########
            answer = df.set_index(['Time'])  # 讓Time 當index
            answer_data = answer.drop(
                ['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4', 'Channel_5', 'Channel_6', 'Channel_7'],
                axis=1)  # 去掉不要的欄位
            answer_data = answer_data[0: answer_data.shape[0] - 30000]  # 去掉後面雜訊
            Ch8_data = answer_data
            Ch8_data.loc['new', :] = 8
            ########## 抓取Ch1 CH8_peaks ##########
            inputSignal_8 = np.array(Ch8_data)
            Ch8_Signal = np.reshape(inputSignal_8, (inputSignal_8.shape[0],))
            CH8_H_peaks, CH8_properties = find_peaks(Ch8_Signal, prominence=(0.5, None), distance=3,
                                                     height=(0.05, None))  # (1,10) 1最低要1以上   10-->最高不超過10

            ### 建立 前10個 index 都是相似點 #####
            ### 不要相似點 剩下的都要 #####
            peak_data = np.ones(answer_data.shape[0] - 1)
            peak_data = pd.DataFrame(peak_data)
            for indx_1 in CH8_H_peaks:
                for add_1 in range(2):
                    if indx_1 - add_1 in set(CH1_H_peaks):
                        peak_data.iloc[indx_1 - add_1] = 0

            ########## 抓低峰 ##########

            ######## 抓取Ch1數值 #########
            answer = df.set_index(['Time'])  # 讓Time 當index
            answer_data = answer.drop(
                ['Channel_2', 'Channel_3', 'Channel_4', 'Channel_5', 'Channel_6', 'Channel_7', 'Channel_8'],
                axis=1)  # 去掉不要的欄位
            answer_data = answer_data[0: answer_data.shape[0] - 30000]  # 去掉後面雜訊
            Ch1_data = answer_data
            # Ch1_data.loc['new',:] = 9
            ########## 抓取Ch1_Signal ##########
            inputSignal = np.array(Ch1_data)
            Ch1_Signal = np.reshape(inputSignal, (inputSignal.shape[0],))
            CH1_peaks, CH1_properties = find_peaks(-Ch1_Signal, prominence=(0.7, None), height=(-5.2, -0.05), wlen=1500)

            ##### 疑似咽喉逆流點 #####
            Ch1_data = Ch1_data.reset_index()
            Ch1_data = Ch1_data.drop(['Time'], axis=1)
            LPR_data = np.zeros(answer_data.shape[0])
            LPR_data = pd.DataFrame(LPR_data)
            for indx_2 in CH1_peaks:
                if (Ch1_data[indx_2:indx_2 + 1].min().sum() < Ch1_data[indx_2 - 360:indx_2 - 7].min().sum()) and (
                        Ch1_data[indx_2:indx_2 + 1].min().sum() <= Ch1_data[indx_2 + 6:indx_2 + 121].min().sum()):
                    LPR_data.iloc[indx_2] = 1
                # elif Ch1_data[indx_2:indx_2+1].min().sum() == Ch1_data[indx_2-5:indx_2].min().sum(): #(抓一些漏掉的疑似逆流點)
                #   LPR_data.iloc[indx_2] = 1

            ######## 抓取Ch8數值 #########
            answer = df.set_index(['Time'])  # 讓Time 當index
            answer_data = answer.drop(
                ['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4', 'Channel_5', 'Channel_6', 'Channel_7'],
                axis=1)  # 去掉不要的欄位\
            answer_data = answer_data[0: answer_data.shape[0] - 30000]  # 去掉後面雜訊
            Ch8_data = answer_data
            # Ch8_data.loc['new',:] = 9
            ########## 抓取Ch8_Signal ##########
            inputSignal_8 = np.array(Ch8_data)
            Ch8_Signal = np.reshape(inputSignal_8, (inputSignal_8.shape[0],))
            CH8_peaks, CH8_properties = find_peaks(-Ch8_Signal, prominence=(0.7, None), distance=3,
                                                   height=(-6, -0.05))  # (1,10) 1最低要1以上   10-->最高不超過10

            ### 建立 前10個 index 都是相似點 #####
            ### 不要相似點 剩下的都要 #####
            new_data = np.ones(answer_data.shape[0])
            new_data = pd.DataFrame(new_data)
            for indx_3 in CH8_peaks:
                for add_2 in range(2):
                    if (indx_3 - add_2 in set(CH1_peaks)):
                        new_data.iloc[indx_3 - add_2] = 0

            ########## 讓Channel_8 讓PH<4 等於1  PH>4 等於0 ##########
            ch8_1 = answer_data['Channel_8']
            ch8_1[ch8_1 <= 4.0] = 1
            answer_data['Channel_8'] = ch8_1

            ch8_2 = answer_data['Channel_8']
            ch8_2[ch8_2 > 4.0] = 0
            answer_data['Channel_8'] = ch8_2

            Ch8_data = answer_data

            ##### 抓疑似逆流之PH<4.0 #####
            Ch8_data = Ch8_data.reset_index()
            Ch8_data = Ch8_data.drop(['Time'], axis=1)
            for indx_4 in CH1_peaks:
                if (Ch8_data[indx_4 - 350:indx_4 + 350].sum() > 1).any() == True:
                    Ch8_data.iloc[indx_4] = 1

            # ########## 抓取Ch1在Ch8 PH<4的數值 ##########
            Ch8_data = np.array(Ch8_data)
            new_data = np.array(new_data)
            peak_data = np.array(peak_data)
            LPR_data = np.array(LPR_data)
            Ch8_data = np.reshape(Ch8_data, (Ch8_data.shape[0],))
            new_data = np.reshape(new_data, (new_data.shape[0],))
            peak_data = np.reshape(peak_data, (peak_data.shape[0],))
            LPR_data = np.reshape(LPR_data, (LPR_data.shape[0],))
            PH_low4 = new_data * Ch8_data * LPR_data * peak_data
            # PH_low4 = Ch8_data * LPR_data
            PH_low4 = pd.DataFrame(PH_low4)
            answer_data.reset_index(inplace=True)
            PH_low4_inCh1 = pd.concat([answer_data, PH_low4], axis=1)
            PH_low4_inCh1 = PH_low4_inCh1.drop(['Channel_8'], axis=1)
            PH_low4_inCh1.columns = ["Time", "PH_low4_inCh1"]
            PH_low4_inCh1 = PH_low4_inCh1.set_index(['Time'])  # 讓Time 當index
            if PH_low4_inCh1.sum().any() > 0:
                data_deal = PH_low4_inCh1[PH_low4_inCh1 == 1]
                data_deal.dropna(inplace=True)
                data_deal.reset_index(inplace=True)  # 重設index
                datetime_obj = data_deal['Time'].str.split('.', expand=True)
                datetime_obj = pd.DataFrame(datetime_obj)
                datetime_obj.columns = ['Time', 'pick_micrsecond']
                datetime_obj = datetime_obj['Time'].str.split(' ', expand=True)
                datetime_obj.columns = ['Date', 'Time']
                datetime_obj = datetime_obj.set_index(["Date"])
                data_final = datetime_obj['Time'].drop_duplicates()
                data_final = data_final.reset_index()

                ####### 去除連續數值 1 2 3 4 連續 最長連續4秒
                Time_data = np.ones(data_final.shape[0])
                Time_data = pd.DataFrame(Time_data)

                for a in data_final.index:
                    if data_final.shape[0] < 5:
                        break
                    if a == data_final.shape[0] - 4:
                        break
                    timeString_now = '2020-11-11' + ' ' + data_final['Time'][a]  # 時間格式為字串
                    struct_time_now = time.strptime(timeString_now, "%Y-%m-%d %H:%M:%S")  # 轉成時間元組
                    time_stamp_now = int(time.mktime(struct_time_now))  # 轉成時間戳

                    timeString_1 = '2020-11-11' + ' ' + data_final['Time'][a + 1]  # 時間格式為字串
                    struct_time_1 = time.strptime(timeString_1, "%Y-%m-%d %H:%M:%S")  # 轉成時間元組
                    time_stamp_1 = int(time.mktime(struct_time_1))  # 轉成時間戳

                    if time_stamp_1 - time_stamp_now == 1:
                        Time_data.iloc[a + 1:a + 2] = 0

                data_final = pd.concat([data_final, Time_data], axis=1)
                data_final = data_final.set_index(['Time', 'Date'])  # 讓Time 當index
                data_final = data_final[data_final == 1]
                data_final.dropna(inplace=True)
                data_final.reset_index(inplace=True)  # 重設indexdata2
                data_final = data_final.drop([0], axis=1)
                print(df_path['path'][i][len(path) + 4:len(path) + 8], 'shaep = ', data_final.shape)
                creat_singal_df()
                auto_patient_record[df_path['path'][i][len(path) + 4:len(path) + 8]] = data_final.shape[0]
            else:
                print(df_path['path'].values[i][len(path) + 4:len(path) + 8] + ' LPR = 0')
                auto_patient_record[df_path['path'].values[i][len(path) + 4:len(path) + 8]] = 0

        end = time.time()
        print("執行時間：%f 秒" % (end - start))
        (pd.DataFrame.from_dict(data=auto_patient_record, orient='index', columns=['auto number'])
         .to_csv(result_pred_path + 'auto_pred_result.csv'))

        """ Prediction """
        start = time.time()
        for j in range(len(df_path)):
            path_6s = path_test + df_path['path'][j][len(path) + 4:len(path) + 8] + "/6s/"
            output_File_6s = []
            allList2 = os.listdir(path_6s)
            allList2.sort()
            for indx in allList2:
                path_data_6 = path_6s + "/" + f"{indx}"
                output_File_6s.append(path_data_6)
            File_6s = pd.DataFrame({'file_name': output_File_6s})

            path_11s = path_test + df_path['path'][j][len(path) + 4:len(path) + 8] + "/11s/"
            output_File_11s = []
            allList2 = os.listdir(path_11s)
            allList2.sort()
            for indx in allList2:
                path_data_11 = path_11s + "/" + f"{indx}"
                output_File_11s.append(path_data_11)
            File_11s = pd.DataFrame({'file_name': output_File_11s})

            path_21s = path_test + df_path['path'][j][len(path) + 4:len(path) + 8] + "/21s/"

            output_File_21s = []
            allList2 = os.listdir(path_21s)
            allList2.sort()
            for indx in allList2:
                path_data_21 = path_21s + "/" + f"{indx}"
                output_File_21s.append(path_data_21)
            File_21s = pd.DataFrame({'file_name': output_File_21s})

            model_6s = tf.keras.models.load_model(f'{modol_address["6s"][0]}')
            abnor = []
            nor = []
            pred_to_nor = {}
            pred_to_abnor = {}

            for i in range(File_6s['file_name'].count()):
                normal_6s = pd.read_csv(f"{File_6s['file_name'].iloc[i]}", na_values=['NA', '?'])
                original_normal_data = normal_6s.drop(['Time'], axis=1)
                maxab_scaler = preprocessing.MaxAbsScaler()
                normal_6s_data = maxab_scaler.fit_transform(original_normal_data)
                normal_6s_data = normal_6s_data.astype('float32')
                normal_6s_data = np.reshape(normal_6s_data, (1, 300, 8))
                predictions_6s = model_6s.predict(normal_6s_data, batch_size=1)

                if predictions_6s.argmax(axis=1) == 1:
                    abnor.append(File_6s['file_name'].iloc[i][len(path_6s) + 1:-4])
                    pred_to_abnor[File_6s['file_name'].iloc[i][len(path_6s) + 1:-4]] = normal_6s['Time'].iloc[
                                                                                           251] + ',6s_model'
                    print(File_6s['file_name'].iloc[i][len(path_6s) + 1:-4] + ' is abnormal  = ',
                          predictions_6s.argmax(axis=1))
                    print(File_6s['file_name'].iloc[i][len(path_6s) + 1:-4] + ' is abnormal in 6s_model  ')
                    print("Time is :", normal_6s['Time'].iloc[250])
                else:
                    model_11s = tf.keras.models.load_model(f'{modol_address["11s"][0]}')
                    normal_11s = pd.read_csv(f"{File_11s['file_name'].iloc[i]}", na_values=['NA', '?'])
                    original_normal_data = normal_11s.drop(['Time'], axis=1)
                    maxab_scaler = preprocessing.MaxAbsScaler()
                    normal_11s_data = maxab_scaler.fit_transform(original_normal_data)
                    normal_11s_data = normal_11s_data.astype('float32')
                    normal_11s_data = np.reshape(normal_11s_data, (1, 550, 8))
                    predictions_11s = model_11s.predict(normal_11s_data, batch_size=1)

                    if predictions_11s.argmax(axis=1) == 1:
                        abnor.append(File_11s['file_name'].iloc[i][len(path_11s) + 1:-4])
                        pred_to_abnor[File_11s['file_name'].iloc[i][len(path_11s) + 1:-4]] = normal_11s['Time'].iloc[
                                                                                                 451] + ',11s_model'
                        print(File_11s['file_name'].iloc[i][len(path_11s) + 1:-4] + ' is abnormal  = ',
                              predictions_11s.argmax(axis=1))
                        print(File_11s['file_name'].iloc[i][len(path_11s) + 1:-4] + ' is abnormal in 11s_model ')
                        print("Time is :", normal_11s['Time'].iloc[450])
                    else:
                        model_21s = tf.keras.models.load_model(f'{modol_address["21s"][0]}')
                        normal_21s = pd.read_csv(f"{File_21s['file_name'].iloc[i]}", na_values=['NA', '?'])
                        original_normal_data = normal_21s.drop(['Time'], axis=1)
                        maxab_scaler = preprocessing.MaxAbsScaler()
                        normal_21s_data = maxab_scaler.fit_transform(original_normal_data)
                        normal_21s_data = normal_21s_data.astype('float32')
                        normal_21s_data = np.reshape(normal_21s_data, (1, 1050, 8))
                        predictions_21s = model_21s.predict(normal_21s_data, batch_size=1)
                        if predictions_21s.argmax(axis=1) == 1:
                            abnor.append(File_21s['file_name'].iloc[i][len(path_21s) + 1:-4])
                            pred_to_abnor[File_21s['file_name'].iloc[i][len(path_21s) + 1:-4]] = \
                                normal_21s['Time'].iloc[1001] + ',21s_model'
                            print(File_21s['file_name'].iloc[i][len(path_21s) + 1:-4] + ' is abnormal  = ',
                                  predictions_21s.argmax(axis=1))
                            print(File_21s['file_name'].iloc[i][len(path_21s) + 1:-4] + ' is abnormal in 21s_model ')
                            print("Time is :", normal_21s['Time'].iloc[1000])
                        else:
                            nor.append(File_21s['file_name'].iloc[i][len(path_21s) + 1:-4])
                            pred_to_nor[File_21s['file_name'].iloc[i][len(path_21s) + 1:-4]] = normal_21s['Time'].iloc[
                                1000]
                            print(File_21s['file_name'].iloc[i][len(path_21s) + 1:-4] + ' is Normal  = ',
                                  predictions_21s.argmax(axis=1))
                            print("Time is :", normal_21s['Time'].iloc[1000])

                print('-' * 50)
                print()
            if pred_to_abnor == {}:
                continue
            else:
                ABNOR = pd.DataFrame.from_dict(data=pred_to_abnor, orient='index', columns=['Time'])
                ABNOR = ABNOR['Time'].str.split(',', expand=True)
                ABNOR.columns = ['Time', 'Singal']
                ABNOR.to_csv(result_pred_path + df_path['path'][j][len(path) + 4:len(path) + 8] + '_pred_LPR.csv')

        end = time.time()
        print("執行時間：%f 秒" % (end - start))
        print('-' * 50)
        print()
        print('Finish')


# 第二頁-轉換檔案
class Dialog_02(QMainWindow, Ui_Ui_Page2):
    def __init__(self):
        super(Dialog_02, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.home_btn_2.clicked.connect(self.homepage)
        self.Exit_btn_2.clicked.connect(self.leave_2)
        self.Analysis_btn_2.clicked.connect(self.Analysis_2)

    def homepage(self):
        self.hide()
        self.dialog_01 = MyMainWindow()
        self.dialog_01.show()
        self.dialog_01.raise_()

    def leave_2(self):
        app = QApplication.instance()
        app.quit()

    def Analysis_2(self):
        self.hide()
        self.dialog_03 = Dialog_03()
        self.dialog_03.show()
        self.dialog_03.raise_()

# 首頁
class MyMainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.Data_Extract_btn_1.clicked.connect(self.DataExtract_1)
        self.Exit_btn_1.clicked.connect(self.leave_1)
        self.Analysis_btn.clicked.connect(self.Analysis_1)
        self.User_btn.clicked.connect(self.User_01)

    def DataExtract_1(self):
        self.hide()
        self.dialog_02 = Dialog_02()
        self.dialog_02.show()
        self.dialog_02.raise_()
        win32process.CreateProcess("C:\\Sandhill\\Utilities\\DataExtract\\Sandhill.Utility.DataExtract.exe", "", None,
                                   None, 0, win32process.CREATE_NO_WINDOW, None, None, win32process.STARTUPINFO())

    def leave_1(self):
        app = QApplication.instance()
        app.quit()

    def Analysis_1(self):
        self.hide()
        self.dialog_03 = Dialog_03()
        self.dialog_03.show()
        self.dialog_03.raise_()

    def User_01(self):
        self.hide()
        self.dialog_back01 = Dialog_Back_01()
        self.dialog_back01.show()
        self.dialog_back01.raise_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())