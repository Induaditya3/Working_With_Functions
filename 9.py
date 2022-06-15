def terms(first,last):
  common_difference=(last-first)/3
  term=first
  for i in range(4):
    print(term)
    term+=common_difference

