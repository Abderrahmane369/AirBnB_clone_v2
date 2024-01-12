#!/usr/bin/python3
"""azezaeae"""
from fabric.api import put, run, env
import os
env.hosts = ['54.144.144.29', '54.158.205.242']


def do_deploy():
    """ This is the function for deploying the content """
    if os.path.exists(archive_path) is False:
        return False

    try:
        p = "/data/web_static/releases/"
        file_name = archive_path.split('/')[1]
        no_ext = file_name.split('.')[0]
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run('rm -rf /data/web_static/releases/*')
        run("mkdir -p /data/web_static/releases/" + no_ext + "/")
        run("tar -xzf /tmp/" + file_name + " -C " + p + no_ext + "/")
        run("rm -rf /tmp/" + file_name)
        run("mv " + p + no_ext + "/web_static/* " + p + no_ext + "/")
        run("rm -rf /tmp/" + file_name)
        run("rm -rf /data/web_static/releases/" + no_ext + "/web_static")
        run("rm -rf " + sym_link)
        run("ln -s /data/web_static/releases/" + no_ext + "/ " + sym_link)
        return True
    except Exception:
        return False
