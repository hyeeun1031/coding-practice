def solution(spell, dic):
    spell_set = set(spell)
    
    for word in dic:
        if set(word) == spell_set and len(word) == len(spell):
            return 1
    return 2
