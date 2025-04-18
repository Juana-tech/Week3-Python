 calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return price 
        else:
            # Return the original if the discount is less than 20%
            return price

    # Prompt the user for input
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        # Use the calculate_discount function
        final_price = calculate_discount (original_price, discount_percentage)

        # Display the result
        if final_price < original price:
            print(f"The final price after applying the discount is: {final_price:.2f}")
            else:
                print(f"No discount applied. The original price is: {orginal_price:.2f}")
        except ValueError:
            print("Please enter valid numeric values for the price and discount percentage")sss