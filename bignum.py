

def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*2, reverse=True)
    print(numbers)
    return answer


solution([6, 10, 2])
