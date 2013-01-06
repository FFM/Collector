
import web
from pymongo import Connection
import re
import settings
import json


db=Connection(settings.dbhost,settings.dbport).statistics
statistics=db.statistics

urls = (
  '/api/(.*)','index'
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


app=web.application(urls,globals())

def do():
  app.run()

def fcgi():
  import os
  if not os.fork():
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
    

if __name__=="__main__":
  do()

