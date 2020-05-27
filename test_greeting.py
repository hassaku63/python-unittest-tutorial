import greeting
from unittest import TestCase


class TestGreeting(TestCase):
    # 正常系(1) - シンプルな正常系のテスト
    def test_greeting_1(self):
        hour = 10
        expect = 'おはよう'
        self.assertEqual(expect, greeting.greeting(hour))

    # 正常系(2) - 複数パラメータを一括テストする (good case)
    def test_greeting_3(self):
        # 境界条件（入力する値によって異なる挙動の仕様を持つ関数）として最小限と思われる入力のみ使用する
        test_data = [
            (0, 'こんばんは'),
            (4, 'こんばんは'),
            (5, 'おはよう'),
            (11, 'おはよう'),
            (12, 'こんにちは'),
            (17, 'こんにちは'),
            (18, 'こんばんは'),
            (23, 'こんばんは'),
        ]
        for hour, grt in test_data:
            # subTest よりも簡単で便利な仕組みとして pytests.parametrize などがある
            #  参考: https://docs.pytest.org/en/latest/parametrize.html
            with self.subTest(msg='subTest による Parameterize Test', hour=hour, grt=grt):
                self.assertEqual(grt, greeting.greeting(hour))