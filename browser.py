# -*-coding:utf-8 -*

import os
from os import path
import sys
import random
from datetime import datetime
from time import sleep
import inspect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Bot:
      
        #def __init__(self):                

        def trace(self,stck):                
                print(f"{stck.function} ({ stck.filename}-{stck.lineno})")

        # init
        def init_webdriver(self):
                options = webdriver.ChromeOptions()
                options.add_argument('--disable-blink-features=AutomationControlled')
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_experimental_option('useAutomationExtension', False)
                options.add_argument("--start-maximized")
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)                
                driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                # resout le unreachable
                driver.set_window_size(1900, 1080)
                # driver.set_window_position(0, 0, windowHandle=) #, windowHandle='current')
                driver.maximize_window()
                 
                return driver
        
        def init_main(self):
                try:
                        self.root_app = os.getcwd()
                        self.trace(inspect.stack()[0])                        
                except Exception as e:                        
                        raise

        def newtab(self,url):            
                self.driver.execute_script("window.open('{0}');".format(url))
                self.driver.switch_to.window(self.driver.window_handles[-1]) 
        
        def main(self): 
                
                try:                       
                        self.trace(inspect.stack()[0])                                        
                        self.init_main()
                        self.driver = self.init_webdriver()
                        self.driver.get("http://localhost:8000/api/visit/") 

                        input("Waiting 4 k")
                        self.driver.close()
                        self.driver.quit()
                except KeyboardInterrupt:
                        print("==Interrupted==")
                        pass
                except Exception as e:
                        print("GLOBAL MAIN EXCEPTION")                            
                finally:                        
                        print("do disconnect")                        
            
# INIT
bot = Bot()
bot.main()
