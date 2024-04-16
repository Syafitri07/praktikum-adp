x = list(range(-10, 11))

fx = []

def f(x):
    if x > 0:
        return x**2 +2*x
    elif x < 0: 
        return 1/x
    else:
        return 10
    
for num in x:
    fx.append(f(num))

print("| x |   f(x)|")
for x_val, f_val in zip(x, fx):
    print(f"|{x_val:3}| {f_val:5} |")