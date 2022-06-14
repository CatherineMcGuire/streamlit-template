# A simple model/view template for Streamlit

import streamlit as st


class Model:
    caption = "This is some text"

# View


def view(model):
    st.set_page_config(layout='wide')
    # Header
    st.header(model.header)

    commentaryCol, spaceCol, chartCol = st.columns((2, 1, 6))
    # Description
    with commentaryCol:
        st.write(model.description)
    # Year Slider
    year = st.slider(model.sliderCaption,
                     model.yearStart, model.yearEnd,
                     model.yearStart, model.yearStep)
    # Chart
    with chartCol:
        st.plotly_chart(model.chart(year),
                        use_container_width=True)

# Start


view(Model())




