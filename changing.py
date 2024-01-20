filename = "D:/matlab_codes/result.txt"

with open(filename) as f:
    binary_string = f.read()

# 输入二进制字符串
print(binary_string)

# 将二进制字符串转为字节串
byte_string = bytes.fromhex(binary_string)
#
# # 将字节串解码为UTF-8字符串
utf8_string = byte_string.decode('zh_CN.UTF-8')
#
# # 输出UTF-8字符串
print(utf8_string)
