def solution(data, ext, val_ext, sort_by):
    # 항목 이름을 인덱스로 매핑
    col_idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    ext_idx = col_idx[ext]
    sort_idx = col_idx[sort_by]
    
    # 조건에 맞는 데이터만 필터링
    filtered = [row for row in data if row[ext_idx] < val_ext]
    
    # 정렬
    filtered.sort(key=lambda x: x[sort_idx])
    
    return filtered
