#!/usr/bin/python
# email: yao050421103@gmail.com
import sys
import os
import string
import shutil

def init_hustdict(argv):
    cwd = os.path.dirname(os.path.abspath(argv[0]))
    root = os.path.dirname(os.path.dirname(cwd))
    os.system('cd ../../ && python hustngx.py nginx-1.12.0.tar.gz samples/schema/hustdict.json')
    items = [
        'auto/modules',
        'src/addon', 
        'conf/nginx.json', 
        'conf/nginx.conf', 
        'autotest.py', 
        'mutitest.py', 
        'mutikill.sh'
        ]
    src_dir = os.path.join(root, 'samples/hustdict/nginx')
    dst_dir = os.path.join(root, 'samples/schema/hustdict/nginx')
    for item in items:
        src = os.path.join(src_dir, item)
        dst = os.path.join(dst_dir, item)
        if os.path.isdir(src):
            shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)
    return True

if __name__ == "__main__":
    init_hustdict(sys.argv)