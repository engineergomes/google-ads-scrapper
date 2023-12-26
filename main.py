import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import spreadsheet
import re
from bs4 import BeautifulSoup
import random
from datetime import datetime
import requests



planilha = spreadsheet.access_spreadsheet()
stack = planilha.worksheet("Geral")
stack2 = planilha.worksheet("Palavras Chave")
valores = spreadsheet.return_values(planilha)
tabela = pd.DataFrame(valores)
keywords = tabela.keyword
ads_url = []
i = 0
ads_list = []
k = 0
word_counter = 0
def scroll_down():
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

options = webdriver.ChromeOptions()
service = Service(executable_path=r'./chromedriver')


# options.add_argument("--headless")
options.add_argument("--incognito")

random.seed()

browser = webdriver.Chrome(service=service, options=options)
browser.get("https://www.google.com/search?q=aaa&source=hp&ei=G5J5Yq3gGpiq1sQP7NCH4AQ&iflsig=AJiK0e8AAAAAYnmgKxlMgmed1qcgn8cSftu1dd1NpfV1&ved=0ahUKEwjt2aytuNP3AhUYlZUCHWzoAUwQ4dUDCAc&uact=5&oq=aaa&gs_lcp=Cgdnd3Mtd2l6EAMyDgguEIAEELEDEMcBEKMCMgsILhCABBCxAxDUAjIFCAAQgAQyCwguEIAEEMcBEK8BMggILhCABBCxAzIFCAAQgAQyBQguEIAEMggIABCxAxCDATIICAAQgAQQsQMyEQguEIAEELEDEIMBEMcBENEDOgsILhCABBCxAxCDAToLCC4QgAQQxwEQ0QM6CwguELEDEIMBENQCOggILhCxAxCDAToUCC4QgAQQsQMQgwEQxwEQowIQ1AI6CwguEIAEEMcBEKMCOgsIABCABBCxAxCDAVC3gAJYiIMCYLKFAmgCcAB4AIABgAGIAcoCkgEDMC4zmAEAoAEBsAEA&sclient=gws-wiz")

for keyword in keywords:
  
  time.sleep(1+(random.random()*2))
  browser.find_element(By.XPATH,"//form//textarea").click()
  action = ActionChains(browser)
  action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
  browser.find_element(By.XPATH,"//form//textarea").send_keys(keyword)
  time.sleep(0.7+(random.random()*2))
  browser.find_element(By.XPATH,"//form//textarea").send_keys(Keys.ENTER)
  time.sleep(1+(random.random()*2))

  for p in list(range(4)):

    ad_name = browser.find_elements(By.XPATH, "//div[@class='uEierd']//div/div/div/a/div[1]/span")
    print("ad name", ad_name)
    upper_url = browser.find_elements(By.XPATH, "//div[@class='uEierd']//div/div/div/a/div[2]/span[1]/span[2]/span[2]")
    print("upper url", upper_url)
    ads_urls = browser.find_elements(By.XPATH, "//div[@class='uEierd']/div/div/div/div/a") #pega o conteudo de toda a tag <a>
    print('ads urls', ads_urls)
    ads_url = [elem.get_attribute('href') for elem in ads_urls] #separa a url (href) da tag <a> e coloca na variavel nova
    print("ads url",ads_url)
    ads_sub = browser.find_elements(By.XPATH, "//div[@class='Va3FIb r025kc lVm3ye']")
    print("adssub",ads_sub)
    top_ads_count = len(browser.find_elements(By.XPATH, "//*[@id='tvcap']//div[@class='uEierd']"))
    print("top_ads_count",top_ads_count)
    google_page = p + 1
    print('google page', google_page)

    lista_palavras = keyword.split()
    print(" ")
    print("Palavra de Pesquisa: " + keyword + "  -  "  + "Pagina google: " + str(google_page) +  "  -  Total de Anuncios: " + str(len(ad_name))+":")
    print("Posicao  URL" )
  
    for i in list(range(len(ad_name))):
      ads_list = []
      flag = ""
    
      #scrapping de contatos dentro da pagina do ads
      print (str(i+1) + "        "+ ads_url[i] )
      try:
        url = ads_url[i]
        res = requests.get(url)
        # time.sleep(8+(random.random()*2))
        html_page = res.text
        soup = BeautifulSoup(html_page, 'html.parser')

        body_bs4 = soup.find('div')

        if body_bs4 == None:
          facebook_link = ""
          instagram_link= ""
          email = ""
          flag = "Site com bloqueio"
          
        else:
          try:
            instagram_link= soup.find(href=re.compile("instagram")).get('href')
          except:
            instagram_link= ""

          try:
            facebook_link = soup.find(href=re.compile("facebook")).get('href')
          except:
            facebook_link = ""

          try:
            email = soup.find(href=re.compile("mailto:")).text
          except:
            email = ""

      except:
        facebook_link = ""
        instagram_link= ""
        email = ""
        flag = "BO no acesso do site"
      
      #faz verificação se o texto do anuncio contem a palavra chave, usar barra de espaço como separador para verificar cada 
      #palavra de forma independente
        
      print("lista palavras", lista_palavras)
      print("list", list(range(len(lista_palavras))))
      for k in list(range(len(lista_palavras))):
        # print(lista_palavras[k])
        print('ad name',ad_name[i].text.lower())
        print('ads sub[i]',ads_sub[i].text.lower())
        if lista_palavras[k].lower() in (" " + ads_sub[i].text.lower() + " " + ad_name[i].text.lower() + " " ):
          word_counter = word_counter + 1
        else:
          word_counter = word_counter + 0
        

      copy_sinergy_ads = str(round((word_counter/len(lista_palavras))*100,1)).replace('.', ',') + "%"
      word_counter = 0

      #faz verificação se o texto do caminho contem a palavra chave, usar barra de espaço como separador para verificar cada palavra de forma independente
      for j in list(range(len(lista_palavras))):
        # print(lista_palavras[j])
        if lista_palavras[j].lower() in (" " + upper_url[i].text.lower()  + " " ):
          word_counter = word_counter + 1
        else:
          word_counter = word_counter + 0
        
      
      copy_sinergy_way = str(round((word_counter/len(lista_palavras))*100,1)).replace('.', ',') + "%"
      word_counter = 0
      
      
      if(i<top_ads_count):
        #site link
        try:
          site_link_validator = browser.find_element(By.XPATH,"//*[@id='tvcap']//div[@class='uEierd']["+str(i+1)+"]//*[@class='bOeY0b'] ")
          site_link = 'Sim'
        except:
          site_link = '-'
        
        #localização
        try:
          location_validator = browser.find_element(By.XPATH,"//*[@id='tvcap']//div[@class='uEierd']["+str(i+1)+"]//*[@class='Qezod'] ")
          location = 'Sim'
        except:
          location = '-'


        try:
          phone_numbers = browser.find_element(By.XPATH,"/div[@jscontroller='x8umHb']")
          phone_number=phone_numbers.get_attribute('data-dpn')
          ads_list.append([ads_url[i],keyword, google_page, copy_sinergy_ads, copy_sinergy_way, site_link , 'Sim', location, '', '', '', '', '', email, instagram_link, facebook_link,  phone_number, '', flag])
        except:
          try:
            phone_numbers = browser.find_element(By.XPATH,"//*[@id='tvcap']//div[@class='uEierd']["+str(i+1)+"]//*[@class='Qezod']/span[2]")
            phone_number=phone_numbers.text
            ads_list.append([ads_url[i],keyword, google_page, copy_sinergy_ads, copy_sinergy_way, site_link , 'Sim', location, '', '', '', '', '', email, instagram_link, facebook_link,  phone_number, '', flag]) 
          except:
            ads_list.append([ads_url[i],keyword, google_page, copy_sinergy_ads, copy_sinergy_way, site_link , '-', location, '', '', '', '', '', email, instagram_link,  facebook_link, '', '', flag])
      else:

              #localização

        try:
          location_validator = browser.find_element(By.XPATH,"//*[@id='bottomads']//div[@class='uEierd']["+str(i+1-top_ads_count)+"]//*[@class='Qezod'] ")
          location = 'Sim'
        except:
          location = '-'

        #site link
        try:
          site_link_validator = browser.find_element(By.XPATH,"//*[@id='bottomads']//div[@class='uEierd']["+str(i+1-top_ads_count)+"]//*[@class='bOeY0b'] ")
          site_link = 'Sim'
        except:
          site_link = '-'

        try:
          phone_numbers = browser.find_element(By.XPATH,"/div[@jscontroller='x8umHb']")
          phone_number=phone_numbers.get_attribute('data-dpn')
          ads_list.append([ads_url[i],keyword, google_page, copy_sinergy_ads, copy_sinergy_way, site_link , 'Sim', location, '', '', '', '', '', email, instagram_link, facebook_link,  phone_number, '', flag])
        except:
          try:
            phone_numbers = browser.find_element(By.XPATH,"//*[@id='tvcap']//div[@class='uEierd']["+str(i+1)+"]//*[@class='Qezod']/span[2]")
            phone_number=phone_numbers.text
            ads_list.append([ads_url[i],keyword, google_page, copy_sinergy_ads, copy_sinergy_way, site_link , 'Sim', location, '', '', '', '', '', email, instagram_link, facebook_link,  phone_number, '', flag]) 
          except:
            ads_list.append([ads_url[i],keyword, google_page, copy_sinergy_ads, copy_sinergy_way, site_link , '-', location, '', '', '', '', '', email, instagram_link,  facebook_link, '', '', flag])

    

      stack.append_rows(ads_list)

      scroll_down()
      time.sleep(1+(random.random()*2))


    # browser.find_element(By.XPATH,"//*[@id='pnnext']").click()  
   
  cell = stack2.find(keyword)
  currentDateTime = datetime.now()
  stack2.update_cell(cell.row, cell.col - 1, currentDateTime.strftime('%d/%m/%Y %H:%M')) 
