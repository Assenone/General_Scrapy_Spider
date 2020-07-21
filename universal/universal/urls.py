def universal(start, end):
    for page in range(start, end + 1):
        yield 'https://travel.qunar.com/travelbook/list.htm?page=' + str(page) + '&order=hot_heat'