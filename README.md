# Proyecto_Integrador-
En esta práctica trabajé con la librería Flet para crear una aplicación gráfica usando Python. La idea principal fue simular un sistema de registro de estudiantes parecido a los que se utilizan en escuelas o plataformas de inscripción. En lugar de usar la consola, todo se realiza mediante una interfaz visual con cajas de texto, listas desplegables, botones y mensajes emergentes.

Lo que más me ayudó de Flet es que permite construir interfaces modernas de manera muy sencilla, sin tener que aprender tecnologías web. Todo se programa directamente con objetos de Python, lo cual hace el desarrollo más intuitivo.
Ejemplo de como se debia ver el resultado final : 

<img width="252" height="239" alt="image" src="https://github.com/user-attachments/assets/49e0c210-4f2c-4b1c-a6a1-fd0567d341bb" />

**1. Importar librerías**
Como al inicio de la mayoría de los códigos que hemos realizado con flet necesitamos impirtarlo , así como también es la parte perfecta para importar las demás librerías que en este caso sera re que nos ayudara a la hora de validar el correo. Si llegará a no importarla no podria verificar correctamente este campo. 

```python
import flet as ft
import re
```
**2. Main**
Creamos la función principal llamada __main__ en esta se colocara todo el codigo y nos va a ayudar al momento de ejecutar el programa. Así mismo dentro de esta colocamos ft.page ya que nos permite mostrar nuestros componentes en pantalla.
   ```python
def main(page: ft.Page):
```
**3. Page**
Luego configurarmos la pantalla, modificaremos el titulo, el color, el borde , si es modo oscuro o no.
- __title__ :Cambia el nombre que aparece en la barra superior de la ventana.
- __bgColor__ : Define el color de fondo usando código hexadecimal.
Elegí un tono claro para que el formulario se vea más limpio.
- __padding__ :Agrega espacio interior para que los controles no queden pegados a los bordes.
Hace que el diseño se vea más profesional.
- __theme_mode__ :Activa el modo claro (LIGHT).
También podría usar modo oscuro.

 ```python
page.title = "Registro de Estudiantes - Tap"
page.bgcolor = "#F5F3E0"
page.padding = 30
page.theme_mode = ft.ThemeMode.LIGHT
```
**4. Ventana del mensaje**
Creación de la ventana emergente, en esta ventana mostraremos los adatos que el usiario alla registrado, además tendrá la opción de cerrar el mensaje.
- __open = False__ → oculta el diálogo

- __page.update()__ → refresca la pantalla
Si no actualizo la página, el cambio no se vería.

 ```python
def cerrar_dialogo(e):
    dlg_resumen.open = False
    page.update()
```
- Este componente:
 + muestra un mensaje cuando el registro es exitos
 + enseña todos los datos capturados
Es como una confirmación final.

Lo usé para que el usuario revise su información antes de cerrar. 

```python
dlg_resumen = ft.AlertDialog(...)
```
**5. Construcción de los campos de entrada de datos**
   
Luego construí todos los controles donde el usuario captura la información. Todos estos elementos forman el cuerpo principal del formulario.

Primero agregué campos de texto simples para el nombre y el correo electrónico, donde el usuario puede escribir libremente.

Para el número de control añadí una restricción especial que solo permite números. Esto evita que el usuario escriba letras o símbolos, previniendo errores desde el momento de la captura.

Después utilicé listas desplegables para la carrera y el semestre. Decidí usar este tipo de controles porque obligan al usuario a seleccionar opciones predefinidas, lo que evita inconsistencias en los datos. Por ejemplo, no habría diferentes formas de escribir la misma carrera.

Para el semestre generé los números automáticamente con un ciclo, lo que hace el código más corto y fácil de modificar.

```python
txt_nombre = ft.TextField(...)
input_filter=ft.NumbersOnlyInputFilter()
txt_email = ft.TextField(...)
[str(i) for i in range(1, 10)]

```
**6. Creación del boton encargado de la selcción del genero.**
Son botones tipo selección única.

Solo se puede elegir uno.

```python

  rg_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino", fill_color="#70EB0B"),
            ft.Radio(value="Femenino", label="Femenino", fill_color="#70EB0B"),
            ft.Radio(value="Otro", label="Otro", fill_color="#70EB0B"),
        ])
    )

    txt_error_genero = ft.Text("", color="red", size=12)
```
**7. Validación de datos y lógica del formulario**

La parte más importante del programa es la validación, ya que aquí se asegura que la información ingresada sea correcta antes de enviarla.

Creé una función que se ejecuta cuando se presiona el botón “Enviar”. Esta función revisa todos los campos.

Primero verifica que ninguno esté vacío. Si detecta un campo sin información, cambia su borde a rojo y muestra un mensaje indicando que es obligatorio. Esto ayuda al usuario a identificar rápidamente qué le falta completar.

Después valida específicamente el correo electrónico usando la expresión regular, comprobando que tenga un formato válido con “@” y dominio.

También verifica que el usuario haya seleccionado el género. Si no lo hizo, aparece un mensaje de advertencia.

Si existe cualquier error, el envío se detiene. Solo cuando todos los datos son correctos se continúa con el siguiente paso.

Cuando todo está validado, el programa construye un resumen con la información capturada y lo muestra dentro del cuadro de diálogo. Así el usuario puede confirmar sus datos.

Esta sección es básicamente el “cerebro” del sistema, porque controla toda la lógica de funcionamiento.

```python
# Función para validar formato de email
    def es_email_valido(email):
        # Verifica que contenga @ y un dominio
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    # Validación
    def validar_y_enviar(e):
        campos = [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]
        hay_error = False

        # 1. Validar campos vacíos
        for campo in campos:
            if not campo.value or campo.value.strip() == "":
                campo.error_text = "Este campo es obligatorio"
                campo.border_color = "red"
                hay_error = True
            else:
                campo.error_text = None
                campo.border_color = "#1B1C24"

        # 2. Validar específicamente el Email (que tenga @)
        if not hay_error: # Solo si no está vacío
            if not es_email_valido(txt_email.value):
                txt_email.error_text = "Introduce un correo válido (debe incluir '@' y '.com')"
                txt_email.border_color = "red"
                hay_error = True

        # 3. Verificar el género
        if not rg_genero.value:
            txt_error_genero.value = "Debes seleccionar un género"
            hay_error = True
        else:
            txt_error_genero.value = ""

        # Si todo está correcto
        if not hay_error:
            resumen_texto = (
                f"Nombre completo: {txt_nombre.value}\n"
                f"Número de control: {txt_control.value}\n"
                f"Correo electrónico: {txt_email.value}\n"
                f"Carrera elegida: {dd_carrera.value}\n"
                f"Semestre actual: {dd_semestre.value}\n"
                f"Género : {rg_genero.value}"
            )
            
            dlg_resumen.content = ft.Text(resumen_texto)
            dlg_resumen.open = True
            if dlg_resumen not in page.overlay:
                page.overlay.append(dlg_resumen)
        
        page.update()
```

**8- Organización visual y botón de envío**

Para finalizar, organicé todos los elementos en la pantalla. Utilicé columnas para acomodar los controles verticalmente y filas para colocar algunos elementos uno al lado del otro, como carrera y semestre.

También agregué espacios para que la interfaz no se vea saturada.

Después coloqué el botón “Enviar”, que es el encargado de activar la función de validación. Es el elemento con el que el usuario interactúa para procesar el formulario.

   ```python
# --- 5. CONSTRUCCIÓN DE LA INTERFAZ ---
    page.add(
        ft.Column([
            ft.Text("Formulario de Registro", size=24, weight="bold", color="#4D2A32"),
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([
                dd_carrera,
                dd_semestre
            ], spacing=10),
            ft.Column([
                ft.Text("Género:", color="#4D2A32", weight="bold"),
                rg_genero,
                txt_error_genero
            ], spacing=5),
            ft.Divider(height=20, color="transparent"),
            btn_enviar
        ], spacing=15)
    )

```
**9. Ejecución**
Por último, agregué la instrucción que inicia la aplicación. Esta línea le indica a Flet que ejecute la función principal y muestre la ventana. Sin esta parte el programa no arrancaría.

```python
if __name__ == "__main__":
    ft.app(target=main)
```


#  Codigo completo 
```python
import flet as ft
import re  # Importamos para validar el email

def main(page: ft.Page):
    # --- CONFIGURACIÓN DE LA PÁGINA ---
    page.title = "Registro de Estudiantes - Tap"
    page.bgcolor = "#F5F3E0"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    def cerrar_dialogo(e):
        dlg_resumen.open = False
        page.update()

    dlg_resumen = ft.AlertDialog(
        title=ft.Text("Registro exitoso!!"),
        content=ft.Text(""),
        actions=[
            ft.TextButton("Cerrar", on_click=cerrar_dialogo),
        ],
    )

    # --- 2. CONTROLES DE ENTRADA (Inputs) ---
    txt_nombre = ft.TextField(label="Nombre", border_color="#1B1C24", expand=True)
    
    # Restringir a solo números usando input_filter
    txt_control = ft.TextField(
        label="Número de control", 
        border_color="#1B1C24", 
        expand=True,
        input_filter=ft.NumbersOnlyInputFilter() # Bloquea letras y símbolos mientras escribes
    )
    
    txt_email = ft.TextField(label="Email", border_color="#1B1C24", expand=True)

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#1B1C24",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
            ft.dropdown.Option("Ingeniería Mecatronica"),
            ft.dropdown.Option("Ingeniería en Gestión Empresarial "),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#1B1C24",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 10)]
    )

    rg_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino", fill_color="#70EB0B"),
            ft.Radio(value="Femenino", label="Femenino", fill_color="#70EB0B"),
            ft.Radio(value="Otro", label="Otro", fill_color="#70EB0B"),
        ])
    )

    txt_error_genero = ft.Text("", color="red", size=12)

    # Función para validar formato de email
    def es_email_valido(email):
        # Verifica que contenga @ y un dominio
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    # Validación
    def validar_y_enviar(e):
        campos = [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]
        hay_error = False

        # 1. Validar campos vacíos
        for campo in campos:
            if not campo.value or campo.value.strip() == "":
                campo.error_text = "Este campo es obligatorio"
                campo.border_color = "red"
                hay_error = True
            else:
                campo.error_text = None
                campo.border_color = "#1B1C24"

        # 2. Validar específicamente el Email (que tenga @)
        if not hay_error: # Solo si no está vacío
            if not es_email_valido(txt_email.value):
                txt_email.error_text = "Introduce un correo válido (debe incluir '@' y '.com')"
                txt_email.border_color = "red"
                hay_error = True

        # 3. Verificar el género
        if not rg_genero.value:
            txt_error_genero.value = "Debes seleccionar un género"
            hay_error = True
        else:
            txt_error_genero.value = ""

        # Si todo está correcto
        if not hay_error:
            resumen_texto = (
                f"Nombre completo: {txt_nombre.value}\n"
                f"Número de control: {txt_control.value}\n"
                f"Correo electrónico: {txt_email.value}\n"
                f"Carrera elegida: {dd_carrera.value}\n"
                f"Semestre actual: {dd_semestre.value}\n"
                f"Género : {rg_genero.value}"
            )
            
            dlg_resumen.content = ft.Text(resumen_texto)
            dlg_resumen.open = True
            if dlg_resumen not in page.overlay:
                page.overlay.append(dlg_resumen)
        
        page.update()

    # --- 4. BOTÓN DE ENVÍO ---
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="white", size=16),
        bgcolor="#4D2A32",
        width=page.width,
        on_click=validar_y_enviar
    )

    # --- 5. CONSTRUCCIÓN DE LA INTERFAZ ---
    page.add(
        ft.Column([
            ft.Text("Formulario de Registro", size=24, weight="bold", color="#4D2A32"),
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([
                dd_carrera,
                dd_semestre
            ], spacing=10),
            ft.Column([
                ft.Text("Género:", color="#4D2A32", weight="bold"),
                rg_genero,
                txt_error_genero
            ], spacing=5),
            ft.Divider(height=20, color="transparent"),
            btn_enviar
        ], spacing=15)
    )

if __name__ == "__main__":
    ft.app(target=main)
```
# Capturas del codigo 

<img width="247" height="263" alt="image" src="https://github.com/user-attachments/assets/d4cebbd1-d17b-4383-8089-09fcd32483d8" />

<img width="246" height="280" alt="image" src="https://github.com/user-attachments/assets/fb8b79c2-c9e8-41ba-a122-b7bfa9812d75" />

<img width="246" height="211" alt="image" src="https://github.com/user-attachments/assets/11b5178c-e108-466e-af36-9bd899c9278e" />

<img width="247" height="270" alt="image" src="https://github.com/user-attachments/assets/3a5866a5-1b3a-4a98-ab9e-abf23186e1bc" />



