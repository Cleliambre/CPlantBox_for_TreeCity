# GROUP 
# GROUP 
obj1 = Cylinder()

obj1.Resolution = 50
obj1.Height = 40
obj1.Radius = 40
obj1.Center = [0., -20,0.]

obj2 = Transform(Input=obj1)
obj2.Transform = 'Transform'
obj2.Transform.Rotate = [90.0, 0.0, 0.0]

obj1Display = Show(obj2,GetActiveView())
obj1Display.Opacity = 0.2
obj1Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#
obj3 = Cylinder()

obj3.Resolution = 50
obj3.Height = 30
obj3.Radius = 25
obj3.Center = [0., -15,0.]

obj4 = Transform(Input=obj3)
obj4.Transform = 'Transform'
obj4.Transform.Rotate = [90.0, 0.0, 0.0]

obj3Display = Show(obj4,GetActiveView())
obj3Display.Opacity = 0.2
obj3Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj4)
obj5= Transform(Input=obj4)
obj5.Transform = 'Transform'
obj5.Transform.Translate = [35,15,10]
obj5.Transform.Rotate = [0,0,0]

obj5Display = Show(obj5,GetActiveView())
obj5Display.Opacity = 0.1
obj5Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#

obj6= GroupDatasets(Input=[obj2,obj5]) 
obj6Display = Show(obj6, GetActiveView())
obj6Display.Opacity = 0.1
obj6Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#
obj7 = Cylinder()

obj7.Resolution = 50
obj7.Height = 20
obj7.Radius = 30
obj7.Center = [0., -10,0.]

obj8 = Transform(Input=obj7)
obj8.Transform = 'Transform'
obj8.Transform.Rotate = [90.0, 0.0, 0.0]

obj7Display = Show(obj8,GetActiveView())
obj7Display.Opacity = 0.2
obj7Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj8)
obj9= Transform(Input=obj8)
obj9.Transform = 'Transform'
obj9.Transform.Translate = [-25,-20,-10]
obj9.Transform.Rotate = [0,0,0]

obj9Display = Show(obj9,GetActiveView())
obj9Display.Opacity = 0.1
obj9Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#

obj10= GroupDatasets(Input=[obj6,obj9]) 
obj10Display = Show(obj10, GetActiveView())
obj10Display.Opacity = 0.1
obj10Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj10)
obj11= Transform(Input=obj10)
obj11.Transform = 'Transform'
obj11.Transform.Translate = [0,0,-100]
obj11.Transform.Rotate = [-50,0,0]

obj11Display = Show(obj11,GetActiveView())
obj11Display.Opacity = 0.1
obj11Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
