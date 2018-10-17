#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock/
# Subject:  Best Time to Buy and Sell Stock 买卖股票的最佳时机 
#########################################################################
def maxProfit(prices):
    total = 0
    low = float("inf")

    for price in prices:
        if price - low > total:
            print "cur price: {0}, cur low:{1}, cur total: {2}".format(price, low, total)
            total = price - low
        if price < low:
            print "pre low: {0}, cur low: {1}".format(low, price)
            low = price
    return total

prices =  [3,2,3,1,2]
print maxProfit(prices)
