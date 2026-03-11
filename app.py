from flask import Flask, render_template, request, jsonify, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

app = Flask(__name__)

@app.route('/process_tc', methods=['POST'])
def process_tc():
    tc = request.json.get('tc')
    if not tc:
        return jsonify({"TC": "Bilinmiyor", "Durum": "Geçersiz İstek"}), 400
        
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=chrome_options)
        
        for sekme in driver.window_handles:
            driver.switch_to.window(sekme)
            if "internetsube" in driver.current_url.lower():
                break
                
        tc_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "sgkCommonId")))
        tc_input.clear()
        tc_input.send_keys(tc)
        time.sleep(1)
        
        devam_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Devam']")
        driver.execute_script("arguments[0].click();", devam_btn)
        
        time.sleep(8) 
        
        borc_durumu = "Okunamaz"
        geri_lazim = True
        
        if len(driver.find_elements(By.CLASS_NAME, "modal-header")) > 0:
            borc_durumu = "Borc Yok"
            kapat_btn = driver.find_element(By.ID, "popupClose")
            driver.execute_script("arguments[0].click();", kapat_btn)
            time.sleep(1.5)
            geri_lazim = False
        else:
            hata_mesajlari = driver.find_elements(By.ID, "messageTag")
            if len(hata_mesajlari) > 0 and "bulunmamaktadır" in hata_mesajlari[0].text:
                borc_durumu = "Borc Yok"
            else:
                try:
                    tutar_el = driver.find_element(By.XPATH, "//td[contains(@class, 'last')]/span")
                    borc_durumu = tutar_el.text.strip()
                except: pass

        if geri_lazim:
            try:
                geri_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Geri']")
                driver.execute_script("arguments[0].click();", geri_btn)
                time.sleep(2.5)
            except:
                pass
                
        return jsonify({"TC": tc, "Durum": borc_durumu})

    except Exception:
        return jsonify({"TC": tc, "Durum": "Hata"})

@app.route('/save_excel', methods=['POST'])
def save_excel():
    data = request.json.get('results', [])
    if data:
        df = pd.DataFrame(data)
        df.to_excel("sonuclar.xlsx", index=False)
    return jsonify({"status": "ok"})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    return send_file("sonuclar.xlsx", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)