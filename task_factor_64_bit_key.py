import hashlib
import json
import typing


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


# This function is only provided for your convenience.
# You are not required to use it.
def rsa_factor_64_bit_key(N: int, e: int) -> typing.Tuple[int, int]:
    p = 0
    q = 0
    test = N
    while (test.is_prime) == False:
        while test % 2 == 0:
            test = test / 2
        while test % 3 == 0:
            test = test / 3
        while test % 5 == 0:
            test = test / 5

    p = test
    q = test / p
    # https://www.calculator.net/prime-factorization-calculator.html
    # TODO: Write the necessary code to get the factors p and q of the public key (N, e)

    return p, q


if __name__ == '__main__':
    print_tests_for_student_id()
