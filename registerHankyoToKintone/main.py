import sys
import os

import pykintone

from src.model.Hankyo import Hankyo

#Environment variable loader
from dotenv import load_dotenv
load_dotenv()

#Initialize App
import pathlib
currentPath = pathlib.Path(__file__).parent.resolve()
account = pykintone.load(os.path.join(currentPath, "account.yml"))
app = account.app()

def registerToKintone(title="無", main="無", mail_to="無", mail_from="無"):
  try:
    print("Trying to register.")
    record = Hankyo()
    record.title = title
    record.main = main
    record.mail_to = mail_to
    record.mail_from  = mail_from
    result = app.create(record)
    print (f"Record Id: {result.record_id} ")
  except:
    print("Failed")

def main():

  if(len(sys.argv) == 5):
    registerToKintone(title=sys.argv[1], main=sys.argv[2], mail_to=sys.argv[3], mail_from=sys.argv[4])
  else:
    registerToKintone()

if __name__ == "__main__":
  main()