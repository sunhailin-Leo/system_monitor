import platform
import sys
import socket
import os
import time
import threading

threads = []
ip_list = []


def get_os():
    """
    get os 类型
    """
    os_type = platform.system()
    if os_type == "Windows":
        return "n"
    else:
        return "c"


def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()

    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            flag = True
            break
    if flag:
        print("ip: %s is ok ***" % ip_str)
        ip_list.append(ip_str)


def find_ip(ip):
    """
    给出当前的127.0.0 ，然后扫描整个段所有地址
    """
    for i in range(1, 256):
        ip = '%s.%s' % (ip, i)
        t = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    print("start time %s" % time.ctime())
    ip_prefix = socket.gethostbyname(socket.gethostname())
    ip_prefix = '.'.join(ip_prefix.split('.')[:-1])
    find_ip(ip_prefix)
    print("end time %s" % time.ctime())