"""Exact rational threshold check only, not a graph theorem verifier."""
from fractions import Fraction as Q
import json

t = 629137
n = 6*t+1
A = Q(99105232761143253014623713, 870045109056532003460)
D = Q(408188186312417039449377, 87004510905653200346)
B = Q(165935746784616540459756, 217511277264133000865)
assert t >= 5*37**2
assert 13*n > 49072639
assert n > 48*(1+B)
assert n > 2*(10*A+D)+3
lower = 1-24*(1+B)/n
upper = (10*A+D)/(n-3)
assert lower > Q(1,2) > upper
print(json.dumps(dict(status='PASS',t=t,n=n,
    lower_expectation=str(lower),upper_expectation=str(upper),
    bad_mass_threshold=str(48*(1+B)),
    finite_error_threshold=str(2*(10*A+D)+3))))
