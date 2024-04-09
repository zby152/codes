from collections import deque


CHARSET = 26  # 假设只有小写字母


class TrieNode:
    def __init__(self):
        self.pattern_indices = []  # 模式串在模式列表中的索引
        self.children = [None] * CHARSET  # 子节点
        self.fail = None  # fail指针


root = TrieNode()


def insert(s, index):
    """将子串造成一个树，叶子的pattern_indices为当前子串的下标"""
    curr = root
    for ch in s:
        idx = ord(ch) - ord('a')  # 获取字符的索引
        if curr.children[idx] is None:  # 如果子节点不存在，创建新节点
            curr.children[idx] = TrieNode()
        curr = curr.children[idx]
    curr.pattern_indices.append(index)  # 存储模式串的索引


def build_fail():
    # q为双向链表
    q = deque()

    root.fail = None  # 根节点的fail指针设置为None
    q.append(root)
    while q:
        curr = q.popleft()
        for i in range(CHARSET):
            if curr.children[i]:
                if curr == root:
                    curr.children[i].fail = root
                else:
                    temp = curr.fail
                    while temp:
                        if temp.children[i]:
                            curr.children[i].fail = temp.children[i]
                            break
                        temp = temp.fail
                    if not temp:
                        curr.children[i].fail = root
                q.append(curr.children[i])


def search(s, res):
    curr = root
    for ch in s:
        index = ord(ch) - ord('a')
        while not curr.children[index] and curr != root:
            curr = curr.fail
        curr = curr.children[index] if curr.children[index] else root
        temp = curr
        while temp != root:
            for idx in temp.pattern_indices:
                res[idx] += 1
            temp = temp.fail

"""
bluemooninthedarkmoon
3
moon
blue
dark
"""
if __name__ == '__main__':
    s = input()
    n = int(input())

    # 子串
    patterns = [input() for _ in range(n)]

    # 将下标和内容一起遍历
    for i, pattern in enumerate(patterns):
        insert(pattern, i)

    build_fail()

    res = [0] * n
    search(s, res)

    for r in res:
        print(r)