
from itertools import permutations

def isMagicSquare(t):
    # Magic number for 3X3 matrix is 15
    magic_num = 15
    if sum(t[0:3]) != magic_num or sum(t[3:6]) != magic_num or sum(t[6:9]) != magic_num:
        return False
    if t[0]+t[3]+t[6] != magic_num or t[1]+t[4]+t[7] != magic_num or t[2]+t[5]+t[8] != magic_num:
        return False
    if t[0]+t[4]+t[8] != magic_num or t[2]+t[4]+t[6] != magic_num:
        return False
    return True


def findCost(t1, t2):
    cost = 0
    for a, b in zip(t1, t2):
        cost += abs(a - b)
    return cost


def minimumCost(nums):
    tpl = tuple()
    for r in range(3):
        for c in range(3):
            tpl += (nums[r][c],)
    min_cost = float('inf')
    for t in permutations(range(10), 9):
        if isMagicSquare(t):
            cost = findCost(t, tpl)
            print(f'\tMagic_Square, cost = {t}, {cost}')
            min_cost = min(min_cost, cost)
    print(f'Min_cost = {min_cost}')
    return min_cost



minimumCost([[1,2,3],[4,5,6],[7,8,9]])


minimumCost([[9,8,7],[6,5,4],[3,2,1]])


minimumCost([[5,3,4],[1,5,8],[6,4,2]])


minimumCost([[4,9,2],[3,5,7],[8,1,5]])


minimumCost([[4,8,2],[4,5,7],[6,1,6]])


# ===============================================================


ranked = [100,100,50,40,40,20,10]

player = [5,25,50,120]


def findPosition(ranked, p):
    left, right = 0, len(ranked)-1
    while left <= right:
        mid = (left + right) // 2
        if ranked[mid] == p:
            return mid
        elif ranked[mid] > p:
            left = mid + 1
        else:
            right = mid - 1
    return left




def climbingLeaderboard(ranked, player):
    # Write your code here
    def findPosition(ranked, p):
        left, right = 0, len(ranked)-1
        while left <= right:
            mid = (left + right) // 2
            if ranked[mid] == p:
                return mid
            elif ranked[mid] > p:
                left = mid + 1
            else:
                right = mid - 1
        return left
    hsh = dict()
    rank = 1
    hsh[0] = rank
    N = len(ranked)
    for i in range(1, N):
        if ranked[i] != ranked[i-1]:
            rank += 1
        hsh[i] = rank
    res = list()
    for p in player:
        ind = findPosition(ranked, p)
        if ind >= N:
            res.append(hsh[N-1]+1)
        else:
            res.append(hsh[ind])
    return res



climbingLeaderboard(ranked, player)


# =====================================================================

def nonDivisibleSubset(k, s):
        # Create an array to store the remainder count for each number
        remainder_count = [0] * k
        for num in s:
            remainder_count[num % k] += 1

        # Initialize the size of the non-divisible subset
        subset_size = 0

        # If there is a remainder of 0, we can only include one number
        if remainder_count[0] > 0:
            subset_size += 1

        # If k is even, we can only include one number with a remainder of k/2
        if k % 2 == 0 and remainder_count[k//2] > 0:
            subset_size += 1

        # Iterate through the remainder counts and add the larger count for each pair of remainders
        for i in range(1, (k+1)//2):
            subset_size += max(remainder_count[i], remainder_count[k-i])

        return subset_size



