#!/usr/bin/python
# -*- coding: UTF-8 -*-
#每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示，时间间隔是以秒为单位的浮点小数。
import time # 引入time模块
import calendar #引入日历模块

def main():
  ticks = time.time()  #获取当前时间戳，单位为秒
  print "当前时间戳为:", ticks

  localtime = time.localtime(time.time())
  print "本地时间为 :", localtime

  localtime = time.asctime( time.localtime(time.time()) )
  print "本地时间为 :", localtime

  print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

  print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

  print '现在是：%s' %(time.strftime("%H:%M:%S", time.localtime()))

  #a = "Sat Mar 28 22:24:24 2016"
  #print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

  cal = calendar.month(2017, 6)
  print "以下输出2017年6月份的日历:"
  print cal;

if __name__ == '__main__':
  main()
