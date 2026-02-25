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