import sys

def getArgByIdx(index=0):
  try:
    return sys.argv[index]
  except:
    return "無"