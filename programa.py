from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import numpy as np

# Declarar tres listas vacías con 800 elementos de tipo float
Tc_99m = np.empty(800, dtype=float)
I_131 = np.empty(800, dtype=float)
F_18 = np.empty(800, dtype=float)
I_124 = np.empty(800, dtype=float)

# Verificar el tamaño de las listas

#Condiciones de los calculos
unidades_dosis = "uSv/hr"
unidades_actividad = "mCi"
armadura = "Lead"
actividad_inicial = [30,15,10,5]
distancia = "200"
radio_nucleos = ["Tc-99m","I-131","F-18","I-124"]
paso_inicial = [0.0005,0.00775,0.00975,0.02375]
numero_pasos = 400



#inicializa la conexión con el driver que maneja chrome
driver = webdriver.Chrome()

#inicializamos la página de interés
driver.get("http://www.radprocalculator.com/Gamma.aspx")

#hace click en la opción de la página de agregar armadura
driver.implicitly_wait(0.5)
checkbox = driver.find_element(By.ID,"chkAddShielding")
if not checkbox.is_selected():
    checkbox.click()
    

#selecciona uno de los radionucleidos de la lista que hay

    
    
# Espera a que el elemento cboDoseRateUnits esté presente y sea interactuable
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.ID, 'cboDoseRateUnits')))\
    .send_keys(unidades_dosis)  # Selecciona una de las opciones

WebDriverWait(driver, 10)\
    .until(EC.presence_of_element_located((By.ID, "cboActivityUnits2")))\
    .send_keys('mCi')


#WebDriverWait(driver, 10)\
 #   .until(EC.presence_of_element_located((By.ID, "cboShieldMaterial")))\
  #  .send_keys("Lead")






time.sleep(1)
select5 = driver.find_element(By.ID,"txtEnterDistance")
select5.send_keys(distancia) #envia al cuadro de texto una distancia inicial



print("datos\n")

#El ciclo va cambiando el espesor para así obtener distintos valores de radiación



# ...

# El ciclo va cambiando el espesor para obtener distintos valores de radiación

contador = 0
for valor in range(4):
    
    time.sleep(1)
    select4 = driver.find_element(By.ID,"txtEnterActivity")
    select4.clear()
    select4.send_keys(actividad_inicial[contador]) #envia al cuadro de texto una distancia inicial
    print("La actividad es: ",actividad_inicial[contador])



    #WebDriverWait(driver, 5)\
    #    .until(EC.presence_of_element_located((By.ID, "txtEnterActivity")))\
    #    .clear()
    #WebDriverWait(driver, 5)\
    #    .until(EC.presence_of_element_located((By.ID, "txtEnterActivity")))\
    #    .send_keys(actividad_inicial[contador])
    #print("La actividad es: ",actividad_inicial[contador])

    try:
        driver.implicitly_wait(0.5)
        element = driver.find_element(By.ID, "cboIsotopes_I")
        driver.execute_script("arguments[0].value = arguments[1];", driver.find_element(By.ID, "cboIsotopes_I"), radio_nucleos[contador])
        print("Calculos para el radio isotopo:",radio_nucleos[contador])

    except:
        print("El elemento no fue encontrado.")

    i = 1
    n = 0
    while i <= 400:
        inicio = paso_inicial[contador] * i

        time.sleep(1.5)
        select6 = driver.find_element(By.ID, "txtShieldThickness")
        select6.clear()
        select6.send_keys(str(inicio))



        
        WebDriverWait(driver, 5)\
            .until(EC.presence_of_element_located((By.ID, "cmdCalculate")))\
            .click()


       # time.sleep(1)
        #select7 = driver.find_element(By.ID, "cmdCalculate")
        #select7.click()  # Da click en el botón para calcular la dosis


        # Encuentra el elemento después de la página se actualiza


        try:
            time.sleep(1)
            select8 = driver.find_element(By.ID, "txtAnswer")
            valor = select8.get_attribute('value')
            print(str(inicio) + "," + valor)
            


            if contador == 0:
                Tc_99m = np.append(Tc_99m, valor)

            elif contador ==1:
                I_131 = np.append(I_131, valor)

            elif contador ==2:
                F_18 = np.append(F_18, valor)

            elif contador ==3:
                I_124 = np.append(I_124, valor)
                
        except:
            print(str(inicio)+","+"No pudo ser encontrado")
        

        
        
        if i == 400 and n == 0:
            n = 1
            distancia = 150
            print("Valores para la distancia: ",str(distancia))
            i=0

            time.sleep(1)
            select5 = driver.find_element(By.ID,"txtEnterDistance")
            select5.clear()
            select5.send_keys(distancia) #envia al cuadro de texto una distancia inicial

        elif i == 400 and n == 1:
            distancia = 200
            print("Valores para la distancia: ",str(distancia))
            i=0
            n=2
            time.sleep(1)
            select5 = driver.find_element(By.ID,"txtEnterDistance")
            select5.clear()
            select5.send_keys(distancia) #envia al cuadro de texto una distancia inicial
        elif i==400 and n==2:
            break
            contador = contador + 1

        
        i = i+1


print("Termino el programa")
        
    #lista_espesor.append(str(inicio))
    #lista_dosis.append(select8.get_attribute('value'))