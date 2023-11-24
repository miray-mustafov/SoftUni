odeven=input()


def sum_odd_even(odeven, nums):
    parity = 0 if odeven == "Even" else 1
    nums=[int(x) for x in nums.split()]
    sum=0

    for num in nums:
        if num%2==parity:
            sum+=num
    return sum*len(nums)

print(sum_odd_even(odeven,input()))