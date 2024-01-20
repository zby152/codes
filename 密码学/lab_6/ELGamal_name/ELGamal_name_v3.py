import random
from sympy import isprime, mod_inverse, gcd


def generate_keys(p, alpha):
    """生成密钥"""
    x = random.randint(2, p - 2)
    y = pow(alpha, x, p)
    return x, y


def sign_message(M, p, alpha, x):
    """对消息进行签名"""
    while True:
        k = random.randint(2, p - 2)
        if gcd(k, p - 1) == 1:
            break

    r = pow(alpha, k, p)

    # 这里的 A, B, C 需要根据设计进行选择
    A = 2  # 示例值
    B = M  # 示例值
    C = r  # 示例值

    s = (B + C * x) * mod_inverse(A * k, p - 1) % (p - 1)
    return r, s


def verify_signature(M, r, s, p, alpha, y):
    """验证签名"""
    if not (1 <= r < p):
        return False

    # 使用相同的A, B, C
    A = 2  # 示例值
    B = M  # 示例值
    C = r  # 示例值

    v1 = pow(r, A, p)
    v2 = (pow(alpha, C, p) * pow(y, B, p)) % p
    return v1 == v2


# 示例
p = 31847  # 选择一个大质数p
alpha = 5  # 选择原根alpha

# 生成密钥
x, y = generate_keys(p, alpha)

# 对消息进行签名
M = 1234  # 消息
r, s = sign_message(M, p, alpha, x)
print("签名:", (r, s))

# 验证签名
valid = verify_signature(M, r, s, p, alpha, y)
print("验证结果:", valid)
