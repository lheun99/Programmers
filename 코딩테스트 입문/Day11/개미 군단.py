def solution(hp):
    general = hp//5
    soldier = (hp-general*5)//3
    worker = (hp-general*5-soldier*3)//1
    return general + soldier + worker


def solution(hp):
    general = hp//5
    soldier = (hp % 5)//3
    worker = ((hp % 5) % 3)//1
    return general + soldier + worker
