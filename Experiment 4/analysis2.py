from pylab import *
prefix="/home/saptarshi/Documents/MasterThesis@RISE/timing_results/experiment/"


Transfer_size=[1024,2048,3072,4096]
noutput_items=[504,1000,2000,4000,'x']

data=[]
Names=[]
for p in range(0,len(noutput_items)):
    t1= fromfile(prefix+str(Transfer_size[2])+"/"+str(Transfer_size[2])+"_1_"+str(noutput_items[p])+"/t1.txt",sep='\n')
    t8= fromfile(prefix+str(Transfer_size[2])+"/"+str(Transfer_size[2])+"_1_"+str(noutput_items[p])+"/t8.txt",sep='\n')
    
    # Calculate tdiff
    tdiff=np.empty(len(t1))
    j=0
    for i in range(0,(len(t1))):
         while(t1[i] > t8[j]):
            j=j+1
            
         tdiff[i]=t8[j]-t1[i]
    data.append(tdiff)
    Names.append(str(noutput_items[p]))

# print data
ylim(ymax=5000)
ylabel(r'RTT($\mu s$)',fontsize=14)
title('RTT vs number of n_output_items, USB Transfer size=3072')
bp_dict=boxplot(data,labels=Names)



for line in bp_dict['medians']:
    # get position data for median line
    x,y = line.get_xydata()[1] # top of median line
    # overlay median value
    text(x+0.05, y-40, '%.1f' % y,
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