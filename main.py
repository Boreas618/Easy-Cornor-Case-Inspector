from services.area import CutLine, OneLineDividedArea, TwoLinesDividedArea, ClosedArea
from services.preprocessing import interpolation, slope
from services.kmeans import find_outliers
from utils.data_utils import load_data, filter_trajectory
from fastapi import FastAPI

app = FastAPI()

# define the areas
area_a = OneLineDividedArea([CutLine([-100, -210], [-60, -230])], 1)
area_b = TwoLinesDividedArea([CutLine([-60, -120], [-21, -142]), CutLine([-100, -210], [-60, -230])], 2)
area_c = ClosedArea(
    [CutLine([15, -100], [-50, -60]), CutLine([-80, -120], [-20, -160]), CutLine([-50, -60], [-20, -160]),
     CutLine([15, -100], [-80, -120])], 3)

data = load_data()


def filter_by_area_and_length(area_id: int, length_lower_bound: int = 5, length_upper_bound: int = 10):
    filtered_trajectories = None
    if area_id == 1:
        filtered_trajectories = filter_trajectory(data, area_a.is_in_area, length_lower_bound, length_upper_bound)
    elif area_id == 2:
        filtered_trajectories = filter_trajectory(data, area_b.is_in_area, length_lower_bound, length_upper_bound)
    elif area_id == 3:
        filtered_trajectories = filter_trajectory(data, area_c.is_in_area, length_lower_bound, length_upper_bound)
    return filtered_trajectories


@app.get("/outliers/")
def get_outliers(area_id: int, length_lower_bound: int = 5, length_upper_bound: int = 10, cluster: int = 10,
                 outlier_threshold: float = 0.05):
    filtered_trajectories = filter_by_area_and_length(area_id, length_lower_bound, length_upper_bound)
    interpolation(filtered_trajectories, length_upper_bound + 1)
    slopes = slope(filtered_trajectories, length_upper_bound)
    outliers = find_outliers(slopes, cluster, outlier_threshold)
    return outliers
