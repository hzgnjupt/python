# -*- coding: utf-8 -*-

""" 检查VPN主机的连接速度（线程池实现） """

import os
import re
import string
from multiprocessing import Pool
 
class CheckResult:
    def __init__(self, svr, val):
        self.svr = svr
        self.val = val
    def __str__(self):
        return '%s %d' % (self.svr, self.val)

def ping(addr):
    tot = 0
    cnt = 0
    for line in os.popen('ping ' + addr).readlines():
        m = re.match('.*=(\\d+)ms.*', line)
        if m is not None:
            tot += string.atoi(m.group(1))
            cnt += 1
    if cnt > 0:
        return CheckResult(addr, tot / cnt)

def checkAddr(svr, cnt):
    for i in xrange(1, cnt + 1):
        ars.append(pool.apply_async(ping, ('%s%02d.yesvpn1.info' % (svr, i),)))

if __name__ == '__main__':
    pool = Pool()
    ars = []  # applyResults
    checkAddr('tw', 4)
    checkAddr('jp', 4)
    checkAddr('kr', 5)
    checkAddr('us', 9)
    checkAddr('hk', 6)
    crs = [ar.get() for ar in ars if ar.get() is not None]  # checkResults
    for cr in crs:
        print cr
    
