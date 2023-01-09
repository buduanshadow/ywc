
# 读取excel的库
import xlrd
import json

'''
功能需求：获取excel文件指定数据
入参
-文件的路径（路径+文件名+文件格式）
-读取指定的sheet表
-读取指定单元格数据

出参：函数使用者需要什么类型的数据
-返回数据是什么
    -请求体body
    -预期响应结果
    -描述
-数据的类型
    -元组
    -字典
    -列表
    -字符串
    -集合
'''

def get_excel_data(file_path, sheet_name, case_name):
    res_list = []  # 存放结果
    # 1、文件在磁盘---读取到--内存
    # 保持原样式---formatting_info
    work_book = xlrd.open_workbook(file_path, formatting_info=True)
    # 获取所有的表名
    print(work_book.sheet_names())
    # 2、选择对应的sheet
    work_sheet = work_book.sheet_by_name(sheet_name)
    # # 获取一行数据
    # print(work_sheet.row_values(0))
    # # 获取一列数据
    # print(work_sheet.col_values(0))
    # 单元格数据
    # print(work_sheet.cell(0,0).value)  #cell(0,0)---0行0列--id
    # 获取需要的数据
    row_index = 0  # 行编号初始值
    for one in work_sheet.col_values(0):
        # 如果用例有空的话，需要处理
        if case_name in one:
            # 请求体数据
            req_body = work_sheet.cell(row_index, 5).value
            # 期望数据
            exp_data = work_sheet.cell(row_index, 6).value
            res_list.append((json.loads(req_body), json.loads(exp_data)))
        row_index += 1
    return res_list  # 列表里面包含元组


if __name__ == '__main__':
    res = get_excel_data('../data/exam.xls', '管理后台-登录', 'login')
    print(res)
