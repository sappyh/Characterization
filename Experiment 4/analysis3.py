from pylab import *
import pandas as pd
prefix="/home/saptarshi/Documents/MasterThesis@RISE/timing_results/experiment/"


Transfer_size=[1024,2048,3072,4096]
noutput_items=[504,1000,2000,4000]

data1=[]
data2=[]
Names=[]
for p in range(0,len(Transfer_size)):
    df= pd.read_csv(prefix+str(Transfer_size[p])+"/"+str(Transfer_size[p])+"_1_2000/nice_data_file.csv",sep=':')
      
    data1.append(df['%usr'])
    data2.append(df['%system'])
    Names.append(str(Transfer_size[p]))

# print data
# ylim(ymax=5000)
subplot(2,1,1)
ylabel('%CPU Usuage',fontsize=14)
title('%CPU usuage in user space vs USB Transfer Sizes, n_output_items=2000',fontsize=14)
bp_dict=boxplot(data1,labels=Names)



for line in bp_dict['medians']:
    # get position data for median line
    x,y = line.get_xydata()[1] # top of median line
    # overlay median value
    text(x+0.05, y, '%.1f' % y,
         horizontalalignment='center') # draw above, centered

for line in bp_dict['boxes']:
    x, y = line.get_xydata()[1] # bottom of left line
    text(x+0.05,y, '%.1f' % y,
         horizontalalignment='center', # centered
         verticalalignment='top')      # below
    x, y = line.get_xydata()[2] # bottom of right line
    text(x+0.05,y, '%.1f' % y,
         horizontalalignment='center', # centered
             verticalalignment='bottom')      # below


subplot(2,1,2)
ylabel('%CPU Usuage',fontsize=14)
title('%CPU usuage in kernel space vs USB Transfer Sizes, n_output_items=2000',fontsize=14)
bp_dict=boxplot(data2,labels=Names)



for line in bp_dict['medians']:
    # get position data for median line
    x,y = line.get_xydata()[1] # top of median line
    # overlay median value
    text(x+0.05, y, '%.1f' % y,
         horizontalalignment='center') # draw above, centered

for line in bp_dict['boxes']:
    x, y = line.get_xydata()[1] # bottom of left line
    text(x+0.05,y, '%.1f' % y,
         horizontalalignment='center', # centered
         verticalalignment='top')      # below
    x, y = line.get_xydata()[2] # bottom of right line
    text(x+0.05,y, '%.1f' % y,
         horizontalalignment='center', # centered
             verticalalignment='bottom')      # below

savefig("/tmp/image.png")
show()