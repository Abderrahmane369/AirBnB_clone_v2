#!/usr/bin/env python3
"""aezeazzaea"""
from fabric.api import put, env, local
from datetime import datetime as dtime

env.hosts = ['54.144.144.29', '54.158.205.242']
env.user = 'ubuntu'
env.key_filename = 'school'


def do_pack():
    """azeaeze"""
    dt = dtime.now()

    local("mkdir -p versions")
    a = "versions/web_static_"
    path = "{}{}{}{}{}{}{}.tgz".format(
        a, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    r = local(f"tar -czvf {path} web_static")

    return None if r.failed else path


for _ in range(10):
    archv = do_pack()
    put(archv, '/data/web_static/releases')
