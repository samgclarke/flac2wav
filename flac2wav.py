# !/usr/bin/python

import os
import sys
import subprocess


class FlacToWav(object):
    def __init__(self, start_path, out_path):
        self.start_path = start_path
        self.out_path = out_path

    def mkbash(self, filename, new_path):
        return ['flac', '-d', filename, '-o', new_path, '-f']

    def flac_to_wav(self):
        for root, dirs, files in os.walk(start_path, out_path):
            for f in files:
                if f.endswith(".flac"):
                    # get absolute path of file
                    abspath = os.path.join(root, f)
                    # derive the new path
                    new_path = out_path + root.replace(start_path, '')
                    # make directories if doesn't exist
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                    # generate list of commands
                    x = f.split()
                    x[-1] = '.wav'
                    new_filename = ''.join(x)
                    cmd_list = self.mkbash(
                        abspath, new_path + '/' + new_filename
                    )
                    # execute bash commands
                    process = subprocess.Popen(
                        cmd_list, stdout=subprocess.PIPE
                    )
                    process.communicate()[0]


if __name__ == "__main__":
    try:
        start_path = sys.argv[1]
    except IndexError:
        start_path = None
    try:
        out_path = sys.argv[2] or None
    except IndexError:
        out_path = None

    # init with sys args
    convertor = FlacToWav(start_path, out_path)
    # call flac_to_wav method
    convertor.flac_to_wav()
