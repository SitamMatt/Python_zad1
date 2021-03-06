def wallis_product(k):
    result = 1
    for n in range(1, k + 1):
        p1 = (2 * n) / (2 * n - 1)  # 1st part
        p2 = (2 * n) / (2 * n + 1)  # 2nd part
        p = p1 * p2  # final iteration result
        result *= p
    return result


def wallis(k):
    result = wallis_product(k)
    # the final result should be multiplied by 2 because Wallis product gives approximation of pi/2
    return result * 2
