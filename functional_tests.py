from selenium import webdriver
browser = webdriver.Chrome('/home/che1/Projects/Django/django_tdd/chromedriver')
browser.get('http://localhost:8000')

assert 'Dango' in browser.title
