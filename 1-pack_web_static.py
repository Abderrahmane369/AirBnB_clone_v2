#!/usr/bin/python3
"""Fabric script that generates a .tgz archive fF"""
from fabric.api import local
from datetime import datetime as dtime


def do_pack():
    """azeaeze"""
    dt = dtime.now()

    local("mkdir -p versions")
    a = "tar -czvf versions/web_static_"
    r = local("{}{}{}{}{}{}{}.tgz web_static".format(
        a, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    ))

    return None if r.failed else None
