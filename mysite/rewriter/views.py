from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
import time
import pathlib
import requests
import urllib
import os
import re

# Create your views here.

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(str(pathlib.Path(__file__).parent.absolute()) + '\\chromedriver.exe',options=options)
url="https://quillbot.com/"
driver.get(url)
elelogins = driver.find_elements_by_class_name('MuiButton-label')
for i in range(0, len(elelogins)):
    if (elelogins[i].text == "Log In"):
        elelogins[i].click()
        break

time.sleep(2)

eleInputs = driver.find_elements_by_class_name('MuiFilledInput-input')
eleInputs[0].send_keys('fadeevdoma@gmail.com')
eleInputs[1].send_keys('quillbotpass')
time.sleep(0.5)

driver.find_element_by_class_name('auth-btn').click()    
time.sleep(3)   

if(len(driver.find_elements_by_class_name('MuiDialog-paper')) > 0):
    elebuttons = driver.find_elements_by_class_name('MuiIconButton-root')
    for i in range(0, len(elebuttons)):
        try:
            elebuttons[i].click()
            break
        except:
            pass     

eleSliders = driver.find_elements_by_class_name('MuiSlider-thumbColorPrimary')

for i in range(0, len(eleSliders)):
    try:
        eleSliders[i].send_keys(Keys.ARROW_RIGHT)
        eleSliders[i].send_keys(Keys.ARROW_RIGHT)
        eleSliders[i].send_keys(Keys.ARROW_RIGHT)
        break
    except:
        pass 

time.sleep(3)  


def index(request):    
    return render(request, 'index.html')

def onRewrite(request):
    sInput = request.POST.get('input', None)
    sListInput = sInput.split('\n')
    sListOutput = sListInput       

    try: 
        for v in range(0, len(sListInput)):

            sListInput[v] = re.sub("[^\u0000-\u007F]", "", sListInput[v])
            if (sListInput[v].strip() != ""):
                if(len(driver.find_elements_by_class_name('MuiDialog-paper')) > 0):
                    elebuttons = driver.find_elements_by_class_name('MuiIconButton-root')
                    for i in range(0, len(elebuttons)):
                        try:
                            elebuttons[i].click()
                            break
                        except:
                            pass     

                WebDriverWait(driver, 600).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0')))              
                time.sleep(1)

                eleInputbox = driver.find_element_by_id('inputText')
                eleInputbox.clear()
                time.sleep(0.5)
                eleInputbox.send_keys(sListInput[v])                

                time.sleep(1)
                WebDriverWait(driver, 600).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0'))).click()
                time.sleep(1)

                WebDriverWait(driver, 600).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0')))

                sOutput = driver.find_element_by_id('articleTextArea').text
                sListOutput[v] = sOutput

    except Exception as e:
        data = {
            'result' : str(e)
        }
        return JsonResponse(data)

    data = {
        'result' : '\n'.join(sListOutput)
    }
    return JsonResponse(data)
