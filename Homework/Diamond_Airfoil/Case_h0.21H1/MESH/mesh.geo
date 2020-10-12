// ================== Mesh of a diamond airfoil

c = 1;		// Chord of the profile
R = 100*c;	// Radius of the far-field boundary
th = 5;	// Angle of the airfoil in degrees
h = 0.21; 
H = 1; 

//
D=0.2; 	// Height of the airfoil

//================= POINTS
// farfield
Point(1) = {	R,	0,	0,	H};
Point(2) = {	0,	R,	0,	H};
Point(3) = {	-R,     0,	0,      H};
Point(4) = {    0,      -R,    0,      H};
//airfoil
Point(5) = {	0,	0,	0,	h};
Point(6) = {	c/2,	D/2,	0,	h};
Point(7) = { 	c,	0,	0,	h};
Point(8) = {	c/2,	-D/2,	0,	h};

//================== LINES
//farfield
Circle(1) = {1,5,2};
Circle(2) = {2,5,3};
Circle(3) = {3,5,4};
Circle(4) = {4,5,1};

//airfoil
Line(5) = {5,6};
Line(6) = {6,7};
Line(7) = {7,8};
Line(8) = {8,5};
//================= LOOPS
//farfield
Line Loop(1) = {1,2,3,4};
//airfoil
Line Loop(2) = {5,6,7,8};

//================= SURFACES
Plane Surface(1) ={1,2};

//================ MESH
Physical Surface("Volume")	= {1};
Physical Line("FARFIELD") 	= {1,2,3,4};
Physical Line("AIRFOIL") 	= {5,6,7,8};

