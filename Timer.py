import time
from time import*
start = int(strftime("%S"))
sleep(4)
end = int(strftime("%S"))
total = end - start
print("our code took:" , total,"secondes")