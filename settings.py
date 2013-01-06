#import collectd.middleware.anonymize
#collector configuration

# database

dbhost="localhost"
dbport=27017

# collectd

listen="127.0.0.1"
port=25500

collectd_middleware=['collectd.middleware.anonymize']

# anonymize middleware

anonymizeseed="".join((chr(x) for x in range(0,32)))

# FCGI settings for API

fcgihost="127.0.0.1"
fcgiport=3331
