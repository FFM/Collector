import settings
import os
import sys

def cold():
  """Starts the Collectd"""
  from collectd.collectd import Collectd
  c=Collectd(settings)
  pid=os.fork()
  if not pid:
    c.collect()
  else:
    if len(sys.argv)>2:
      f=open(sys.argv[2],"w")
      f.write("%s"%pid)
      f.close()

def rsvr():
  """ Runs the development server """
  sys.argv.pop()
  import api.api
  api.api.do()

def fcgi():
  """ Starts the FastCGI server """
  sys.argv.pop()
  import api.api
  api.api.fcgi()

commands={"collectd":cold, 
  "devserver":rsvr,
  "fastcgi":fcgi,
  }

if __name__=="__main__":
  try:
    cmd=sys.argv[1]
  except IndexError:
    cmd=""
  if cmd not in commands.keys():
    print """Collectd management console.... 
    Usage: python run.py command"""
    print """Known commands: """
    for (k,v) in commands.items():
      print "%s: %s"%(k,v.__doc__)

  else:
    commands[cmd]()
