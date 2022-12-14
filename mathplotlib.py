import matplotlib.pyplot as plt
import numpy as np
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("AHMED IS THE BEST",fontdict=font1)
x=np.array([30,40,20,50])
y=np.array([60,40])
# plt.pie(y)  ## pie chart
# plt.bar(x,y)  ##Draw a bar
plt.plot(x,marker = "o",ms = 20,color = "r",mec = "r",mfc = "b",lw=3)
    ##Draw a lines with a marker mec:endge of the marker,mfc:color of the marker,ms:size of marker,lw:widgh of the line
# plt.plot(x,linestyle = "--")
    ##Draw a line with a defferent styles ":" dotted, "--" dashed,"-." dash dott

plt.xlabel("SHEEEEEEEEEEESH",fontdict=font1)
plt.ylabel("SHAWARMA",fontdict=font1)
plt.show()
