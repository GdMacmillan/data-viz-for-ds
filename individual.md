# Exploratory Data Visualization

In this exercise we will understand the machinery of what it takes to make a web based interactive data visualization.  We will be using [Bokeh](http://bokeh.pydata.org/) and Seaborn for today's sprint.  We will be working with data on crime statistics that originally came from InfoChimps but has since been removed, but we have saved it for posterity in [data/crime.csv](data/crime.csv)

## The Data

The data represents the number of reported crimes (per 100,000 population) across seven categories of crimes.  They are broken up into:
* **Violent Crimes:** Murder, Rape, Aggravated Assault, Robbery
* **Property Crimes:** Burglary, Larceny Theft, Motor Vehicle Theft

_If you are curious (as I was) to the differences between the various forms of stealing, here is a great video: [https://www.translegal.com/legal-english-lessons/theft-larceny-burglary-and-robbery](https://www.translegal.com/legal-english-lessons/theft-larceny-burglary-and-robbery)_

|State|Murder|Rape|Robbery|Aggravated Assault|Burglary|Larceny Theft|Motor Vehicle Theft|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|Alabama |8.2|34.3|141.4|247.8|953.8|2650|288.3|
|Alaska |4.8|81.1|80.9|465.1|622.5|2599.1|391|
|Arizona |7.5|33.8|144.4|327.4|948.4|2965.2|924.4|
|Arkansas|6.7|42.9|91.1|386.8|1084.6|2711.2|262.1|
|California |6.9|26|176.1|317.3|693.3|1916.5|712.8|
|...|...|...|...|...|...|...|...|...|
<hr>

## Exercise

### Getting Started

If you do not have Bokeh installed already, please follow the instructions [here](http://bokeh.pydata.org/en/latest/docs/installation.html)

### Exploratory Data Analysis

This exercise will build complexity gradually. To start we will perform some exploratory data analysis to figure out the story we want to tell.  And we will then progressively build up an interactive data visualization.

To start we will be using Seaborn for these exploratory plots.

1. Load the dataset into pandas.

2. Perform some exploratory analysis to answer the following questions:
    * Which states have the highest/lowest rate of each of the seven crimes?
    * Across the states, are any of the crime rates highly correlated?

3. Create a heatmap of these correlations using Seaborn.

 ![](images/heat.png)
 
3. Create a histogram for each of the seven crimes to visualize their distributions using Seaborn or `pandas`.  Do this with a KDE plot as well.  Which one better displays the distributions?

4. To get a better sense of how these distributions compare, create multiple box-plots on a single plot.

 ![](images/box_eda.png)

5. A somewhat more nuanced plot for a similar purpose is a [violin plot](http://en.wikipedia.org/wiki/Violin_plot).  Instead of box-plots, repeat #4 with a violin plot instead.

 ![](images/violin_eda.png)

6. And finally to compare some of the violent crimes, make a violin plot of Murder and Rape.

7. What information does the box-plot more easily provide us?  And which aspects of the distributions does the violin plot better communicate?

### Explanatory Data Viz

Now that we have a sense for the _shape_ of our data and have determined the relationships we want to display we can start sketching with visual representations.  One of the steps to becoming data-viz literate is to develop a **visual vocabulary**.  How we represent abstract concepts/data with visual representations is often a function of:
* Data Types
* Visual Encodings

Think of the **visual encodings** as our parts of speech in constructing a coherent data narrative.  Given that our states are categorical data, and our rates are continuous, what is the best chart type to represent this data?

**For these explanatory plots we will use Bokeh as it has many more interactive and advanced features**

8. Create a bar chart of the aggregate (total) crime rates of each state.


9. Create a [stacked bar chart](http://bokeh.pydata.org/en/latest/docs/gallery/stacked_bar_chart.html) (with hover tooltips) to convey the total crime rate of each state without hiding the individual breakdown of crime type.

 __[here](http://bokeh.pydata.org/en/latest/docs/gallery/unemployment.html) is an example of hover tooltips__

 ![](images/sorted_stacked_bar.png)

10. To better communicate the breakdown per state, transform the data to normalize each state's data to give a percentage.  This will make all of the bars the full width of the plot.

 ![](images/normed_bar.png)

  ### Maps!

  The data we have been working with is inherently geographic.  To get a better sense of it, lets plot it on a map! There are some very powerful (and quite easy to use) mapping specific tools like [CartoDB](https://cartodb.com/) and [Mapbox](https://www.mapbox.com/) but for this portion of the exercise we will stay with Bokeh.

  Bokeh comes with sample [data](http://bokeh.pydata.org/en/latest/docs/gallery/choropleth.html) to plot a map of the US states conveniently.  Use the sample code below to get a basic map.

  ```
  from bokeh.sampledata import us_states
  from bokeh.plotting import *

  us_states = us_states.data.copy()

  del us_states["HI"]
  del us_states["AK"]

  state_xs = [us_states[code]["lons"] for code in us_states]
  state_ys = [us_states[code]["lats"] for code in us_states]

  p = figure(title="State Crime Rates", toolbar_location="left",
  plot_width=1100, plot_height=700)

  p.patches(state_xs, state_ys, fill_alpha=0.0,
  line_color="#884444", line_width=2)

  show(p)
  ```

  For now we will just plot a single crime as a choropleth map of the states.  To create a crime map where each state is colored according to the rate of `Larceny Theft` there are a few steps we need to take:
  * Draw the state borders
  * Figure out the correct color mapping from (rate => hexadecimal value)
  * Put it all together with original source data
  * Add hover tooltip interaction

  We have already seen the first step here in the sample code above on how to draw the state borders.  Now we need to calculate the correct color to fill each state with based on the rate of `Larceny Theft` in that state.

1. Using `matplotlib`s [color maps](http://matplotlib.org/examples/color/colormaps_reference.html), get a new cmap and create a [ScalarMappable](http://matplotlib.org/api/cm_api.html#matplotlib.cm.ScalarMappable) color scale.
 
 This is an object that can take a continuous value in an input domain and give the appropriate color value from the output range in return.

2. A quirk of our dataset is that it uses the full state name rather than the abbreviation (which is how Bokeh stores its State borders).  Using the [us](https://pypi.python.org/pypi/us) python library, iterate through the state names from the Bokeh data loading function (`us_states.data.copy()`) and transform them into the full long name (WA => Washington).

3. Now that we have the names mapped correctly, we can build our array of colors to plug into our Bokeh plotting function.  Iterate through the state names again and this time lookup the rate of `Larceny Theft` for each state and store these values in a list.

4. Using the ScalarMappable's `to_rgb()` method on all of the states' Larceny rates convert the larceny rate into an rgb value.

5. These returned values are actually normalized from 0 -> 1 however and we want them in the range 0 -> 255 to properly convert them into hex.  Transform these rgb values now. __note: the 4th value corresponds to the alpha channel, we do not need this so we can discard it__

5. For the Bokeh map to show correctly we now need to go from `rgb` to hex.  You can do that quite simply in Python with this snippet of code: `'#%02x%02x%02x' % (r, g, b)`

6. Now that we have a proper list of hex values we can finally draw our map!  Putting all the pieces together draw the choropleth map of `Larceny Theft` rates.  This example is a good reference for how the pieces fit together: [http://bokeh.pydata.org/en/latest/docs/gallery/choropleth.html](http://bokeh.pydata.org/en/latest/docs/gallery/choropleth.html)

 ![](images/state_crime_rates.png)

 The last bit is to enable the hover interaction with the state name and crime rate in the tooltip. Before we can customize the tooltip hover, we need to add the source data to the map.

7. Create a `ColumnDataSource` to attach to our map to store the State Name and the Larceny rate.

8. Using the [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#hover-tool) and [examples](http://bokeh.pydata.org/en/latest/docs/gallery/texas.html), add a custom tooltip that has the State name and crime rate.

## Extra Credit

Recreate the bar chart with D3.js and add interactivity to it.

[viz-ani]: images/crime-map.png
[mongoose]: http://cesanta.com/mongoose.shtml
[sublime]: http://www.sublimetext.com/2
[chrome]: https://www.google.com/chrome/browser/desktop/
[zip]: https://github.com/Jay-Oh-eN/strata-interactive-data-viz/archive/master.zip
[gitit]: http://jlord.us/git-it/
[mongoose-config]: images/mongoose-config.png

[grayarea]: http://grayarea.org/
[swiss]: http://www.swissnexsanfrancisco.org/
[lift]: http://liftconference.com/lift15
[data-canvas-img]: images/data-canvas.png
[data-canvas]: http://datacanvas.org/
[data-canvas-map]: http://map.datacanvas.org/
[dump]: https://s3.amazonaws.com/localdata-export/datacanvas/full.zip
[data-canvas-data]: http://map.datacanvas.org/#!/data

[d3]: http://d3js.org/
[dimple]: http://dimplejs.org/
[moment]: http://momentjs.com/
[d3plus]: http://d3plus.org/
[rickshaw]: http://code.shutterstock.com/rickshaw/
[dc.js]: http://dc-js.github.io/dc.js/
[nvd3]: http://nvd3.org/
[c3]: http://c3js.org/
[raw]: http://app.raw.densitydesign.org/
[queue]: https://github.com/mbostock/queue

[crimespotting]: http://sanfrancisco.crimespotting.org/#zoom=13&lon=-122.438&types=AA,Mu,Ro,SA,DP,Na,Al,Pr,Th,VT,Va,Bu,Ar&lat=37.760&hours=0-23&dtend=2014-02-28T23:59:59-07:00&dtstart=2014-02-21T23:59:59-07:00
[crimespotting-screenshot]: images/crimespotting-screenshot.png
[facebook]: http://www.nytimes.com/interactive/2012/05/17/business/dealbook/how-the-facebook-offering-compares.html
[facebook_ipo_nyt]: images/facebook_ipo_nyt.png
[mbta]: http://mbtaviz.github.io/
[mbta-img]: images/mbta-img.png
[guns]: http://guns.periscopic.com/
[guns-img]: images/periscopic.png
[syria]: http://visualizations.manassra.com/syria
[syria-img]: images/syria-img.png
[final-viz]: images/animated_line.png
[viz-ani]: images/viz-ani.gif

[udacity]: https://www.udacity.com/course/ud507
[uw-viz]: http://courses.cs.washington.edu/courses/cse512/14wi/
[murray]: http://chimera.labs.oreilly.com/books/1230000000345
[ritchie]: http://ritchiesking.com/book/
[jscats]: http://jsforcats.com/
[eloquent]: http://eloquentjavascript.net/
[supjs]: http://superherojs.com/
[codeschool]: https://www.codeschool.com/paths/javascript
[barchart]: http://bost.ocks.org/mike/bar/
[d3noob]: http://www.d3noob.org/
[dashing]: https://www.dashingd3js.com/
[showreel]: http://bl.ocks.org/mbostock/1256572
[gallery]: https://github.com/mbostock/d3/wiki/Gallery
[tuts]: https://github.com/mbostock/d3/wiki/Tutorials
[joins]: http://bost.ocks.org/mike/join/
[selections]: http://bost.ocks.org/mike/selection/
[update]: http://bl.ocks.org/mbostock/3808218
[blocksplore]: http://bl.ocksplorer.org/
[transitions]: http://bost.ocks.org/mike/transition/
[zoo]: http://homes.cs.washington.edu/~jheer/files/zoo/
[meetups]: http://d3-js.meetup.com/
[charts]: http://bost.ocks.org/mike/chart/
