from get_data import main as get_data_from_remote
from weather_analysis import main as weather_analysis


file_path = get_data_from_remote()
weather_analysis(file_path)
