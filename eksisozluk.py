from selenium import webdriver

browser = webdriver.Chrome("/Users/ksergenozel/Desktop/chromedriver")

url = "https://eksisozluk.com/python-programlama-dili--6303607"

browser.get(url)

last = int(browser.find_element_by_css_selector(".last").text)

entries = list()

for i in range(1, last + 1):
  url = "https://eksisozluk.com/python-programlama-dili--6303607?p="
  url = url + str(i)
  browser.get(url)
  elements = browser.find_elements_by_css_selector(".content")
  for element in elements:
    entries.append(element.text)

with open("entries.txt", "w", encoding = "UTF-8") as file:
  for entry in entries:
    file.write(entry + "\n" + "*"*100 + "\n")
  
browser.close()