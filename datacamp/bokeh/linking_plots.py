from bokeh.io import output_file, show
import pandas as pd
from bokeh.models import ColumnDataSource

from bokeh.layouts import gridplot, row
from bokeh.plotting import figure

p1 = figure()
p2 = figure()
p3 = figure()
p4 = figure()

# Link the x_range of p2 to p1: p2.x_range
p2.x_range = p1.x_range

# Link the y_range of p2 to p1: p2.y_range
p2.y_range = p1.y_range

# Link the x_range of p3 to p1: p3.x_range
p3.x_range = p1.x_range

# Link the y_range of p4 to p1: p4.y_range
p4.y_range = p1.y_range

layout = gridplot([row([p1, p2]), row([p3, p4])])

# Specify the name of the output_file and show the result
output_file('linked_range.html')
show(layout)

data = pd.DataFrame()

# Create ColumnDataSource: source
source = ColumnDataSource(data)

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select')

# Add a circle glyph to p1
p1.circle('fertility','female literacy',source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            tools='box_select,lasso_select')

# Add a circle glyph to p2
p2.circle('fertility','population',source=source)

# Create row layout of figures p1 and p2: layout
layout = row([p1,p2])

# Specify the name of the output_file and show the result
output_file('linked_brush.html')
show(layout)