#!python

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    uniq_scores = list(set(scores))
    uniq_scores.sort()
    if len(uniq_scores) == 1:
        print()
    else:
        print(uniq_scores[-2])

