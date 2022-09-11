'''
Перевод числа, написанного арабскими цифрами в риские.
num - Исходное число
'''

def rom(num: int):
    res = list(map(int, str(num)))
    rim = []
    print(f'res = {res}')
    print(f'Это длина res: {len(res)}')
    if len(res) < 2:
        num = Num_first(res[0])
        rim.append(num.dig())
    elif len(res) >= 2 or len(res) <= 3:
        num = Num_second(res[1],res[0])     #не понимаю, почему прядое res[1],res[0] важен
        rim.append(num.dig2())
        rim.append(num.dig())
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
        #if self.num_min == 0:
            #dig() == 0

        if self.num_mid < 4:
            nessery_m = "X" * self.num_mid
            return nessery_m
        if self.num_mid == 4:
            nessery_m = "XL"
            return nessery_m
        if self.num_mid == 5:
            nessery_m = "L"
            return nessery_m
        if self.num_mid == 6:
            nessery_m = "LX"
            return nessery_m
        if self.num_mid == 7:
            nessery_m = "LXX"
            return nessery_m
            #print(*res, sep='')
        if self.num_mid == 8:
            nessery_m = "LXXX"
            return nessery_m
        if self.num_mid == 9:
            nessery_m = "XC"
            return nessery_m

#Видимо надо сразу разворачивать число в список и рассылать уже проанализированные
#числа

'''

def rom(num):
    if num < 10:
        print(num)
        dig = Num_first(num)
    if num > 10:
        print(num)
        dig1 = Num_sekond(num)
           
            while res[0] >= 5 and res[0] <= 8:
                
                res[0] = 'L'+'X'*(res[0] - 5)
                num_min = res[1]
                nessery_n = ""
                if num_min <= 3 and num_min >= 1:
                    nessery_n += num_min*'I'    
                if num_min == 4:
                    nessery_n += 'IV'
                if num_min == 5:
                    nessery_n += 'V'    
                if num_min > 5 and num_min <= 8:
                    nessery_n += 'V'+(num_min - 5)*'I'    
                if num_min == 9:
                    nessery_n += "IX"
                res[1] = nessery_n
                print(*res, sep='')
                res[0] += 1

'''

rom(16)

#print(nessery_n)
#dig = Num_first(6)