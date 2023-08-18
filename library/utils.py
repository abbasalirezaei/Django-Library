def calculate_borrowing_days(n, f):
    print('im here')
    print(n,f)
    
    if (1 + (( (30 * n ) /  n) + f )) > 3:
       
        return (int(1 + (( (30 * n ) /  n) + f )))
    else:
        return (3)