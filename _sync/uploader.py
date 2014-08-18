'''
This module updates the contents of the website depending on the changes present on the
_site folder of the jekyll site
'''
import os
import subprocess
import ftplib
import argparse
import pdb

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from os import path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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
        result = ''
        if path.isdir(it_file):
            print "Creating directory {}".format(it_file)

            try:
                result = py_ftp.mkd(it_file)

                # Compare if the results of creating the directory where ok
                splt_it_file = it_file.split('/')
                splt_it_file.remove('')
                splt_result = result.split('/')
                splt_result.remove('')

                if not splt_it_file == splt_result:
                    errors_exist = True
                    break

            except Exception, e:
                print(bcolors.FAIL + e.message + bcolors.ENDC)
        else:
            print 'Uploading {}'.format(it_file)

            try:
                result = py_ftp.storbinary('STOR {}'.format(it_file), open(it_file, 'rb'))
            except Exception, e:
                print(bcolors.FAIL + e.message + bcolors.ENDC)

            if result != '226 Transfer complete':
                errors_exist = True

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


def main(arguments):
    os.chdir(CONFIG['jekyll_working_dir'])

    files = get_files_to_upload()

    # pdb.set_trace()

    if not arguments.dry_run:
        errors = upload_files(files)

        if not errors:
            update_rsync_dir()
    else:
        print("Changes to upload")

        for it_file in files:
            print(it_file)

        print("\n\nNo changes will be updated (dry run)")




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fa un update de la plana web per mig de ftp en base a els canvis que n'hi han hagut en local",
                                     prog="File uploader")
    parser.add_argument('-D', '--dry-run', action="store_true")

    args = parser.parse_args()

    CONFIG = load_config()
    main(args)