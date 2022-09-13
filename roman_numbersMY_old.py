'''
Перевод числа, написанного арабскими цифрами в риские.
num - Исходное число
'''

def rom(num: int):
    try:
        isinstance(num, int)
    except:
        print("stop введенное значение не конвертируемо") #Не удалось создать остановку кода при not isinstance(num, int)
    res = list(map(int, str(num)))
    rim = []
    print(f'res = {res}')
    print(f'Это длина res: {len(res)}')
    if len(res) < 2:
        num = Num_first(res[0])
        rim.append(num.dig())
    if 2 <= len(res) < 3:
        num = Num_second(res[1],res[0])
        dig2_sum = num.dig2()
    if 3 <= len(res) and num < 400:          #После введения 3-го разряда, 1-ый стал "вызыван до определения" - решай
        num = Num_second(res[1], res[0])
        dig2_sum = res[0]*'C' + num.dig2()
        print(f'Это третий разряд: {dig2_sum}')
    rim.append(dig2_sum)
    rim.append(num.dig())  #как поставить условие - если num.dig() == None, то не заносить его в rim (обработка 0 в разряде)?
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
#       Число, соответствующее арабскому 10 - 99, второй разряд

    def __init__(self,num_min, num_mid):
        super().__init__(num_mid) 
        self.num_min = num_min
        self.num_mid = num_mid
        print(f'num_mid = {self.num_mid}')
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
    rom(9)
