# -*- coding: utf-8 -*-
# @Time    :2020/12/6 10:20
# @Author  :robot_zsj
# @File    :test_demo.py
import re
from time import sleep

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.remote.webelement import WebElement


def load_data(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def test_load_data():
    print(load_data("test_data.yml"))


def data_gen(data):
    # 啥也不是
    res = []
    # 判断数据是否为字典类型
    if isinstance(data, dict):
        # 获取字典值长度
        length = len(list(data.values())[0])
        # 循环字典值长度的次数
        for i in range(length):
            temp = []
            # 将字典值依次取出
            for value in data.values():
                # 在temp中添加value1
                temp.append(value[i])
            # res中添加temp1
            res.append(temp[0])
    print(res)
    # 返回res
    return res

class TestDemo:
    data_file = load_data("test_data.yml")
    test_data = data_gen(data_file['data'])
    test_steps = data_file['steps']

    driver: WebDriver = None
    current_element: WebElement = None
    _var = {}

    @pytest.mark.parametrize("data", test_data)
    def test_search(self, data):
        # driver = webdriver.Chrome()
        # driver.get("https://ceshiren.com/")
        # driver.find_element(By.ID, 'search-button').click()
        # driver.find_element(By.ID, 'search-term').send_keys(keyword)
        for step in self.test_steps:
            # 从steps中读取字典
            if isinstance(step, dict):
                # 会自动把step默认置为字典，这样编写时可以提示
                if 'webdriver' in step:
                    brower = str(step.get('webdriver', {}).get('browser', "chrome")).lower()
                    if brower == 'chrome':
                        driver = webdriver.Chrome()
                    elif brower == 'firefox':
                        driver = webdriver.Firefox()
                    else:
                        print(f"{driver} don't know which browser")

                    if driver is not None:
                        driver.implicitly_wait(10)

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
                    if by == "css":
                        by = By.CSS_SELECTOR
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
                    value = self.replace(value, data)
                    current_element.send_keys(value)
                if str(list(step.keys())[0]).startswith('get_a'):
                    _return = current_element.get_attribute(list(step.values())[0])
                    print(_return)
                    self._var["return"] = _return

                if 'var' in step:
                    for k, v in dict(step.get("var")).items():
                        v = self.replace(v, data)
                        self._var[k] = v

                if 'asser_in' in step:
                    assert_data = list(step.values())[0]
                    sub = assert_data[0]
                    sub = self.replace(sub, data)
                    collection = assert_data[1]
                    collection = self.replace(collection, data)
                    assert sub in collection

        sleep(5)
        driver.quit()

    def replace(self, content, param=None):
        if isinstance(content, str):
            for k, v in self._var.items():
                if v is None:
                    v = ""
                content = content.replace(f'${{{k}}}', v)
            if param is not None:
                content = content.replace('${data}', param)
        return content
