// STRUCTURED MESH OF LAMINAR FLAT PLATE

h = 0.01;

// POINTS

Point (1) = {-0.06, 0, 0, h};
Point (2) = {0, 0, 0, h};
Point (3) = {0.3084, 0, 0, h};
Point (4) = {0.3084, 0.03, 0, h};
Point (5) = {0, 0.03, 0, h};
Point (6) = {-0.06 ,0.03, 0, h};

// LINES 

Line (1) = {1, 2};
Line (2) = {2, 3};
Line (3) = {3, 4};
Line (4) = {4, 5};
Line (5) = {5, 6};
Line (6) = {6, 1};
Line (7) = {5, 2};	// Usefull for block-structured mesh. It splits the two blocks

// LINE LOOPS

// Line Loop (1) = {1, 2, 3, 4, 5, 6};
Line Loop (1) = {1,-7,5,6};

// SURFACE

Plane Surface (1) = {1};

// TRANSFINITE (structured meshing)
Transfinite Line{1} 	= 30 	Using Progression 0.8;
Transfinite Line{5}	= 30	Using Progression 1/0.8;
Transfinite Line{6}	= 110 	Using Progression 0.6;
Transfinite Line{7}	= 110	Using Progression 0.6;


Transfinite Surface{1}	= {1,2,5,6};
Recombine Surface{1};

//MESH

Physical Surface ("VOLUME") = {1};
// Physical Line ("inlet") = {6};
// Physical Line ("wall") = {2};
// Physical Line ("simmetry") = {1};
// Physical Line ("outlet") = {3, 4, 5};
