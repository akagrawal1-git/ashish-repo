#!/usr/bin/env python
# coding: utf-8

# In[14]:


['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
list1 = [element*i for element in ["x","y","z"] for i in range(1,5)  ]
print(list1)
list1 == ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']


# In[15]:


['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
list2 = [element*i  for i in range(1,5) for element in ["x","y","z"] ]
print(list2)
list2 == ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']


# In[18]:


[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
list3 = [[element+i]  for i in range(1,4) for element in [1,2,3] ]
print(list3)
list3 == [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 


# In[23]:


[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
list4 = [[element+i  for i in range(1,5)] for element in [1,2,3,4] ]
print(list4)
list4 == [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 


# In[24]:


[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
list5 = [(element,i)  for i in range(1,4) for element in [1,2,3] ]
print(list5)
list5 == [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 

