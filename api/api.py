
import web
from pymongo import Connection
import re
import settings
import json


db=Connection(settings.dbhost,settings.dbport).statistics
statistics=db.statistics

urls = (
  '/(.*)','index'
    )

class index:
  def GET(self,name):
    web.header('Content-Type', 'application/json')
    i=name.split("/")
    def tt(a):
      while True:
        try:
          yield(a.pop(0),a.pop(0))
        except IndexError:
          raise StopIteration()
    if i>2:      
      query=dict([a for a in tt(i)])     
      result=[x for x in statistics.find(query)]
      for r in result:  
        r.pop("_id")
      return json.dumps(result)
    else:
      return json.dumps({})


def do():
  app=web.application(urls,globals())
  app.run()

def fcgi():
  import os
  if not os.fork():
    web.wsgi.runfcgi(do,(settings.fcgihost,settings.fcgiport))

if __name__=="__main__":
  do()

