#!/usr/bin/python

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/che1/Projects/Django/django_tdd/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 사용자가 새로운 'to-do list' 앱에 대해 알게됨.
        # to-do list 앱 홈페이지에 접속함.
        self.browser.get('http://localhost:8000')

        # 사용자가 홈페이지의 타이틀과 헤더를 보고 맞게 찾아온것을 확인함.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 사용자가 해야할 일을 바로 입력할 수 있도록 준비되어있음.

        # 사용자가 '기타줄 갈기' 를 텍스트 입력칸에 입력함.

        # 사용자가 엔터를 치면, 페이지가 갱신되고, 입력한 할일 목록이 표시됨.
        # "1: 기타줄 갈기"

        # 다른 할일 목록을 추가할 수 있도록  텍스트 입력칸이 유지됨.
        # 사용자가 '피크 사기' 를 추가함.

        # 페이지가 다시 갱신되고, 할일 목록에 추가한 항목이 표시됨.
        # "1: 기타줄 갈기"
        # "2: 피크 사기"

        # 사용자가 이 목록을 저장하고 싶어하는 찰나에, 사이트에서 사용자를 위한 고유한 URL을 만들어 준 것을 발견함. (이 URL에 대한 설명이 달려있음)

        # 사용자가 해당 URL에 접속하면 작성한 할일 목록이 저장되어 있음.

        # 사용자는 만족하고 자러감.


if __name__ == '__main__':
    unittest.main(warnings='ignore')