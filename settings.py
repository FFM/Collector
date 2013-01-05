import collectd.middleware.anonymize
#collector configuration

# database

dbhost="localhost"
dbport=27017

# collectd

listen="127.0.0.1"
port=25500

collectd_middleware=[collectd.middleware.anonymize]
