import pandas as pd

# Define the data
data = {
    'Name': ['Nikhil', 'Sanchit', 'Aditya', 'Sagar'],
    'Branch': ['CSE', 'CSE', 'IT', 'IT'],
    'Year': [2, 2, 2, 1],
    'CGPA': [9.0, 9.1, 9.3, 9.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Writing to student.csv
df.to_csv('student.csv', index=False)

print("CSV file 'student.csv' has been created successfully.")
