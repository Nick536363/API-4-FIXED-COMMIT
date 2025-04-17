import os
import urllib
import urllib.parse


def get_file_ext(url):
    path = urllib.parse.urlparse(url).path
    return os.path.splitext(path)[1]
