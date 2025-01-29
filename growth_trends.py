def sorted_squares(growth_percentages):
    n = len(growth_percentages)
    result = [0] * n
    left, right = 0, n - 1
    position = n - 1

    while left <= right:
        left_square =  growth_percentages[left] ** 2
        right_square =  growth_percentages[right] ** 2

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        
        position -=1
        
    return result