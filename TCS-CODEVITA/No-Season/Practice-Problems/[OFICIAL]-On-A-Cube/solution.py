import math

#TAKING INPUTS FROM THE USER
N = int(input("Enter the number of points  : "))
coord_string  = input(" enter the coordinates x , y and z respectively: ")

#CREATING A COMBINED LIST OF ALL COORDINATES 

coord_list = coord_string.split(',')
coord_list = [int(e) for e in coord_list] # TYPECASTING FROM STRING TO INTEGER



# A TWO DIMENSIONAL LiSt OF POINTS 
points = []
j = 0
for i in range(0 , N):
	points.append([coord_list[j] , coord_list[j+1] ,coord_list[j+2]])
	j += 3


#function which checks 
#on which face a point lies 

def check_face(point):
	x , y , z = point 
	if z == 10:
		return "top"
	elif z == 0:
		return "bottom"
	elif x == 10:
		return "right"
	elif x == 0:
		return "left"
	elif y == 10:
		return "back"
	elif y == 0:
		return "front"
		
#It calculates the distance between two points a and b 
def distance_formula(A , B):
	x1 , y1 , z1 = A
	x2 , y2 , z2 = B
	return ((x2-x1)**2 + (y2-y1)**2+ (z2-z1)**2)**0.5


# function which calculates the shortest distance 
#between two points lying on top and side faces

def topToSide(top , side):
	x1 , y1 , z1 = top
	x2 , y2 , z2 = side
	if check_face(side) == "front":
		y2 = y2 - 10 + z2
		z2 = z1
	elif check_face(side) == "back":
		y2 = y2 + 10 - z2
		z2 = z1
	elif check_face(side) == "right":
		x2 = x2 +10- z2
		z2 = z1
	elif check_face(side) =="left":
		x2 = x2 -10+ z2
		z2 = z1
	return distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
	
#function which calculates shortest distance between two points lying on sides 

def sideToSide(side1 , side2):
	if((check_face(side1) == "front" and check_face(side2) == "right" )or (check_face(side1) == "right" and check_face(side2) == "front" )):
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		x2 = x2+ y2
		y2 = y1
		return distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		
	elif((check_face(side1) == "front" and check_face(side2) == "left" )or (check_face(side1) == "left" and check_face(side2) == "front" )):
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		x2 = x2- y2
		y2 = y1
		return distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		
	elif((check_face(side1) == "back" and check_face(side2) == "right" )or (check_face(side1) == "right" and check_face(side2) == "back" )):
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		x2 = x2+ 10-y2
		y2 = y1
		return distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		
	elif((check_face(side1) == "back" and check_face(side2) == "left" )or (check_face(side1) == "right" and check_face(side2) == "left" )):
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		x2 = x2- 10+y2
		y2 = y1
		return distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		
	elif((check_face(side1) == "front" and check_face(side2) == "back" )or (check_face(side1) == "back" and check_face(side2) == "front" )):
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		y2 = x2-10
		y1 = 20-x1
		x2 = 10
		x1 = 10
		dist1 = distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		y2 = -x2
		y1 = 10+x1
		x2 = 10
		x1 = 10
		dist2 = distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		return min(dist1 , dist2)

	elif((check_face(side1) == "left" and check_face(side2) == "right" )or (check_face(side1) == "right" and check_face(side2) == "left" )):
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		x2 = x2+y2
		x1 = x1-y1
		y1 = 0
		y2 = 0
		dist1 = distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		
		x1 , y1 , z1 = side1
		x2 , y2 , z2 = side2
		x2 = x2+10-y2
		x1 = x1+10-y1
		y1 = 0
		y2 = 0
		dist2 = distance_formula([x1 , y1 , z1] , [x2 , y2 , z2])
		return min(dist1 , dist2)
				
# LOGIC FOR CALCULATING THE DISTANCE 
distance  = 0
for x , point  in enumerate(points):
	if not (x == N-1):
		if(check_face(point) == check_face(points[x+1])):
			distance += (math.pi*(( (point[0]-points[x+1][0])**2 + (point[1]-points[x+1][1])**2 + (point[2]-points[x+1][2])**2  )**0.5))/3
		#print(check_face(point) , check_face(points[x+1]))
		
		elif(check_face(point)=="top" and not check_face(points[x+1]) == "top" ):
			distance += topToSide(point , points[x+1])
		elif(check_face(point)== "bottom"):
			continue
		else:
			distance += sideToSide(point , points[x+1])

print(round(distance , 2))  