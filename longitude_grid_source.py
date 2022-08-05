# ���������
import numpy as np
from vtk.util.numpy_support import numpy_to_vtk
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

# ������, �� ������� ������������ ��������� (���, ����, ���)
lon_step_deg = 10
medirians = np.arange(-180, 180, lon_step_deg)
N_OF_MERIDIANS = medirians.shape[0]

RESOLUTION = 100 # ���������� ����� � ������ ���������� ���������
EARTH_RADIUS_KM = 6372 # ������ ����������� �����, �� + 1 ��

# ���������� ����������
vtkpoints = vtk.vtkPoints()
meridians_steps = np.linspace(-80,80, RESOLUTION) # ��������� ���� ����� � ����� ���������
for idx_mer, lon_deg in enumerate(medirians):
    # ���������� ����� ���������
    lon_rad = radians(lon_deg) # ������ ��������� � ��������
    # ����� ��������� �� �����
    for idx_pt, lat_deg in enumerate(meridians_steps):
        lat_rad = radians(lat_deg) # ������� � ��������
        x = EARTH_RADIUS_KM * cos(lat_rad) * cos(lon_rad)
        y = EARTH_RADIUS_KM * cos(lat_rad) * sin(lon_rad)
        z = EARTH_RADIUS_KM * sin(lat_rad)
        vtkpoints.InsertPoint(idx_mer*RESOLUTION + idx_pt, x,y,z)
output.SetPoints(vtkpoints)
print("vtkpoints = ", vtkpoints)
output.Allocate(N_OF_MERIDIANS, 1)
for idx_mer, lon_deg in enumerate(medirians):
    vtkpolyline = vtk.vtkPolyLine()
    vtkpolyline.GetPointIds().SetNumberOfIds(RESOLUTION)
    for i in range(0,RESOLUTION):
        vtkpolyline.GetPointIds().SetId(i, i + RESOLUTION * idx_mer)
    output.InsertNextCell(vtkpolyline.GetCellType(), vtkpolyline.GetPointIds()) 