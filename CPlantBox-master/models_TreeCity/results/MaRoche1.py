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

Hide(obj2)
obj3= Transform(Input=obj2)
obj3.Transform = 'Transform'
obj3.Transform.Translate = [0,0,-100]
obj3.Transform.Rotate = [0,0,0]

obj3Display = Show(obj3,GetActiveView())
obj3Display.Opacity = 0.1
obj3Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#
obj4 = Cylinder()

obj4.Resolution = 50
obj4.Height = 30
obj4.Radius = 25
obj4.Center = [0., -15,0.]

obj5 = Transform(Input=obj4)
obj5.Transform = 'Transform'
obj5.Transform.Rotate = [90.0, 0.0, 0.0]

obj4Display = Show(obj5,GetActiveView())
obj4Display.Opacity = 0.2
obj4Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj5)
obj6= Transform(Input=obj5)
obj6.Transform = 'Transform'
obj6.Transform.Translate = [35,15,-90]
obj6.Transform.Rotate = [0,0,0]

obj6Display = Show(obj6,GetActiveView())
obj6Display.Opacity = 0.1
obj6Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#

obj7= GroupDatasets(Input=[obj3,obj6]) 
obj7Display = Show(obj7, GetActiveView())
obj7Display.Opacity = 0.1
obj7Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#
obj8 = Cylinder()

obj8.Resolution = 50
obj8.Height = 20
obj8.Radius = 30
obj8.Center = [0., -10,0.]

obj9 = Transform(Input=obj8)
obj9.Transform = 'Transform'
obj9.Transform.Rotate = [90.0, 0.0, 0.0]

obj8Display = Show(obj9,GetActiveView())
obj8Display.Opacity = 0.2
obj8Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj9)
obj10= Transform(Input=obj9)
obj10.Transform = 'Transform'
obj10.Transform.Translate = [-25,-20,-110]
obj10.Transform.Rotate = [0,0,0]

obj10Display = Show(obj10,GetActiveView())
obj10Display.Opacity = 0.1
obj10Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
#

obj11= GroupDatasets(Input=[obj7,obj10]) 
obj11Display = Show(obj11, GetActiveView())
obj11Display.Opacity = 0.1
obj11Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()

Hide(obj11)
obj12= Transform(Input=obj11)
obj12.Transform = 'Transform'
obj12.Transform.Translate = [0,0,0]
obj12.Transform.Rotate = [50,0,0]

obj12Display = Show(obj12,GetActiveView())
obj12Display.Opacity = 0.1
obj12Display.DiffuseColor = [0., 0., 1.0]
GetActiveView().ResetCamera()
