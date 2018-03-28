# end of chapter question

1. a. 
i. cityin(london, uk).
ii. iVisited(strasbourg).
b. chile, argentina
c. countriesIVisited(Country) :-
	iVisited(City),
	cityIn(City,Country).

2. a. 
i. clause 01
ii. clause 15
b. 
i. Who = jack.
ii. False
iii. False
c.
i. qualifiedDriver(Driver,car).
ii. theoryOnly(X) :-
	passedTheoryTest(X),
	not(passedDrivingTest(X)).
d. Clause 11 (true), clause 01 (instantiates L as 18), clause 05 (instantiates A as 17), clause 15 ( A >= L is false) result is false.