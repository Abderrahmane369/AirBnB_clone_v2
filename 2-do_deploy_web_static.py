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

    a = put(archive_path, '/tmp/')
    b = run('rm -rf /data/web_static/releases/*')
    c = run('mkdir -p /data/web_static/releases/{}/'.format(
        archive_path.split("/")[1][:-4]))

    d = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
        archive_path.split("/")[1],
        archive_path.split("/")[1][:-4]
    ))
    e = run(f'rm -rf /tmp/{archive_path.split("/")[1]}')
    f = run('mv {}{}/web_static/* {}{}/'.format(
        '/data/web_static/releases/',
        archive_path.split("/")[1][:-4],
        '/data/web_static/releases/',
        archive_path.split("/")[1][:-4]
    ))
    g = run('rm -rf /data/web_static/releases/{}/web_static'.format(
        archive_path.split("/")[1][:-4]
    ))
    h = run('rm -rf /data/web_static/current')
    k = run('ln -sf /data/web_static/releases/{} {}'.format(
        archive_path.split("/")[1][:-4], '/data/web_static/current'))

    f0 = a.failed or b.failed or c.failed or d.failed or e.failed
    f1 = f.failed or g.failed or h.failed or k.failed

    return False if f1 else True
