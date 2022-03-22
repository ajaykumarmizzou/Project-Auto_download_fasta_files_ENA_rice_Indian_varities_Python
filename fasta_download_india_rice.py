# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:25:58 2022

@author: Ajay Kumar (xenificity)
"""

#Import packages
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time
import os

#fetching locus ids from excel file
os.chdir('D:/_IRRI-SOUTH ASIA/Team_works/Dr_Krishna/Script_2_download_data') #Set your path where you are keeping IRIS id list
print("*****Automation Script for extracting haplotypic information*****")
print("\n PLEASE WAIT uploading in progress, list of locus id......")
time.sleep(5)

df = pd.read_csv('varieties-Variety_List.csv')
print("\n\n Your locus ids are following:")

#Pass loc_id or csv file containing loc_ids
df = df.iloc[0:,1] #Select the column of IRIS ids
print(df)
print("\n\n Your data is starting to download, please wait.!")
time.sleep(4)

#For each loc_id, script will execute and download the corresponding dataset
def automate_SNP(df):
    for x in df:
        locus_id = x # for each id
        print("\n\n")
        print("Downloading data for \t",locus_id)
        #passing url here
        try:
            file_url = r'https://www.ebi.ac.uk/ena/browser/home'
            open_tab = webdriver.Chrome()
            #driver = webdriver.Chrome(executable_path='D:/_IRRI-SOUTH ASIA/Breeding for Crop Improvement Training - IRRI CGIAR/Breeding for Crop Improvement Training/Automation_python_script_Ajay/88.0.4324.104_chrome_installer.exe') #note here you should have installed webdriver for opening browser
            open_tab.get(file_url) #opening tab here
            input_box =open_tab.find_element_by_xpath('/html/body/div[1]/div/header/div/app-header/div/div[2]/div[1]/form/div/div[1]/input')
            input_box.send_keys(locus_id)
            time.sleep(5)
            search_button = open_tab.find_element_by_xpath('/html/body/div[1]/div/header/div/app-header/div/div[2]/div[1]/form/div/div[2]/button')
            search_button.click()
            time.sleep(5)
            click_1 = open_tab.find_element_by_xpath('/html/body/div[1]/section/div/div/div/app-root/div/section/app-text-search/div/div[2]/div[2]/div[2]/div/ul/div/div[2]/div[1]/a')
            click_1.click() #readmore
            time.sleep(15)
            click_2 = open_tab.find_element_by_xpath('/html/body/div[1]/section/div/div/div/app-root/div/section/app-view/div/app-view-record/div/div[2]/div[2]/div[1]/div[4]/div/div[2]/a')
            click_2.click() #download all fasta
            time.sleep(10)
            click_3 = open_tab.find_element_by_xpath('/html/body/div[1]/section/div/div/div/app-root/div/section/app-view/div/app-view-record/div/div[2]/div[1]/div[4]/div/div[2]/app-read-file-links/div/div[3]/table/thead/tr/th[7]/div/a')
            click_3.click() #clicking yes 
            time.sleep(10)
            click_4 = open_tab.find_element_by_xpath('/html/body/div[6]/div[2]/div/mat-dialog-container/app-confirmation-dialog/div[3]/button[2]')
            click_4.click()
            time.sleep(20)
            Alert(open_tab).accept()
            
            
            #open_tab.close() #close the tab
          
        except:
            print('An error occured at',locus_id)
            continue

    print("Fasta files successfully downloaded!")
automate_SNP(df)
