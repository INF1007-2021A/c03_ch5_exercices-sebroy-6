#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List

def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    List = []
    for letter in prefixes:
        List.append(letter + suffixe)
    return List


def prime_integer_summation() -> int:
    Sum = 3    # Pourquoi est-ce que ma loop considère pas 3 comme un nombre premier?
    is_prime = True
    number = 1
    nb_premiers = 1
    while nb_premiers !=100:
        number += 1
        for i in range(2, number):
            if number % i == 0 :
                is_prime = False
                break
        if is_prime :
            Sum += number
            nb_premiers += 1
            is_prime = False
        else :
            is_prime = True

    return Sum


def factorial(number: int) -> int:
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def use_continue() -> None:
    for number in range(1,11):
        if number == 5:
            continue
        print(number)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    Acceptance_list = []
    is_50years = False
    isMore_70_years = False

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
                    isMore_70_years = True

            if is_50years and isMore_70_years:
                is_accepted = False
                is_50years, isMore_70_years = False, False

        if good_length:
            for member_age in group:
                if member_age == 25:  # condition 4
                    is_accepted = True

        if is_accepted:  # Here is where we add to the Acceptance_list the decision of accepted or not
            Acceptance_list.append(True)
        if is_accepted != True:
            Acceptance_list.append(False)

    return Acceptance_list


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
