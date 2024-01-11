#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime as dtime


def do_pack():
    dt = dtime.now()

    local("tar -czvf versions/web_static_{}{}{}{}{}{}".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    ))
