# -*- coding: UTF-8 -*-
"""
Created on 2017年12月27日
@author: Leo
"""

import json

# 第三方库
from flask_restful import Resource
from pyecharts import Gauge, Style

# 项目内部库
from backend.common.system_info import SystemChecker

# 初始化
system = SystemChecker(lang="en")


# 系统信息
class SystemInfo(Resource):
    @staticmethod
    def get():
        return json.loads(system.get_system_info())


# 内存信息
class MemoryChecker(Resource):
    def __init__(self):
        self._style = Style(width=1440, height=900)

    def draw_gauge(self, data):
        chart = Gauge("", **self._style.init_style)
        chart.add("", "内存使用率", data['percent'].replace("%", ""))
        return chart.options

    def get(self):
        json_result = dict(json.loads(system.get_memory_dict()))
        graph_result = self.draw_gauge(data=json_result['data'][0])
        json_result.update(dict(graph=graph_result))
        print(json_result)
        return json_result


# CPU信息
class CpuChecker(Resource):
    @staticmethod
    def get():
        return json.loads(system.get_cpu_info())


# 用户信息
class UserInfo(Resource):
    @staticmethod
    def get():
        return json.loads(system.get_user_start_time())


# 进程信息
class ProcessInfo(Resource):
    @staticmethod
    def get():
        return json.loads(system.get_process_info())


# 可用端口信息
class UsingPortInfo(Resource):
    @staticmethod
    def get():
        return json.loads(system.get_port_info())
