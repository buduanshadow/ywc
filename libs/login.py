'''
封装代码：类
封装
继承
多态
'''

'''
 data: 使用场景 -----在请求头里面的type类型--表单格式
 -表单格式 form ---a=1&b=2
 -表单里有json  a=1&b={"name":"XXX"}
 json: 使用场景 -----在请求头里面的type类型--json格式
 
 分析接口特性：
 MD5：
    -简单的MD5
    -MD5 加盐 salt
    -MD5 双重加盐
    -RSA公密钥
    -AES  
 '''

import requests
from configs.config1 import HOST
from utils.handle_data import get_md5_data
# 封装 登录类，命名规范：首字母大写，使用驼峰法
class Login:
    # 封装登录接口
    def login(self, body_data):
        # 1、请求的url
        url = f'{HOST}/api/auth/oauth/token?grant_type=password'
        # 2、请求头：可以不写
        headers = {"Authorization": "Basic YmFja2VuZDpiYWNrZW5k", "Content-Type": "application/x-www-form-urlencoded"}
        # 3、请求body
        # 字典更新值操作 字典【键名】=新值
        # body_data['password'] = get_md5_data(body_data['password'])  #目前管理后台的加密方式非MD5，这里仅作参考使用
        payload = body_data

        # 4、发送请求
        resp = requests.post(url, data=payload, headers=headers)
        # 5、打印响应数据
        # return resp.text  # 字符串类型
        return resp.json()  #字典类型

# 调用类
if __name__ == '__main__':   # ctrl+j
    # test_data = {"username": "admin","password": "3j2rDKKWiG2QMydKsEoxBQ=="}
    test_data = {"username": "13030878050", "password": "ALakYguKskK7dXwW/2wRug=="}
    # test_data = {"username": "13030878050", "password": "123456"}   #目前管理后台的加密方式非MD5，所以这里仅作参考使用
    # 1、使用类创建实例
    Login = Login()
    # 2、调用登录接口
    res = Login.login(test_data)
    print(res)
