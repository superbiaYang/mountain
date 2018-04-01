import os
import urllib
import sys
from flask import *

def get_dir_info(target_dir):
    target_dir = target_dir.decode("utf8")
    if os.path.isdir(target_dir):
        file_list = []
        for s in os.listdir(target_dir):
            new_dir = os.path.join(target_dir, s)
            if os.path.isdir(new_dir):
                file_list.append({
                    'name' : s,
                    'dir' : urllib.quote(new_dir.encode('utf8')),
                    'type' : "dir",
                })
            elif os.path.isfile(new_dir):
                size = os.path.getsize(new_dir)
                file_list.append({
                    'name' : s,
                    'dir' : urllib.quote(new_dir.encode('utf8')),
                    'type' : "file",
                    'size' : size,
                })
        return file_list
    return []

def init(app):
    @app.route('/files/<target_dir>')
    def get_files(target_dir):
        target_dir = urllib.unquote(target_dir.encode())
        return render_template("file_list.html", file_list=get_dir_info(target_dir))

    @app.route('/file/<target_dir>')
    def get_file(target_dir):
        target_dir = urllib.unquote(target_dir.encode()).decode("utf8")
        return send_file(target_dir, as_attachment=True)
