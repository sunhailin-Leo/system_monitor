# -*- coding: UTF-8 -*-
"""
Created on 2017年12月27日
@author: Leo
"""

from flask import Flask, Blueprint
from flask_restful import Api

# 项目路由路径
from backend.resources.monitor import SystemInfo
from backend.resources.monitor import MemoryChecker
from backend.resources.monitor import CpuChecker
from backend.resources.monitor import UserInfo
from backend.resources.monitor import ProcessInfo


# 项目配置文件
BACKEND_CONFIG = "./conf/backend_config.json"


class Backend:
    def __init__(self, mode="dev"):
        # 项目启动模式
        self._mode = mode

        # 项目版本前缀
        self._version_prefix = "/v1"

        # 项目初始化
        self._app = Flask(__name__)
        self._api_bp = Blueprint('api', __name__)
        self._api = Api(self._api_bp)

    @staticmethod
    def _load_config() -> dict:
        """
        加载配置文件(暂时不启用)
        :return: json
        """
        pass

    def _register_router(self):
        """
        注册路由
        """
        self._api.add_resource(SystemInfo, self._version_prefix + "/monitor/info")
        self._api.add_resource(MemoryChecker, self._version_prefix + "/monitor/memory")
        self._api.add_resource(CpuChecker, self._version_prefix + "/monitor/cpu")
        self._api.add_resource(UserInfo, self._version_prefix + "/monitor/user")
        self._api.add_resource(ProcessInfo, self._version_prefix + "/monitor/process")

        self._app.register_blueprint(self._api_bp)

    def start(self):
        # 注册路由
        self._register_router()
        # 启动
        self._app.run(port=8000, debug=True)


if __name__ == '__main__':
    # 初始化
    b = Backend()
    # 启动
    b.start()
