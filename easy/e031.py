n_cases = int(input())

for _ in range(n_cases): 
    nr, dr = input().split()
    
    try:
        print(int(nr)//int(dr))
    except ValueError as e:
        print(f"Error Code: {e}")
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")