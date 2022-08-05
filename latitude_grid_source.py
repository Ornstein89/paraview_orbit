# параллели
import numpy as np
from vtk.util.numpy_support import numpy_to_vtk
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

# широты, на которых отображаются параллели (мин, макс, шаг)
lat_step_deg = 10
parallels = np.arange(-160, 160, lat_step_deg)
N_OF_PARALLELS = parallels.shape[0]

RESOLUTION = 100 # количество точек в каждой окружности широты или долготы
EARTH_RADIUS_KM = 6372 # радиус сферической Земли, км + 1 км

# построение параллелей
vtkpoints = vtk.vtkPoints()
parallels_steps = np.linspace(0,360, RESOLUTION) # градусные меры точек в одной параллели
for idx_par, lat_deg in enumerate(parallels):
    # построение одной параллели
    lat_rad = radians(lat_deg) # широта параллели в радианах
    # набор параллели из точек
    for idx_pt, lon_deg in enumerate(parallels_steps):
        lon_rad = radians(lon_deg) # долгота в радианах
        x = EARTH_RADIUS_KM * cos(lat_rad) * cos(lon_rad)
        y = EARTH_RADIUS_KM * cos(lat_rad) * sin(lon_rad)
        z = EARTH_RADIUS_KM * sin(lat_rad)
        vtkpoints.InsertPoint(idx_par*RESOLUTION + idx_pt, x,y,z)
output.SetPoints(vtkpoints)
print("vtkpoints = ", vtkpoints)
output.Allocate(N_OF_PARALLELS, 1)
for idx_par, lat_deg in enumerate(parallels):
    vtkpolyline = vtk.vtkPolyLine()
    vtkpolyline.GetPointIds().SetNumberOfIds(RESOLUTION)
    for i in range(0,RESOLUTION):
        vtkpolyline.GetPointIds().SetId(i, i + RESOLUTION * idx_par)
    output.InsertNextCell(vtkpolyline.GetCellType(), vtkpolyline.GetPointIds()) 