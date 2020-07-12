#!/usr/bin/python3
# coding:utf-8
# -*- coding: utf-8 -*-

import datetime
import tushare as ts
import numpy as np
import scipy.stats as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ts_token = '50b60260a0b87536a2d0231f89b4d5460d97270385f444c0badfe64d'
olderr = np.seterr(all='ignore')


def get_daily_basic(ts_code, days):
    # 定义ts_token
    # 可从推广连接 https://tushare.pro/register?reg=378233 获取
    ts_tokens = '50b60260a0b87536a2d0231f89b4d5460d97270385f444c0badfe64d'

    # 接入tushare api
    pro = ts.pro_api(ts_token)

    # 获取数据的时间范围
    end_date = datetime.date.today().strftime('%Y%m%d')
    start_date = (datetime.date.today() - datetime.timedelta(days=days)).strftime('%Y%m%d')

    # 获取每日指标
    df = pro.daily_basic(ts_code=ts_code, start_date=start_date, end_date=end_date,
                         fields='ts_code,trade_date,close,turnover_rate,volume_ratio,pe,pb,'
                                'total_mv')
    # 存入文件
    # df.to_csv('e:/dat/stock_daily_' + ts_code + '_' + end_date + '.csv')

    return df


def temperature(stock_data):
    # 默认温度50度
    stock_data['pe_temperature'] = 0.5
    stock_data['pb_temperature'] = 0.5

    # 计算每日温度
    for i in range(1, len(stock_data)):
        mean = np.mean(stock_data['pe'][0:(i + 1)])
        std = np.std(stock_data['pe'][0:(i + 1)], ddof=1)
        stock_data['pe_temperature'].iloc[i] = st.norm.cdf(stock_data['pe'].iloc[i], loc=mean,
                                                           scale=std)
        mean = np.mean(stock_data['pb'][0:(i + 1)])
        std = np.std(stock_data['pb'][0:(i + 1)], ddof=1)
        stock_data['pb_temperature'].iloc[i] = st.norm.cdf(stock_data['pb'].iloc[i], loc=mean,
                                                           scale=std)

    stock_data['temperature'] = (stock_data['pe_temperature'] + stock_data['pb_temperature']) * 50
    return stock_data

def plot_data(stock_data):
    stock_data.sort_values(by='trade_date', ascending=True, inplace=True)

    data_length = stock_data.shape[0]
    # data_close = stock_data['close']
    # data_close = (data_close - data_close.min()) / (data_close.max() - data_close.min())
    # data_close = data_close * 100

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.set_title('stock temperature')
    ax1.set_xlabel('time')
    ax1.set_ylabel('temperature')
    ax2.set_ylabel('close')

    xmajorLocator = MultipleLocator(data_length/10)
    ax1.xaxis.set_major_locator(xmajorLocator)
    ax2.xaxis.set_major_locator(xmajorLocator)

    ax1.plot(stock_data['trade_date'], stock_data['temperature'], linestyle='--',
                     marker='.', alpha=0.5,
                     color='r',
                     label='temperature')
    ax2.plot(stock_data['trade_date'], stock_data['close'], linestyle='-',
                     marker='.',
                     color='g',
                     label='close')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # savefig保存图片，dpi分辨率，bbox_inches子图周边白色空间的大小
    # plt.savefig('stock_temperature.jpg', dpi=400, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    stock_data = get_daily_basic('000001.SZ', 365*10)
    stock_data = temperature(stock_data)
    # print(stock_data.head(5))
    plot_data(stock_data)