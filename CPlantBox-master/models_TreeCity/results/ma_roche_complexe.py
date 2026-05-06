# GROUP 
obj1 = Box()

obj1.XLength = 2000
obj1.YLength = 2000
obj1.ZLength = 2000
obj1.Center = [0.,0., -1000]

obj1Display = Show(obj1,renderView1)
obj1Display.Opacity = 0.1
obj1Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()
#
# GROUP 
# GROUP 
obj2 = Cylinder()

obj2.Resolution = 50
obj2.Height = 40
obj2.Radius = 40
obj2.Center = [0., -20,0.]

obj3 = Transform(Input=obj2)
obj3.Transform = 'Transform'
obj3.Transform.Rotate = [90.0, 0.0, 0.0]

obj2Display = Show(obj3,renderView1)
obj2Display.Opacity = 0.2
obj2Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()

Hide(obj3)
obj4= Transform(Input=obj3)
obj4.Transform = 'Transform'
obj4.Transform.Translate = [0,0,-100]
obj4.Transform.Rotate = [0,0,0]

obj4Display = Show(obj4,renderView1)
obj4Display.Opacity = 0.1
obj4Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()
#
obj5 = Cylinder()

obj5.Resolution = 50
obj5.Height = 30
obj5.Radius = 25
obj5.Center = [0., -15,0.]

obj6 = Transform(Input=obj5)
obj6.Transform = 'Transform'
obj6.Transform.Rotate = [90.0, 0.0, 0.0]

obj5Display = Show(obj6,renderView1)
obj5Display.Opacity = 0.2
obj5Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()

Hide(obj6)
obj7= Transform(Input=obj6)
obj7.Transform = 'Transform'
obj7.Transform.Translate = [35,15,-90]
obj7.Transform.Rotate = [0,0,0]

obj7Display = Show(obj7,renderView1)
obj7Display.Opacity = 0.1
obj7Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()
#

obj8= GroupDatasets(Input=[obj4,obj7]) 
obj8Display = Show(obj8, renderView1)
obj8Display.Opacity = 0.1
obj8Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()
#
obj9 = Cylinder()

obj9.Resolution = 50
obj9.Height = 20
obj9.Radius = 30
obj9.Center = [0., -10,0.]

obj10 = Transform(Input=obj9)
obj10.Transform = 'Transform'
obj10.Transform.Rotate = [90.0, 0.0, 0.0]

obj9Display = Show(obj10,renderView1)
obj9Display.Opacity = 0.2
obj9Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()

Hide(obj10)
obj11= Transform(Input=obj10)
obj11.Transform = 'Transform'
obj11.Transform.Translate = [-25,-20,-110]
obj11.Transform.Rotate = [0,0,0]

obj11Display = Show(obj11,renderView1)
obj11Display.Opacity = 0.1
obj11Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()
#

obj12= GroupDatasets(Input=[obj8,obj11]) 
obj12Display = Show(obj12, renderView1)
obj12Display.Opacity = 0.1
obj12Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()
#

obj13= GroupDatasets(Input=[obj1,obj12]) 
obj13Display = Show(obj13, renderView1)
obj13Display.Opacity = 0.1
obj13Display.DiffuseColor = [0., 0., 1.0]
renderView1.ResetCamera()
