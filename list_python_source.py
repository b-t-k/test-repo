import sys

import requests


name = input("your name?")
print("hello", name)


def greeting(who):
    greeting = "hey {}".format(who)
    return greeting


#  print (sys.version)
print(sys.executable)

r = requests.get("https://macblaze.ca")

print(r.status_code)

# shft opt f = autoformat
