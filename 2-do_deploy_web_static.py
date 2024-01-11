#!/usr/bin/python3
"""Fabric script that generates a .tgz archive fF"""
from fabric.api import local, env, put, run
from datetime import datetime as dtime
from os.path import isfile
import re as rgx

env.hosts = ['54.144.144.29', '54.158.205.242']


def do_deploy(archive_path):
    """azeaeze"""
    if not isfile(archive_path):
        return False

    dt = dtime.now()

    x = local("mkdir -p versions")
    a = "tar -czvf versions/web_static_"
    r = local("{}{}{}{}{}{}{}.tgz web_static".format(
        a, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    ))

    b = put(archive_path, '/tmp/')
    u = run('mkdir -p /data/web_static/releases/{}/'.format(
        archive_path.split("/")[1][:-4]))

    c = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
        archive_path.split("/")[1],
        archive_path.split("/")[1][:-4]
    ))
    d = run(f'rm -rf /tmp/{archive_path.split("/")[1]}')
    o = run('mv {}{}/web_static/* {}{}/'.format(
        '/data/web_static/releases/',
        archive_path.split("/")[1][:-4],
        '/data/web_static/releases/',
        archive_path.split("/")[1][:-4]
    ))
    lo = run('rm -rf /data/web_static/releases/{}/web_static'.format(
        archive_path.split("/")[1][:-4]
    ))
    e = run('rm -rf /data/web_static/current')
    f = run('ln -sf /data/web_static/releases/{} {}'.format(
        archive_path.split("/")[1][:-4], '/data/web_static/current'))

    isFail = x.failed or r.failed or b.failed or c.failed or d.failed
    isFail2 = isFail or e.failed or f.failed

    return isFail2
