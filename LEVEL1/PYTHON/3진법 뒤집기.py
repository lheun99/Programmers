def solution(n):
    num = ""
    while n > 0:
        num += str(n % 3)
        n = n//3

    return int(num, 3)



temp = [1, 2, 3]

#temp += 4

print(temp)

#[1, 2, 3, 4]

temp_2 = "123"
temp_2 += "4"
print(temp_2)