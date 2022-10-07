# Вычислить число c заданной точностью d

from decimal import Decimal


def round_number(number, d):
    number_round = Decimal(number)
    return number_round.quantize(Decimal(d))


print(round_number(input("Enter a real number: "),
      input("Enter the required accuracy: ")))
