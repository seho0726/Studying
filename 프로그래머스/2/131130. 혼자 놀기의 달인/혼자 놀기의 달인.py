def solution(cards):
    open_cards = [0] * len(cards)
    group = []
    
    x = 0
    for i in range(len(cards)) :
        if open_cards[i] == 1 :
            continue
        
        count = 0
        x = i
        while open_cards[x] == 0:
            open_cards[x] = 1
            x = cards[x] - 1
            count += 1
            
        group.append(count)
            
    group.sort(reverse=True)
    
    if len(group) == 1:
        answer = 0
    else:
        answer = group[0] * group[1]
        

    return answer