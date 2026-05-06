# GROUP 
obj1 = Box()

obj1.XLength = 2000
obj1.YLength = 2000
obj1.ZLength = 2000
obj1.Center = [0.,0., -1000]

obj1Display = Show(obj1,GetActiveView())
obj1Display.Opacity = 0.1
obj1Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#
obj2 = Cylinder()

obj2.Resolution = 50
obj2.Height = 5
obj2.Radius = 10
obj2.Center = [0., -2.5,0.]

obj3 = Transform(Input=obj2)
obj3.Transform = 'Transform'
obj3.Transform.Rotate = [90.0, 0.0, 0.0]

obj2Display = Show(obj3,GetActiveView())
obj2Display.Opacity = 0.2
obj2Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj3)
obj4= Transform(Input=obj3)
obj4.Transform = 'Transform'
obj4.Transform.Translate = [0,0,-250]
obj4.Transform.Rotate = [0,0,0]

obj4Display = Show(obj4,GetActiveView())
obj4Display.Opacity = 0.1
obj4Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#

obj5= GroupDatasets(Input=[obj1,obj4]) 
obj5Display = Show(obj5, GetActiveView())
obj5Display.Opacity = 0.1
obj5Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
