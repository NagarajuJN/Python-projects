import time
  
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60) # returns on the only reimder and  quotient of the given number
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Time Completed !!')
  
  
t = input("Plss Enter the time in seconds: ")
  
countdown(int(t))