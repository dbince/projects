"""
given an array of time intervals where intervals[i] = [start, end], determine if a person can attend all their meetings

input: [[0, 30], [5, 10], [15, 20]]
output: false

input: [[7, 10], [2, 4]]
output: true
"""

def canAttendMeetings(intervals):
  intervals.sort(key=lambda val: val[1])
  
  for i in range(len(intervals)-1):
    if intervals[i][1] > intervals[i+1][0]:
      return False
  return True

print("SHOULD BE FALSE")
print(canAttendMeetings([[0,9],[5,10],[15,20]]))
print(canAttendMeetings([[1,3], [4,6], [3,4], [7,8], [3,6]]))
print(canAttendMeetings([[2, 4], [10, 12], [9, 11]]))


print("SHOULD BE TRUE")
print(canAttendMeetings([[7,10],[2,4]]))
print(canAttendMeetings([[1,3], [4,6], [3,4], [7,8], [6,7]]))
print(canAttendMeetings([[2, 4], [10, 12], [9, 10]]))