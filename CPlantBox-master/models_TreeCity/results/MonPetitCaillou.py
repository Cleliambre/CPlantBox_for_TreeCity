obj1 = Cylinder()

obj1.Resolution = 50
obj1.Height = 5
obj1.Radius = 10
obj1.Center = [0., -2.5,0.]

obj2 = Transform(Input=obj1)
obj2.Transform = 'Transform'
obj2.Transform.Rotate = [90.0, 0.0, 0.0]

obj1Display = Show(obj2,GetActiveView())
obj1Display.Opacity = 0.2
obj1Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj2)
obj3= Transform(Input=obj2)
obj3.Transform = 'Transform'
obj3.Transform.Translate = [0,0,-125]
obj3.Transform.Rotate = [0,0,0]

obj3Display = Show(obj3,GetActiveView())
obj3Display.Opacity = 0.1
obj3Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
