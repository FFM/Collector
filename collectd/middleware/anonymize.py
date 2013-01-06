""" This module takes the message as string and replaces all ips with
cryptopan anonymized ips

This is done so it also works on address ids - which are ip addresses """

from cryptopan import CryptoPan
try:
  from settings import anonymizeseed
except ImportError:
  """ If the seed cannot be imported use a random seed """
  import random
  anonymizeseed="".join(chr(x) for x in random.sample(range(0,256),32))
import re
cp=CryptoPan(anonymizeseed)

def process(message):
  ips=re.findall("([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})",message)
  ips=((ip,cp.anonymize(ip)) for ip in ips)
  return reduce(lambda x,y: re.sub(y[0],y[1],x), ips,message)


if __name__=="__main__":
  message="""the lazy fox 127.0.0.1, jumps over 192.168.0.42"""
  print message
  print process(message)
