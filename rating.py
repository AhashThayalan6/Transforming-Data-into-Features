# Task 7: Create a dictionary for `rating`
rating_dict = {
    'Loved it': 5,
    'Liked it': 4,
    'Was okay': 3,
    'Not great': 2,
    'Hated it': 1
}

# Task 8: Transform the `rating` column
reviews['rating'] = reviews['rating'].map(rating_dict)
print("\nTransformed 'rating' Value Counts:")
print(reviews['rating'].value_counts())

# Task 9: Print `department_name` value counts
print("\nValue Counts for 'department_name':")
print(reviews['department_name'].value_counts())

# Task 10: One-hot encode `department_name`
one_hot = pd.get_dummies(reviews['department_name'], prefix='department')

# Task 11: Join one-hot encoded columns to the DataFrame
reviews = pd.concat([reviews, one_hot], axis=1)
print("\nUpdated Column Names After One-Hot Encoding:")
print(reviews.columns)
