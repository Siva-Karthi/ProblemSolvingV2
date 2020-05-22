# todo: replace this with an actual task
from collections import Counter


def print_common_chars(str1, str2):
    if str1 == str2:
        return str1
    else:
        str1_chars_count_map = Counter(str1)
        str2_chars_count_map = Counter(str2)
        res = ""
        for key, val in str1_chars_count_map.items():
            no_of_appearance_in_s2 = str2_chars_count_map.get(key, 0)
            for i in range(min(val, no_of_appearance_in_s2)):
                res += key
        return res