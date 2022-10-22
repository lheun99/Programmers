def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']

    answer = my_string
    for al in my_string:
        if al in vowel:
            answer = answer.replace(al, "")
    return answer
