def min_one_digit(x,y):
  if (x%10)<(y%10):
    return x
  else:
    return y

'''
Alternative

min_one_digit=lambda x,y:x if (x%10)<(x%10) else y
'''