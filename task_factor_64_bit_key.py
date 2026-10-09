import hashlib
import json
import typing
from sympy import isprime

##############################################
# Change this to your 9-digit Georgia Tech ID!
STUDENT_ID = '904316962'
##############################################


def print_tests_for_student_id() -> None:
    f = open('student_tests.json')
    student_tests = json.load(f)

    student_id_hash = hashlib.sha256(STUDENT_ID.encode()).hexdigest()
    try:
        tests = student_tests[student_id_hash]
        print('The tests for ID {} are:'.format(STUDENT_ID))
        print('========================================================')
        for test_id, test in tests.items():
            print('{} -> {}'.format(test_id, test))
        print('========================================================')
    except KeyError:
        print('ERROR: ID {} was not found in student_tests.'.format(STUDENT_ID))
    return tests


# This function is only provided for your convenience.
# You are not required to use it.
def rsa_factor_64_bit_key(N: int, e: int) -> typing.Tuple[int, int]:
    p = 0
    q = 0
    test = N
    #https://www.geeksforgeeks.org/python/python-sympy-isprime-method/
    while (isprime(test)) == False:
        while test % 2 == 0:
            test = test / 2
        while test % 3 == 0:
            test = test / 3
        while test % 5 == 0:
            test = test / 5
        while test % 7 == 0:
            test = test / 7
        while test % 11 == 0:
            test = test / 11
        while test % 13 == 0:
            test = test / 13
        while test % 
    p = test
    q = test / p
    # https://www.calculator.net/prime-factorization-calculator.html
    # TODO: Write the necessary code to get the factors p and q of the public key (N, e)
    print("P: ", p, " Q: ", q)
    return p, q


if __name__ == '__main__':
    tests = print_tests_for_student_id()
    for test_id, test in tests.items():
        rsa_factor_64_bit_key(test['N'], test['e'])
