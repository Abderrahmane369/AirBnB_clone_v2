#!/usr/bin/python3
""" azea"""
from fabric.api import put, run, env, local
from os.path import isfile
from datetime import datetime as dtime
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


def deploy():
    archive = do_pack()

    if archive is None:
        return False

    return do_deploy(archive)
