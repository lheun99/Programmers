from collections import Counter


def solution(spell, dic):
    cnt_spell = Counter(spell)

    for word in dic:
        cnt_word = Counter(word)
        if cnt_spell == cnt_word:
            return 1

    return 2
