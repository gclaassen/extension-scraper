# Extension Scraper

_V1.0.0_

Scraper Scripts written in Python

These scrapers will allow the user to search in set source directories (all folders and subfolders in the source directory) for files with a set extension (and EXIF info).

The files matching the extension will either be moved or copied to a destination directory

## Argument List

| Command | Description                                      | Example        |
| ------- | ------------------------------------------------ | -------------- |
| -t      | File extension to be moved/copied                | -t _.ext1_ _.extn_      |
| -s      | Source Directory                                 | -s _src/dir/_  |
| -d      | Destination Path                                 | -d _dest/dir/_ |
| -c      | Copy the file to the destination **OR**          | -c             |
| -m      | Move the file from the source to the destination | -m             |
| -z      | Check all the ext types not only EXIF            | -z             |

Run **\_\_runScraper.bat**
or call command in terminal:

```
python ./pyscraper.py "-t" ".jpg" "-s" "c:/" "-d" "f:/scrapedFiles/" "-c" "-z"
```

## Required Modules

- exif (photograph)
- os
- getopt
- sys
- shutil
- time

## Python

- Python 3.7.3

## TODO:

- [ ] Arguments
- [ ] Better Code Format
- [x] Check if dirs exist
- [x] Create list of invalid directories [no go areas]
- [ ] Create list of directories were files may not be deleted
- [x] Create text file with inputs of where files were located, file dates, file names and comments
- [x] Used arguments to either list locations of files, copy files or movE files
- [x] Show in terminal places of current search, the files in question and progress
- [x] Check EXIF data for camera info
- [ ] Other type of file naming conventions to choose from
- [ ] GUI
- [ ] Installer and executable

*vir ma. lief ma baie*
