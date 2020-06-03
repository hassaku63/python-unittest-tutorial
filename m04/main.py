# unittest.mock
#  https://docs.python.org/ja/3.7/library/unittest.mock.html

from datetime import datetime
from m04 import sub


def main():
    """外部機能を呼び出すユースケース的な関数
    """
    # 単純に文字列を初期化するだけの処理ですが、
    # 実際には表示の元になる文字列をなにがしかの手段（外部API叩いたり）で取得したりしている、と想定してください
    text = 'hello'

    sub.notify(text=text)


if __name__ == '__main__':
    main()