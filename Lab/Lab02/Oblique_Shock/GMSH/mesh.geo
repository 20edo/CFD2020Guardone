// ============================SUPERSONIC WEDGE MESH
// This is a comment because it begins with double slash

// VARIABLES DEFINITION

dx = 0.03;

//  1D dimension

// POINTS
// The fisrt three entries are coordinates, the fourth is the mesh size
Point(1) = {0, 0, 0, dx};
Point(2) = {0.3, 0, 0, dx};
Point(3) = {2, 0.2, 0, dx};
Point(4) = {2, 1, 0, dx};
Point(5) = {0, 1, 0, dx};

// LINES

Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,5};
Line(5) = {5,1};

// LOOPS

Line Loop(1) = {1,2,3,4,5};

// SURFACE

Plane Surface(1) = {1};

// MESHING
Physical Surface("Volume") = {1};
Physical Line("inlet") = {5};
Physical Line("outlet") = {3};
Physical Line("upper") ={4};
Physical Line("lower") = {1,2};

