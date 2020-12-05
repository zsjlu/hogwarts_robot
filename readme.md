## 第三阶段 第一次作业
./homework/python_practice/game

## 第三阶段 第二次作业

### 作业一
./homework/python_practice/game_opp/homework_describe.py

### 作业二
./homework/python_practice/game_opp/homework_dragon_oath 模块


## 第四阶段 

### 第一次作业

./homework/pytest_learn/tests/test_calc.py

- 使用了@pytest.mark.parametrize（）对案例参数化
- 使用allure工具进行了测试报告生成

    pytest -s -q --alluredir=./report
    
    allure serve ./report
    
### 第二次作业

./homework/pytest_learn/tests/test_par_calc.py

- 使用pyyaml进行案例数据驱动

## 第五阶段 Web自动化

### 第一次作业

./homework/web/demo/test_contact_i_get_cookies.py

- 浏览器复用，获取cookies

### 第二次作业
./homework/web/po_demo

- 问题.一个页面封装的操作的返回值：当前页面对象；其他页面对象；用于断言的元素,这些返回值我们是根据实际页面情况进行返回吗？这里是否是由一条自动化案例的测试重点来界定的。

## 第六阶段 APP自动化（使用了老版本的企业微信，元素定位与老师不同）

### 第一次作业

./homework/app/demo/demo2.py

- demo1.py为练习脚本

### 第二次作业

./homework/app/po_demo

- 新增内容：
    - contact_list_page中增加find_member()方法进行搜索按钮跳转
    
    - 新增page：
    
        - find_contact_page.py
        - persional_*.py

- 问题：请问老师，为什么我在base_page中设置的logging无法打印和写入日志？