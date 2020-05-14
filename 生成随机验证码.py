"""
封装一个函数,函数的功能是生成指定长度的验证码
要求:由数字和大小写英文字母构成的随机字符串
"""
import random
def rcode(n):
    code_list=[]
    for i in range(10):
        code_list.append(str(i))
    for i in range(65,91):
        code_list.append(chr(i))
    for i in range(97, 123):
        code_list.append(chr(i))

    code = random.sample(code_list,n)
    code = "".join(code)
    return code

if __name__ == '__main__':
    print(rcode(4))