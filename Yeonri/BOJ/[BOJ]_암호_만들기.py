# 입력받은 문자를 모두 정렬
# -> ord로 변경을 한 후, 숫자를 비교해보기
# 두개중 하나?

# 암호를 전부 선택하였을 때, vowels를 체크
# (len(password) - vowels_count) = consonant_count -> 자음은 2개 이상

def is_valid(password):
    vowels = set('aeiou')
    # 파이써---------닉
    vowel_count = sum(1 for char in password if char in vowels)
    consonant_count = len(password) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

def dfs(count, password):
    # 문자열의 길이가 입력 받은 조건일 때, 조건 만족을 확인
    if len(password) == L:
        if is_valid(password):
            print(''.join(password))
        return

    # 만약 카운트가 C까지 왔을 때,
    # 충분한 문자를 선택하지 못한경우로 종료
    if count == C:
        return

    # 현재 문자 선택
    dfs(count + 1, password + [sorted_lst[count]])
    # 현재 문자 선택하지 않음
    dfs(count + 1, password)

L, C = map(int, input().split())
lst = input().split()
sorted_lst = sorted(lst)  # 알파벳 정렬

dfs(0, [])