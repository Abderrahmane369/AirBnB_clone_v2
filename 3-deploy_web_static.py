#!/usr/bin/python3
""" azea"""
from fabric.api import put, run, env, local
import os
env.hosts = ['54.144.144.29', '54.158.205.242']

def do_pack():
    """azeaeze"""
    dt = dtime.now()

    local("mkdir -p versions")
    a = "versions/web_static_"
    path = "{}{}{}{}{}{}{}.tgz".format(
        a, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    r = local(f"tar -czvf {path}.tgz web_static")

    return path if r.failed else None

def deploy():
    archive = do_pack()
    
    