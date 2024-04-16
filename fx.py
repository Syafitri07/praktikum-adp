x = list(range(-10, 11))

fx = [i**2 + 2*i if i > 0 else (1/i if i < 0 else 10) for i in x]

print("|  x|\tf(x)|")
for i in range(len(x)):
    if x[i] < 0:
        fx_str = f"-0.{str(fx[i])[3:]}"
    else: 
        fx_str = f"{fx[i]:.3f}"
    print(f"|{x[i]:3}| {fx[i]:7}|")