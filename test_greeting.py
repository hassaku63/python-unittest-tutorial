import greeting
from unittest import TestCase


class TestGreeting(TestCase):
    # 正常系(1) - シンプルな正常系のテスト
    def test_greeting_1(self):
        hour = 10
        expect = 'おはよう'
        self.assertEqual(expect, greeting.greeting(hour))

    # 正常系(2) - 想定する入力値すべてをチェックする (bad case)
    def test_greeting_2(self):
        test_data = [
            (0, 'こんばんは'),
            (2, 'こんばんは'),
            (3, 'こんばんは'),
            (4, 'こんばんは'),
            (5, 'おはよう'),
            (6, 'おはよう'),
            (7, 'おはよう'),
            (8, 'おはよう'),
            (9, 'おはよう'),
            (10, 'おはよう'),
            (11, 'おはよう'),
            (12, 'こんにちは'),
            (13, 'こんにちは'),
            (14, 'こんにちは'),
            (15, 'こんにちは'),
            (16, 'こんにちは'),
            (17, 'こんにちは'),
            (18, 'こんばんは'),
            (19, 'こんばんは'),
            (20, 'こんばんは'),
            (21, 'こんばんは'),
            (22, 'こんばんは'),
            (23, 'こんばんは'),
        ]
        for hour, grt in test_data:
            self.assertEqual(
                grt,
                greeting.greeting(hour))
