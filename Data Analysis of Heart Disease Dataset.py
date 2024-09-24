#!/usr/bin/env python
# coding: utf-8

# In[3]:


#load the package
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[4]:


#load data
path_file =r'C:\Users\user\Desktop\heart.csv'
heart_data=pd.read_csv(path_file)
heart_data


# In[5]:


#First 6 values of the dataset
heart_data.head()


# In[6]:


#last 6 values of the dataset
heart_data.tail()


# In[7]:


#sanity check of the data
#info
heart_data.info()


# In[8]:


#shape
#Checking the number of rows and columns of the data
heart_data.shape


# In[9]:


#finding the missing values of each column
heart_data.isnull().sum()


# In[10]:


#percentage
heart_data.isnull().sum()/heart_data.shape[0]*100


# In[11]:


#checking for duplicates
heart_data.duplicated().sum()


# In[12]:


#Identifying gabage values
for i in heart_data.select_dtypes(include='object').columns:
    print(heart_data[i].value_counts())
    print("***"*10)


# In[13]:


#EXPLORATORY DATA ANALYSIS
#Descriptive Statistics and transpause
heart_data.describe().T


# In[14]:


#histogram for each numerical column
for i in heart_data.select_dtypes(include="number").columns:
    sns.histplot(data=heart_data,x=i)
    plt.show()
#incase there are warnings then
import warnings
warnings.filterwarnings("ignore")


# In[15]:


#Boxplot to identify outliers
for i in heart_data.select_dtypes(include="number").columns:
    sns.boxplot(heart_data,x=i)
    plt.show()


# In[16]:


#scatter plot to understand the relationship in the data between the variables
#get the columns first
heart_data.select_dtypes(include="number").columns


# In[17]:


#plot
for i in ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']:
    sns.scatterplot(data=heart_data,x=i,y='restecg')
plt.show()



# In[20]:


#correlation matrix of the numerical columns
s=heart_data.select_dtypes("number").corr()


# In[24]:


#Heat map
plt.figure(figsize=(15,15))
sns.heatmap(s,annot=True)


# In[25]:


#Outlier treatment
def wisker(col):
    q1,q3=np.percentile(col,[25,75])
    iqr=q3-q1
    lw=q1-1.5*iqr
    uw=q3+1.5*iqr
    return lw,uw


# In[29]:


wisker(heart_data['chol'])


# In[27]:


heart_data.columns


# In[ ]:




