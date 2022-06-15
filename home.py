# A simple model/view template for Streamlit

from views.home_view import home_view
from models.home_model import HomeModel


home_view(HomeModel())




