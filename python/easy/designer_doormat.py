#!python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())

# Top part
start, end = 0, (N-1)//2
for i in range(start, end):
    triangle_pattern = '.|.' * (2*i + 1)
    filler_count = (M - len(triangle_pattern))//2
    filler_line = '-' * filler_count
    print('%s%s%s' % (filler_line, triangle_pattern, filler_line))

# Welcome line
welcome_str = 'WELCOME'
filler_count = (M - len(welcome_str))//2
filler_line = '-' * filler_count
print('%s%s%s' % (filler_line, welcome_str, filler_line))

# Bottom part
start, end = (N-1)//2 - 1, -1
for i in range(start, end, -1):
    triangle_pattern = '.|.' * (2*i + 1)
    filler_count = (M - len(triangle_pattern))//2
    filler_line = '-' * filler_count
    print('%s%s%s' % (filler_line, triangle_pattern, filler_line))

