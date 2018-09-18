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

pc = get_ratings(sys.argv[1] , sys.argv[2] , sys.argv[3])
res = 0.000000000000000000000
for x in pc:
  print("On {0} you have a Rating of {1}".format(x , pc[x]))
  if x == "Codeforces":
    res += 1.18 * float(pc[x])
  else:
    res += float(pc[x])
res = res / 3
print("On Orion Rating you have a Rating of {0:.4f}".format(res))
