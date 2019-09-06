#!/usr/bin/env python
# coding: utf-8

# In[ ]:


InH=int(input())
InM=int(input())
OutH=int(input())
OutM=int(input())
timeH = (OutH - InH)
timeM = (OutM - InM)
MixH = (timeH * 10)

if  timeH >= 6 :
    print("200")

if  15 <= timeM  <= 59   :
    if timeM <= 15 :
        print("0")
    else:
        timeM > 15
        print(round(timeM / timeM * 10))



elif 3 >= timeH :

    if timeH >= 3 and timeM >= 1 :
        print(MixH+20)
    else:
        timeH >= 3
        print(MixH)


# In[ ]:




