# -*- coding: utf-8 -*-
"""
Created on 2018年1月2日
@author: Leo
"""
import socket
import threading

lock = threading.Lock()
openNum = 0
threads = []


class PortScanner:
    def __init__(self):
        self.port_list = []

    def port_scanner(self, host, port):
        global openNum
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = s.connect_ex((host, port))
            if res == 0:
                lock.acquire()
                openNum += 1
                # print('[+] %d open' % port)
                self.port_list.append(port)
                lock.release()
            else:
                s.close()
        except Exception as err:
            print(err)

    def entrance(self, host=None) -> dict:
        socket.setdefaulttimeout(1)
        # print('Scanning the host:%s......' % host)
        for p in range(1, 65536):
            t = threading.Thread(target=self.port_scanner, args=(host, p))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
        # print('[*] The host:%s scan is complete!' % host)
        # print('[*] A total of %d open port ' % openNum)
        return {"IP_Address": host, "Port": self.port_list, "msg": "Success"}
