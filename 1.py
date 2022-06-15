#void function which does not return anything explicitly and has side effects only

def usd_inr(amount_dollar,conversion_factor):
  inr=amount_dollar*conversion_factor
  print(inr)
  
#non-void function (aka fruitful function) which return the value

def usd_inr(amount_dollar,conversion_factor):
  inr=amount_dollar*conversion_factor
  return inr

'''Alternative solution using lambda function'''

usd_inr=lambda amount_dollar,conversion_factor:amount_dollar*conversion_factor
