
from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

#Manhattan distance is basically subtracting the value of rating 2 with rating 1
# and finding the absolute of the value
def manhattandistance(rating1 , rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])
	return distance 



# To Test Manhattan distance run :
# manhattan(users['Hailey'] , users['Veronica'])




#A function to find the closest person to the user X 

def computeNearestNeighbor(username , users):
	"""Creates a sorted list of users based 
	on theyre distance to the username specified"""

	distances = []
	for user in users:
		if user!=username:
			#distance = manhattan(users[user] , users[username])
			distance = minkowski(users[user] , users[username] , 2)
			distances.append((distance , user))

	distances.sort()
	return distances


#Recommendation function to give list of recommendations
def recommend(username , users):
	#Find Nearest neighbor
	nearest = computeNearestNeighbor(username , users)[0][1]
	recommedations = []

	#Finding bands neighbors likes that username doesnt
	neighborRatings = users[nearest]
	userRatings  = users[username]
	for artist in neighborRatings:
		if not artist in userRatings:
			recommedations.append((artist , neighborRatings[artist]))
	return sorted(recommedations , key = lambda artistTuple: artistTuple[1], reverse = True)

#Example of testing Recommend 
#recommend('Angelica' , users)

#Minkowski Distance Function 
'''Higher Dimension distance function'''

def minkowski(rating1,rating2,r):
	distance = 0
	commonRatings = False
	for in key in rating1:
		if key in rating2:
			distance+=pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True
	if commonRatings:
		return pow(distance , 1/r)
	else:
		return 0 #No Ratings in common


#Pearsons correlation coefficient
'''to fix issues when two people give similar
ratings for a band ,however they're thoughts on the 
band are different for each rating.to fix such problems
we use pcc'''

def pearson(rating1 , rating2):
	sum_xy = 0
	sum_x = 0
	sum_y = 0
	sum_x2 = 0
	sum_y2 = 0
	n = 0

	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key]
			y = rating2[key]
			sum_xy += x * y
			sum_x += x
			sum_y += y
			sum_x2 += x**2
			sum_y2 += y**2

	#if no ratings in common return 0
	if n == 0
		return 0

	#computing denominator 

	denominator = sqrt(sum_x2 - (sum_x**2) / n) * sqrt(sum_y2 - (sum_y**2) / n )

	if denominator == 0:
		return 0
	else:
		return (sum_xy - (sum_x * sum_y) /n) /denominator

