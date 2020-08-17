#!/usr/bin/python3
""" Write a Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive
"""

import os
import re
from fabric.api import *
env.hosts = ['34.74.151.236', '34.75.172.55']


def do_deply(archive_path):
    """ Deploys the archive """
    if os.path.exists(archive_path) is False:
        return False
    ar_path_split = re.split('[\. | _ | /]', archive_path)
    time_str = ar_path_split[-2]

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/web_static_{}/".format(
                    time_str))
        run("tar -xzf /tmp/web_static_{}.tgz -C \
                /data/web_static/releases/web_static_{}/\
                ".format(time_str, time_str))
        run("rm /tmp/web_static_{}.tgz".format(time_str))
        run("mv /data/web_static/releases/web_static_{}/web_static/* \
                /data/web_static/releases/web_static_{}/\
                ".format(time_str, time_str))
        run("rm -rf /data/web_static/releases/web_static_{}/web_static\
                ".format(time_str))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/web_static_{}/ \
                /data/web_static/current".format(time_str))
        return True
    except Exception:
        return False
