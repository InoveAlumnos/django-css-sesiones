![Inove banner](inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - Diseño y flujo de aplicación

Al realizar esta tarea pondremos en práctica los conocimientos adquiridos en clase.
Una vez finalizada, el alumno debe subir el enlace a su repositorio "forkeado" el foro de tarea correspondiente -NO SE ADMITE LA DEVOLUCIÓN POR OTRO CANAL SALVO SE ESPECIFIQUE LO CONTRARIO- 

Recuerde que no debe subir la base de datos al sistema, para ello se encuentra el archivo .gitignore que especifica los archivos y directorios omitidos.

--- 
## NOTA: Para todos los ejercicios se debe utilizar el ejemplo_clase como base.

### 1) Realizar la página de detalle de usuario
En esta página se debe reflejar toda la información perteneciente al usuario autenticado, así como ser:

Nombre
Apellido
Username
E-Mail
### 2) Extender la información del usuario
Se debe extender la tabla de usuario para agregar más campos, entre ellos, los solicitados son:
País
Provincia o estado
Ciudad
Código Postal
Teléfono de contacto
Para extender los datos, se puede relacionar una tabla mas con los nuevos datos del usuario, y luego agregar un FK de la tabla "User". Luego, estos datos también deben reflejarse en esta página (No importa si deben agregarse desde el Admin de Django).
### 3) Construir una página para actualizar los datos del usuario.
Construir una página para actualizar los datos del usuario por medio de un formulario y generar un enlace desde la página "user profile" hacia esa página. Al completar el formulario, se debe actualizar el contenido de los datos del usuario y redirigir a la página "user profile"
### 4) Modificar la página "cart".
La página de carrito tiene implementada la lista de comics que el usuario posee en su carrito de compras y un botón de "confirmar pedido", el cual no realiza ninguna acción más que redirigir al usuario a la página de agradecimiento de compra. Incorpore dentro de la lista de comics la capacidad de poder comprar más de un comic de cada uno, incrementando el atributo "wished_qty" de la entidad "WishList". Para evitar el uso de JavaScript, puede implementar un formulario para cada comic con un "input" de tipo numérico y un botón de "agregar" (submit de este formulario). De manera que cuando se agregue la cantidad, se haga un submit del formulario con los datos y se redirija a la página "cart".
### 5) Construir la lógica de la página "cart".
Incorpore la lógica del mecanismo de compra teniendo en cuenta que: - Al realizar el pedido se debe almacenar en algún lugar y de algún modo tanto la lista, como la cantidad de comics y el usuario que realizó. - Se debe pasar a cero el atributo "wished_qty" que el usuario compró. - Se debe pasar el estado del atributo "cart" a "False" para cada comic que el usuario compró.
### 6) Modifique el estilo de la página
Modifique el estilo de la página a gusto. Puede utilizar el método de su preferencia, ya sea con CSS o con Bootstrap o similar.

---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en inove.