
'''
таблица находится по адресу https://matematika-club.ru/roman-numerals
1	I
4	IV
5	V
6	VI
7	VII
9	IX
10	X
20 XX
30 XXX
В этом промежутке изменяеются правые знаки числа
40	XL
В этом промежутке изменяеются правые знаки числа
50	L
60 LX
70 LXX
80 LXXX
В этом промежутке изменяеются правые знаки числа
90	XC
100	C
В этом промежутке комбинации нижестоящих знаков
400	CD
500	D
600	DC
700	DCC
800 DCCC
900	CM
1000	M
До 4000 идут комбинации нижестоящих знаков

'''
def check_list(fun):
    def wrapper(num_start):
        for i in range(num_start, 3000, 1):
            num=i
            res1=fun(num)
            print(fun(num))
            num_r=res1
            print(digit1(num_r))
    return wrapper





# @check_list
def rom(num):
    res=list(map(int, str(num)))[::-1]
    a=['C','D','I','L','M','V','X']
    num1 = Num_first(res,a)


    # Передача данных и вызоы внутри кода
    print(f"Это digit1(num_r): {digit1(num1.count())}")
    return num1.count()


class Num_first():
    def __init__(self, res1, a1):
        self.res1 = res1
        self.a1 = a1

    def count(self):
        ness4 = ness3 = ness2 = ness1 = ''
        if self.res1[0] == 9:
            ness1 = self.a1[2] + self.a1[6]  # IX
        elif 5 <= self.res1[0] <= 8:
            ness1 = self.a1[5] + (self.res1[0]-5) * self.a1[2]
        elif self.res1[0] == 4:
            ness1 = self.a1[2] + self.a1[5]
        elif 1 <= self.res1[0] <= 3:
            ness1 = self.res1[0] * self.a1[2]

        if len(self.res1)>1:
            if self.res1[1]==9:
                ness2=self.a1[6] + self.a1[0]
            elif 5<=self.res1[1]<=8:
                ness2=self.a1[3]+(self.res1[1]-5)*self.a1[6]
            elif self.res1[1]==4:
                ness2=self.a1[6] + self.a1[3]
            elif 1<=self.res1[1]<=3:
                ness2=self.res1[1]*self.a1[6]

        if len(self.res1)>2:
            if self.res1[2] == 9:
                ness3 = self.a1[0] + self.a1[4]
            elif 5 <= self.res1[2]<= 8:
                ness3 = self.a1[1] + (self.res1[2]-5) * self.a1[0]
            elif self.res1[2] == 4:
                ness3 = self.a1[0] + self.a1[1]
            elif 1 <= self.res1[2] <= 3:
                ness3 = self.res1[2] * self.a1[0]
        if len(self.res1)>3:
            ness4 = self.res1[3]*self.a1[4]

        if len(self.res1)==1:
            return ness1
        elif len(self.res1)==2:
            return (ness2+ness1)
        elif len(self.res1)==3:
            return (ness3+ness2+ness1)
        else:
            return (ness4+ness3+ness2+ness1)





'''
Вариант покороче, вряд ли заработает
'''
def rom1(num_s):
    res=list(map(int, str(num_s)))[::-1]
    if 0 < len(res) <= 1:
        num1 = Num_first1(res[0], 2)
        return num1.count()
    if 1<len(res)<=2:
        num1 = Num_first1(res[0], 2)
        num2 = Num_first1(res[1], 6)
        return (num2.count()+num1.count())
    if 2<len(res)<=3:
        num1 = Num_first1(res[0], 2)
        num2 = Num_first1(res[1], 7)
        num3 = Num_first1(res[2], 0)
        return (num3.count()+num2.count()+num1.count())

class Num_first1():
    a = ['C', 'D', 'I', 'L', 'M', 'V', 'X', 'C', 'D', 'I', 'L', 'M', 'V','X']
    def __init__(self, res1, i1):
        self.res1 = res1
        self.i1 = i1
    def count(self):
        ness1=''                                                                #ВОПРОС: Почему после введения этой строки, начинает
                                                                                #обрабатывать нули в исходном числе корректно
        if self.res1 == 9:
            ness1 = self.a[self.i1] + self.a[self.i1+4]  # IX
        elif 5 <= self.res1 <= 8:
            ness1 = self.a[self.i1+3] + (self.res1-5) * self.a[self.i1]
        elif self.res1 == 4:
            ness1 = self.a[self.i1] + self.a[self.i1+3]
        elif 1 <= self.res1 <= 3:
            ness1 = self.res1 * self.a[self.i1]
        return ness1
        #
        # if len(self.res1)>3:
        #     ness4 = self.res1[3]*self.a1[4]


'''
Из римских в арабские
'''
def digit1(num_r):
    ness_b = ness_mid = ness_m = ness_mic = 0
    i = 0
    if num_r[i]=='M':
        while i<=(len(num_r)-1) and num_r[i]=='M':
            i+=1
        # i=i
        ness_b=1000*(i)
    # i+=1

    if i<=(len(num_r)-1) and num_r[i]=='C' and num_r[i+1]=='M': #Здесь при числе С не хватает разряда и код клинит - реши
        ness_mid=900
        i+=2
    elif i<=(len(num_r)-1) and num_r[i]=='D':
        i+=1
        ness_mid=500
        j=i
        while i<=(len(num_r)-1) and num_r[j]=='C':
            j+=1
        ness_mid=ness_mid+((j-i)*100)
        i=j
    elif i<=(len(num_r)-1) and num_r[i]=='C' and num_r[i+1]=='D':#Здесь при числе с окончанием на C не хватает разряда и код клинит - реши
        i+=2
        ness_mid=400
    elif i<=(len(num_r)-1) and num_r[i] == 'C' and num_r[i + 1] != 'D': #Здесь при числе с окончанием на C не хватает разряда и код клинит - реши
        j = i
        while j<=(len(num_r)-1) and num_r[j] == 'C':
            j += 1
        ness_mid = (j-i) * 100
        i=j
    if i == (len(num_r) - 1) and num_r[i] == 'C':
        ness_mid = 100
    if i<(len(num_r)-1) and num_r[i]=='X' and num_r[i+1]=='C':  #Здесь при числе C (100) не хватает разряда и код клинит - реши
        ness_m=90
        i+=2
    elif i<=(len(num_r)-1) and num_r[i]=='L':
        i+=1
        ness_m=50
        j = i
        while j<=(len(num_r)-1) and num_r[j] == 'X':
            j += 1
        ness_m = ness_m + ((j-i) * 10)
        i=j
    elif i<=(len(num_r)-1) and num_r[i] == 'X' and num_r[i + 1] == 'L':
        ness_m=40
        i+=2
    elif i<=(len(num_r)-1) and num_r[i] == 'X'and num_r[i + 1] != 'L':
        j = i
        while j<=(len(num_r)-1) and num_r[j] == 'X':
            j += 1
        ness_m =(j-i)*10
        i=j
    # if i<=(len(num_r)-1) and num_r[i] == 'I' and num_r[i + 1] == 'X':     #Здесь при числе I не хватает разряда и код клинит - реши
    if i == (len(num_r) - 1) and num_r[i] == 'I':
        ness_mic=1
    elif i<=(len(num_r)-1) and num_r[i] == 'I' and num_r[i + 1] == 'X':
        ness_mic=9
    elif i<=(len(num_r)-1) and num_r[i] == 'V':
        i+=1
        ness_mic = 5
        j = i
        while j<=(len(num_r)-1) and num_r[j] == 'I':
            j += 1
        ness_mic = ness_mic + (j-i)
        i=j
    elif i<=(len(num_r)-1) and num_r[i] == 'I' and num_r[i + 1] != 'X':     #Здесь при числе I не хватает разряда и код клинит - реши
        j = i
        while j<=(len(num_r)-1) and num_r[j] == 'I':
            j += 1
        ness_mic = (j-i)
    return (ness_b+ness_mid+ness_m+ness_mic)



if __name__ == '__main__':

    trans1=21
    # print(f"Исходное число: {trans1}")
    print(f"Из арабского в римский: {rom(trans1)}")  # should return 'M'
    # print(f"Из римского в арабский: {digit1(rom(trans1))}")
    # digit1(rom(trans1))
    check_list(rom)(trans1)



