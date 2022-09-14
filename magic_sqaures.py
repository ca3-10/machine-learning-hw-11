
digits = [1,2,3,4,5,6,7,8,9]
original_digits = digits.copy()
square = [[None, None, None],[None, None, None],[None, None, None]]

def is_hopeless(square): 
    
    for i in range(3): 
        #rows
        if (square[i][0] is not None and square[i][1] is not None and square[i][2] is not None) and (square[i][0] + square[i][1] + square[i][2] != 15):
            return True
        #columns
        if (square[0][i] is not None and square[1][i] is not None and square[2][i] is not None) and (square[0][i] + square[1][i] + square[2][i] != 15):
            return True 
        #diagonal 1
        if (square[0][0] is not None and square[1][1] is not None and square[2][2] is not None) and (square[0][0] + square[1][1] + square[2][2] != 15):
            return True
        #diagonal 2
        if (square[0][2] is not None and square[1][1] is not None and square[2][0] is not None) and (square[0][2] + square[1][1] + square[2][0] != 15):
            return True
        else: 
            return False

for num1 in digits:
    digits2 = list(digits)
    digits2.remove(num1)
    square1 = [[num1, None, None], [None, None, None], [None, None, None]]
    if is_hopeless(square1): 
        continue

    for num2 in digits2:
        digits3 = list(digits2)
        digits3.remove(num2)
        square2 = [[num1, num2, None], [None, None, None], [None, None, None]]
        if is_hopeless(square2): 
            continue

        for num3 in digits3:
            digits4 = list(digits3)
            digits4.remove(num3)
            square3 = [[num1, num2, num3], [None, None, None], [None, None, None]]
            if is_hopeless(square3): 
                continue

            for num4 in digits4:
                digits5 = list(digits4)
                digits5.remove(num4)
                square4 = [[num1, num2, num3], [num4, None, None], [None, None, None]]
                if is_hopeless(square4): 
                    continue

                for num5 in digits5:
                    digits6 = list(digits5)
                    digits6.remove(num5)
                    square5 = [[num1, num2, num3], [num4, num5, None], [None, None, None]]
                    if is_hopeless(square5): 
                        continue

                    for num6 in digits6:
                        digits7 = list(digits6)
                        digits7.remove(num6)
                        square6 = [[num1, num2, num3], [num4, num5, num6], [None, None, None]]
                        if is_hopeless(square6): 
                            continue

                        for num7 in digits7:
                            digits8 = list(digits7)
                            digits8.remove(num7)
                            square7 = [[num1, num2, num3], [num4, num5, num6], [num7, None, None]]
                            if is_hopeless(square7): 
                                continue

                            for num8 in digits8:
                                digits9 = list(digits8)
                                digits9.remove(num8)
                                square8 = [[num1, num2, num3], [num4, num5, num6], [num7, num8, None]]
                                if is_hopeless(square8): 
                                     continue
                                for num9 in digits9:
                                    square = [[num1, num2, num3], [num4, num5, num6], [num7, num8, num9]]
                                    nums = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
                                    #print(sorted(nums))
                                    if (square[0][0] + square[1][0] + square[2][0]) == (square[0][1] + square[1][1] + square[2][1]) == (square[0][2] + square[1][2] + square[2][2]) == (square[0][0] + square[0][1] + square[0][2]) == (square[1][0] + square[1][1] + square[1][2]) == (square[2][0] + square[2][1] + square[2][2]) == (square[0][0] + square[1][1] + square[2][2]) == (square[0][2] + square[1][1] + square[2][0]) == 15 and sorted(nums) == original_digits:
                                        print(square)
                                        print()

