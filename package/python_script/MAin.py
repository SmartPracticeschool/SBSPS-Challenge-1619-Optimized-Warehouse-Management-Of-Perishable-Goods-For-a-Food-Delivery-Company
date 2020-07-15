#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import joblib
import sys
from sklearn.preprocessing import OneHotEncoder


# In[2]:


filename_input= 'sys.argv[1]'
test=pd.read_excel(filename_input)


# In[3]:


def print_to_stderr(*a): 
    print(*a, file = sys.stderr) 
if(test.shape[1]!=8):
    print_to_stderr("wrong input type") 


# In[4]:


meal_info=pd.read_csv('./python_script/'+'meal_info.csv')
fulfilment_center=pd.read_csv('./python_script/'+'fulfilment_center_info.csv')
test=pd.merge(test,meal_info,left_on='meal_id',right_on='meal_id')
test=pd.merge(test,fulfilment_center,left_on='center_id',right_on='center_id')
categorical=test[['id','week','category','cuisine','city_code','center_id','region_code','center_type']]
test.drop(columns=['id','category','cuisine','week','city_code','center_id'],inplace=True)
test.tail()


# In[5]:


x=test[['center_type','region_code']]


# In[6]:


X = x.values
c_type=fulfilment_center.center_type.unique()
r_type= [23,34,35,56,71,77,85,93]
ohe = OneHotEncoder(categories=[c_type,r_type])
X = ohe.fit_transform(X).toarray()
X[0:5]
df=pd.DataFrame(X,columns=['center_type_TYPE_A','center_type_TYPE_B','center_type_TYPE_C','region_code_23','region_code_34','region_code_35','region_code_56','region_code_71','region_code_77','region_code_85','region_code_93'])
df.head()


# In[7]:


test=pd.concat([test,df],axis=1)
test.drop(columns=['center_type','region_code'],inplace=True)


# In[8]:


test.tail()


# In[9]:



test.checkout_price/=200
test.base_price/=200
test.op_area/=10
test.describe()


# In[10]:


s=[]
for i in range(len(test)):
    r=test.loc[i]
    filename=f'{r.meal_id:.0f}'
    pipe1=joblib.load('./python_script/'+filename+'.sav')
    pipe2=joblib.load('./python_script/'+filename+'2.sav')
    a= r.to_numpy()
    a= a[1:]
    a=a.reshape(-1,16)
    b=np.array(pipe1.predict(a))
    T= r.values
    T=np.append(T,b)
    T= T[1:]
    T=T.reshape(-1,17)
    s.extend(pipe2.predict(T))


# In[11]:


test.drop(columns=['center_type_TYPE_A','center_type_TYPE_B','center_type_TYPE_C','region_code_23','region_code_34','region_code_35','region_code_56','region_code_71','region_code_77','region_code_85','region_code_93'],inplace=True)


# In[12]:


test=pd.concat([categorical,test],axis=1)


# In[13]:


test['predicted_num_orders']=s


# In[15]:


def worker_division(num):
    if num < 136.0:
        return 'Can leave out some workers'
    elif num < 324.0:
        return 'Optimum number of workers'
    elif num < 609.0:
        return 'May need some extra workers'
    else:
        return 'Lot of extra workers required'
    
test['worker_division_category'] = test['predicted_num_orders'].apply(worker_division)
test


# In[ ]:


test.to_excel("result.xlsx")
print("Completed")

