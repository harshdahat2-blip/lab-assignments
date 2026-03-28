#Task 1
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))


print("Total number of items in tuple:", len(numbers))


print("Last item in the tuple:", numbers[-1])


print("Tuple elements in reverse order:", numbers[::-1])


if 5 in numbers:
    print("Yes, the tuple contains integer 5")
else:
    print("No, the tuple does not contain integer 5")


new_tuple = numbers[1:-1]
sorted_tuple = tuple(sorted(new_tuple))

print("Tuple after removing first and last elements and sorting:", sorted_tuple)

#Task 2

prices = tuple(map(int, input("Enter prices of sold items separated by space: ").split()))

print("Total number of items sold:", len(prices))

print("Price of cheapest item sold:", min(prices))

print("Price of costliest item sold:", max(prices))

print("Prices in ascending order:", tuple(sorted(prices)))

costliest = max(prices)
count = prices.count(costliest)

print("Number of costliest items sold:", count)