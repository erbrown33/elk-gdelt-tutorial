# ElasticSearch-LogStash-Kibana stack setup for processing GDELT files
Configuration, scripts and filters to get an ELK stack analyzing the famous GDELT (http://gdeltproject.org/data.html) data set. Includes a handy Py script to download the GDELT files locally for a date range in addition to a LogStash grok REGEX pattern for the GDELT data file format.

# ELK Setup
Should work for tutorial/dev purposes on a basic local environment with minimal to no configuration. See docs:

* [ElasticSearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)
* [LogStash Documentation](https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html)
* [Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/setup.html)

## LogStash Configuration
When starting LogStash, you'll need to specify your configuration file from this repo using your local path:

```
./logstash -f <YOUR_PATH_TO_THE_LS_CONFIG>/ls-gdelt-pipeline.conf
```

If you have issues and want to fully "reset" LogStash, you'll need to manually remove its "since" DB...e.g. in Linux:

```
rm ~/.sincedb*
```

If things don't seem to be processing correcly, add the ```--debug``` flag to the command line on startup and take a look at output.

## Kibana Configuration
From the Settings tab, you'll need to configure an index pattern for the GDELT output. Type "gdelt" and it should show up. The grok filter should format index timestamps so you have a "@timstamp" time-field available.

## Elasticsearch template
After elasticsearch is installed, you can add an index template for the GDELT index.  This classifies the Location field in the logstash mapping as a [GeoPoint type](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-geo-point-type.html) in elasticsearch, allowing you to create a map visualization in Kibana. To add the mapping simply issue a PUT request to the elasticsearch
```
PUT http://<your_elastic_search_url>:9200/gdelt
```
The body  of that PUT request should be copied from the ```elasticsearch/gdelt-template.json``` file. 

# GDELT Data Files
This tutorial is no fun without data of course. The Python script should be helpful to pull files down within a date range. Start with a small range first as recent daily files are relatively large. **NOTE:** requires Python3 for urllib module.
