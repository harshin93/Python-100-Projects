'''
Distance Between Two Cities - Calculates the distance between two cities.
This program may require finding coordinates for the cities like latitude and longitude.
'''

import math


def solution(c_1, c_2):
    '''
    asfycgcfuih
    '''
    ans = math.sqrt((c_2[0] - c_1[0]) **2 + (c_2[1] - c_1[1]) ** 2)
    return ans


def test_solution():
    '''
    sdjifgsdufg
    '''
    c_1 = (0, 0)
    c_2 = (6, 0)
    ans = 6
    assert solution(c_1, c_2) == ans

if __name__ == "__main__":
    test_solution()
