# 입력된 숫자 중 3개 더해서 소수 찾기
def solution(nums):
    answer = 0

    for i in range(0, len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for x in range(j+1,len(nums)):
                result = nums[i] + nums[j] + nums[x]
                count = True
                for a in range(2, result):
                    if result % a == 0:
                        count = False
                        break
                if count == True:
                    answer += 1


    return answer

solution([1,2,3,4,5])

# count = lambda a : False if result % a == 0 in range(2, result)
