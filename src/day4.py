#!/usr/bin/env /usr/bin/python36


def check_pw_rules(pw):
    """
    Check the two rules for the given password
    :param pw:
    :return: True, if both rules are fulfilled
    """
    equal_flag = False
    greater_flag = True
    for index in range(0, len(pw) - 1):
        # if the next char is smaller, we're done, rule #4 is broken
        if pw[index + 1] < pw[index]:
            return False
        # only as long as we haven't found any doubles, let's see if this is a double
        # If it is a double, set the flag and never check again
        if not equal_flag and pw[index] == pw[index + 1]:
            equal_flag = True
    return equal_flag

def doit_day4a(pw_min, pw_max):
    """
    return the number of correct passwords from the given range
    :param pw_min:
    :param pw_max:
    :return:
    """

    count =0
    for pw in range(pw_min, pw_max):
        if check_pw_rules(str(pw)):
            count += 1

    return count


def main():

    pw_smallest = 264793
    pw_largest = 803935

    different_passwords = doit_day4a(pw_smallest, pw_largest)

    print("Different passwords: {}".format(different_passwords))


if __name__ == "__main__":
    main()
