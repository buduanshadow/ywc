'''
测试用例获取
登录接口发送请求
'''
from libs.login import Login
from utils.handle_excel import get_excel_data
import pytest
import os
# 测试类
class TestLogin:
    # 测试方法--接口
    # 数据驱动
    @pytest.mark.parametrize('request_data, excepted', get_excel_data('../data/exam.xls', '管理后台-登录', 'login'))
    def test_login(self, request_data, excepted):
        # 1.调用登录接口
        res = Login().login(request_data)
        if 'code' in res:
            assert res['code'] == excepted['code']

if __name__ == '__main__':
    pytest.main([__file__, '-s'])

