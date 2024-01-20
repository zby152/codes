letters = ['A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

M = ("I am alive here, my beloved, for the reason to adore you. Oh!How anxious I have been for you and how sorry "
     "I am about all you must have suffered in having no news from us. May heaven grant that this letter reaches "
     "you. Do not write to me, this would compromise all of us and above all,do not return under any "
     "circumstances. It is known that it was you who helped us to get away from here and all would be lost if you "
     "should show yourself.We are guarded day and night. I do not care you are not here. Do not be troubled on my "
     "account. Nothing will happen to me. The national assemble will show leniency. Farewell the most loved of "
     "men. Be quiet if you can take care of yourself.For myself I cannot write any more, but nothing in the world "
     "could stop me to adore you up to the death.")

K = "hongye"


def c_alpha(cipher):
    """去掉密文中的非字母且全部转换为大写"""
    cipher_alpha = ''
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            cipher_alpha += cipher[i]

    return cipher_alpha.upper()


def printf(output):
    """将要输出的字符串每150个一行进行输出"""
    i = 0
    for x in output:
        if i == 150:
            print("")
            i = 0
        print(x, end='')
        i += 1
    print("")


def change(M, K):
    """将明文通过密钥加密为密文"""
    m = -1
    k = -1
    result = []
    # index代表当前正在加密的明文标号
    for index in range(len(M)):
        for i in range(len(letters)):

            if letters[i] == M[index]:
                m = i  # m代表当前明文字母的字母表顺序
            if letters[i] == K[index % len(K)]:
                k = i  # k代表当前密钥字母的字母表顺序
        c = (m + k) % 26
        result.append(letters[c])
    return result


if __name__ == "__main__":
    M = c_alpha(M)  # 明文
    K = c_alpha(K)  # 密钥

    print("你输入的明文为:")
    printf(M)
    print("你输入的密钥为:", K)

    C = change(M, K)

    print("所得的密文为：")
    printf(C)
