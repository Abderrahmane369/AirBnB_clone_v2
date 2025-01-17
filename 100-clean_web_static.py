#!/usr/bin/python3
"""logarthim"""
from fabric.api import local, run, env
from datetime import datetime as dtime
from re import search as srch

env.hosts = ['54.158.205.242', '54.144.144.29']


def do_clean(number=0):
    """zeeazazezaezeaz"""
    vers = local('ls -tr versions', capture=True).stdout

    if vers.find('ls: cannot access') != -1:
        return

    number = int(number)

    if number == 0:
        number = 1

    def istgz(e): return srch('web_static_[0-9]+[.]tgz', e) != -1

    archives = [_ for _ in vers.split('\n') if istgz(_)]

    for _ in archives[:-number]:
        local(f'rm -rf versions/{_}')
        run(f'rm -rf /data/web_static/releases/{_}')
