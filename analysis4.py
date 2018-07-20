import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# Read the dataframe

import numpy as np
from pylab import *


t1= np.fromfile("/tmp/t1.txt",sep='\n')
t8= np.fromfile("/tmp/t8.txt",sep='\n')
print len(t1),len(t8)
from matplotlib import pyplot as plt
tdiff=np.empty(len(t1))
j=0
for i in range(0,(len(t1))):
     while(t1[i] > t8[j]):
            j=j+1
#      print t8[j]-t1[i]
     tdiff[i]=t8[j]-t1[i]

outliners=where(tdiff>1750)
out_time=t8[outliners]/10 **6
print out_time
df= pd.read_csv('/tmp/nice_data_file.csv',sep=':')
# df
# print df
# Access elements of the dataframe
# print(df['%CPU'])
# print(pd.to_numeric(df['%CPU'], errors='coerce'))
plt.subplot(2,1,1)
ylabel('%CPU',fontsize=14)
xlabel('Time in seconds since epoch',fontsize=14)
title(' CPU vs Time',fontsize=14)
plt.plot(df['Time'],df['%CPU'])


def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return idx-1
    else:
        return idx
    
for i in range(0,len(out_time)):
       index=find_nearest(df['Time'],out_time[i])
       x= df['Time'][index]
#        print x
       y= df['%CPU'][index]
       plot(x,y,'ro')
#        text(x,y, '%.1f' % y,
#          horizontalalignment='center', # centered
#          verticalalignment='baseline')      # below

plt.subplot(2,1,2)
ylabel('context switches',fontsize=14)
xlabel('Time in seconds since epoch',fontsize=14)
title('Context Switches vs Time',fontsize=14)
for i in range(0,len(out_time)):
       index=find_nearest(df['Time'],out_time[i])
       x= df['Time'][index]
#        print x
       y= df['cswitch/s'][index]
       plot(x,y,'ro')
plt.plot(df['Time'],df['cswitch/s'])
savefig("/tmp/resource.png")
show()