from selenium import webdriver
import time
root = '1861010111'
password = 'Ldh02218'
url = 'http://my.hhu.edu.cn/login.portal'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(root)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="changeBack"]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/div/input[1]').click()
form = 'http://form.hhu.edu.cn/pdc/form/list'
driver.get(form)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/section/section/div/a/div[2]').click()
driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
