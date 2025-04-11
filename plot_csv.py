import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Load CSV file
data = pd.read_csv('mydata.csv')

# Check if the CSV has at least 4 columns
if data.shape[1] < 4:
    raise ValueError("CSV file must contain at least 4 columns.")

# Select columns (column indices start at 0)
x = data.iloc[:, 1]  # Column 2
y1 = data.iloc[:, 2]  # Column 3
y2 = data.iloc[:, 3]  # Column 4

# Create output directory if it doesn't exist
output_dir = 'plot outputs'
os.makedirs(output_dir, exist_ok=True)

# Create timestamp for filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
filename = f'Plot_{timestamp}.png'
output_path = os.path.join(output_dir, filename)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Column 3')
plt.plot(x, y2, label='Column 4')
plt.xlabel('Column 2')
plt.ylabel('Values column 3 & 4 ')
plt.title('Plot of Column 3 and 4 vs Column 2')
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.show() #unncomment this line to show the plot, plot will also be saved into the ouput folder called 'plot outputs'

# Save the plot
plt.savefig(output_path)
plt.close()

print(f"Plot saved to {output_path}")
