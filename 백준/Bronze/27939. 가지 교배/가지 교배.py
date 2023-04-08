'''P를 1, W를 0이라 한다면, P-우선 교배는 or 연산, W-우선 교배는 and 연산'''
'''결국 조수들이 교배한 결과에서 W-가지가 하나라도 존재하면, 키위 교수가 교배할 때는 무조건 W-가지가 탄생.'''
'''[교배해서 나온 품종을 포함하여 자신이 교배한 적 없는 품종이 하나만 남을 때까지 현재 가지고 있는 교배하지 않은 품종들을 모두 교배한다.]'''
'''이 말인 즉슨, 교배의 결과물은 무조건 한 종류. P-가지 또는 W-가지.'''
'''따라서, 조수들이 W-가지를 하나라도 만들어내면 되고, 그러려면 조수들 중 한 명이라도 W-가지만 가진 사람이 있어야 함.'''

n = int(input())
eggplant = list(input().split())
m, k = map(int, input().split())

result = False

for i in range(m):
    plants = list(map(int, input().split()))
    isW = True
    for k in plants:
        if eggplant[k-1] == 'P':
            isW = False
            break
    if isW:
        result = True

if result:
    print('W')
else:
    print('P')