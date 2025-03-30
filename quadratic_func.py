from cmath import sqrt

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен нулю.")
    
    # Вычисляем дискриминант
    D = b**2 - 4*a*c
    
    # Находим два корня
    root1 = (-b + sqrt(D)) / (2 * a)
    root2 = (-b - sqrt(D)) / (2 * a)
    
    return root1, root2