# -*- coding: UTF-8 -*-
"""
Created on 2017年11月29日
@author: Leo
"""

# 内部库
import sys
import json
import time
import platform
from collections import OrderedDict

# 第三方库
import psutil


# 系统信息查询
class SystemChecker:
    def __init__(self, lang):
        # 系统信息字段
        self.system_dict_en = OrderedDict()
        self.system_dict_zh = OrderedDict()

        # 内存字典字段
        self.memory_dict_en = OrderedDict()
        self.memory_dict_zh = OrderedDict()

        # CPU信息字段
        self.cpu_dict_en = OrderedDict()
        self.cpu_dict_zh = OrderedDict()

        # 用户信息
        self.user_info_en = OrderedDict()
        self.user_info_zh = OrderedDict()

        # 进程信息
        self.process_info_en = OrderedDict()
        self.process_info_zh = OrderedDict()

        # 获取当前内存大小
        self.memory_result = psutil.virtual_memory()

        # 输出语言
        if lang != "en" and lang != "zh":
            raise ValueError("Unsupported language!")
        else:
            self.language = lang

    '''
    工具方法
    '''

    # 转换时间戳
    @staticmethod
    def change_timestamp(timestamp):
        time_local = time.localtime(int(timestamp))
        return str(time.strftime("%Y-%m-%d %H:%M:%S", time_local))

    # 转换容量单位
    @staticmethod
    def bytes_2_human_readable(number_of_bytes):
        """
        转换单位(上限是TB)
        :param number_of_bytes:
        :return: 返回大小 + 单位(字符串)
        """
        if number_of_bytes < 0:
            raise ValueError("!!! number_of_bytes can't be smaller than 0 !!!")

        step_to_greater_unit = 1024.

        number_of_bytes = float(number_of_bytes)
        unit = 'bytes'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'KB'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'MB'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'GB'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'TB'

        precision = 1
        number_of_bytes = round(number_of_bytes, precision)

        return str(number_of_bytes) + unit

    '''
    核心方法
    '''
    def get_system_info(self):
        # 判断操作系统
        system = platform.system()
        system_version = platform.platform()
        system_architecture = platform.architecture()

        json_data = {"data": []}

        self.system_dict_en['sys_name'] = self.system_dict_zh['系统类型'] = system
        self.system_dict_en['sys_version'] = self.system_dict_zh['系统版本'] = system_version

        # 系统不一样
        if system == "Windows":
            self.system_dict_en['sys_info'] = self.system_dict_zh['系统信息'] = "".join(system_version.split("-")[:2]) + " x" + system_architecture[0].replace("bit", "")
        elif system == "Linux":
            if "Ubuntu" in system:
                system_info = system + " " + system_version.split("-")[6:8] + " x" + platform.architecture()[0].replace("bit", "")
                self.system_dict_en['sys_info'] = self.system_dict_zh['系统信息'] = system_info
            elif "centos" in system or "redhat" in system:
                system_info = system + " " + system_version.split("-")[5:7] + " x" + platform.architecture()[0].replace("bit", "")
                self.system_dict_en['sys_info'] = self.system_dict_zh['系统信息'] = system_info
            else:
                self.system_dict_en['info'] = self.system_dict_zh['信息'] = "Unknown Device"
        else:
            self.system_dict_en['info'] = self.system_dict_zh['信息'] = "Unknown Device"

        if self.language is None or self.language == "zh":
            json_data['data'].append(dict(self.system_dict_zh))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)
        elif self.language == "en":
            json_data['data'].append(dict(self.system_dict_en))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)

    # 获取容量大小
    def get_memory_dict(self):
        json_data = {"data": []}
        # 总内存
        self.memory_dict_en['total'] = \
            self.memory_dict_zh['总内存'] = self.bytes_2_human_readable(self.memory_result.total)

        # 可用内存
        self.memory_dict_en['available'] = \
            self.memory_dict_zh['可用内存'] = self.bytes_2_human_readable(self.memory_result.available)

        # 百分比
        self.memory_dict_en['percent'] = \
            self.memory_dict_zh['百分比'] = str(self.memory_result.percent) + "%"

        # 已使用内存
        self.memory_dict_en['used'] = \
            self.memory_dict_zh['已用内存'] = self.bytes_2_human_readable(self.memory_result.used)

        # 剩余内存
        self.memory_dict_en['free'] = \
            self.memory_dict_zh['剩余内存'] = self.bytes_2_human_readable(self.memory_result.free)

        if self.language is None or self.language == "zh":
            json_data['data'].append(dict(self.memory_dict_zh))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)
        elif self.language == "en":
            json_data['data'].append(dict(self.memory_dict_en))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)

    # 获取CPU信息
    def get_cpu_info(self):
        json_data = {"data": []}
        # CPU核数
        self.cpu_dict_en['CPU Core Count'] = \
            self.cpu_dict_zh['CPU核数'] = str(psutil.cpu_count(logical=False))

        # CPU线程数
        self.cpu_dict_en['CPU Thread Count'] = \
            self.cpu_dict_zh['CPU线程数'] = str(psutil.cpu_count())

        if self.language is None or self.language == "zh":
            json_data['data'].append(dict(self.cpu_dict_zh))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)
        elif self.language == "en":
            json_data['data'].append(dict(self.cpu_dict_en))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)

    # 获取本机用户时间和启动时间
    def get_user_start_time(self):
        json_data = {"data": []}
        # 当前用户名
        self.user_info_en['name'] = \
            self.user_info_zh['用户名'] = psutil.users()[0].name

        # 系统启动时间
        self.user_info_en['system_start_time'] = \
            self.user_info_zh['系统启动时间'] = self.change_timestamp(psutil.users()[0].started)

        if self.language is None or self.language == "zh":
            json_data['data'].append(dict(self.user_info_zh))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)
        elif self.language == "en":
            json_data['data'].append(dict(self.user_info_en))
            json_data.update(dict(msg="Success"))
            return json.dumps(json_data, ensure_ascii=False)

    # 获取进程信息
    def get_process_info(self):
        # 创建一个json
        json_data = {"data": []}
        for pid in psutil.pids():
            try:
                # 进程号
                self.process_info_en['PID'] = \
                    self.process_info_zh['进程号'] = pid

                # 进程名
                self.process_info_en['Name'] = \
                    self.process_info_zh['进程名'] = psutil.Process(pid).name()

                # 进程状态
                self.process_info_en['Status'] = \
                    self.process_info_zh['进程状态'] = psutil.Process(pid).status()

                # 进程内存占用率
                self.process_info_en['Percent'] = self.process_info_zh['进程内存使用率'] = str(
                    round(psutil.Process(pid).memory_percent(), 3)) + "%"

                # 进程内存占用大小
                self.process_info_en['MemoryUsed'] = self.process_info_zh['进程内存占用'] = self.bytes_2_human_readable(
                    (psutil.Process(pid).memory_percent() / 100) * self.memory_result.total)

                # 写入json数组
                if self.language is None or self.language == "zh":
                    json_data['data'].append(dict(self.process_info_zh))
                elif self.language == "en":
                    json_data['data'].append(dict(self.process_info_en))
                else:
                    raise ValueError("Unsupported language!")
            except psutil.NoSuchProcess:
                continue
        # 状态
        json_data.update(dict(msg="Success"))

        # 返回
        return json.dumps(json_data, ensure_ascii=False)

    # 获取全部信息
    def get_all(self):
        # 获取信息
        sys_info = json.loads(self.get_system_info())
        memory_info = json.loads(self.get_memory_dict())
        cpu_info = json.loads(self.get_cpu_info())
        user_info = json.loads(self.get_user_start_time())
        process_info = json.loads(self.get_process_info())

        # 输出
        print("---\t操作系统信息\t---")
        for sys_value in sys_info['data']:
            print(sys_value)
        print("\n")

        print("---\t内存使用详情(Memory used info)\t---")
        for memory_value in memory_info['data']:
            print(memory_value)
        print("\n")

        print("---\tCPU详情(CPU used info)\t---")
        for cpu_value in cpu_info['data']:
            print(cpu_value)
        print("\n")

        print("---\t本机用户详情(Computer user info)\t---")
        for user_value in user_info['data']:
            print(user_value)
        print("\n")

        print("---\t进程详情(Process info)\t---")
        for process in process_info['data']:
            print(process)


# 帮助文档
def help_center():
    print("Options and arguments (and corresponding environment variables):")
    print("-l\t:this parameter need a language type, like zh or en.\n\t Chinese and English.")
    print("-h\t:print this help message and exit (also --help)")


if __name__ == '__main__':

    '''
    'Linux - 4.4.0 - 85 - generic - x86_64 - with - Ubuntu - 16.04 - xenial' [6:8]
    'Linux - 2.6.32 - 431.el6.x86_64 - x86_64 - with - centos - 6.5 - Final' [5:7]
    'Linux - 3.10.0 - 514.e17.x86_64 - x86_64 - with - redhat - 7.3 - Maipo' [5:7]
    '''

    try:
        # 获取参数(操作和语言类型)
        options = sys.argv[1:]
        # 如果参数为 -l
        if options[0] == "-l":
            # 如果参数
            language = options[1::1]
            if language[0] != "zh" and language[0] != "en":
                raise ValueError("Language parameter is error!")
            else:
                m = SystemChecker(lang=language[0])
                m.get_all()
        # 如果参数为 -h
        elif options[0] == "-h" or options[0] == "--help":
            help_center()
        # 误操作
        else:
            help_center()
            print("\n")
            raise ValueError("You give wrong option! You need read the doc.")
    except IndexError:
        print("You miss 1 argument!")
        help_center()
