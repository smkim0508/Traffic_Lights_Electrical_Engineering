# ans = 1

# def test():
#     global ans
#     ans += 1
#     res = ans
    
#     return res
    

# while(True):
#     p = test()
#     print(p)


# res = test()
# print(res)
# print(res[1])

# t = 1
# f = 0

# # while not f: print("false")

# while f or t: print("either true")

import time 
import asyncio

# prepare_for_foo()
# task = loop.create_task(foo())
# remaining_work_not_depends_on_foo()
# loop.run_until_complete(task)

async def timer():
    print("2")
    # await asyncio.sleep(5)
    time.sleep(5)
    print("4")

async def timer2():
    print("5")
    # await asyncio.sleep(2)
    time.sleep(2)
    print("6")

async def timer3():
    loop = asyncio.get_event_loop()
    loop.create_task(timer())
    loop.create_task(timer2())
    # asyncio.create_task(timer())
    # asyncio.create_task(timer2())
    # asyncio.get_running_loop()
   
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.create_task(timer())
    # # loop.create_task(timer2())
    # loop.run_forever()


print("1")
# time = loop.create_task(timer())
# asyncio.run(timer())
# asyncio.run(timer2())
asyncio.run(timer3())
print("3")