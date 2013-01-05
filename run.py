import settings
import os
import sys

def cold():
  """Starts the Collectd"""
  from collectd.collectd import Collectd
  c=Collectd(settings)
  if not os.fork():
    c.collect()

commands={"collectd":cold, 
  }

if __name__=="__main__":
  try:
    cmd=sys.argv[1]
  except IndexError:
    cmd=""
  if cmd not in commands.keys():
    print """Collecd management console.... 
    Usage: python run.py command"""
    print """Known commands: """
    for (k,v) in commands.items():
      print "%s: %s"%(k,v.__doc__)

  else:
    commands[cmd]()