import sys
import codechef_rating_extractor as cc
import codeforces_rating as cf
import hackerrank_rating as hr

def get_ratings(usernamehr , usernamecc , usernamecf):
  ratings = {'HackerRank' : '' , "Codechef" : "" , "Codeforces" : ""}
  ratings['HackerRank'] = hr.get_rating(usernamehr)
  ratings['Codechef'] = cc.get_rating(usernamecc)
  ratings['Codeforces'] = cf.get_rating(usernamecf)
#  print(ratings)
  return ratings

#uncomment the next line for debugging on local pc
#pc = get_ratings('abhiy13' , 'abhiy13' , 'abhiroxx')

#comment this wile debugging on local pc
if(len(sys.argv) == 2):
  if(sys.argv[1] == "-h"):
    print("Help In Progress!")
    exit()

if(len(sys.argv) != 4):
  ratings = {'-cc' : 'Codechef' , '-hr' : 'Hackerrank' , '-cf' : 'Codeforces'}
  output = []
  for i in range(len(sys.argv)):
    if sys.argv[i] == "-cc" and i + 1 < len(sys.argv):
      output.append([ratings['-cc'] , cc.get_rating(sys.argv[i + 1])])
    elif sys.argv[i] == "-cf" and i + 1 < len(sys.argv):
      output.append([ratings['-cf'] , cf.get_rating(sys.argv[i + 1])])
    elif sys.argv[i] == "-hr" and i + 1 < len(sys.argv):
      output.append([ratings['-hr'] , hr.get_rating(sys.argv[i + 1])])
  if len(output) == 0:
    print("Invalid Arguments!")
  else:
    for i in output:
      print('Your {0} Rating is {1}'.format(i[0] , i[1]))
  exit()

pc = get_ratings(sys.argv[1] , sys.argv[2] , sys.argv[3])
res = 0.000000000000000000000

for x in pc:
  print("On {0} you have a Rating of {1}".format(x , pc[x]))
  if x == "Codeforces":
    res += 1.18 * float(pc[x])
  else:
    res += float(pc[x])
res = res / 3
print("Your Orion Rating will be {0:.7f}".format(res))
