import random

lotteries = []

''' 그냥 자동
for i in range(10):
    nums = random.sample(range(1, 46), 6)
    nums.sort()
    lotteries.append(nums)
'''

''' 범위 지정 자동
percentages = {
    '1~10' : 0,
    '11~20' : 0,
    '21~30' : 0,
    '31~40' : 0,
    '41~45' : 0
}

for i in percentages:
    percentages[i] = int(input('{}대 갯수: '.format(i)))

for i in percentages.items():
    print('{}: {}%'.format(i[0], round(i[1] / 6 * 100,1)))


nums = []
for i in percentages.items():
    zone = i[0].split('~')
    nums.append(random.sample(range(int(zone[0]), int(zone[1]) + 1), i[1]))

for i in nums:
    for j in i:
        print(j, end=' ')
'''

#자동 + 수동
nums = []
wantedNums = input('원하는 숫자들: ').split()
wantedLength = len(wantedNums)

for i in wantedNums:
    nums.append(int(i))

restNums = [i for i in range(1, 46) if not i in wantedNums]
#print(restNums)

nums.extend(random.sample(restNums, 6 - wantedLength))
nums.sort()
print(nums)
    

    
