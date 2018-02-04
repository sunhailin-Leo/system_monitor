# system_monitor

---

* 作用:
    * include backend and frontend(still developing...) 
    * can monitor linux,windows.

---

* 进度
    * 目前完成了几个接口(2018-01-28)
    
    ```html
    全部都是get的接口:  
       SystemInfo --- "/monitor/info" --- 系统信息
       MemoryChecker --- "/monitor/memory" --- 内存使用情况
       CpuChecker --- "/monitor/cpu" --- CPU使用情况
       UserInfo --- "/monitor/user" --- 系统用户信息
       ProcessInfo --- "/monitor/process" --- 进程使用信息
       UsingPortInfo --- "/monitor/port" --- 端口使用情况
    ```
    
    * 使用说明举例:
    ```html
    url: http://127.0.0.1:8000/v1/monitor/info
    method: get
    
    response:
    {
          "msg": "Success",
          "data": [
              {
                  "sys_info": "Windows10 x64",
                  "sys_version": "Windows-10-10.0.14393",
                  "sys_name": "Windows"
              }
          ]
    }
    ```
    
    * 项目说明:
        * Python版本： Python3.4.4
        * 用到的包见跟目录的requirements.txt
       
    * 运行方法:
        * 方法1：(未来的使用方式)
            * 根目录 cd backend
            * python system_monitor.py 
            * 暂时用restful的请求去获取状态
        * 方法2：(暂时使用方式)
            * 可以去common里面单独运行
            ```commandline
            # 帮助
            python system_info.py -h 
            
            # 使用
            python system_info.py -l 
            ```