# design a function which takes in a number as a string, and returns the number in words

# step 1: understand the problem

# step 2: testcases
# input --> 11
# output --> eleven

#input --> 14
#output --> fourteen

#input --> 346
#output --> three hundred fourty six

#input --> 0
#output --> zero

# step 3: make a plan
# make a dict which has 0 - 9
# make a dict which has teens
# make a dict which holds values for tens

# if it's a 2 digit number and starts with 1 --> maps it to teens

# if it's a 2 digit number and doesn't start with 1 --> map it to tens
onesMap = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
teensMap = {
    '1': ' eleven',
    '2': ' twelve',
    '3': ' thirteen',
    '4': ' fourteen',
    '5': ' fifteen',
    '6': ' sixteen',
    '7': ' seventeen',
    '8': ' eighteen',
    '9': ' nineteen'
}
tensMap = {
    '1': 'ten ',
    '2': 'twenty ',
    '3': 'thirty ',
    '4': 'fourty ',
    '5': 'fifty ',
    '6': 'sixty ',
    '7': 'seventy ',
    '8': 'eighty ',
    '9': 'ninety '
}
prefixMap = {
  "1" : "",
  "4" : " thousand ",
  "7" : " million ",
  "10" : " billion ",
  "13" : " trillion ",
  "16" : " quadrillion "
}

# "340"

# 303

# time complexity --> big "O" notation --> "worst case scenario" O(3)
def threeDigitNumToWords(num):
  ans = ""
  if num == "0":
    return "zero"
  onesPosition = len(num) - 1
  tensPosition = len(num) - 2
  for i in range(len(num) - 1, -1, -2 if num[tensPosition] == "1" else -1):
    char = num[i]
    # add a check to see if in the ones column and not zero
    if char != "0" and i == onesPosition:
      # 346, 414
      # add a check to make sure
      if num[tensPosition] == "1":
        ans += teensMap.get(char)
        i -= 1
      else:
        ans += onesMap.get(char)
  
    elif char == "0":
      continue
    else:
      # check if tens column
      if i == tensPosition:
        ans = tensMap.get(char) + ans
      # check if hundreds column
      else:
        ans = onesMap.get(char) + " hundred " + ans
  return ans.strip()

# 345, 678 --> three hundred fourty five six hundred seventy eight
# 897, 345, 678 --> three hundred fourty five six hundred seventy eight

def largeNumToWords(num):
  ans = ""
  # use the helper function to divide the large number into chunks of 3
  # evaluate each chunk with the helper function starting from the first three digits on the right
  for i in range(len(num) - 1, -1, -3):
    ones = num[i]
    tens = num[i-1] if i - 1 >= 0 else ""
    hundreds = num[i-2] if i - 2 >= 0 else ""
    threeDigitNum = hundreds + tens + ones
    diff = len(num) - i
    if threeDigitNum == "000":
      continue
    ans = threeDigitNumToWords(threeDigitNum) + prefixMap.get(str(diff)) + ans
  return ans.strip()

# print(largeNumToWords("345678"))
# print(largeNumToWords("897345678"))
# print(largeNumToWords("45678"))
# print(largeNumToWords('123123123123'))
# print(largeNumToWords('100000000023'))
# print(largeNumToWords('5250100000000023'))


# print(threeDigitNumToWords("44"))
# print(threeDigitNumToWords('123'))
# print(threeDigitNumToWords('719'))
# print(threeDigitNumToWords('109'))
# print(threeDigitNumToWords('1'))
# print(threeDigitNumToWords('0'))
# print(threeDigitNumToWords('12'))
