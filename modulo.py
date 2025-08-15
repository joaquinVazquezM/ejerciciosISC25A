estudiantes = 85
cupoAutobus = 12

busNecesario = estudiantes // cupoAutobus
print(f"El número de autobuses necesarios son: {busNecesario}")

restante = estudiantes % cupoAutobus
print(f"Los alumnos que sobran son: {restante}")