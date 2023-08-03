# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["android://127.0.0.1:5037/0000038cce7c204e?cap_method=JAVACAP&touch_method=MAXTOUCH&",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)

# 启动
start_app("app.cozylife.app")

# 点击我的
touch(Template(r"tpl1690447699878.png", record_pos=(0.332, 1.05), resolution=(1080, 2400)))

# 点击头像
touch(Template(r"tpl1690447730260.png", record_pos=(0.374, -0.751), resolution=(1080, 2400)))

# 点击退出
touch(Template(r"tpl1690447754999.png", record_pos=(0.009, 0.069), resolution=(1080, 2400)))

# 返回
home()