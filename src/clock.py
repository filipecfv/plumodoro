from time import sleep 

def clock(time):
    for i in range(0, time): 
        for n in range(0, 60):
            print(">>>", i, ":", n, end = "\r")
            sleep(1)
