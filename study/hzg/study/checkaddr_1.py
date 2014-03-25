# -*- coding: utf-8 -*-

""" 检查VPN主机的连接速度（普通线程实现） """

import os
import re
import string
from threading import Thread, RLock

class CheckAddrThread(Thread):
    printlock = RLock()
    def __init__(self, addr):
        Thread.__init__(self)
        self.addr = addr
    def run(self):
        tot = 0
        cnt = 0
        for line in os.popen('ping ' + self.addr).readlines():
            m = re.match('.*=(\\d+)ms.*', line)
            if m is not None:
                tot += string.atoi(m.group(1))
                cnt += 1
        if cnt > 0:
            CheckAddrThread.printlock.acquire()
            print CheckResult(self.addr, tot / cnt)
            CheckAddrThread.printlock.release()

class CheckResult:
    def __init__(self, svr, val):
        self.svr = svr
        self.val = val
    def __str__(self):
        return '%s %d' % (self.svr, self.val)

def checkAddr(svr, cnt):
    for i in xrange(1, cnt + 1):
        CheckAddrThread('%s%02d.yesvpn1.info' % (svr, i)).start()

if __name__ == '__main__':
    checkAddr('tw', 4)
    checkAddr('jp', 4)
    checkAddr('kr', 5)
    checkAddr('us', 9)
    checkAddr('hk', 6)
