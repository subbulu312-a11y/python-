nums=[1,2,3]
__iter=iter(nums)
while True:
    try:
        x=next(__iter)
        print(x)
    except StopIteration:
        break

