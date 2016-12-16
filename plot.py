from pyteomics import mzxml, auxiliary
import numpy as np
import matplotlib.pyplot as plt
file='TTE-75-1-01-3.mzXML'
mz_rt_list='mz_rt_list'


def read_csv(fname): 
    fi = open(fname)
    data = []
    for line in fi:
        arr = line.strip().split('\t') # remove \n
        data.append(arr) 
    fi.close()
    data = np.array(data)
    return data


mrlist=read_csv(mz_rt_list)
mrlist=mrlist[1:].astype(float)


mz=559.62096
time=25.324
def plot(mz,time,name):
    RT=[time-5,time+5]
    
    xml=mzxml.read(file)
    XIC=[]
    
    for i in xml:
        if RT[0]<=(i['retentionTime']/60) and  RT[1]>=(i['retentionTime']/60) and i['msLevel']=='1':
            inty=0
            for k in range(len(i['m/z array'])):
                if i['m/z array'][k]>mz-0.05 and i['m/z array'][k]<mz+0.05:
                    inty=inty+i['intensity array'][k]
            XIC.append([(i['retentionTime']/60),inty])
            
    XIC=np.array(XIC)
     
    plt.plot(XIC[:,0],XIC[:,1],)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）  
    plt.xlabel("Temps(min))") #X轴标签  
    plt.ylabel("intensite(coups/sec)")  #Y轴标签  
    plt.title("Extracted Ion Chromatogram(XIC)") #图标题
    plt.savefig(name+'.jpg')
    plt.show()


for k in range(len(mrlist)):
    plot(mrlist[k][0],mrlist[k][1],str(k+1))

   
   