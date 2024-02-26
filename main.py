#info_usuario
nombre = input ("Ingrese su(s) nombre(s): ")
apellidos = input ("Ingrese sus apellidos: ")
edad = input ("Ingrese su edad: ")
altura = input ("Ingrese su altura en metros: ")
info = tuple ((nombre, apellidos, edad, altura))
print (f"El/La usuario/a {info[0]} {info[1]} tiene {info[2]} y mide {info[3]}")

#direcciones
d_casa = input ("Ingrese su direccion principal (hogar):") 
d_trabajo = input ("Ingrese su direccion laboral (trabajo): ")
dire = tuple ((d_casa, d_trabajo))
print (f"El/La usuario/a {info[0]} {info[1]} vive en {dire[0]} y labora en {dire[1]}")

#educacion
nvl_edu = input ("Ingrese el/los nivel(es) de educacion recibida (preescolar, basica, media o superior): ")
cursos = input ("Ingrese el/los curso(s) que ha realizado: ")
titulos = input ("Ingrese el/los titulo(s) que ha obtenido: ")
edu = tuple ((nvl_edu, cursos, titulos))
print (f"El/La usuario/a {info[0]} {info[1]} recibio educacion {edu[0]}, realizo un/os curso(s) de {edu[1]} y posee un/os titulo(s) como {edu[2]}  ")

#exp_laboral
sn = input ("¿Ha tenido experiencia laboral? (responda si o no): ")
exp_laboral= input ("Ingrese su experiencia laboral: ")
exp = tuple ((sn, exp_laboral))
print (f"El/La usuario/a {info[0]} {info[1]} {exp[0]} ha tenido experiencia laboral como {exp[1]} ")
