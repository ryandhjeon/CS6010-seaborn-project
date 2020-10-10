import pandas as pd

from bokeh.layouts import column, row
from bokeh.models import Select
from bokeh.palettes import Spectral5
from bokeh.plotting import curdoc, figure

df = pd.read_csv("../data/raw/forestfires.csv")

month_int_season = {
    'jan' : [1, "winter"],
    'feb' : [2, "winter"],
    'mar' : [3, "spring"],
    'apr' : [4, "spring"],
    'may' : [5, "spring"],
    'jun' : [6, "summer"],
    'jul' : [7, "summer"],
    'aug' : [8, "summer"],
    'sep' : [9, "summer"],
    'oct' : [10, "fall"],
    'nov' : [11, "fall"],
    'dec' : [12, "winter"]
}

df["month_int_season"] = df['month'].map(month_int_season) 
df[['month_int','season']] = pd.DataFrame(df.month_int_season.to_list())

df = df.sort_values(['month_int']).reset_index(drop=True)

SIZES = list(range(6, 22, 3))
COLORS = Spectral5
N_SIZES = len(SIZES)
N_COLORS = len(COLORS)

# convert X and Y to strings
df.X = df.X.astype(str)
df.Y = df.Y.astype(str)

columns = sorted(df.columns)
discrete = [x for x in columns if df[x].dtype == object]
continuous = [x for x in columns if x not in discrete]

def create_figure():
    xs = df[x.value].values
    ys = df[y.value].values
    x_title = x.value.title()
    y_title = y.value.title()

    kw = dict()
    if x.value in discrete:
        kw['x_range'] = sorted(set(xs))
    if y.value in discrete:
        kw['y_range'] = sorted(set(ys))
    kw['title'] = "%s vs %s" % (x_title, y_title)

    p = figure(plot_height=600, plot_width=800, tools='pan,box_zoom,hover,reset', **kw)
    p.xaxis.axis_label = x_title
    p.yaxis.axis_label = y_title

    if x.value in discrete:
        p.xaxis.major_label_orientation = pd.np.pi / 4

    sz = 9
    if size.value != 'None':
        if len(set(df[size.value])) > N_SIZES:
            groups = pd.qcut(df[size.value].values, N_SIZES, duplicates='drop')
        else:
            groups = pd.Categorical(df[size.value])
        sz = [SIZES[xx] for xx in groups.codes]

    c = "#31AADE"
    if color.value != 'None':
        if len(set(df[color.value])) > N_COLORS:
            groups = pd.qcut(df[color.value].values, N_COLORS, duplicates='drop')
        else:
            groups = pd.Categorical(df[color.value])
        c = [COLORS[xx] for xx in groups.codes]

    p.circle(x=xs, y=ys, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)

    return p


def update(attr, old, new):
    layout.children[1] = create_figure()


x = Select(title='X-Axis', value='area', options=columns)
x.on_change('value', update)

y = Select(title='Y-Axis', value='wind', options=columns)
y.on_change('value', update)

size = Select(title='Size', value='None', options=['None'] + continuous)
size.on_change('value', update)

color = Select(title='Color', value='None', options=['None'] + continuous)
color.on_change('value', update)

controls = row(x, y, color, size, width=800)
layout = column(controls, create_figure())

curdoc().add_root(layout)
curdoc().title = "Compare two variables"