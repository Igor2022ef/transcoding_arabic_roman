#Генератор чисел Фибоначи
def gen_f(a,b):
    ans = []
    c = 0
    while c < 11:
        b, a = a, a+b #Как же это работает?
        c = c + 1
        ans.append(a) #Как убрать первую единицу в списке?
    return (ans)

def gen_f_1(a_1,b_1):
    ans_1 = []
    s = 0
    while s < 11:
        c_1 = a_1 + b_1
        ans_1.append(c_1)
        a_1 = b_1
        b_1 = c_1
        s = s + 1
    return (ans_1)




if __name__ == "__main__":
    print(gen_f(0,1))
    print(gen_f_1(0, 1))