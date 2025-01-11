Task 12: Transform `review_date` to date-time
reviews['review_date'] = pd.to_datetime(reviews['review_date'])
print("\nData Type of 'review_date':", reviews['review_date'].dtype)

# Task 13: Select numerical columns
numerical_cols = reviews.select_dtypes(include=['number'])
print("\nNumerical Columns Preview:")
print(numerical_cols.head())

# Task 14: Reset index to `clothing_id`
reviews.set_index('clothing_id', inplace=True)

# Task 15: Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_cols)

# Convert scaled data back to a DataFrame
scaled_df = pd.DataFrame(scaled_data, columns=numerical_cols.columns, index=numerical_cols.index)
print("\nScaled Data Preview:")
print(scaled_df.head())

# Task 16: Congratulations!
print("\nData Transformation Completed Successfully!")
