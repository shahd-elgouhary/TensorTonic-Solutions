def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    op = []
    for n in x:
        if(n>0):
            op.append(n)
        else:
            op.append(alpha*(math.exp(n)-1))
    
    return op

