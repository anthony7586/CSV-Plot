import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime


###############################################################################################################
###############################################################################################################
###############################################################################################################


###############################################################################################################
###############################################################################################################
###############################################################################################################

#uncomment y2_col to be able to plt a 3rd line, make  sire data y2 is assigned and updated into the plot. 
def scatter_plot_course_csv(csv_file,x_col,y1_col,y2_col=None):

    # Load CSV file
    #data = pd.read_csv('mydata.csv')                                   #uncomment to plot extra column of data 
    data = pd.read_csv(csv_file)

    # Check if the CSV has at least 4 columns
    if data.shape[1] < 2:
        raise ValueError("CSV file must contain at least 2 columns.")

    # Select columns (column indices start at 0)
    x = data.iloc[:, x_col]  
    y1 = data.iloc[:, y1_col]  
    # Optional third column
    y2 = data.iloc[:, y2_col] if y2_col is not None else None

    # Create output directory if it doesn't exist
    output_dir = 'plot outputs'
    os.makedirs(output_dir, exist_ok=True)

    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f'Coarse_Scatter_Plot_{timestamp}.png'
    output_path = os.path.join(output_dir, filename)


    # Plotting
    plt.figure(figsize=(10, 6))

    # Fine-tuned scatter plot for y1
    plt.scatter(x, y1, s=10, marker='o', label=str('Column '+ str(y1_col)))

    # Optional third line using plot (line plot for contrast)
    if y2 is not None:
        plt.scatter(x, y2, color='orange', linewidth=1.5, label=f'Column {y2_col}')
                                     #uncomment to plot extra column of data to graph
    plt.xlabel('time (ms)')
    plt.ylabel('Coarse degree')
    plt.title('Course degree over time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.show() #unncomment this line to show the plot, plot will also be saved into the ouput folder called 'plot outputs'

    # Save the plot
    plt.savefig(output_path)
    plt.close()

    print(f"Plot saved to {output_path}")



###############################################################################################################
###############################################################################################################
###############################################################################################################


###############################################################################################################
###############################################################################################################
###############################################################################################################


    #uncomment y2_col to be able to plt a 3rd line, make  sire data y2 is assigned and updated into the plot. 
def linear_plot_course_csv(csv_file,x_col,y1_col,y2_col=None):

    # Load CSV file
    #data = pd.read_csv('mydata.csv')                                   #uncomment to plot extra column of data 
    data = pd.read_csv(csv_file)

    # Check if the CSV has at least 4 columns
    if data.shape[1] < 2:
        raise ValueError("CSV file must contain at least 2 columns.")

    # Select columns (column indices start at 0)
    x = data.iloc[:, x_col]  
    y1 = data.iloc[:, y1_col]  
    # Optional third column
    y2 = data.iloc[:, y2_col] if y2_col is not None else None 

    # Create output directory if it doesn't exist
    output_dir = 'plot outputs'
    os.makedirs(output_dir, exist_ok=True)

    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f'Coarse_Linear_Plot_{timestamp}.png'
    output_path = os.path.join(output_dir, filename)

    # Plotting line plot 
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label=str('Column '+ str(y1_col)))

    # Optional third line using plot (line plot for contrast)
    if y2 is not None:
        plt.plot(x, y2, color='orange', linewidth=1.5, label=f'Column {y2_col}')

    plt.xlabel('time (ms)')
    plt.ylabel('Coarse degree')
    plt.title('Course degree over time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.show() #unncomment this line to show the plot, plot will also be saved into the ouput folder called 'plot outputs'

    # Save the plot
    plt.savefig(output_path)
    plt.close()


    print(f"Plot saved to {output_path}")

###############################################################################################################
###############################################################################################################
###############################################################################################################


###############################################################################################################
###############################################################################################################
###############################################################################################################

#example use
#scatter_plot_csv('parsed_serial_log.csv')