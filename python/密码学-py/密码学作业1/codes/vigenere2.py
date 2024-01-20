import wordninja

letters = ['A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']


def c_alpha(cipher):
    """去掉密文中的非字母"""
    cipher_alpha = ''
    for i in range(len(cipher)):
        if (cipher[i].isalpha()):
            cipher_alpha += cipher[i]
    return cipher_alpha


def count_CI(cipher):
    """计算cipher的重合指数"""
    N = [0.0 for i in range(26)]
    cipher = c_alpha(cipher)
    L = len(cipher)
    if cipher == '':
        return 0
    else:
        for i in range(L):  # 计算所有字母的频数，存在数组N当中
            if (cipher[i].islower()):
                N[ord(cipher[i]) - ord('a')] += 1
            else:
                N[ord(cipher[i]) - ord('A')] += 1
    CI_1 = 0
    for i in range(26):
        CI_1 += ((N[i] / L) * ((N[i] - 1) / (L - 1)))
    return CI_1


def Bias(uncip):
    """计算当前key_len的偏差"""
    result = 0.0
    for x in uncip:
        result += pow(abs(0.065 - x), 2)
    result = result / len(uncip)
    return result


def count_key_len_CI(cipher, key_len):
    """计算秘钥长度为 key_len 的重合指数,并返回该组的偏差"""
    un_cip = ['' for i in range(key_len)]  # un_cip 是分组
    aver_CI = 0.0
    count = 0
    for i in range(len(cipher_alpha)):
        z = i % key_len
        un_cip[z] += cipher_alpha[i]

    for i in range(key_len):
        un_cip[i] = count_CI(un_cip[i])
        aver_CI += un_cip[i]

    key_len_bias = Bias(un_cip)
    return key_len_bias


def find_key_len(cipher):
    """找出偏差最小的密钥长度并输出"""
    M = [(1, count_CI(cipher))] + [(0, 0.0) for i in range(49)]
    for i in range(2, 50):
        M[i] = (i, count_key_len_CI(cipher, i))

    M = sorted(M, key=lambda x: x[1])  # 按照数组第二个元素排序

    print("密钥长度为：", M[1][0])
    return M[1][0]


# 密文
cipher = (
    'krkpekmcwxtvknugcmkxfwmgmjvpttuflihcumgxafsdajfupgzzmjlkyykxdvccyqiwdncebwhyjmgkazybtdf'
    'sitncwdnolqiacmchnhwcgxfzlwtxzlvgqecllhimbnudynagrttgiiycmvyyimjzqaxvkcgkgrawxupmjwqemi'
    'ptzrtmqdciakjudnnuadfrimbbuvyaeqwshtpuyqhxvyaeffldmtvrjkpllsxtrlnvkiajfukycvgjgibubldpp'
    'kfpmkkuplafslaqycaigushmqxcityrwukqdftkgrlstncudnnuzteqjrxyafshaqljsljfunhwiqtehncpkgxs'
    'pkfvbstarlsgkxfibffldmerptrqlygxpfrwxtvbdgqkztmtfsqegumcfararhwerchvygczyzjaacgntgvfktm'
    'jvlpmkflpecjqtfdcclbncqwhycccbgeanyciclxncrwxofqieqmcshhdccughsxxvzdnhwtycmcbcrttvmurql'
    'phxnwddkopqtehzapgpfrlkkkcpgadmgxdlrchvygczkerwxyfpawefsawukmefgkmpwqicnhwlnihvycsxckf')


def count_n(c1, c2):  # 确定两个子串最优的相对偏移量n=k1-k2
    n = 0
    mins = 100
    k = [0.0 for i in range(26)]
    for i in range(26):
        k[i] = count_MIC(c1, c2, i)
        # print(i,k[i])
        if (abs(k[i] - 0.065) < mins):
            mins = abs(k[i] - 0.065)
            n = i
    return n


def count_MIC(c1, c2, n):
    """计算c1字符串和c2字符串的互重合指数，n为k1-k2的偏移量"""
    count_1 = [0 for i in range(26)]
    count_2 = [0 for i in range(26)]
    L_1 = len(c1)
    L_2 = len(c2)
    MIC = 0
    for i in range(L_1):
        if (c1[i].isupper()):
            count_1[ord(c1[i]) - ord('A')] += 1
        elif (c1[i].islower()):
            count_1[ord(c1[i]) - ord('a')] += 1
    for i in range(L_2):
        if (c2[i].isupper()):
            count_2[(ord(c2[i]) - ord('A') + n + 26) % 26] += 1
        elif (c2[i].islower()):
            count_2[(ord(c2[i]) - ord('a') + n + 26) % 26] += 1
    for i in range(26):
        MIC += count_1[i] * count_2[i] / (L_1 * L_2)
    return MIC


def group_k(cipher, key_len):
    """完成分组操作并计算每一组与第一组的最优相对偏移量并返回"""
    N = ['' for i in range(key_len)]
    MIC = [0 for i in range(key_len)]
    s = [0 for i in range(key_len)]
    for i in range(len(cipher)):  # 对密文进行分组
        m = i % key_len
        N[m] += cipher[i]
    for i in range(1, key_len):  # 计算与第一组之间的相对偏移量
        s[i] = count_n(N[0], N[i])  # s[i] = k1-k(i+1)
        MIC[i] = count_MIC(N[0], N[i], s[i])  # MIC[i] = MIC(1,i+1)
    return s


def miyao(key_len, s, k):
    """当密钥的第一个字母的下标为k时，输出其对应的密钥，返回密钥"""
    mi = ['' for i in range(key_len)]
    for i in range(key_len):
        mi[i] = letters[(k - s[i] + 26) % 26]
    print("第一个偏移量为%d,密钥为%s时" % (k, mi))
    return mi


def change(cipher, key_len, key):
    """输入密文字符串，密钥长度以及密钥返回明文的翻译结果"""
    plain = ''
    i = 0
    key_number = []  # 代表key的下标
    for x in key:
        key_number.append(ord(x) - ord('A'))
    while (i < len(cipher)):
        for j in range(key_len):
            if (cipher[i].isupper()):
                plain += chr((ord(cipher[i]) - ord('A') - key_number[j] + 26) % 26 + ord('A'))
            else:
                plain += chr((ord(cipher[i]) - ord('a') - key_number[j] + 26) % 26 + ord('a'))
            i += 1
            if (i == len(cipher)):
                break
    return plain


def printf(output):
    """将要输出的字符串每150个一行进行输出"""
    i = 0
    for x in output:
        if i == 150:
            print("")
            i = 0
        print(x, end='')
        i += 1


if __name__ == "__main__":
    # 得到密文的字符串
    cipher_alpha = c_alpha(cipher)

    # 求得密钥的长度
    key_len = find_key_len(cipher_alpha)

    # 求得密钥的每个字符之间的偏移量
    s = group_k(cipher_alpha, key_len)
    print("密钥每个字符之间的偏移量是", s)

    # 将26个不同的密钥的翻译结果分词之后输出
    for k in range(26):
        key = miyao(key_len, s, k)
        plain = change(cipher_alpha, key_len, key)
        word = wordninja.split(plain[0:20])
        word_result = ''
        for i in range(len(word)):
            word_result += word[i]
            word_result += ' '
        print(word_result)

    # 获取最合适的密钥
    k = int(input("请参考上面的输出，输入符合语义的结果的偏移量"))
    key = miyao(key_len, s, k)
    print("得到的密钥为:", key)

    # 已知密钥，将密文转换为明文
    plain = change(cipher_alpha, key_len, key)
    word = wordninja.split(plain)
    word_result = ''
    for i in range(len(word)):
        word_result += word[i]
        word_result += ' '

    # 将明文结果输出
    print("翻译之后的明文为:")
    printf(word_result)
