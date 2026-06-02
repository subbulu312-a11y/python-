nums=[1,2,3]
it=iter(nums)
print(hasattr(nums,'__iter__'))
print(hasattr(nums,'__next__'))
print(hasattr(it,'__iter__'))
print(hasattr(it,'__next__'))
