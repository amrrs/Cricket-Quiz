
# coding: utf-8

# # # Automated Cricket Quiz Generator

# from bs4 import BeautifulSoup as bs
# import urllib2
# import pandas as pd
# import random
# #from collections import defaultdict

# In[3]:

url = 'http://stats.espncricinfo.com/ci/content/records/223646.html'


# In[4]:

header = {'User-Agent': 'Mozilla/5.0'} 
req = urllib2.Request(url,headers=header)
content = urllib2.urlopen(req)
soup = bs(content)


# In[5]:


table = soup.find('table',{'class':'engineTable'})

header = [th.text for th in table.find('thead').select('th')]

empty = []
for row in table.findAll('tr',{'class':'data1'}):
    newr = []
    for td in row.select('td'):
        newr.append(td.text)
    #print(newr)
    empty.append(newr)   

score_data = pd.DataFrame(empty,columns=header)
#score_data


# In[6]:


def qn_generator(row_index,col_index):
    qn_key_f = {'What is the ':['HS','Ave'],'How many ':['Scored by ','Played by ']}
    qn_key_b = dict({'Scored by ':['100','50','Runs','0','NO'],'Played by ':['Mat','Inns']})
    for key,val in qn_key_f.items():
    #print(col_index)
        if col_index in val:
            #print(col_index)
            print 'What is the ' + col_index + ' of ' +score_data.iloc[row_index]['Player'] + '?\n'
            break
        else:
            for keyb,valb in qn_key_b.items():
            #print(valb)
                if col_index in valb:
                    print 'How many ' + col_index, keyb  +score_data.iloc[row_index]['Player'] + '?\n'
                    break
        break           


# In[7]:

def option_generator(row_index,column_index):
    
    options = [row_index,random.choice(range(len(score_data))),random.choice(range(len(score_data))),random.choice(range(len(score_data)))]
    random.shuffle(options)
    #print(options)
    for i,val in enumerate([score_data.iloc[option][column_index].replace('*','') for option in options]):
        print('Option '+str(i+1)+' : '+val)
        if val == score_data.iloc[row_index][column_index].replace('*',''):
            right_option = i+1
    return(right_option)        


# In[14]:

if __name__ == "__main__":
    row_index = random.choice(range(len(score_data)))
    col_index = random.choice(score_data.columns[2:])
    print 'Welcome to Cricket Test Quiz'
    qn_generator(row_index,col_index)
    right_option = str(option_generator(row_index,col_index))
    answer = raw_input('\nEnter the right option 1/2/3/4:  ')
    print('You are right' if answer == right_option else 'Sorry, Good Luck Next time')


# Courtesy: 'http://stats.espncricinfo.com/ci/content/records/223646.html'
