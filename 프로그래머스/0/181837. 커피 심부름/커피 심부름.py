def solution(order):
    total = 0
    for menu in order:
        if "americano" in menu or menu == "anything":
            total += 4500
        elif "cafelatte" in menu:
            total += 5000
    return total
