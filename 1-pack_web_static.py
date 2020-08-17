#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive from
    the contents of the web_static folder """

from datetime import datetime
from fabric.api import *


def do_pack():
    """ .tgz archive """
    date_type = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions/')
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(
              date_type))
        return "versions/web_static_{}.tgz".format(date_type)
    except Exception:
        return None
