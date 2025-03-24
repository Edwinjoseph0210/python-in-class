import pandas as pd

# Define the data
data = {
    'Name': ['Nikhil', 'Sanchit', 'Aditya', 'Sagar'],
    'Branch': ['CSE', 'CSE', 'IT', 'IT'],
    'Year': [2, 2, 2, 1],
    'CGPA': [9.0, 9.1, 9.3, 9.5]
}

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(data)
df.to_csv('student.csv', index=False)
print("CSV file 'student.csv' created successfully.")

# Read the CSV file
df = pd.read_csv('student.csv')

# Perform operations
print("\n️⃣ 1 Average CGPA:", df['CGPA'].mean())

print("\n2️⃣ Students with CGPA > 9:")
print(df[df['CGPA'] > 9])

print("\n3️⃣ CSE students with CGPA > 9:")
print(df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)])

print("\n4️⃣ Student with maximum CGPA:")
print(df[df['CGPA'] == df['CGPA'].max()])

print("\n5️⃣ Average CGPA per branch:")
print(df.groupby('Branch')['CGPA'].mean())
