def linear_search(lists, search):
    for list in lists:
        if list == search:
            return True
    return False


grades = [85,6,8,78,98,96];

result = 789 in grades

print(result)