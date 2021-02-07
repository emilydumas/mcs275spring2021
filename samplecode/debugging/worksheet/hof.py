"""Compute and display terms in an integer sequence"""

computed_terms = [1,1]

def reducer(y,aux):
    aux = max(int(aux),int(1/aux))
    if y % 3 == 0:
        return (y + computed_terms[-1])//2 
    return y - min(y//8,aux)

def next_term(n,aux):
    x = computed_terms[n - computed_terms[-1]] + computed_terms[n - computed_terms[-2]]
    return reducer(x,aux)

if __name__ == "__main__":
    for k in computed_terms:
        print(k)
    t = 3.123456789
    for i in range(1_000_000):
        t = 0.5*(t - 1/t)
        computed_terms.append(next_term(i,t))
        print(computed_terms[-1])
