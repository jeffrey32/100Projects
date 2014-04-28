#!/usr/bin/env python

import requests
from lxml import etree
import StringIO
import datetime

import sqlite3
conn = sqlite3.connect('stocks.db')
c = conn.cursor()

#c.execute('CREATE TABLE stocks (date text, symbol text, price real)')


def get_price():
    user_raw = str(raw_input("Enter stock symbol: ")).lower()
    url = "http://au.finance.yahoo.com/q?s=" + user_raw
    source = requests.get(url).text

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO.StringIO(source), parser)

    xpath_price = tree.xpath(".//*[contains(@id, 'yfs_l84_')]/text()")
    xpath_title = tree.xpath(".//*[@id='yfi_rt_quote_summary']/div[1]/div/h2/text()")

    if xpath_title:
        xpath_title = xpath_title[0]
    if xpath_price:
        xpath_price = xpath_price[0]
    

    if not xpath_price:
        print "%s doesn't exist, exiting." % user_raw.upper()
        exit(0)
    print '\n', xpath_title , '\n'


    ### Check if table exists in DB
    try:
        c.execute('SELECT * FROM stocks')
    except sqlite3.OperationalError:
        c.execute('CREATE TABLE IF NOT EXISTS stocks (date text, symbol text, price real)')
        print "Creating table 'stocks'."


    ### Pull last price for stock from DB ###
    query_get = (xpath_title,)
    c.execute("SELECT * FROM stocks WHERE symbol=(?) ORDER BY date DESC limit(1)", query_get)
    query_result = c.fetchone()
    if query_result:
        print "Last Price: $",query_result[2], "On :", query_result[0][:-7]


    ### Pull lowest price the stock has been from DB ###
    c.execute("SELECT * FROM stocks WHERE symbol=(?) ORDER BY price limit(1)", query_get)
    query_result = c.fetchone()
    if query_result:
        print "Lowest:", query_result[2]
    else:
        print "First time %s has been searched, no previous data." % xpath_title


    ### Pull highest price the stock has been from DB ###
    c.execute("SELECT * FROM stocks WHERE symbol=(?) ORDER BY price DESC limit(1)", query_get)
    query_result = c.fetchone()
    if query_result:
        print "Highest:", query_result[2]
    else:
        pass


    ###  Insert current stock into DB  ###
    d = str(datetime.datetime.now())
    query_insert = (d,xpath_title,xpath_price)
    c.execute("INSERT INTO stocks VALUES (?,?,?)", query_insert)
    conn.commit()

    conn.close()


    print "Current price: $%s" % (xpath_price)


if __name__ == "__main__":
    get_price()

