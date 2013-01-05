import zmq
from pymongo import Connection
import json
import importlib

class Collectd:
  
  def __init__(self,config):
    self.config=config
    self.connection=Connection(self.config.dbhost,self.config.dbport)
    self.db=self.connection.statistics
    self.statistics=self.db.statistics
    self.run=True
    self.middleware=[importlib.import_module(m) for m in
    self.config.collectd_middleware]

  def collect(self):
    context=zmq.Context()
    receiver = context.socket(zmq.PULL)
    print "listening on %s:%s"%(self.config.listen,self.config.port)
    receiver.bind("tcp://%s:%s"%(self.config.listen,self.config.port))

    while self.run:
      m=receiver.recv()
      m=reduce(lambda x,y: y.process(x),self.middleware,m)
      self.statistics.insert(json.loads(m))

if __name__=="__main__":
  import settings
  c=Collectd(settings)
  c.collect()
