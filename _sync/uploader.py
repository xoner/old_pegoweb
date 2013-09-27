'''
This module updates the contents of the website depending on the changes present on the
_site folder of the jekyll site
'''
import os
import subprocess
import ftplib

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from os import path


def get_files_to_upload():
    print 'Checking for changes:\n'
    proc = subprocess.Popen('rsync -rvchn {} {}'.format(CONFIG['rsync_jekyll_gen_dir'],
                                                        CONFIG['rsync_last_update_dir']),
                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = proc.communicate()

    # Check if there weren't errors running the rsync command
    # and parse the output
    files_content = False
    files_list = []
    if err is '':
        for line in out.split('\n'):
            if line == 'sending incremental file list':
                files_content = True
                continue
            if files_content and line != '':
                if line.startswith('sent'):
                    files_content = False
                    break
                else:
                    files_list.append(line)
    else:
        print err


    return files_list


def upload_files(files_list):
    print '\nUploadding changes:'

    if len(files_list) == 0:
        print 'Nothing to update'
        return True

    errors_exist = False
    py_ftp = ftplib.FTP(CONFIG['ftp_host'],
                        CONFIG['ftp_user'],
                        CONFIG['ftp_pass'])

    # Get sure that we are working where the jekyll sit is being generated.
    if os.getcwd() != CONFIG['rsync_jekyll_gen_dir']:
        os.chdir(CONFIG['rsync_jekyll_gen_dir'])

    for it_file in files_list:
        print 'Uploading {}'.format(it_file)
        result = py_ftp.storbinary('STOR {}'.format(it_file), open(it_file, 'rb'))

        if result != '226 Transfer complete':
            errors_exist = True
        print result

    py_ftp.quit()

    return errors_exist


def update_rsync_dir():
    print '\nUpdating aux repository:\n'

    subprocess.call('rsync -rvch {} {}'.format(CONFIG['rsync_jekyll_gen_dir'],
                                               CONFIG['rsync_last_update_dir']),
                    shell=True)


def load_config():
    file_config_path = 'config.yaml'
    if not path.exists(file_config_path):
        file_config_path = path.join(path.dirname(__file__), file_config_path)

    file_config_obj = open(file_config_path, 'r')

    config = yaml.load(file_config_obj.read(), Loader=Loader)

    file_config_obj.close()

    return config


def main():
    os.chdir(CONFIG['jekyll_working_dir'])

    files = get_files_to_upload()
    errors = upload_files(files)

    if not errors:
        update_rsync_dir()



if __name__ == '__main__':
    CONFIG = load_config()
    main()