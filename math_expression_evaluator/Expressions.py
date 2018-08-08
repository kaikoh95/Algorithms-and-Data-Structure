from Structures import Stack, Deque, Queue
import re
import doctest
import os

OP_PREC={"(":1,
         "+":2,
         "-":2,
         "*":3,
         "/":3,
         ")":4}




def calculate(operator, param1, param2):
    """
    Returns the result of a calculation between param1 and param2 using the
    given operator.
    Supported operators: *, /, +, -, ^

    >>> calculate('*', 2, 3)
    6
    >>> calculate('+', 2, 3)
    5
    >>> calculate('-', 2, 3)
    -1
    """
    if operator == '*':
        return param1 * param2
    elif operator == '/':
        # Promote these to floats to avoid truncation
        return float(param1) / float(param2)
    elif operator == '+':
        return param1 + param2
    elif operator == '-':
        return param1 - param2
    else:
        raise Exception(operator+" is an invalid operator!")


def evaluate_postfix(expression):
    """
    Evaluates an expression in postfix notaion.
    Numerical operands must be integers.

    >>> evaluate_postfix('2 3 +')
    5
    >>> evaluate_postfix('2 3 4 * +')
    14
    >>> evaluate_postfix('2 3 + 4 *')
    20
    >>> evaluate_postfix('2 3 2 * + 5 -')
    3
    >>> evaluate_postfix('2 3 + 2 5 - *')
    -15
    >>> evaluate_postfix('2 3 + 5 2 / *')
    12.5
    >>> evaluate_postfix('2 3 4 8 + * + 1 + 4 * 5 -')
    151
    """
    # Split postfix string into tokens. For example:
    #  '2 3 +' => ['2', '3', '+']
    # Don't worry about how this works
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', expression)

    #Code to evaluate the postfix expression and return the result goes here
    # ---start student section---
    list2 = []
    stack = Stack()
    for symbol in tokens:
        if symbol not in OP_PREC:
            stack.push(symbol)
        else:
            list2.append(stack.pop())
            list2.append(stack.pop())
            alpha = float(list2[0])
            beta = float(list2[1])
            result = calculate(symbol, beta, alpha)
            list2.pop()
            list2.pop()
            stack.push(result)
    final = stack.pop()
    if final % int(final) == 0:
        final = round(final)
    return final      
    # ===end student section===


def infix_to_postfix(infix_expression):
    """
    Converts an infix expression to a postfix expression.
    Numerical operands must be integers.

    >>> infix_to_postfix('2 + 3')
    '2 3 +'
    >>> infix_to_postfix('2 + 3 * 4')
    '2 3 4 * +'
    >>> infix_to_postfix('(2 + 3) * 4')
    '2 3 + 4 *'
    >>> infix_to_postfix('2 + 3 * 2 - 5')
    '2 3 2 * + 5 -'
    >>> infix_to_postfix('(2 + 3) * (2 - 5)')
    '2 3 + 2 5 - *'
    >>> infix_to_postfix('(2 + 3) * (5 / 2)')
    '2 3 + 5 2 / *'
    """

    # Split infix string into tokens. For example:
    #  '2+3*4' => ['2', '+', '3', '*', '4']
    # Don't worry too much about how...
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', infix_expression)

    #Code to process tokens and return the postfix string goes here
    # ---start student section---
    output = []
    stack = Stack()
    for s in tokens:
        if s not in OP_PREC:
            output.append(s)
        elif s == '(':
            stack.push(s)
        elif s == ')':
            item = stack.pop()
            while item != '(':
                output.append(item)
                item = stack.pop()
        else:
            while not stack.is_empty() and OP_PREC[s] <= OP_PREC[stack.peek()]:
                output.append(stack.peek())
                stack.pop()
            stack.push(s)
    while not stack.is_empty():
        output.append(stack.pop())
    string = ''
    count = 0
    for i in range(len(output) - 1):
        string += output[i]
        string += ' '
        count += 1
    string += output[-1]
    return string
    # ===end student section===


def evaluate_infix(infix_expression):
    """
    Evaluates an infix expression.
    Numerical operands must be integers.

    >>> evaluate_infix('2 + 3 * 4')
    14
    >>> evaluate_infix('2 + (3 * 4)')
    14
    >>> evaluate_infix('(2 + 3) * 4')
    20
    >>> evaluate_infix('2 + 3 * 2 - 5')
    3
    >>> evaluate_infix('(2 + 3) * (2 - 5)')
    -15
    >>> evaluate_infix('(2 + 3) * (5 / 2)')
    12.5
    """

    # Split infix string into tokens. For example:
    #  '2+3*4' => ['2', '+', '3', '*', '4']
    # Don't worry too much about how...
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', infix_expression)


    #Code to process tokens and evaluate the infix expression

    # ---start student section---
    operator = Stack()
    operand = Stack()
    for s in tokens:
        if s not in OP_PREC: #s is an integer
            operand.push(s)
        elif s == '(':
            operator.push(s)
        elif s == ')':
            item = operator.pop()
            while item != '(':
                alpha = float(operand.pop())
                beta = float(operand.pop())
                if item == '(':  
                    operator.pop()                
                else:
                    delta = calculate(item, beta, alpha)
                    operand.push(delta)
                item = operator.pop()
        else: #s is an operator
            if len(operator) > 1 and len(operand) > 2:
                if OP_PREC[s] < OP_PREC[operator.peek()]:
                    sign = operator.pop()
                    alpha = float(operand.pop())
                    beta = float(operand.pop())
                    delta = calculate(sign, beta, alpha)
                    operand.push(delta) 
            operator.push(s)
    while not operand.is_empty() and not operator.is_empty():
        sign = operator.pop()
        alpha = float(operand.pop())
        beta = float(operand.pop())
        delta = calculate(sign, beta, alpha)
        operand.push(delta)       
    result = operand.pop()
    if result % int(result) == 0:
        result = round(result)
    return result
    # ===end student section===




def evaluate_prefix(prefix_expression):
    """
    Evaluates a prefix expression directly, using a Deque.
    Numerical operands must be integers and are initialy cast as ints.
    Remember intermediate values may be floats (eg, 3/4 gives 0.75)
    so don't cast anything to int after the input phase.

    >>> evaluate_prefix('+ 2 4')
    6
    >>> evaluate_prefix('+ 2 * 4 3')
    14
    >>> evaluate_prefix('* + 2 * 1 2 8')
    32
    >>> evaluate_prefix('* - + 2 1 2 8')
    8
    >>> evaluate_prefix('+ / 8 - 6 2 4')
    6.0
    """

    # Split prefix string into tokens.
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', prefix_expression)

    # add everything to a queue
    dq = Deque()
    operator_dq = Deque()
    operand_dq = Deque()
    for token in tokens:
        if token not in OP_PREC:
            # is a number so convert to integer
            token = int(token)
        dq.enqueue_rear(token)    
    while dq.__len__() > 3:
        for s in dq._items:
            delta = []
            operator_count = 0
            operand_count = 0            
            first = dq.dequeue_front()
            second = dq.dequeue_front()
            third = dq.dequeue_front()
            delta =[first, second, third]
            for symbol in delta:
                if symbol in OP_PREC:
                    operator_count += 1
                    operator_dq.enqueue_rear(symbol)
                else:
                    operand_count += 1
                    operand_dq.enqueue_rear(symbol)
            if delta[0] in OP_PREC and delta[1] not in OP_PREC and delta[2] in OP_PREC:
                dq.enqueue_rear(operator_dq.dequeue_front())
                dq.enqueue_rear(operand_dq.dequeue_front())
                dq.enqueue_front(operator_dq.dequeue_front())               
            elif delta[0] in OP_PREC and delta[1] not in OP_PREC and delta[2] not in OP_PREC:
                result = calculate(delta[0], delta[1], delta[2])
                dq.enqueue_rear(result)
                operator_dq.dequeue_front()
                operand_dq.dequeue_front()
                operand_dq.dequeue_front()
            else:
                dq.enqueue_rear(delta[0])
                dq.enqueue_rear(delta[1])
                dq.enqueue_rear(delta[2])
                while not operator_dq.is_empty():
                    operator_dq.dequeue_front()
                while not operand_dq.is_empty():
                    operand_dq.dequeue_front()
    if dq.__len__() == 3:
        first = dq.dequeue_front()
        second = dq.dequeue_front()
        third = dq.dequeue_front()
        delta =[first, second, third]
        if delta[0] in OP_PREC:
            final = calculate(delta[0], delta[1], delta[2])
        elif delta[1] in OP_PREC:
            final = calculate(delta[1], delta[0], delta[2])
        else:
            final = calculate(delta[2], delta[0], delta[1])
    elif dq.__len__() == 1:
        final = dq.dequeue_front()
    return final

if __name__ == '__main__':
    # os.environ['TERM'] = 'linux' # Suppress ^[[?1034h

    # Uncomment the next line to run the doctests
    doctest.testmod()  # If everything works then the doctests will output nothing...