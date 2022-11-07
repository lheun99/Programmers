def solution(id_pw, db):
    for user in db:
        if id_pw == user:
            return "login"
        elif id_pw[0] == user[0] and id_pw[1] != user[1]:
            return "wrong pw"
    return "fail"
