
from selenium import webdriver
import os
import selenium
import time
import io
import requests
import csv
import re
#from webdriver_manager.chrome import ChromeDriverManager    # *******=====for chrome 
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
# Create your views here.
import pandas as pd

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path = '/home/sagar/Daily_Work/Scrapping/scrap_data/geckodriver')

#driver.maximize_window()

#from selenium.webdriver.common.keys import Keys  #************====
#driver = webdriver.Chrome("/usr/bin/chromedriver") #************====
def remove_unwanted_data(c_list):
    kk=[]
    for i in range(0,len(c_list)):
        for j in c_list[i]:
                j=j.replace('\t','')
                j=j.replace('\n','')
                kk.append(j)
    return(kk)


def find_table_td_of_tr(all_tr):
    list1=[]
    for tr_index in range(0,len(all_tr)):
        all_td = all_tr[tr_index].find_elements_by_tag_name('td') #find the td(table data)
        weekend_b=(all_td[0].get_attribute('innerText'),all_td[1].get_attribute('innerText'),all_td[2].get_attribute('innerText'),all_td[7].get_attribute('innerText'))
        list1.append(weekend_b)
    return(list1)
def comp_list_fun(ss):
    n=4
    chunks = [ss[i:i+n] for i in range(0, len(ss), n)]
    # print(chunks)
    return(chunks)

with open('urls1.txt') as url:
    final_data = []
    page = 1
    for line in url:
        print("                                           page no", page                                            )
        #sleep(3)
        driver.get(line)
        sleep(3)

        t_table_all = driver.find_element_by_xpath('//*[@id="main-content"]/div/section[1]/div/article/div[4]/div[2]/div[2]/div[2]/div[1]/div/table/tbody')
        all_tr = t_table_all.find_elements_by_tag_name('tr') #find table rows.
        l=find_table_td_of_tr(all_tr)
        #print(l)
        new_list1=remove_unwanted_data(l)
        main_data=comp_list_fun(new_list1)
        print(main_data)
        final_data += main_data
        page+=1
        sleep(3)

data=pd.DataFrame(final_data)
data.to_csv('output.csv',mode='a',header=['LIBELLÉ','DERNIER','VAR. 3 ANS','CAP. BOUR.(MEUR)'])


