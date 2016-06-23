import os
import sys

data = '19100 18202 18267 18966 17205 17188'
data = map(int, str(data).split())

prob = {}
for i in xrange(6):
    if i<3 and data[i]>0:
        prob[i]=data[i]*1
    if i==3 and data[i]>0:
        prob[i]=data[i]*0.75
    if i==4 and data[i]>0:
        prob[i]=data[i]*0.5
    if i==5:
        prob[i]=0

print 2*sum(prob.values())