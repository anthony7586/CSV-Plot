# this main calls plot functions, each function saves to the folder "/plot outputs"
from plot_csv import scatter_plot_course_csv, linear_plot_course_csv






def main():
    #example use 
    #scatter_plot_course_csv('mydata.csv',0,1)
    #scatter_plot_course_csv('mydata.csv',0,1,2)
    #linear_plot_course_csv('mydata.csv',0,1,2)

    linear_plot_course_csv('mydata.csv',0,1)



if __name__ == "__main__":
    main()