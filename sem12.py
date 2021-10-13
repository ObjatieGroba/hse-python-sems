class F:
    def __init__(self):
        pass


def f(s):  # вернуть все символы на нечетных позициях
    return s[1::2]


def f(s):  # вернуть все символы на нечетных позициях без среза
    res = ""
    for i in range(len(s)):
        if i % 2 == 1:
            res += s[i]
    return res


def f(s):  # вернуть все символы на нечетных позициях
    # return str(s[i] for i in range(1, len(s), 2))
    return ''.join(s[i] for i in range(1, len(s), 2))


# Чет - f(n + 1)
# кратно 3 - n // 3
# иначе f(n + 2)

def f(n):
    if n not in memo:
        if n % 2 == 0:
            memo[n] = f(n + 1)
        if n % 3 == 0:
            memo[n] = n // 3
        memo[n] = f(n + 2)
    return memo[n]


memo = {}


# Сделать нижний регистр s.lower()
def cmp(f_str, s_str) -> bool:  # case insensitive cmp
    #     if len(f_str) == len(s_str):

    return f_str.lower() == s_str.lower()


import typing as tp


def cmp(f: tp.Set[str], s: tp.Set[str]) -> bool:
    f = set(map(lambda x: x.lower(), f))
    s = {x.lower() for x in s}  # set
    # s = set(x.lower() for x in s)  # set
    # s = {x.lower(): 1 for x in s} # dict

    return f == s


class Storage:
    def __init__(self):
        self.dates = dict()  # date -> value
        self.shops = dict()  # shop -> value
        self.date_shops = dict()  # (shop, date) -> value
        self.cu_value = 0

    def add(self, date, value, shop_name):
        if date not in self.dates:
            self.dates[date] = 0
        self.dates[date] += value
        # for others ...

    def cummulative_value(self):
        return self.cu_value

    def cummulative_value_filtered(self, date=None, shop_name=None):
        if date is None and shop_name is None:
            return self.cu_value
        if date is None:
            return self.shops[shop_name]
        if shop_name is None:
            return self.dates[date]
        return self.date_shops[(shop_name, date)]

