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
  print("Invalid use !\nPlease try again with Correct Parameters\nFor help run $ python3 get_rating.py -h")
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
