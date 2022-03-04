def computepay(h, r):
    if h > 40:
        total = (40 * r) + (h - 40) * (r * 1.5)
        return total
    else:
        total = h * r
        return total

hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate) 
print("Pay", p)