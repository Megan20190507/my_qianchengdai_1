# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 7:57
# @Author  : Megan
# @Email   : 732286263@qq.com
# @File    : home_woek1_0226.py
# @Software: PyCharm Community Edition

#  maketrans函数和translate函数
a='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
b=a.swapcase()
intab= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
outtab='ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
table=b.maketrans(intab, outtab)
print('转换为大写后的字符为：%s'%(b))
print('        镜像字符串为：%s'%(b.translate(table)))
print('--------------------------------------------------------------------')
#chr函数和ord函数
s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
new_s=''
# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))
for i in s.swapcase():
    if i.islower():
        i=chr(219-ord(i))
        new_s+=i
    elif i.isupper():
        i=chr(155-ord(i))
        new_s+=i
print('转换为大写后的字符为：%s'%(b))
print('        镜像字符串为：%s'%(new_s))




