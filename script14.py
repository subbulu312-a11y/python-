from idlelib.browser import browseable_extension_blocklist


class student:
    school='python academy'
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1
aslice=student('alice',age=20)
bob=student('bob',19)
print(aslice.name)
print(bob.name)
print(student.count)
print(aslice.school)
