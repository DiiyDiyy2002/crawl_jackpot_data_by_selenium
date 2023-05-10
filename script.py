#Import các thư viện cần thiết
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

data = []
stt = 0
current_date = datetime(2023,2,20) #Khai báo ngày đầu tiên lấy dữ liệu
if stt <= 20*365: #Nếu như quá 20 năm thì thoát vòng lặp
    print("Đang lấy dữ liệu 300 ngày trở về trước kể từ ngày {} tháng {} năm {}".format(current_date.day, current_date.month, current_date.year))
    url = "https://www.thantai.net/so-ket-qua"
    browser.get(url)
    date_pos = browser.find_element(By.ID,"end") #thay thế cho find_element_by_id -- Vào vị trí điền ngày
    date_pos.clear() #Xóa giá trị trong ô
    date_pos.send_keys("{}-{}-{}".format(current_date.day, current_date.month, current_date.year)) #Nhập ngày
    btn = browser.find_element(By.XPATH,"/html/body/div[3]/main/div/form/div[2]/div/button[9]") #Lấy vị trí button
    btn.click()
    
    results = browser.find_elements(By.CLASS_NAME, "font-weight-bold.text-danger.col-12.d-block.p-1.m-0") #tìm vị trí giải đặt biệt
    for row in results:
        print(row.text)
        stt += 1 #Lưu lại số lần ghi dữ liệu
        data.append(row.text) #Ghi dữ liệu vào data
    current_date -= timedelta(days = 300) #Sau một vòng lặp giảm đi 300 ngày

browser.close() #Tắt trình duyệt
