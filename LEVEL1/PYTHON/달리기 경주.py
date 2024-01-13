def solution(players, callings):
    rank = {}
    for i, player in enumerate(players):
        rank[i] = player
        #{rank : name}

    name = {}
    for i, player in enumerate(players):
        name[player] = i
        #{name : rank}

    for call in callings:
        # call: 불린 선수 name
        c_rank = name[call]  # 불린 선수 rank
        c_f_rank = c_rank - 1  # 앞 선수 rank
        c_f_name = rank[c_f_rank]  # 앞 선수 name

        rank[c_rank] = c_f_name
        rank[c_f_rank] = call

        name[call] = c_f_rank
        name[c_f_name] = c_rank

    return list(rank.values())


print(solution(["mumu", "soe", "poe", "kai", "mine"],
      ["kai", "kai", "mine", "mine"]))
