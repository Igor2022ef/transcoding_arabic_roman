
# num - Исходное число

def rom(num: int):
    res = list(map(int, str(num)))
    print(res, len(res))
    if len(res) < 2:
        num_1 = Num_first(res[0]).dig()
    else:
        num_1 = ''
    if len(res) >= 2:
        num_2 = Num_second(res[0], res[1]).dig_second()
    else:
        num_2 = ''
    print(f'num = {num_1 + num_2}')


# Число, соответствующее арабскому 0 - 9, первый разряд

class Num_first():
    def __init__(self, num_min):
        self.num_min = num_min
        print(f'Это первое число - {self.num_min}')

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
        if self.num_min > 5:
            nessery_n += 'V' + (self.num_min - 5) * 'I'
            return nessery_n
        if self.num_min == 9:
            nessery_n += "IX"
            return nessery_n


# Число, соответствующее арабскому 11 - 39, второй разряд

class Num_second(Num_first):
    def __init__(self, num_min, num_mid):
        super().__init__(num_min)
        self.num_mid = num_mid
        print(f'Это второе число - {num_mid}')

    def dig_second(self):
        nessery_n = ""
        if 1 <= self.num_mid <= 3:
            nessery_n += self.num_min * 'I'
        if self.num_mid == 4:
            nessery_n += 'IV'
        if self.num_mid == 5:
            nessery_n += 'V'
        if 5 < self.num_mid <= 8:
            nessery_n += 'V' + (self.num_mid - 5) * 'I'
        if self.num_mid == 9:
            nessery_n += "IX"
        return self.dig() + nessery_n  # Что означает self.dig()


#        res[1] = nessery_n
#        print(*res, sep='')


if __name__ == "__main__":
    rom(19)
