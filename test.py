
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import math
import time

def run():
    #첫 페이지 파싱하기
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    container = soup.find('div', id="_review_filter_container")
    div_atcs = container.find_all('div', class_='atc')
    for div_atc in div_atcs:
        review_text = div_atc.getText()

        #텍스트파일에 넣기
        with open("./text.txt",'a',encoding= 'UTF-8') as f:
            f.write(str(review_text) + '\n')


    #두번째 페이지부터 크롤링



    #리뷰 갯수 구하기
    review_div = soup.find('div', id='fixed_tab_area')
    review_lis = review_div.find_all('li')
    print(str(review_lis[2].getText()))


    #정규표현식
    #p = re.compile('[0-9]+')
    #m = p.search(str(review_lis[2].getText()))
    #review_count = m.group() # 서치한 결과값을 반환해주는 함수 group()
    review_count = 2931


    for i in range(1,math.ceil(review_count/20)):
        paging_btn = driver.find_element_by_xpath('//*[@id="_review_paging"]/a[%d]' % i)
        paging_btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        container = soup.find('div', id="_review_filter_container")
        div_atcs = container.find_all('div', class_='atc')
        for div_atc in div_atcs:
            review_text = div_atc.getText()
            with open("./text.txt", 'a', encoding='UTF-8') as f:
                f.write(str(review_text) + '\n')

        time.sleep(1)





#크롤 내용 저장할 텍스트 파일 만들기
with open('./text.txt', 'w', encoding='UTF-8') as f:
    f.write('크롤링시작! \n')

# Create your tests here.

driver = webdriver.Chrome('./chromedriver')



driver.get('https://search.shopping.naver.com/detail/detail.nhn?cat_id=50000151&nv_mid=16932807264&query=%EB%85%B8%ED%8A%B8%EB%B6%81&frm=NVSCPRO&NaPm=ct%3Djzz3nluo%7Cci%3D9424046f4b74c73bd30305f7d087a3211bdfa8f2%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D14b9618c7e0f4d451f45194f2add0c53c53b695c')
run()