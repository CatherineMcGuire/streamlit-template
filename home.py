# A simple model/view template for Streamlit

import streamlit as st
import pandas as pd
import plotly.express as px


class Model:
    def __init__(self):
        self.df = pd.DataFrame(px.data.gapminder())
        self.ylist = [int(i) for i in self.df['year'].unique()]
        self.yearStart = self.ylist[0]
        self.yearEnd = self.ylist[-1]
        self.yearStep = self.ylist[1] - self.ylist[0]

    def chart(self, year):
        return px.scatter(self.df[self.df['year'] == year],
                          x='lifeExp', y='gdpPercap',
                          title=f'Year: {year}',
                          color='continent', size='pop')

    header = 'Global Statistics from Gapminder'

    description = '''
      See how life expectancy changes over time 
      and in relation to GDP.
      Move the slider to change the year to display.
   '''
    sliderCaption = 'Select the year for the chart'

# View


def view(model):
    st.set_page_config(layout='wide')
    # Header
    st.header(model.header)

    commentary_col, space_col, chart_col = st.columns((2, 1, 6))
    # Description
    with commentary_col:
        st.write(model.description)

    # Year Slider
        year = st.slider(model.sliderCaption,
                         model.yearStart, model.yearEnd,
                         model.yearStart, model.yearStep)
    # Chart
    with chart_col:
        st.plotly_chart(model.chart(year),
                        use_container_width=True)

# Start


view(Model())




