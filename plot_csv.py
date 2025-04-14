import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime


def scatter_plot_csv(csv_file,x_col,y1_col):

    # Load CSV file
    #data = pd.read_csv('mydata.csv')
    data = pd.read_csv(csv_file)

    # Check if the CSV has at least 4 columns
    if data.shape[1] < 2:
        raise ValueError("CSV file must contain at least 4 columns.")

    # Select columns (column indices start at 0)
    x = data.iloc[:, x_col]  # Column 1
    y1 = data.iloc[:, y1_col]  # Column 3
    #y2 = data.iloc[:, 3]  # Column 4

    # Create output directory if it doesn't exist
    output_dir = 'plot outputs'
    os.makedirs(output_dir, exist_ok=True)

    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f'Scatter_Plot_{timestamp}.png'
    output_path = os.path.join(output_dir, filename)


    # plotting scatter of same data
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y1, label='Column 3, Course degree over time(scatter)')
    #plt.plot(x, y2, label='Column 4') ##uncomment to add another column of data from .csv, specify what y2 is 
    plt.xlabel('time (ms)')
    plt.ylabel('Coarse degree over time')
    plt.title('Course degree over time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.show() #unncomment this line to show the plot, plot will also be saved into the ouput folder called 'plot outputs'

    # Save the plot
    plt.savefig(output_path)
    plt.close()

    print(f"Plot saved to {output_path}")


def linear_plot_csv(csv_file,x_col,y1_col):

    # Load CSV file
    #data = pd.read_csv('mydata.csv')
    data = pd.read_csv(csv_file)

    # Check if the CSV has at least 4 columns
    if data.shape[1] < 2:
        raise ValueError("CSV file must contain at least 4 columns.")

    # Select columns (column indices start at 0)
    x = data.iloc[:, x_col]  # Column 1
    y1 = data.iloc[:, y1_col]  # Column 3
    #y2 = data.iloc[:, 3]  # Column 4

    # Create output directory if it doesn't exist
    output_dir = 'plot outputs'
    os.makedirs(output_dir, exist_ok=True)

    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f'Linear_Plot_{timestamp}.png'
    output_path = os.path.join(output_dir, filename)

    # Plotting line plot 
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='Column 3, Course degree over time')
    #plt.plot(x, y2, label='Column 4') ##uncomment to add another column of data from .csv, specify what y2 is 
    plt.xlabel('time (ms)')
    plt.ylabel('Coarse degree over time')
    plt.title('Course degree over time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.show() #unncomment this line to show the plot, plot will also be saved into the ouput folder called 'plot outputs'

    # Save the plot
    plt.savefig(output_path)
    plt.close()


    print(f"Plot saved to {output_path}")

#example use
#scatter_plot_csv('parsed_serial_log.csv')