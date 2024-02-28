def fast_acoth_approximator(x: float|int, /, *, 
precision: int = 60, 
seed: float|int = 1.0) -> float|Exception:
    _ = "preconditions"
    assert isinstance(x, float|int)
    assert type(precision) is int
    assert isinstance(seed, float|int)
    
    _ = "undefined between -1 and 1"
    if -1 <= x <= 1:
        class AcothIsUndefined(Exception):
            pass
        return AcothIsUndefined
        
    _ = "main case"
    total: float = seed
    for depth in range(precision, -1, -1):
        if isDenominatorZero := (total==0):
            total += 0.01
        if reachedTheTopOfFrac := (depth==0):
            return 1/x + (x**-3)/total
        offset: float = 2*depth+1
        coeff: float = (depth+2*(depth%2==1))**2
        numerator: float = coeff*(x**-2)
        total = offset - numerator/total
        
    _ = "never reaching the top of the frac"
    class TopOfFracWasNeverReached(Exception):
            pass
    return TopOfFracWasNeverReached
    
