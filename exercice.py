#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List

def convert_to_absolute(number: float) -> float:
    return number if number > 0 else number * -1  # Connaitre cette syntaxe pour l'examen (peut-être demandé)


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    List = []

    for letter in prefixes:
        List.append(letter + suffixe)

    return List


def prime_integer_summation() -> int:
    sum = 0
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
              59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
              137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
              211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
              283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
              379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
              461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

    for number in primes:
        sum += number
    return sum


def factorial(number: int) -> int:
    result = 1

    for i in range(2, number + 1):
        result *= i

    return result


def use_continue() -> None:
    for number in range(1, 11):
        if number == 5:
            continue
        print(number)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance_list = []
    is_50years = False
    is_more_70years = False

    for group in groups:
        is_accepted = True  # reset bool values for the next group in the first dimension list
        good_length = True

        if len(group) > 10 or len(group) <= 3: # condition 1
            is_accepted = False
            good_length = False

        if good_length:
            for member_age in group:
                if member_age < 18:  # condition 2
                    is_accepted = False
                    break

                elif member_age == 50:  # condition 3
                    is_50years = True
                elif member_age > 70:
                    is_more_70years = True

            if is_50years and is_more_70years:
                is_accepted = False
                is_50years, is_more_70years = False, False

        if good_length:
            for member_age in group:
                if member_age == 25:  # condition 4
                    is_accepted = True

        if is_accepted:  # Here is where we add to the Acceptance_list the decision of accepted or not
            acceptance_list.append(True)
        if is_accepted != True:
            acceptance_list.append(False)

    return acceptance_list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
