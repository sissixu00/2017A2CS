factorial(0,1).
factorial(N,F):-
	X is N - 1,
	factorial(X,Y)
	F is N*Y.

bunnyEars(0,0).
bunnyEars(N,B):-
	X is N - 1,
	bunnyEars(X,Y),
	B is Y+2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(2,1).
fiboacci(N,F):-
	X is N-1,
	Y is N-2,
	fibonacci(X,A),
	fibonacci(Y,B),
	F is A+B.

bunnyears2(0,0).
bunnyears2(N,B):-
	even(N),
	X is N-1,
	bunnyears2(X,A),
	B is A+3.
bunnyears2(N,B):-
	odd(N),
	X is N-1,
	bunnyears2(X,A),
	B is A+2.

triangle(0,0).
triangle(N,T):-
	X is N-1,
	triangle(X,A),
	T is A+N.

sumdigits(N,S):-
	0 is N//10,
	S is N.
sumdigits(N,S):-
	A is N//10,
	B is mod(N,10),
	sumdigits(A,C),
	S is B+C.

count7(N,C):-
	0 is N//10,
	7 is N,
	C is 1.`g
count7(N,C):-
	0 is N//10,
	  7 is not N,
	  C is 0.
count7(N,C):-
	  0 is not N//10,
	  7 is mod(N,10),
	  A is N//10,
	  count7(A,D),
	  C is 1+D.
count7(N,C):-
	  0 is not N//10,
	  7 is not mod(N,10), 
	  A is N//10,
	  count7(A,D),
	  C is D.
