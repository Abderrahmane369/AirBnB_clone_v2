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
        put(archive_path, '/tmp/')
        run('rm -rf /data/web_static/releases/*')
        run('mkdir -p /data/web_static/releases/{}/'.format(
            archive_path.split("/")[1][:-4]))

        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            archive_path.split("/")[1],
            archive_path.split("/")[1][:-4]
        ))
        run(f'rm -rf /tmp/{archive_path.split("/")[1]}')
        run('mv {}{}/web_static/* {}{}/'.format(
            '/data/web_static/releases/',
            archive_path.split("/")[1][:-4],
            '/data/web_static/releases/',
            archive_path.split("/")[1][:-4]
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_path.split("/")[1][:-4]
        ))
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/{} {}'.format(
            archive_path.split("/")[1][:-4], '/data/web_static/current'))

    except Exception:
        return False

    return True
