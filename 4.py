from random import randrange

def random_generator(x,y):
  return randrange(x,y+1)
  
def main():
  a=float(input("Enter upper limit:"))
  b=float(input("Enter lower limit:"))
  for i in range(3):
    print(random_generator(b,a))

if __name__=='__main__':
  main()