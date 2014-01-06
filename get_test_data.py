#!/usr/bin/env python

import os
import json
from urllib2 import urlopen, URLError, HTTPError

DATADIR = 'test_data'
DATAFILE = 'data.json'


def dlfile(url, dest):
    try:
        f = urlopen(url)
        print "Test file not found locally, downloading: "
        print "  " + url

        with open(dest, "wb") as local_file:
            local_file.write(f.read())

    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def get_test_data():
    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)
    data_files = json.loads(open(DATAFILE).read())
    for data_file in data_files.keys():
        data_file_path = os.path.join(DATADIR, data_file)
        if not os.path.exists(data_file_path):
            # The test file doesn't exist so we need to grab it from the URL in
            # in the JSON file and place it at data_file_path
            dlfile(data_files[data_file]['url'], data_file_path)
        else:
            pass
            #print "File exists: ", data_file_path


if __name__ == '__main__':
    get_test_data()
