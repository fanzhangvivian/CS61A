class Dog:
    d_type = "jingba"
    sss = "sss"

    def __init__(self, name, age) -> None:
        print('hahhah', name, age)
        self.name2 = name
        self.age2 = age
    def say_hi(self):
        print("hello, i am a dog, my type is ",self.d_type, self.name2)


d = Dog("mjj",3)
d2 = Dog("maodan",2)

import heapq

heap = []

heapq.heappush(heap, (5,2,3))
heapq.heappush(heap, (4,3,4))
heapq.heappush(heap, (6,1,1))



print(heap)
heapq.heappop(heap)
print(heap)





