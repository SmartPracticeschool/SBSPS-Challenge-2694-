def bill_count(amount,bills):
    bills.sort()
    flag=0
    for i in bills:
        if i<0:
            flag=1
            break;
    if amount<0:
        flag=1
    if amount<bills[0]:
        return "Invalid condition,amount is less than list of bills."
    if flag==1:
        return "Invalid Input,currency cannot be negative."
    else:
        count=0
        for i in reversed(bills):
            x=amount//i
            count+=x
            if x>0:
                amount-=i*x
    return count


            
        
