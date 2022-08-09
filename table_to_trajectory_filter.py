# the single input table this filter is applied to
table = inputs[0]

# print table properties and metrics just for sure
print("table: ", table)
print("table.GetNumberOfRows() = ", table.GetNumberOfRows())

num_rows = table.GetNumberOfRows()

# usual vtk workflow: fill vtkPoints first
vtkpoints = vtk.vtkPoints()
for i in range(0, num_rows):
    vtkpoints.InsertPoint(i,
        table.GetValue(i,0).ToFloat(), #x column
        table.GetValue(i,1).ToFloat(), #y column
        table.GetValue(i,2).ToFloat()  #z column
        )
output.SetPoints(vtkpoints)

# allocate vtkCell, representing single line
# if more lines, use output.Allocate(N_OF_LINES, 1) 
output.Allocate(1, 1) 

vtkpolyline = vtk.vtkPolyLine()
vtkpolyline.GetPointIds().SetNumberOfIds(num_rows)
# enumerate points to include in polyline
for i in range(0,num_rows):
    vtkpolyline.GetPointIds().SetId(i, i)
# assign vtkPolyLine graphical object to created vtkCell
output.InsertNextCell(vtkpolyline.GetCellType(),
                      vtkpolyline.GetPointIds()) 