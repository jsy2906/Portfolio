import random as r

for i in range(10):
    lotto_numbers = r.sample(range(1, 51), 7)
    # random.sample( (튜플, 문자열, range, 리스트 등), 뽑을 인자의 개수 ) : 랜덤하게 뽑은 인자들을 리스트로 만들어서 반환
    lotto_numbers.sort()
    print(lotto_numbers)
