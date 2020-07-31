#!/usr/bin/env python
# coding: utf-8

# In[14]:



numbers = ""
# loop through a range
# find the mod of number with 7
# if mod is zero then check mod with 5
# if mod is not zero add to the string
for num in range(2000,3200):
    if(num % 7 == 0):
        if(num % 5 != 0):
            numbers = numbers + str(num) + ","
print(numbers[:len(numbers)-1])


# In[ ]:




