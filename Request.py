import urllib.request

my_req = urllib.request.urlopen("https://www.google.com/")

print(my_req.read())

