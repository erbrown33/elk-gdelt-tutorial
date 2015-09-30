import sys

if sys.version_info[0] < 3:
    print("Please use python 3 to run this script. We currently need it for urllib.")
    sys.exit(2)

import urllib.request
import datetime
import zipfile
import os
import datetime

#TODO: variables for processing - add main method with args for input
min_date = datetime.date(2013, 5, 25)
max_date = datetime.date(2013, 5, 26)

# GLOBAL CONSTANTS
BASE_FILE_URL = "http://data.gdeltproject.org/events/"
MIN_DAILY_DATE = datetime.date(2013, 4, 1)
MIN_MONTHLY_DATE = datetime.date(2006, 1, 1)
MIN_ANNUAL_DATE = datetime.date(1979, 1, 1)

curr_date = max_date

def main(argv):
    #TODO: allow for input and process args
    
    global curr_date

    while (curr_date >= min_date):

        try:
            if (curr_date >= MIN_DAILY_DATE):
                extract_zip(get_daily_file())
                curr_date = curr_date - datetime.timedelta(days=1)
            elif (curr_date >= MIN_MONTHLY_DATE):
                extract_zip(get_monthly_file())
                curr_date = datetime.date(
                    curr_date.year if curr_date.month > 1 else curr_date.year - 1,
                    curr_date.month - 1 if curr_date.month > 1 else 12, 
                    1)
            elif (curr_date >= MIN_ANNUAL_DATE):
                extract_zip(get_annual_file())
                curr_date = datetime.date(curr_date.year - 1, 1, 1)
            else:
                raise Exception("Minimum date supplied not supported. Stopped execution. Data not available prior to 1979.")


        except Exception as ex:
            print("Uh oh. Something bad happened: {0}".format(ex))
            sys.exit(2)

def get_daily_file():
    file_date_format = "%Y%m%d"
    event_file_name = "{0}.export.CSV.zip".format(curr_date.strftime(file_date_format))
    event_file_url = BASE_FILE_URL + event_file_name
    print("Fectching daily GDELT data file: {0}".format(event_file_name))
    download_file_from_url(event_file_url, event_file_name)
    return event_file_name


def get_monthly_file():
    file_date_format = "%Y%m"
    event_file_name = "{0}.zip".format(curr_date.strftime(file_date_format))
    event_file_url = BASE_FILE_URL + event_file_name
    print("Fectching monthly GDELT data file: {0}".format(event_file_name))
    download_file_from_url(event_file_url, event_file_name)
    return event_file_name


def get_annual_file():
    file_date_format = "%Y"
    event_file_name = "{0}.zip".format(curr_date.strftime(file_date_format))
    event_file_url = BASE_FILE_URL + event_file_name
    print("Fectching annual GDELT data file: {0}".format(event_file_name))
    download_file_from_url(event_file_url, event_file_name)
    return event_file_name


def download_file_from_url(url=None, target_path=None):
    response = urllib.request.urlopen(url)
    with open(target_path, 'b+w') as f:
        print("Writing file from URL: {0}...".format(url))
        f.write(response.read())
        print("...file written")


def extract_zip(zip_path):
    with zipfile.ZipFile(zip_path) as z:
        print("Extracting archive...")
        z.extractall()
        print("...archive extracted.")

    os.remove(zip_path)


if __name__ == "__main__":
   main(sys.argv[1:])