# 🧪 PyLogic Lab: Evaluador de Lógica y Condicionales

**PyLogic Lab** es una herramienta educativa e interactiva construida con **Python** y **Streamlit** para explorar, visualizar y comprender en tiempo real la evaluación de expresiones booleanas y estructuras de control de flujo (`if / else`, `and`, `or`, `>=`).

---

## 🌟 Características Principal de la Aplicación

- **🎨 Diseño Visual Moderno (Glassmorphism)**: Estilos desacoplados en `styles.css` con paleta oscura, bordes suaves y fuentes modernas (`Inter` y `Fira Code`).
- **🎯 Escenarios Predefinidos (Presets)**: Permite seleccionar casos comunes en la barra lateral (ej. *Menor con tutor y dinero*, *Adulto sin saldo suficiente*, etc.) para una prueba rápida.
- **🧪 Desglose de Evaluación Paso a Paso**: Visualización clara del flujo booleano con badges brillantes en tiempo real (🟢 `True` / 🔴 `False`).
- **📊 Tabla de Verdad Interactiva**: Matriz de 8 combinaciones posibles que resalta automáticamente la fila del estado actual.
- **💡 Guía de Operadores**: Explicaciones claras sobre el funcionamiento de los operadores `OR` (disyunción) y `AND` (conjunción).
- **🐍 Generador de Código Python**: Muestra el código fuente Python exacto equivalente a la configuración seleccionada.

---

## 📁 Estructura del Proyecto

```text
PyLogic-Lab/
├── app.py          # Lógica principal y componentes de la interfaz en Streamlit
├── styles.css      # Hoja de estilos CSS externa e independiente (UI Glassmorphism)
└── README.md       # Documentación oficial del laboratorio
```

---

## ⚙️ Requisitos e Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/simonlopez25/PyLogic-Lab.git
cd PyLogic-Lab
```

### 2. Instalar dependencias
Asegúrate de tener Python 3.8+ instalado y ejecuta:
```bash
pip install streamlit pandas
```

### 3. Ejecutar la aplicación
```bash
python -m streamlit run app.py
```
*(O simplemente `streamlit run app.py`)*

---

## 🧠 Explicación de la Lógica Evaluada

La aplicación simula el control de acceso a un evento con las siguientes reglas:

```python
# 1. Variables de entrada
edad = 16
tiene_tutor = True
saldo = 50.0
PRECIO_ENTRADA = 30.0

# 2. Evaluación paso a paso
es_mayor_edad = edad >= 18                              # False
puede_entrar_por_edad = es_mayor_edad or tiene_tutor    # True (por tener tutor)
tiene_dinero_suficiente = saldo >= PRECIO_ENTRADA        # True ($50.0 >= $30.0)

# 3. Condición final combinada
acceso_concedido = puede_entrar_por_edad and tiene_dinero_suficiente # True

# 4. Flujo del programa
if acceso_concedido:
    print("Acceso PERMITIDO")
else:
    print("Acceso DENEGADO")
```

---

## 🛠️ Tecnologías Utilizadas

- **[Python](https://www.python.org/)**: Lenguaje principal de desarrollo.
- **[Streamlit](https://streamlit.io/)**: Framework para la creación de la interfaz web interactiva.
- **[Pandas](https://pandas.pydata.org/)**: Renderizado y estructurado de la Tabla de Verdad.
- **CSS3 / Glassmorphism**: Estilos desacoplados y personalizados.
