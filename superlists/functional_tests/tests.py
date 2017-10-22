#!/usr/bin/python
import time

from django.test import LiveServerTestCase
from selenium import webdriver

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/che1/Projects/Django/django_tdd/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 사용자가 새로운 'to-do list' 앱에 대해 알게됨.
        # to-do list 앱 홈페이지에 접속함.
        self.browser.get(self.live_server_url)

        # 사용자가 홈페이지의 타이틀과 헤더의 To-Do를 보고 맞게 찾아온것을 확인함.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 사용자가 해야할 일을 바로 입력할 수 있도록 입력칸이 준비되어있음.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '할 일을 입력하세요.'
        )

        # 사용자가 '기타줄 갈기' 를 텍스트 입력칸에 입력함.
        inputbox.send_keys('기타줄 갈기')

        # 사용자가 엔터를 치면, 페이지가 갱신되고, 입력한 할일 목록이 표시됨.
        # "1: 기타줄 갈기"
        inputbox.send_keys(Keys.ENTER)
        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url, r'lists/.+')
        self.check_for_row_in_list_table('1: 기타줄 갈기')

        # 다른 할일 목록을 추가할 수 있도록  텍스트 입력칸이 유지됨.
        # 사용자가 '피크 사기' 를 추가함.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('피크 사기')
        inputbox.send_keys(Keys.ENTER)

        # 페이지가 다시 갱신되고, 할일 목록에 추가한 항목이 표시됨.
        # "1: 기타줄 갈기"
        # "2: 피크 사기"
        self.check_for_row_in_list_table('1: 기타줄 갈기')
        self.check_for_row_in_list_table('2: 피크 사기')

        # 새로운 사용자가 사이트에 접속함
        ## 이전 사용자의 정보가 쿠키 등으로 새로운 사용자에 전달되지 않도록 하기 위해 새로운 브라우저를 사용함.
        self.browser.quit()
        self.browser = webdriver.Chrome('/home/che1/Projects/Django/django_tdd/chromedriver')

        # 새로운 사용자가 홈페이지에 접속하면 이전 사용자의 리스트가 보이지 않음.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: 기타줄 갈기', page_text)
        self.assertNotIn('2: 피크 사기', page_text)

        # 새로운 사용자가 새로운 할 일 목록을 입력함.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('우유 사기')
        inputbox.send_keys(Keys.ENTER)

        # 새로운 사용자는 자신만의 고유한 URL을 할당받음.
        new_user_list_url = self.browser.current_url
        self.assertIn(new_user_list_url, r'list/.+')
        self.assertNotEqual(new_user_list_url, user_list_url)

        # 이전 사용자의 목록이 없는지 재확인
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: 기타줄 갈기', page_text)
        self.assertNotIn('2: 피크 사기', page_text)

        # 두 사용자 모두 만족함

        self.fail('Finish the test!')
