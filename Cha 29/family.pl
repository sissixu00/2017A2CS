male(david).
male(sam).
male(jack).
male(simon).
male(tim).
male(ken).

female(tina).
female(cindy).
female(lily).
female(linda).
female(ella).
female(anna).

parent(david,sam).
parent(david,jack).
parent(tina,lily).
parent(simon,cindy).
parent(sam,lily).
parent(linda,ella).
parent(linda,anna).
parent(john,ken).
parent(john,tim).

brother(X,Y):- 
	male(X),
	male(Y),
	parent(A,X),
	parent(A,Y),
	not(X=Y).

siseter(X,Y):- 
	female(X),
	female(Y),
	parent(A,X),
	parent(A,Y),
	not(X=Y).

son(S,P):-
	parent(P,S),
	male(S).

daughter(X,Y):-
	parent(Y,X),
	female(Y).

married(X,Y):-
	parent(X,A),
	parent(Y,A),
	not(X=Y).

ancestor(X,Y):-
	parent(X,Y).

ancestor(X,Y):-
	parent(X,A),
	parent(A,Y).

mother(X,Y):-
	parent(X,Y),
	female(X).