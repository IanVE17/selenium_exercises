# Importes 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Seleccionar el WebDriver y definir la URL
d = webdriver.Chrome(executable_path=r"C:\Users\ianve\Documents\Universidad\7 Semestre\Calidad de Software\chromedriver.exe")
d.get("https://clima.com")

# Encontrar los elementos 
mx = d.find_element(By.CLASS_NAME, "m_list_countrys_mx")
mx.click()

r = d.find_element(By.CLASS_NAME, "title")
r.click()

sel = d.find_element(By.XPATH, '//*[@id="cityTable"]/div/article/section/ul[1]/li[2]')
sel.click()

# time.sleep(3)

txtcolumns  = d.find_element(By.CLASS_NAME, 'm_table_weather_hour_day').text
# txtcolumns  = d.find_element(By.XPATH, '//*[@id="cityTable"]/div/article/section/ul[1]/li[2]').text
# print("\n --> ", txtcolumns.split('Hoy'))

lista = list(txtcolumns.split('\n'))
todays_weather = txtcolumns.split('Hoy')[0].split('\n')[1:-1]
print(todays_weather)
print(lista)

horas=list()
temp=list()
v_viento=list()

for i in range(0,len(todays_weather),3):
    horas.append(todays_weather[i])
    temp.append(todays_weather[i+1])
    v_viento.append(todays_weather[i+2])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'Velocidad_viento (Km/h)': v_viento})

print(df)
df.to_csv('tiempo_hoy.csv', index=False)
