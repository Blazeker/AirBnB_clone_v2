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
    