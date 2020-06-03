def greeting(hour: int):
    """整数の時間を受け取り、その時間に応じて「挨拶」を返す
    5時以降12時未満 => おはよう
    12時以降18時未満 => こんにちは
    18時以降、5時未満 => こんばんは
    :param hour: 0 - 23 までの時間
    :type hour: int
    """
    if 0 <= hour < 5:
        return 'こんばんは'
    elif 5 <= hour < 12:
        return 'おはよう'
    elif 12 <= hour < 18:
        return 'こんにちは'
    elif 18 <= hour < 24:
        return 'こんばんは'