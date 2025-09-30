def solution(id_pw, db):
    user_id, user_pw = id_pw
    
    for db_id, db_pw in db:
        if db_id == user_id:          # 아이디 일치
            if db_pw == user_pw:      # 비밀번호도 일치
                return "login"
            else:                     # 아이디는 맞는데 비밀번호 틀림
                return "wrong pw"
    
    # 아이디가 아예 없음
    return "fail"
