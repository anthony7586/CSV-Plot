# this main calls plot functions, each function saves to the folder "/plot outputs"
from plot_csv import scatter_plot_csv, linear_plot_csv






def main():
    #example use 
    #linear_plot_csv(data_file_path.csv, x_data_column_from_csv, y_data_column_from_csv)
    scatter_plot_csv('parsed_serial_log.csv',0,2)
    linear_plot_csv('parsed_serial_log.csv',0,2)



if __name__ == "__main__":
    main()