# ----------------------------------------------------------------------
# Name:      homework6
# Purpose:   illustrate the use of unit testing Python
# Author(s): Hrishikesh Joshi and Paul Chon
# Date: 18 March 2023
# ----------------------------------------------------------------------

"""
This file creates two methods: final_grades amd most_words

The final
"""

def final_grade(student_grades, extra_credit=1):
    '''

    :param student_grades: a dictionary of students and their respective
    grades
    :param extra_credit: the amount of credit by which each student's
    grade will be boosted
    :return:
    '''
    return {key:value+extra_credit for key, value in
            student_grades.items()}
def most_words(*strings):
    """
    Finds the string with the most words

    :param strings: arbitrary number of strings
    :return: the string with the most words
    """
    if not strings:
        return None
    return max(strings, key=lambda x: len(x.split()))