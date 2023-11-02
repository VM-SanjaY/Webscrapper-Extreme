from fuzzywuzzy import fuzz

# User's input
user_input = "samsung s23"

# Threshold for similarity (adjust as needed)
similarity_threshold = 50  # You can choose an appropriate value
product_name = "SAMSUNG Galaxy S23 5G"  # Example product name from the website
similarity = fuzz.partial_ratio(user_input.lower(), product_name.lower())
print("Similarity Score:", similarity)
if similarity >= similarity_threshold:
    print("yes" )
else:
    print("no")
    
    