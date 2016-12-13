#evaluates a reverseion polish notat
def parseexpr(expr):
    stack = []
    for operator in expr.split(' '):
        if operator in ['+', '-', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if operator == '+':
                result = op2 + op1
            elif operator == '-':
                result = op2 - op1
            elif operator == '*':
                result = op2 * op1
            elif operator == '/':
                result = op2 / op1
            #elif operator == '^':
                #Sresult = op1 ^ op2
            stack.append(result)
        else:
            stack.append(float(operator))
 
    return stack.pop()

if __name__ == '__main__':
    expr = '6 4 5 + * 25 2 3 + / -'
    result = parseexpr(expr)
    print (result)
 
    
