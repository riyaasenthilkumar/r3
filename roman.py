ROMAN=[(100,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C")]
def int_to_roman(number):
  result=" "
  for(arbic,roman)in ROMAN:
    (factor,number)=divmod(number,arabic)
      result+=roman*factor
    return result
