def fibonacci(n):
  if n in {0,1}:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
  if n == 0: return 2
  elif n == 1: return 1
  else:
      return lucas(n-1)+lucas(n-2)

def  sum_series(n,param1, param2):
  if param1 == 0 and param2 == 1: 
    return fibonacci(n)
  elif param1 == 2 and param2 == 1 :
    return lucas(n)
  else:
    if n == 0: return param1
    elif n == 1: return param2
    else:
      return sum_series(n-1,param1,param2)+sum_series(n-2,param1,param2)