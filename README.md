# Visualization with Seaborn and Matplotlib

## Reflection

In this assignment, the goal was to extract at least 10 data visualizations from the ForestFires dataset using tools such as Matplotlib, Seaborn and Bokeh. Specifically, if we had a question in mind that we wanted from our data, the instructions were to specify the question, display the visualization process, and make conclusions based on what you observed. We used different types of images such as barplot, lineplot, histogram, heatmap, boxplot, etc.

One of the best methods that we used in the assignment would be querying such as:
```python
month = data.query("month == ['aug','sep']")
day = month.query("day == ['fri']")
```

The awesome advantage of using the query function would be that when it comes to analyzing our data based on month and day, the query function makes visualization a lot easier to extract overall.

### Another important note when using Bokeh:
We wanted to utilize the amazing feature of interaction graph in Bokeh, so we implemented one in the source folder. To view it, please navigate to the `source` directory and run:

```bash
bokeh serve --show bokeh_app.py
```

Based on where your directory is, if you are running a plot that has the ability to use any column you want, on terminal, you have to copy and paste the terminal command above.

  
  
  

## Reflection Questions

#### Q1: What do I believe I did well on this assignment?

We all did well in extracting the columns that we would need to make visualizations. We knew based on our information what columns we can connect together to make some exploratory analysis.

#### Q2:  What was the most challenging part of this assignment?

Given that there were at least 10 visualizations that we had to come up with, trying to come up with a few more questions and approaching them was a little tricky. Also, answering our own questions in graphs was a bit tough. This included questions, such as which data and graph we would use, how would we clean the data before using them in the visualization.

Another challenging part of this assignment was trying to extract visualizations from Bokeh. It was just new for all of us, and we need a bit of time to go through the tutorial.

#### Q3:  What would have made this assignment a better experience?

This assignment would have been a way better experience if we had prior exposure to Bokeh. Many of us knew about Seaborn and Matplotlib, but only a few of us knew that Bokeh existed. 

Also, it would be great to see what are the best practices of visualizing graphs in different fields. The way of creating effective graphs in business, engineering, statistics and others are so different as they are targeting different audiences with different purpose.

#### Q4:  What do I need help with?

We would need more assistance in knowing how to use Bokeh better. It seemed simple when we can look up visualizations, but it's much harder when we have to think and extract the visualization of our liking. I believe it was because it was more of lower level visualization tool compared to seaborn package. However, we do believe that it has an amazing power to visualize graphs more effectively.

## License

The license to be used is [MIT](https://choosealicense.com/licenses/mit/)