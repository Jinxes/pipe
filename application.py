#!python3
#-*- coding:utf8 -*-
from boot import create_app
from boot.setting import DevConfig, ProdConfig

app = create_app(DevConfig)

application = app

if __name__ == '__main__':
    application.run(port=8080)
