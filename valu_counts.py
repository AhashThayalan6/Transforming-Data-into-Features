# Task 3: Transform the `recommended` feature
print("\nValue Counts for 'recommended':")
print(reviews['recommended'].value_counts())

# Task 4: Create a binary dictionary for `recommended`
binary_dict = {True: 1, False: 0}

# Task 5: Apply transformation to `recommended`
reviews['recommended'] = reviews['recommended'].map(binary_dict)
print("\nTransformed 'recommended' Value Counts:")
print(reviews['recommended'].value_counts())

# Task 6: Print `rating` value counts
print("\nValue Counts for 'rating':")
print(reviews['rating'].value_counts())
