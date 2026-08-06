def solution(record):
    nickname = {}
    logs = []

    for line in record:
        parts = line.split(' ')
        action = parts[0]
        if action == 'Enter':
            uid, nick = parts[1], parts[2]
            nickname[uid] = nick
            logs.append(('Enter', uid))
        elif action == 'Leave':
            uid = parts[1]
            logs.append(('Leave', uid))
        else:  # Change
            uid, nick = parts[1], parts[2]
            nickname[uid] = nick

    result = []
    for action, uid in logs:
        if action == 'Enter':
            result.append(f"{nickname[uid]}님이 들어왔습니다.")
        else:
            result.append(f"{nickname[uid]}님이 나갔습니다.")

    return result