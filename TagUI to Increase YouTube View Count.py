#!/usr/bin/env python
# coding: utf-8

# In[21]:


#pip install tagui


# #### Using this script to increase youtube views. Do use it at your own risk because Youtube's algorithm may be to detect this and either your views may not count after a while or YouTube may decide to ban you instead!
# 
# #### Key assumptions
# - Running Jupyter Notebook on Chrome
# - if running python on terminal, you should be on Chrome page
# 

# In[22]:


import tagui as t


# In[23]:


cycles = input("Number of Cycles :") #Number of View tabs you want to create
duration = input("Duration to Run Videos Before Stopping(Seconds):") #Duration you want to give before closing all videos
url = input("YouTube URL: ")
int_cycles = int(cycles)
int_duration = int(duration)


# In[24]:


t.init(visual_automation = True, chrome_browser = True) #chrome_browser set to false since I am already running chrome
t.url(url)
for i in range(int_cycles):
    t.keyboard('[ctrl][shift][n]')
    t.keyboard(url)
    t.keyboard('[enter]')
    t.wait(3)
    t.click(900, 300)
t.wait(int_duration) #Time you want to let the video run

for i in range(int_cycles):
    t.click(1900, 15)
t.close()

