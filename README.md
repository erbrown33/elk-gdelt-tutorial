# ElasticSearch-LogStash-Kibana stack setup for processing GDELT files
Configuration, scripts and filters to get an ELK stack analyzing the famous GDELT (http://gdeltproject.org/data.html) data set. Includes a handy Py script to download the GDELT files locally for a date range in addition to a grok REGEX for the GDELT data file format.

# ELK Setup
Should work for tutorial/dev purposes on a basic local environment with minimal to no configuration. See docs:

* [ElasticSearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)
* [LogStash Documentation](https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html)
* [Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/setup.html)

## LogStash Configuration
When starting LogStash, you'll need to specify your configuration file from this repo using your local path:
'''
./logstash -f <YOUR_PATH_TO_THE_LS_CONFIG>/ls-gdelt-pipeline.conf
'''

If things don't seem to be processing correcly, add the ```--debug``` flag to the command line on startup and take a look at output.

## Kibana Configuration
From the Settings tab, you'll need to configure an index pattern for the GDELT output. Type "gdelt" and it should show up. The grok filter should format index timestamps so you have a "@timstamp" time-field available.
