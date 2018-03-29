task 3.1

character(habib).
charcater_type(habib,explorer).
has_skill(habib,timetravel).
pet(habib,fish).

task 3.2

onlyPet(C,P) :-
	character(C),
	animal(P).

task 3.3

character(a).
character(b).
animal(cat).
animal(dog).
pet(a,cat).
pet(b,dog).
has_skill(a,walk).
has_skill(b,run).

task 3.4

X = princess.
X = jim.
X = invisibility.
X = jim.

task 3.5

pet(jim,X).

has_skill(X,fly).

skill(X).

type_pet(T,P) :-
	character_type(C,T),
	pet(C,P).
type_pet(princess,X).