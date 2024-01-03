# solving the activity selection problem , which is a problem of finding the maximum number of activities that can be performed by a person according to time range/ free time

# index 0 - activity name
# index 1 - start time
# index 2 - end time
activities = [
  ["A1",0,6],
  ["A2",3,4],
  ["A3",1,2],
  ["A4",5,8],
  ["A5",5,7],
  ["A6",8,9]
]

def printMaxActivities(activities): #------> O(nlogn)
  activities.sort(key=lambda x: x[2]) # picks out the end time and sorts them
  i = 0
  firstActivity = activities[i][0]
  print(firstActivity)
  for j in range(len(activities)):
    if activities[j][1] > activities[i][2]:
      print(activities[j][0])
      i = j


printMaxActivities(activities)