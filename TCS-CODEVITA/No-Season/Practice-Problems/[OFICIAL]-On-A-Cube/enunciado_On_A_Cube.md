# CodeVita-problem-On-A-Cube
The sample problem "On A Cube" By tcs CodeVita solved using python. 
Here's the problem and step by step solution.

## Problem Description
A solid cube of 10 cm x 10cm x 10 cm rests on the ground.  It has a beetle on it, and some sweet honey spots at various locations on the surface of the cube.  The beetle starts at a point on the surface of the cube, and goes to the honey spots in order along the surface of the cube.

1. If it goes from a point to another point on the same face (say X to Y), it goes in an arc of a circle that subtends an angle of 60 degrees at the centre of the circle

2. If it goes from one point to another on a different face, it goes by the shortest path on the surface of the cube, except that it never travels along the bottom of the cube

The beetle is a student of Cartesian geometry, and knows the coordinates (x, y, z) of all the points it needs to go to.  The origin of coordinates it uses is one corner of the cube on the ground, and the z axis points up.  Hence, the bottom surface (on which it does not crawl) is z=0, and the top surface is z=10.  The beetle keeps track of all the distances travelled, and rounds the distance travelled to two decimal places once it reaches the next spot, so that the final distance is a sum of the rounded distances from spot to spot.

## Input
The first line gives an integer N, the total number of points (including the starting point) the beetle visits

The second line is a set of 3N comma separated non-negative numbers, with up to two decimal places each.  These are to be interpreted in groups of three as the x, y, z coordinates of the points the beetle needs to visit in the given order.

## Output 
One line with a number giving the total distance travelled by the beetle accurate to two decimal places.  Even if the distance travelled is an integer, the output should have two decimal places.

## Constraints
None of the points the beetle visits is on the bottom face (z=0) or on any of the edges of the cube (the lines where two faces meet)

2<=N<=10

# SOLUTION 

### 1. initialisation 
In the first step. we need to take inputs from the user. Number of points **N** And coordinates separated by comma, 
coordinates are stored as string , we will convert them into a list using the `split(',')` method 

```
N = int(input("enter the number of points"))
coord_string  = input(" enter the coordinates x , y and z respectively: ")
coord_list = coord_string.split(',') #the coordinates are still string, we need to convert them into numbers 
coord_list = [int(e) for e in coord_list]
```
creating a two dimensional list of points for easier access to the points


```
# A TWO DIMENSIONAL LiSt OF POINTS 
points = []
j = 0
for i in range(0 , N):
	points.append([coord_list[j] , coord_list[j+1] ,coord_list[j+2]])
	j += 3
```

> <img src="/cube.png" width="400" style= "border: 1px solid #000" >

now we create a function which takes point as an argument and tells us that on which face the points is lying 

```
#i assumed the cube to be placed as shown in the figure above

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


#function to calculate the distance between two points a and b 
def distance_formula(A , B):
	x1 , y1 , z1 = A
	x2 , y2 , z2 = B
	return ((x2-x1)**2 + (y2-y1)**2+ (z2-z1)**2)**0.5

```
Now we need to check if two consecutive points lies on same face or not.
if they do lie on same face then we will calculate the distance traveled by the beetle moving in an arc of 60°
we know θ = l/r where θ is the angle subtended by the arc and r is the radius of the circle and l is the length of the arc
l = rθ
to calculate r we need to find the distance between these two consecutive points which are lying on the same face.
plug in the values we get 

```
for x , point  in enumerate(points):
	if not (x == N-1):
		if(check_face(point) == check_face(points[x+1])):
			distance += (math.pi*(( (point[0]-points[x+1][0])**2 + (point[1]-points[x+1][1])**2 + (point[2]-points[x+1][2])**2  )**0.5))/3

```

for the points lying on different faces. we need to unfold the cube and calculate the shortest distance between the points 
