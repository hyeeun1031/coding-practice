def solution(box, n):
    width = box[0]  # 가로 길이
    depth = box[1]  # 세로 길이
    height = box[2] # 높이 길이
    
    num_fit_width = width // n
    num_fit_depth = depth // n
    num_fit_height = height // n
    
    total_cubes = num_fit_width * num_fit_depth * num_fit_height
    
    return total_cubes