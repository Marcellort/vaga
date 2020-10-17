from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


from selenium.webdriver.support.wait import WebDriverWait


class login:
    def __init__(self,user,passw):
        self.user=user
        self.passw=passw
        self.driver = webdriver.Firefox(executable_path=r'E:\Desktop\geko\geckodriver.exe')

    def relatorio(self):
        driver= self.driver
        driver.get('https://marketplace.integracommerce.com.br/v2/Order')
        time.sleep(4)
        usuario = driver.find_element_by_id("username")
        usuario.send_keys(self.user)
        first_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/div[2]/div/div/div[1]/div/form/div[1]/label")))
        first_option.click()
        password = driver.find_element_by_id("password")
        password.send_keys(self.passw)
        first_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/div[2]/div/div/div[1]/div/form/div[1]/label")))
        first_option.click()
        time.sleep(2)
        login= driver.find_element_by_xpath('//*[@id="kc-login"]').click()
        time.sleep(10)
        fecharmodal = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".bootbox-close-button")))
        fecharmodal.click()
        time.sleep(3)
        ordens = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#intPedidosV2 > a:nth-child(1)")))
        ordens.click()
        time.sleep(5)
        driver.switch_to.frame(driver.find_element_by_css_selector('.container-fluid > iframe:nth-child(1)'))

        data = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[1]").click()
        time.sleep(5)
        data=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/button[3]").click()
        data=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/button[3]").click()
        data=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/button[8]").click()
        data=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/button[1]").click()
        data=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/button[1]").click()
        data=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/button[3]").click()
        data=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/button[2]").click()

teste = login('desenvolvimento@comprenet.com.br',"tecnol@gia2@17")
teste.relatorio()

