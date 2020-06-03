import greeting
from unittest import TestCase


class TestGreeting(TestCase):
    # 正常系(1) - 複数パラメータを一括テストする (not good)
    def test_greeting_1(self):
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
            # アサーションルーレットと呼ばれるアンチパターン
            # https://scrapbox.io/furuk4wa/%E3%82%A2%E3%82%B5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AB%E3%83%BC%E3%83%AC%E3%83%83%E3%83%88
            self.assertEqual(grt, greeting.greeting(hour))

    # 正常系(2) - 複数パラメータを一括テストする (good case)
    def test_greeting_2(self):
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