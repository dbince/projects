### practice question
# create a function that takes in a string of brackets, and returns whether or not there are matching brackets
# input = "([{[]}])"
# output = True

# input =  "([{[}])"
# output = False

# input =  "([{[]}])["
# output = False

# step 1: understand the problem ✅
# step 2: testcases ✅
# step 3: plan ✅
"""
make a string, and see if the right most one matches up with the left most one
bracket = str[i]
output += bracket
right most bracket --> "], ), }"
if there isn't a right most bracket that matches the left most bracket, false

stacks --> list
last in, first out
stack = []
for loop
    bracket = str[i]
    # add on to the stack if it's a opening bracket
    if # add condition
        stack.append(bracket)
    # if closing bracket
    check if closing matches top of the stack
    if some condition
        remove that element from the top
    if not matching
        return false
return !stack.length
"""

bracketDict = {
  "[": "]",
  "{": "}",
  "(": ")"
}

def isValidBrackets(brackets):
  stack = []
  for i in range(len(brackets)):
    bracket = brackets[i]
    if bracketDict.get(bracket) is not None:
      stack.append(bracket)
    else:
      # opening bracket
      mostRecentBracket = stack.pop()
      if bracketDict[mostRecentBracket] is not bracket:
        return False
  # if (len(stack)):
  #   return True
  # else:
  #   return False
  return len(stack) != 0