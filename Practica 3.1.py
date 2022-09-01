# Importes 
from selenium import webdriver
from selenium.webdriver.common.by import By

# Seleccionar el WebDriver y definir la URL
d = webdriver.Chrome(executable_path=r"C:\Users\Dell\Documents\IAN\Universidad\7 Semestre\Calidad de Software\chromedriver.exe")
d.get("https://clima.com")

# Encontrar los elementos 
mx = d.find_element(By.CLASS_NAME, "m_list_countrys_mx")
mx.click()

r = d.find_element(By.CLASS_NAME, "title")
r.click()

sel = d.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[4]/div[1]/section[4]/section[1]/div[1]/article[1]/section[1]/ul[1]/li[2]/h2[1]/a[1]")
sel.click()
