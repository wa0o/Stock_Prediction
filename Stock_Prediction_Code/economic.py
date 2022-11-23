import pandas as pd
import baostock as bs
import time


def create_data(number):
    lg = bs.login(user_id="anonymous", password="123456")  # needn't resign, just enter this code

    t = time.localtime()
    year = t.tm_year
    month = t.tm_mon
    day = t.tm_mday
    localtime = str(year) + '-' + str(month) + '-' + str(day)

    # number = 601318
    stock_number = 'sh.' + str(number)
    fields = "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,\
    peTTM,pbMRQ,psTTM,pcfNcfTTM,isST"
    rs = bs.query_history_k_data(stock_number, fields, start_date='2018-01-01', end_date=localtime, frequency="d",
                                 adjustflag="3")
    data_list = []
    while rs.next():
        data_list.append(rs.get_row_data())
    data = pd.DataFrame(data_list, columns=rs.fields)
    # Look at the first five rows of the data
    data.head()
    # output data
    data.to_csv('data\\' + str(number) + '.csv')


# create_data()
