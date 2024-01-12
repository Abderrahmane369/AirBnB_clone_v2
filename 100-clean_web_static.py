#!/usr/bin/python3
"""logarthim"""
from fabric.api import local, run, env
from datetime import datetime as dtime
from re import search as srch

env.hosts = ['54.158.205.242', '54.144.144.29']


def do_clean(number=0):
    vers = local('ls -tr versions', capture=True)

    number = int(number)

    if number == 0:
        number = 1

    def istgz(e): return srch('web_static_[0-9]+[.]tgz', e) != -1

    archives = [_ for _ in vers.stdout.split('\n') if istgz(_)]

    if number > len(archives) or number < 0:
        return

    for _ in archives[:-number]:
        local(f'rm -rf versions/{_}')
        run(f'rm -rf /data/web_static/releases/{_}')
