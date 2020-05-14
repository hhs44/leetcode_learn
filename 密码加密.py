"""
封装一个函数,函数的功能是对密码加密,
默认密码中只有小写字母和空格，
加密规则是 a变d, b变e, c变f, ...., u变x, v变y, w变z,  x变a, y变b,  z变c. 空格保持不变
"""
def rfcode(s):
    rfcode_dict={}
    for i in range(97, 123):
        rfcode_dict[chr(i)]=chr(i+3)
    rfcode_dict['x']='a'
    rfcode_dict['y']='b'
    rfcode_dict['z']='c'
    code=''
    for x in s:
        code+=rfcode_dict[x]
    print(code)

if __name__ == '__main__':
    rfcode('asdfg')