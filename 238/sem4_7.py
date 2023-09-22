func = lambda x, y: lambda z: x + y + z
func(1, 2)(3)

increaser4 = (lambda x: lambda y: x + y)(4)
print(increaser4(3))