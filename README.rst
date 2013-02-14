A Statistics collector for Network Data
=======================================

Introduction
------------

Requirements
------------

* python-zmq : pip install pyzmq==2.2.0 (or use local version> 2.2.0)
* pycryptopan: pip install pycrypto pycryptopan
* pymongo: pip install pymongo==1.7
* importlib - for python < 2.7
* Mongodb as backend
* web.py for the API
* flup and spawn-fcgi for fastcgi

also can be installed as pip install -r requirements.txt 

Version numbers refer to the version numbers available on debian squeeze
and squeeze-backports respectively

Principles
----------

The collector has three different elements:

* A Collecting daemon `Collector`
* A Query daemon
* A python module to write statistics easily `Collectclient`

Collecting daemon
_________________

The collecting daemon opens a zmq pull socket and listens to any collecting
device. JSON is used as message passing protocol... Entries generally
consist of::

  {"timestamp": unix timestamp,
  "<object>": "<objectid>",
  "test": "<test>",
  "data": {datastructure}}

<object> is in "node","device","interface","address" where each has it's
own <objectid>. 

test describes the tests done, data is the data object for the test - as
json...

This will be parsed by json.loads() and then added to the database... IP
addresses will be anonymized using pycryptopan.

Query Daemon
____________

TBD

Statistics Write Module
_______________________

A statistics write module to easily write statistics, uses zmq push to
connect to the collector and implements message passing and serialization..

It lives on http://github.com/FFM/Collectclient
