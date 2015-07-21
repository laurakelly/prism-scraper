To use this script:

1. Install pip, Python's package manager: https://pip.pypa.io/en/latest/installing.html
2. In the command line, install dependencies (listed in `requirements.txt`) with pip:
  `sudo pip install`
3. Run the script: `python prism-about-us-scraper.py`

Note: this assumes you are using Python 2.7 or higher

The script will print a warning because we are fetching an https url. I could not 
get around this in time. I tried the following solution: http://stackoverflow.com/a/29099439/1880100
but it did not work. It might be a system-specific issue.
