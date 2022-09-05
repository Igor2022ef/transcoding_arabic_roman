'''
Исходный код перекодировшика из арабских цифр в римские. Реализовани до 89
Работает с оговоркой
'''


def rom(num):
    if num < 10:
        num_min = num
        nessery_n = ""

        if 1 <= num_min <= 3:
            nessery_n += num_min*'I'    
        if num_min == 4:
            nessery_n += 'IV'
        if num_min == 5:
            nessery_n += 'V'    
        if 5 < num_min <= 8:
            nessery_n += 'V'+(num_min - 5)*'I'
        if num_min == 9:
            nessery_n += "IX"
        print(nessery_n)

    if num >= 10:
        res = list(map(int, str(num)))
        d = len(res)
        if d == 2:
            if res[0] < 4:
                res[0] = "X"*res[0]

                num_min = res[1]
                nessery_n = ""
                if num_min == 0:
                    nessery_n == 'X'
                if 1 <= num_min <= 3:
                    nessery_n += num_min*'I'    
                if num_min == 4:
                    nessery_n += 'IV'
                if num_min == 5:
                    nessery_n += 'V'    
                if 5 < num_min <= 8:
                    nessery_n += 'V'+(num_min - 5)*'I'    
                if num_min == 9:
                    nessery_n += 'IX'
                res[1] = nessery_n

                print(*res, sep='')
            if res[0] == 4:
                res[0] = "XL"

                num_min = res[1]
                nessery_n = ""
                if 1 <= num_min <= 3:
                    nessery_n += num_min*'I'    
                if num_min == 4:
                    nessery_n += 'IV'
                if num_min == 5:
                    nessery_n += 'V'    
                if 5 < num_min <= 8:
                    nessery_n += 'V'+(num_min - 5)*'I'    
                if num_min == 9:
                    nessery_n += "IX"
                res[1] = nessery_n
                print(*res, sep='')
            
            while res[0] >= 5 and res[0] <= 8:
                res[0] = 'L'+'X'*(res[0] - 5)

                num_min = res[1]
                nessery_n = ""
                if 1 <= num_min <= 3:
                    nessery_n += num_min*'I'    
                if num_min == 4:
                    nessery_n += 'IV'
                if num_min == 5:
                    nessery_n += 'V'    
                if 5 < num_min <= 8:
                    nessery_n += 'V'+(num_min - 5)*'I'    
                if num_min == 9:
                    nessery_n += "IX"
                res[1] = nessery_n
                print(*res, sep='')
#                res[0] += 1

rom(31)