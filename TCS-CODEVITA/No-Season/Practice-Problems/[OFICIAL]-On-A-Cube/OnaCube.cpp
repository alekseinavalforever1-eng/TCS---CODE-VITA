// On a Cube
// A solid cube of 10 cm x 10cm x 10 cm rests on the ground. It has a beetle on it, and some sweet honey spots at various locations on the surface of the cube. The beetle starts at a point on the surface of the cube and goes to the honey spots in order along the surface of the cube.

//     If it goes from a point to another point on the same face (say X to Y), it goes in an arc of a circle that subtends an angle of 60 degrees at the center of the circle
//     If it goes from one point to another on a different face, it goes by the shortest path on the surface of the cube, except that it never travels along the bottom of the cube

// The beetle is a student of cartesian geometry and knows the coordinates (x, y, z) of all the points it needs to go to. The origin of coordinates it uses is one corner of the cube on the ground, and the z-axis points up.Hence, the bottom surface (on which it does not crawl) is z=0, and the top surface is z=10.The beetle keeps track of all the distances traveled, and rounds the distance traveled to two decimal places once it reaches the next spot so that the final distance is a sum of the rounded distances from spot to spot.

// Input Format:

//     The first line gives an integer N, the total number of points (including the starting point) the beetle visits
//     The second line is a set of 3N comma separated non-negative numbers, with up to two decimal places each. These are to be interpreted in groups of three as the x, y, z coordinates of the points the beetle needs to visit in the given order.

// Output Format:

//      One line with a number giving the total distance traveled by the beetle accurate to two decimal places. Even if the distance traveled is an integer, the output should have two decimal places

// Constraints:

//     None of the points the beetle visits is on the bottom face (z=0) or on any of the edges of the cube (the lines where two faces meet)

//     2<=N<=10

// Sample Input 1:
// 3
// 1, 1, 10, 2, 1, 10, 0, 5, 9
// Sample Output 1:
// 6.05
// Sample Input 2:
// 3
// 1, 1, 10, 2, 1, 10, 0, 1, 9
// Sample Output 2:
// 4.05

#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct Point3D {
  double x;
  double y;
  double z;
  Point3D() : x(0), y(0), z(0) {}
  Point3D(double x_val, double y_val, double z_val)
      : x(x_val), y(y_val), z(z_val) {}
};
bool is_same_face(Point3D a, Point3D b) {
  return (a.x == b.x and (a.y == b.y or a.z == b.z)) or
         (a.y == b.y and a.z == b.z);
}

double find_distance(Point3D a, Point3D b) {
  double t = pow(a.x - b.x, 2) + pow(a.y - b.y, 2) + pow(a.z - b.z, 2);
  double result = sqrt(t);
  return result;
}

double find_straight_distance(Point3D a, Point3D b) {
  double x_distance = abs(a.x - b.x);
  double y_distance = abs(a.y - b.y);
  double z_distance = abs(a.z - b.z);
  double tot = x_distance + y_distance + z_distance;
  if (a.x == b.x || a.y == b.y) {
    return round(tot * 100) / 100.0;
  } else {
    return round((tot - 2) * 100) / 100.0;
  }
}

double find_same_face_area(double r) {
  double arc_length = 1.0472 * r;
  return arc_length;
}

int main() {
  int n;
  cin >> n;
  vector<Point3D> points(n);
  for (int i = 0; i < n; i++) {
    int x, y, z;
    cin >> x >> y >> z;
    points[i].x = x;
    points[i].y = y;
    points[i].z = z;
  }
  double total_distance = 0;
  for (int i = 0; i < n - 1; i++) {
    bool is_same = is_same_face(points[i], points[i + 1]);
    double dist = find_distance(points[i], points[i + 1]);
    double dist1 = find_straight_distance(points[i], points[i + 1]);
    if (is_same) {
      total_distance += find_same_face_area(dist);
    } else {
      total_distance += dist1;
    }
  }
  cout << fixed << setprecision(2) << total_distance << endl;
  return 0;
}
