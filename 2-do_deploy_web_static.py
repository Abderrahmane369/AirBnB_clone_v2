#!/usr/bin/python3
"""Fabric script that generates a .tgz archive fF"""
from fabric.api import env, put, run
from datetime import datetime as dtime
from os.path import isfile

env.hosts = ['54.144.144.29', '54.158.205.242']


def do_deploy(archive_path):
    """azeaeze"""
    if not isfile(archive_path):
        return False
    try:
        tgz = archive_path.split("/")[1]
        fname = tgz[:-4]
        put(archive_path, '/tmp/')
        run('rm -rf /data/web_static/releases/*')
        run('mkdir -p /data/web_static/releases/' +
            fname + '/')
        run('tar -xzf /tmp/' + tgz +
            ' -C /data/web_static/releases/' + fname + '/')
        run('rm -rf /tmp/' + tgz)
        run('mv /data/web_static/releases/' + fname +
            'web_static/* /data/web_static/releases/'
            + fname + '/')
        run('rm -rf /data/web_static/releases/' + fname
            + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/' + fname +
            '/ /data/web_static/current')
        return True
    except Exception:
        return False