import numpy as np
n=200
ntrials = 5000
for i in range (1,200):
    n=i
    x=0
    for i in range (ntrials):
        y=np.random.normal(loc= 0, scale = 1, size=n)
        y=np.amax(y)
        x+=y
    x=x/ntrials
    print ("n=",n ,"Max Deviation",x)
