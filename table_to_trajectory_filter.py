print("inputs = ", inputs[0])
table = inputs[0]
print("table.GetNumberOfRows() = ", table.GetNumberOfRows())
num_points = table.GetNumberOfRows()
#print("table.GetValue() = ",table.GetValue(0,0))
vtkpoints = vtk.vtkPoints()
for i in range(0,num_points):
    vtkpoints.InsertPoint(i,
        table.GetValue(i,0).ToFloat(),
        table.GetValue(i,1).ToFloat(),
        table.GetValue(i,2).ToFloat())

#print("GetNumberOfPoints = ", )
output.SetPoints(vtkpoints) 
output.Allocate(1, 1)
vtkpolyline = vtk.vtkPolyLine()
vtkpolyline.GetPointIds().SetNumberOfIds(num_points)
for i in range(0,num_points):
    vtkpolyline.GetPointIds().SetId(i, i)
output.InsertNextCell(vtkpolyline.GetCellType(), vtkpolyline.GetPointIds()) 