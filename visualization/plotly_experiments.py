import plotly.graph_objects as go

# Sample data
years = [2018, 2019, 2020, 2021, 2022]
values = [100, 150, 200, 180, 220]

# Create a line plot
fig = go.Figure()

# Add a scatter trace
scatter_trace = go.Scatter(x=years, y=values, mode='lines+markers', name='Data')
fig.add_trace(scatter_trace)

# Add slider
steps = []
for year in years:
    step = dict(
        method="update",
        args=[{"visible": [False] * len(years)},
              {"title": f"Data for Year {year}"}],
        label=str(year)
    )
    step["args"][0]["visible"][years.index(year)] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Year: "},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    title='Data Over Years',
    xaxis_title='Year',
    yaxis_title='Value'
)

# Show plot
fig.show()
