#!/usr/bin/python3
"""Fabric script that generates a .tgz archive fF"""
from fabric.api import local
from datetime import datetime as dtime


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
