# FTP uploader

This folder contains a python script to update my site through ftp, the only method available from my webhoster.

The main idea behind this script is to obtain the list of files to be updated, comparing two local folders (the one where jekyll generates its content and one that contains a 'copy' of the deployed verison) with rsync with a dry run. Upload the contents that has changed and then if there where no errors uploading files, update with rsync the folder that contains the copy of the live site.

## config.yaml
In order to this script to work you must place a config.yml in this same directory with this contents:

    jekyll_working_dir: /path/to/jekyll/site
    rsync_last_update_dir: /path/to/folder/containing/copy/of/live/site
    rsync_jekyll_gen_dir: /path/to/jekyll/generation/directory

    ftp_host: your.ftp.host.url
    ftp_user: your-ftp-username
    ftp_pass: your-ftp-pasword

## TODOS.

* Add a dry run option, only see what is going to be updated.
* Add an option to publish without updating the sitemap.xml (make this actually the default behaviour?).
* Add an option to publish without updating the feed.xml.
