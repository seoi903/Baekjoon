def sol(nums):
    n = len(nums)
    current_defend = 0
    for i in range(n):
        defend =  100 - (100-current_defend)*(100-nums[i])/100
        print(defend)
        current_defend = defend
 
if __name__ == '__main__':
    len_nums = int(input())
    nums = list(map(int, input().split()))
    sol(nums)