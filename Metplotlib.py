import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020]
home_runs = [30, 45, 50, 40, 60]

plt.plot(years, home_runs)  # Line plot
plt.xlabel("Year")
plt.ylabel("Home Runs")
plt.title("Home Runs Over the Years")

plt.show()
