## Reflection

In this assignment, the goal was to extract at least 10 data visualizations from the ForestFires dataset using tools such as Matplotlib, Seaborn and Bokeh.

Specifically, if we had a question in mind that we wanted from our data, the instructions were to specify the question, display the visualization process, and make conclusions based on what you observed.

We used different types of images such as barplot, lineplot, histogram, heatmap, boxplot, etc.

One of the best methods that we used in the assignment would be querying such as:

```python
month = data.query("month == ['aug','sep']")
day = month.query("day == ['fri']")
```

The awesome advantage of using the query function would be that when it comes to analyzing our data based on month and day, the query function makes visualization a lot easier to extract overall.

Another important note when using Bokeh:

```bash
bokeh serve --show mainapp.py
```

Based on where your directory is, if you are running a plot that has the ability to use any column you want, on terminal, you have to copy and paste the terminal command above.

The mainapp.py is an example of a file name, so make sure you copy and paste the correct name of your file.



## Reflection Questions

#### 1

We all did well in extracting the columns that we would need to make visualizations.

We knew based on our information what columns we can connect together to make some exploratory analysis.

#### 2

The most challenging part of this assignment was trying to extract visualizations from Bokeh.

Also, given that there were at least 10 visualizations that we had to come up with, trying to come up with a few more questions and approaching them was a little tricky as well.

#### 3

This assignment would have been a way better experience if we had prior exposure to Bokeh. 

Many of us knew about Seaborn and Matplotlib, but only a few of us knew that Bokeh existed.

#### 4

We would need more assistance in knowing how to use Bokeh better. 

It seemed simple when we can look up visualizations, but it's much harder when we have to think and extract the visualization of our liking.


## License

The license to be used is [MIT](https://choosealicense.com/licenses/mit/)
