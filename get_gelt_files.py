import urllib.request
import datetime
import zipfile
import os
from datetime import timedelta

base_file_url = "http://data.gdeltproject.org/events/"
file_date_format = "%Y%m%d"
min_date = datetime.date(2015, 9, 1)
max_date = datetime.date(2015, 9, 15)
curr_date = max_date
date_increment = timedelta(days=1)

while (curr_date >= min_date):
	event_file_name = "{0}.export.CSV.zip".format(curr_date.strftime(file_date_format))
	event_file_url = base_file_url + event_file_name
	try:
		print("File: {0}".format(event_file_name))
		response = urllib.request.urlopen(event_file_url)
		with open(event_file_name, 'b+w') as f:
			print("Writing file from response: {0}...".format(event_file_url))
			f.write(response.read())
			print("...file written")

			with zipfile.ZipFile(event_file_name) as z:
				print("Extracting archive...")
				z.extractall()
				print("...archive extracted.")

			os.remove(event_file_name)

	except Exception as ex:
		print("Exception {0}".format(ex))

	curr_date = curr_date - date_increment
