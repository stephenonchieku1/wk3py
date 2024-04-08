def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(price, discount_percent)
        
        if final_price != price:
            print("Final price after discount: $", final_price)
        else:
            print("No discount applied. Original price: $", price)
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()
