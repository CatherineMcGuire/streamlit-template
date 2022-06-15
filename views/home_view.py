import streamlit as st


def home_view(model):
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