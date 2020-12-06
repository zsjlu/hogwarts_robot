# -*- coding: utf-8 -*-
# @Time    :2020/12/6 10:20
# @Author  :robot_zsj
# @File    :test_demo.py
import re
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def load_data(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def test_load_data():
    print(load_data("test_data.yml"))


class TestDemo:
    @pytest.mark.parametrize("data", load_data("test_data.yml")["data"])
    def test_search(self, data):
        # driver = webdriver.Chrome()
        # driver.get("https://ceshiren.com/")
        # driver.find_element(By.ID, 'search-button').click()
        # driver.find_element(By.ID, 'search-term').send_keys(keyword)
        for step in load_data("test_data.yml")['steps']:
            # 从steps中读取字典
            if 'webdriver' in step:
                brower = str(step.get('webdriver', {}).get('browser', "chrome")).lower()
                if brower == 'chrome':
                    driver = webdriver.Chrome()
                elif brower == 'firefox':
                    driver = webdriver.Firefox()
                else:
                    print(f"{driver} don't know which browser")
            if 'get' in step:
                url = step.get('get')
                driver.get(url)

            if 'find_element' in step:
                if isinstance(step.get("find_element"), list):
                    by = step.get("find_element")[0]
                    locator = step.get("find_element")[1]
                elif isinstance(step.get("find_element"), dict):
                    by = step.get("find_element")['by']
                    locator = step.get("find_element")['value']
                current_element = driver.find_element(by, locator)

            if 'click' in step:
                current_element.click()

            if 'send_keys' in step:
                value = str(step.get('send_keys'))
                # 判断value是否是变量 ${data}
                # if value == '${data}':
                #     value = data
                # else:
                #     pass
                value = value.replace('${data}', data)
                current_element.send_keys(value)
        sleep(5)
        driver.quit()
