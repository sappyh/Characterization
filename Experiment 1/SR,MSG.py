from pylab import *
prefix="/home/saptarshi/Documents/MasterThesis@RISE/experiment/Experiment 1/Machine2/results/"

Sampling_Rate=[4,8,16]
Message_Sizes=[1,37,74,112]

for q in range(0,len(Message_Sizes)):
    data=[]
    Names=[]
    for p in range(0,len(Sampling_Rate)):
        t1= fromfile(prefix+str(Sampling_Rate[p])+"/"+str(Sampling_Rate[p])+"_"+str(Message_Sizes[q])+"/t1.txt",sep='\n')
        t8= fromfile(prefix+str(Sampling_Rate[p])+"/"+str(Sampling_Rate[p])+"_"+str(Message_Sizes[q])+"/t8.txt",sep='\n')
        
        # Calculate tdiff
        tdiff=np.empty(len(t1))
        j=0
        for i in range(0,(len(t1))):
            while(t1[i] > t8[j]):
                j=j+1
                
            tdiff[i]=t8[j]-t1[i]
        tdiff=tdiff[tdiff<4000]
        data.append(tdiff)
        Names.append(str(Sampling_Rate[p]))

    # print data
    ylabel(r'RTT($\mu s$)',fontsize=14)
    title('RTT vs USB Transfer Sizes, Message_Size='+str(Message_Sizes[q]))
    bp_dict=boxplot(data,labels=Names)



    for line in bp_dict['medians']:
        # get position data for median line
        x,y = line.get_xydata()[1] # top of median line
        # overlay median value
        text(x+0.05, y-40, '%.1f' % y,
            horizontalalignment='right') # draw above, centered

    for line in bp_dict['boxes']:
        x, y = line.get_xydata()[1] # bottom of left line
        text(x+0.05,y, '%.1f' % y,
            horizontalalignment='right', # centered
            verticalalignment='top')      # below
        x, y = line.get_xydata()[2] # bottom of right line
        text(x+0.05,y, '%.1f' % y,
            horizontalalignment='right', # centered
                verticalalignment='bottom')      # below

    savefig("/tmp/image.png")
    show()