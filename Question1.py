time=float(input("Enter time (min):"))
if time >52.36:
  print("Overflow")
elif time == 52.36:
    print("Full")
else:
    print("UnderFlow")

    #another

vol = time*15
if vol>785:
      a=vol-785
      print("Overflow Water",a)
elif vol==785:
      print("full")
else:
      fh=vol/(3.14*5**2)
      rh=10-fh
      print("Water UnderFlow",vol)
      print("Filled Height:",round(fh,2))
      print("Reamaining Height:",round(rh,2))