// STRUCTURED MESH OF LAMINAR FLAT PLATE

h = 0.01;
m = 0.2;
m2 = 0.8;

// POINTS

Point (1) = {-0.06, 	0, 	0, 	h};
Point (2) = {0, 	0, 	0, 	h};
Point (3) = {0.3084, 	0, 	0, 	h};
Point (4) = {0.3084, 	0.03, 	0, 	h};
Point (5) = {0, 	0.03, 	0, 	h};
Point (6) = {-0.06,	0.03, 	0, 	h};

// LINES 

Line (1) = {1, 2};
Line (2) = {2, 3};
Line (3) = {3, 4};
Line (4) = {4, 5};
Line (5) = {5, 6};
Line (6) = {6, 1};
Line (7) = {5, 2};	// Usefull for block-structured mesh. It splits the two blocks

// LINE LOOPS

// Line	Loop (1) = {1, 2, 3, 4, 5, 6};
Line	Loop (1) = {1,-7, 5, 6};
Line	Loop (2) = {2, 3, 4, 7};

// SURFACE

Plane 	Surface (1) = {1};
Plane	Surface (2) = {2};

// TRANSFINITE (structured meshing)
Transfinite 	Line{1}	= 153*m	Using Progression 0.984966;
Transfinite 	Line{5}	= 153*m	Using Progression 1/0.984966;
Transfinite 	Line{6}	= 110*m2	Using Progression 0.95;
Transfinite 	Line{7}	= 110*m2	Using Progression 0.95;

Transfinite	Line{3}	= 110*m2	Using Progression 1/0.95;
Transfinite	Line{2} = 789*m	Using Progression 1.00293;
Transfinite	Line{4} = 789*m	Using Progression 1/1.00293;

Transfinite 	Surface{1}	= {1,2,5,6};
Transfinite	Surface{2};
Recombine 	Surface{1,2};

//MESH

Physical 	Surface	("VOLUME")	= {1,2};
Physical	Line	("inlet")	= {6};
Physical	Line	("wall")	= {2};
Physical 	Line	("symmetry") 	= {1};
Physical 	Line	("outlet") 	= {3, 4, 5};
