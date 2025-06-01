def separate_squares(start, end):
    a = [num**2 for num in range(start, end + 1)]
    e = [sq for sq in a if sq % 2 == 0]
    o = [sq for sq in a if sq % 2 != 0]
    
    return a, e, o

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

a, e, o = separate_squares(start, end)

print(f"Squares roots: {a}")
print(f"Even squares roots: {e}")
print(f"Odd squares roots: {o}")


