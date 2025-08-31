def solution(todo_list, finished):
    answer = []
    for task, done in zip(todo_list, finished):
        if not done:
            answer.append(task)
    return answer