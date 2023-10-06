import os
import pandas as pd
import streamlit as st
from streamlit import runtime


# import data_explorer
# import eviction_analysis
# import equity_explorer
# import queries
# import analysis
#import utils
from constants import AFRICAN_COUNTRIES

# Pandas options
pd.options.display.max_rows = 25
pd.options.display.max_columns = 12
pd.options.display.expand_frame_repr = True
pd.options.display.large_repr = 'truncate'
pd.options.display.float_format = '{:.2f}'.format

PAGES = [
    'Trade Deficit',
    'Imports',
    'Exports'
]


def run_UI():
    st.set_page_config(
        page_title="African Countries' Trade Deficit/Surplus over time",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Sidebar
    st.sidebar.title('Select Economic Indicator')
    page = st.sidebar.radio('Go to', PAGES)

    # Main content
    # if page == 'Trade Deficit':
    #     trade_deficit()
    # elif page == 'Imports':
    #     imports()
    # elif page == 'Exports':
    #     exports()

    # if st.session_state.page:
    #     page=st.sidebar.radio('Navigation', PAGES, index=st.session_state.page)
    # else:
    #     page=st.sidebar.radio('Navigation', PAGES, index=1)

    # st.experimental_set_query_params(page=page)


if __name__ == '__main__':
    if not os.path.exists('Output'):
        os.makedirs('Output')
    run_UI()
