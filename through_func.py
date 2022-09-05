'''
Перекодировка из арабских цифр в римские. Реализовано до 89. При этом есть три блока кода, практически эдентичные
как их выделить и обращатся к ним по условию, сократив код придумать не могу. Попытка реализовать через классы в другом
файле.
Одинаковые блоки выделены в коде двумя строками.

'''


def rom(num):
   res = list(map(int, str(num)))
   if len(res) < 2:

      num_min = res[0]
      nessery_n = ""
      if 1 <= num_min <= 3:
         nessery_n += num_min * 'I'
      if num_min == 4:
         nessery_n += 'IV'
      if num_min == 5:
         nessery_n += 'V'
      if 5 < num_min <= 8:
         nessery_n += 'V' + (num_min - 5) * 'I'
      if num_min == 9:
         nessery_n += "IX"
      print(nessery_n)

   if len(res) == 2:
      if res[0] < 4:
         res[0] = "X" * res[0]
         num_min = res[1]
         nessery_n = ""
         if num_min == 0:
            nessery_n == 'X'


         if 1 <= num_min <= 3:
            nessery_n += num_min * 'I'
         if num_min == 4:
            nessery_n += 'IV'
         if num_min == 5:
            nessery_n += 'V'
         if 5 < num_min <= 8:
            nessery_n += 'V' + (num_min - 5) * 'I'
         if num_min == 9:
            nessery_n += 'IX'
         res[1] = nessery_n

         print(*res, sep='')
      if res[0] == 4:
         res[0] = "XL"

         num_min = res[1]
         nessery_n = ""
         if 1 <= num_min <= 3:
            nessery_n += num_min * 'I'
         if num_min == 4:
            nessery_n += 'IV'
         if num_min == 5:
            nessery_n += 'V'
         if 5 < num_min <= 8:
            nessery_n += 'V' + (num_min - 5) * 'I'
         if num_min == 9:
            nessery_n += "IX"
         res[1] = nessery_n
         print(*res, sep='')

      while res[0] >= 5 and res[0] <= 8:
         res[0] = 'L' + 'X' * (res[0] - 5)

         num_min = res[1]
         nessery_n = ""
         if 1 <= num_min <= 3:
            nessery_n += num_min * 'I'
         if num_min == 4:
            nessery_n += 'IV'
         if num_min == 5:
            nessery_n += 'V'
         if 5 < num_min <= 8:
            nessery_n += 'V' + (num_min - 5) * 'I'
         if num_min == 9:
            nessery_n += "IX"
         res[1] = nessery_n
         print(*res, sep='')


#                res[0] += 1

rom(89)
