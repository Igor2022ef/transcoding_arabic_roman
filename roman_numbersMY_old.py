'''
Перевод числа, написанного арабскими цифрами в риские.
num - Исходное число
Пока реализовано до 399, далее конфликт
'''

def rom(num: int):
    if not isinstance(num, int) is True or num == 0:
        raise SystemExit('Это значение не конвертируемо') #Верно ли сделал остановку при ошибке?
    if num >= 1000:
        raise SystemExit('M - и все на этом')                       #Последнее число, не знаю, как верно оформить этот шаг
    res = list(map(int, str(num)))
    rim = []
    print(f'res = {res}')
    print(f'Это длина res: {len(res)}')
    if len(res) < 2:
        num = Num_first(res[0])
    if 2 <= len(res) < 3:
        num = Num_second(res[1],res[0])
        dig2_sum = num.dig2()
        print(f'Это dig2_sum для Num_second: {dig2_sum}')
        rim.append(dig2_sum)
    if 3 <= len(res) < 4:
        print(f'Это res[2] для Num_second от 3 до 4: {res[2]}')
        num = Num_second(res[2], res[1])
        print(f'Это dig2 для Num_second от 3 до 4: {num.dig2()}')
        print(f'Это num.dig() для Num_second от 3 до 4: {num.dig()}')
        if res[0] < 4:
            first_n = res[0] * 'C'
        if 4 <= res[0] < 5:
            first_n = 'CD'
        if 5 <= res[0] < 6:
            first_n = 'D'
        if 6 <= res[0] < 9:
            first_n = ('D' + 'C'*(res[0] - 5))
        if 9 <= res[0]:
            first_n = 'CM'
        if num.dig() != None:
            dig2_sum = first_n + num.dig2() + num.dig()
        dig2_sum = first_n + num.dig2()
        print(f'Это третий разряд: {dig2_sum}')
        rim.append(dig2_sum)
    if num.dig() != None:
        rim.append(num.dig())
        print(rim)
    print(f'Это результат со всеми разрядами: {"".join(rim)}')

class Num_first():
#    Число, соответствующее арабскому 0 - 9, первый разряд

    def __init__(self,num_min):
        self.num_min = num_min      
        print(f'Это num_min из Num_first = {self.num_min}')
    def dig(self):    
        nessery_n = ''
        if 1 <= self.num_min <= 3:
            nessery_n += self.num_min*'I'
            return nessery_n 
        if self.num_min == 4:
            nessery_n = 'IV'
            return nessery_n 
        if self.num_min == 5:
            nessery_n += 'V'
            return nessery_n     
        if 5 < self.num_min <= 8:
            nessery_n += 'V'+(self.num_min - 5)*'I'
            return nessery_n     
        if self.num_min == 9:
            nessery_n += "IX"
            return nessery_n

class Num_second(Num_first):
#       Число, соответствующее арабскому 10 - 999, старшие разряды

    def __init__(self,num_min, num_mid):
        super().__init__(num_mid) 
        self.num_min = num_min
        self.num_mid = num_mid
        print(f'num_mid из Num_second = {self.num_mid}')
        print(f'Это min из Num_second т.е num_min = {self.num_min}')
    def dig2(self):
        if self.num_mid < 4:
            nessery_m = "X" * self.num_mid
            return nessery_m
        if self.num_mid == 4:
            nessery_m = "XL"
            return nessery_m
        if 5 <= self.num_mid <= 8:
            nessery_m = ('L' + 'X'*(self.num_mid - 5))
            return nessery_m
        if self.num_mid == 9:
            nessery_m = "XC"
            return nessery_m

if __name__ == "__main__":
    rom('111111')
