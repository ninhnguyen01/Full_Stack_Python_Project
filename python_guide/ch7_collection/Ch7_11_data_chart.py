""" Plotting List Data with the matplotlib Package """

# Alternate Method
import matplotlib.pyplot as plt # plt is alias name - common practice for package import

# plt.plot(arguments...)
x_coords = [0,1,2,3,4]
y_coords = [0,3,1,5,2]

plt.plot(x_coords,y_coords)
plt.show()

# line graph1
def line_graph():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.show()

line_graph()

# line graph2
def line_graph2():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.title('Sample Data')
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')
    plt.grid(True)
    plt.show()

line_graph2()

# line graph3
def line_graph3():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.title('Sample Data')
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)
    plt.grid(True)
    plt.show()

line_graph3()

# line graph4
def lin_graph4():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks([0,1,2,3,4],['2016','2017','2018',
    '2019','2020'])
    plt.yticks([0,1,2,3,4,5],['$0m','$1m','$2m',
    '$3m','$4m','$5m'])
    plt.grid(True)
    plt.show()

lin_graph4()

# line graph5
def line_graph5():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords,marker = 'o')
    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks([0,1,2,3,4],['2016','2017','2018',
    '2019','2020'])
    plt.yticks([0,1,2,3,4,5],['$0m','$1m','$2m',
    '$3m','$4m','$5m'])
    plt.grid(True)
    plt.show()

line_graph5()

# bar chart1
def bar_chart1():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    plt.bar(left_edges,heights)
    plt.show()

bar_chart1()

# bar chart2
def bar_chart2():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    bar_width = 5
    plt.bar(left_edges,heights,bar_width)
    plt.show()

bar_chart2()

# with color
def color_chart():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    bar_width = 5
    plt.bar(left_edges,heights,bar_width,
    color=('r','g','b','y','k'))
    plt.show()

color_chart()

# bar chart3
def bar_chart3():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    bar_width = 10
    plt.bar(left_edges,heights,bar_width,
    color=('r','g','b','y','k'))
    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks([5,15,25,35,45],['2016','2017','2018',
    '2019','2020'])
    plt.yticks([0,100,200,300,400,500],['$0m','$1m','$2m',
    '$3m','$4m','$5m'])
    plt.show()

bar_chart3()

# pie chart1
def pie_chart1():
    values = [20,60,80,40]
    plt.pie(values)
    plt.show()

pie_chart1()

# pie chart2
def pie_chart2():
    sales = [100,400,300,600]
    slice_labels = ['1st Qtr','2nd Qtr',
    '3rd Qtr','4th Qtr']
    plt.pie(sales,labels= slice_labels)
    plt.title('Sales by Quarter')
    plt.show()

pie_chart2()

# with color
def pie_chart_color():
    sales = [100,400,300,600]
    slice_labels = ['1st Qtr','2nd Qtr',
    '3rd Qtr','4th Qtr']
    plt.pie(sales,labels= slice_labels,
    colors=('r','g','b','y','k'))
    plt.title('Sales by Quarter')
    plt.show()

pie_chart_color()