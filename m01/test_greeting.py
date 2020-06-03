import greeting
from unittest import TestCase


class TestGreeting(TestCase):
    # 正常系(1) - シンプルな正常系のテスト
    def test_greeting_1(self):
        hour = 10
        expect = 'おはよう'
        self.assertEqual(expect, greeting.greeting(hour))