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

    tgz = archive_path.split("/")[1]
    fname = tgz[:-4]
    a = put(archive_path, '/tmp/')
    b = run('rm -rf /data/web_static/releases/*')
    c = run('mkdir -p /data/web_static/releases/' + fname + '/')
    d = run('tar -xzf /tmp/' + tgz +
            ' -C /data/web_static/releases/' + fname + '/')
    e = run('rm -rf /tmp/' + tgz)
    f = run('mv /data/web_static/releases/' + fname +
            '/web_static/* /data/web_static/releases/'
            + fname + '/')
    g = run('rm -rf /data/web_static/releases/' + fname
            + '/web_static')
    h = run('rm -rf /data/web_static/current')
    k = run('ln -s /data/web_static/releases/' + fname +
            '/ /data/web_static/current')
    f0 = a.failed or b.failed or c.failed or d.failed or e.failed
    f1 = f.failed or g.failed or h.failed or k.failed
    return False if f1 else True
