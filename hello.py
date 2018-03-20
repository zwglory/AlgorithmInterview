# -*- coding:utf-8 -*-


def test_encode():
    """
    这里主要为了测试 python3 的编码
    :return:
    """
    a = "这是一个中文的句子"
    print("[a] %s [type] %s" % (a, type(a)))
    b = a.encode("utf-8")
    print("[b] %s [type] %s" % (b, type(b)))


if __name__ == '__main__':
    test_encode()

