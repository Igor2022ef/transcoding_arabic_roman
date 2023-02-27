'''
Перевод числа, написанного арабскими цифрами в риские.
num - Исходное число
'''

def rom(num: int):
    assert isinstance(num, int), 'Это значение не конвертируемо'
    res = list(map(int, str(num)))
    rim = []
    match len(res):
        case 1:
            num = Num_first(res[0])
        case 2:
            num = Num_second(res[1], res[0])
            dig2_sum = num.dig2()
            rim.append(dig2_sum)
        case 3:
            num = Num_second(res[2], res[1])
            if res[0] < 4:
                first_n = res[0] * 'C'
            elif 4 <= res[0] < 5:
                first_n = 'CD'
            elif 5 <= res[0] < 6:
                first_n = 'D'
            elif 6 <= res[0] < 9:
                first_n = ('D' + 'C' * (res[0] - 5))
            elif 9 <= res[0]:
                first_n = 'CM'
            if num.dig() != None:
                dig2_sum = first_n + num.dig2() + num.dig()
            dig2_sum = first_n + num.dig2()
            rim.append(dig2_sum)
        case _:
            raise ValueError('M - и все на этом')
    if num.dig() != None:
        rim.append(num.dig())
    print(f'Это результат со всеми разрядами: {"".join(rim)}')

class Num_first():
    #    Число, соответствующее арабскому 0 - 9, первый разряд

    def __init__(self, num_min):
        self.num_min = num_min

    def dig(self):
        nessery_n = ''
        if 1 <= self.num_min <= 3:
            nessery_n += self.num_min * 'I'
            return nessery_n
        if self.num_min == 4:
            nessery_n = 'IV'
            return nessery_n
        if self.num_min == 5:
            nessery_n += 'V'
            return nessery_n
        if 5 < self.num_min <= 8:
            nessery_n += 'V' + (self.num_min - 5) * 'I'
            return nessery_n
        if self.num_min == 9:
            nessery_n += "IX"
            return nessery_n

class Num_second(Num_first):
    #       Число, соответствующее арабскому 10 - 999, старшие разряды

    def __init__(self, num_min, num_mid):
        super().__init__(num_mid)
        self.num_min = num_min
        self.num_mid = num_mid

    def dig2(self):
        if self.num_mid < 4:
            nessery_m = "X" * self.num_mid
            return nessery_m
        if self.num_mid == 4:
            nessery_m = "XL"
            return nessery_m
        if 5 <= self.num_mid <= 8:
            nessery_m = ('L' + 'X' * (self.num_mid - 5))
            return nessery_m
        if self.num_mid == 9:
            nessery_m = "XC"
            return nessery_m

if __name__ == "__main__":
    rom(999)
