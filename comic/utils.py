def paddingLeftStr(strToPad, charToAdd, nums):
  """ To pad the left of the strToPad with charToAdd """
  while len(strToPad) < nums:
    strToPad = charToAdd + strToPad
  return strToPad
