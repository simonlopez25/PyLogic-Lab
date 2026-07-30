import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="PyLogic Lab - Evaluador de Lógica",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")


st.markdown('<div class="main-title">🧪 PyLogic Lab: Variables y Condicionales</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Explora y visualiza en tiempo real la evaluación de expresiones booleanas y control de flujo en Python.</div>', unsafe_allow_html=True)
st.sidebar.header("⚙️ Configuración")

preset = st.sidebar.selectbox(
    "🎯 Escenarios Predefinidos",
    [
        "Personalizado",
        "Menor sin tutor y sin dinero",
        "Menor con tutor y saldo suficiente",
        "Adulto con saldo suficiente",
        "Adulto sin saldo suficiente"
    ]
)

default_edad = 16
default_tutor = False
default_saldo = 50.0

if preset == "Menor sin tutor y sin dinero":
    default_edad = 15
    default_tutor = False
    default_saldo = 10.0
elif preset == "Menor con tutor y saldo suficiente":
    default_edad = 16
    default_tutor = True
    default_saldo = 40.0
elif preset == "Adulto con saldo suficiente":
    default_edad = 22
    default_tutor = False
    default_saldo = 60.0
elif preset == "Adulto sin saldo suficiente":
    default_edad = 20
    default_tutor = False
    default_saldo = 15.0

st.sidebar.divider()
PRECIO_ENTRADA = st.sidebar.slider("💵 `PRECIO_ENTRADA` ($)", min_value=10.0, max_value=100.0, value=30.0, step=5.0)


def get_badge(value: bool) -> str:
    if value:
        return '<span class="badge-true">True</span>'
    return '<span class="badge-false">False</span>'

tab_lab, tab_matrix, tab_guide, tab_code = st.tabs([
    "🧪 Simulador Interactivo",
    "📊 Tabla de Verdad",
    "💡 Guía de Operadores",
    "🐍 Código Python"
])

with tab_lab:
    st.subheader("1. Control de Variables de Entrada")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        edad = st.number_input("`edad` (años)", min_value=10, max_value=80, value=default_edad, key="input_edad")
    
    with col2:
        st.write("`tiene_tutor`")
        tiene_tutor = st.checkbox("¿Acompañado de tutor legal?", value=default_tutor, key="input_tutor")
    
    with col3:
        saldo = st.slider("`saldo` ($)", min_value=0.0, max_value=100.0, value=default_saldo, step=5.0, key="input_saldo")
    
    st.divider()

    es_mayor_edad = edad >= 18
    puede_entrar_por_edad = es_mayor_edad or tiene_tutor
    tiene_dinero_suficiente = saldo >= PRECIO_ENTRADA
    acceso_concedido = puede_entrar_por_edad and tiene_dinero_suficiente

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.subheader("2. Desglose de Evaluación Paso a Paso")
        
        b_es_mayor = get_badge(es_mayor_edad)
        st.markdown(f"""
        <div class="card-box">
            <strong>Paso 1: Verificación de Edad</strong><br/>
            <span class="logic-expr">es_mayor_edad = {edad} >= 18</span> &nbsp;&rarr;&nbsp; {b_es_mayor}
        </div>
        """, unsafe_allow_html=True)
        
        b_puede_entrar_edad = get_badge(puede_entrar_por_edad)
        st.markdown(f"""
        <div class="card-box">
            <strong>Paso 2: Regla de Edad o Tutoría (<code>OR</code>)</strong><br/>
            <span class="logic-expr">puede_entrar = {es_mayor_edad} or {tiene_tutor}</span> &nbsp;&rarr;&nbsp; {b_puede_entrar_edad}
        </div>
        """, unsafe_allow_html=True)

        b_tiene_dinero = get_badge(tiene_dinero_suficiente)
        st.markdown(f"""
        <div class="card-box">
            <strong>Paso 3: Verificación de Solvencia (<code>>=</code>)</strong><br/>
            <span class="logic-expr">tiene_dinero = {saldo:.1f} >= {PRECIO_ENTRADA:.1f}</span> &nbsp;&rarr;&nbsp; {b_tiene_dinero}
        </div>
        """, unsafe_allow_html=True)

        b_acceso = get_badge(acceso_concedido)
        st.markdown(f"""
        <div class="card-box" style="border: 1px solid #6366f1;">
            <strong>Paso 4: Evaluación Final (<code>AND</code>)</strong><br/>
            <span class="logic-expr">acceso_concedido = {puede_entrar_por_edad} and {tiene_dinero_suficiente}</span> &nbsp;&rarr;&nbsp; {b_acceso}
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.subheader("3. Decisión del Programa (Flujo)")
        
        if acceso_concedido:
            st.markdown("""
            <div class="result-banner-granted">
                <div class="result-title-granted">✅ ¡Acceso PERMITIDO!</div>
                <p style="color: #cbd5e1; margin-bottom: 0;">Se ejecuta la rama: <code>if acceso_concedido:</code></p>
                <hr style="border-color: rgba(16, 185, 129, 0.3); margin: 0.8rem 0;" />
                <small style="color: #94a3b8;">El usuario cumple con el requisito de edad/tutor y posee saldo suficiente ($%.1f &ge; $%.1f).</small>
            </div>
            """ % (saldo, PRECIO_ENTRADA), unsafe_allow_html=True)
        else:
            motivos = []
            if not puede_entrar_por_edad:
                motivos.append("No es mayor de edad y tampoco viene con tutor.")
            if not tiene_dinero_suficiente:
                motivos.append(f"Saldo insuficiente (${saldo:.1f} < ${PRECIO_ENTRADA:.1f}).")
            
            motivo_txt = "<br/>• " + "<br/>• ".join(motivos)
            
            st.markdown("""
            <div class="result-banner-denied">
                <div class="result-title-denied">❌ Acceso DENEGADO</div>
                <p style="color: #cbd5e1; margin-bottom: 0;">Se ejecuta la rama: <code>else:</code></p>
                <hr style="border-color: rgba(244, 63, 94, 0.3); margin: 0.8rem 0;" />
                <div style="text-align: left; font-size: 0.9rem; color: #fca5a5;">
                    <strong>Causa(s) de denegación:</strong> %s
                </div>
            </div>
            """ % motivo_txt, unsafe_allow_html=True)


with tab_matrix:
    st.subheader("📊 Matriz de Combinaciones Lógicas (Tabla de Verdad)")
    st.markdown("La siguiente tabla representa todas las combinaciones posibles de variables y la decisión resultante. La fila **resaltada** corresponde a tu configuración actual.")

    matrix_data = []
    for es_mayor in [False, True]:
        for tutor in [False, True]:
            for dinero in [False, True]:
                p_edad = es_mayor or tutor
                acceso = p_edad and dinero
                
                is_current = (es_mayor == es_mayor_edad) and (tutor == tiene_tutor) and (dinero == tiene_dinero_suficiente)
                
                matrix_data.append({
                    "Estado Actual": "👉 ACTIVO" if is_current else "",
                    "Mayor Edad (>=18)": "True 🟢" if es_mayor else "False 🔴",
                    "Tiene Tutor": "True 🟢" if tutor else "False 🔴",
                    "Tiene Dinero (>=Precio)": "True 🟢" if dinero else "False 🔴",
                    "Edad u/o Tutor (OR)": "True 🟢" if p_edad else "False 🔴",
                    "Acceso Concedido (AND)": "PERMITIDO ✅" if acceso else "DENEGADO ❌"
                })

    df_matrix = pd.DataFrame(matrix_data)
    
    st.dataframe(
        df_matrix,
        use_container_width=True,
        hide_index=True
    )


with tab_guide:
    st.subheader("💡 Guía Rápida de Operadores en Python")
    
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        st.markdown("""
        <div class="card-box">
            <h4 style="color: #6366f1; margin-top:0;">Operador <code>or</code> (Disyunción)</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Devuelve <code>True</code> si <strong>al menos una</strong> de las condiciones es verdadera.</p>
            <ul>
                <li><code>True or False</code> &rarr; <strong>True</strong></li>
                <li><code>False or False</code> &rarr; <strong>False</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with g_col2:
        st.markdown("""
        <div class="card-box">
            <h4 style="color: #a855f7; margin-top:0;">Operador <code>and</code> (Conjunción)</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Devuelve <code>True</code> <strong>únicamente si ambas</strong> condiciones son verdaderas.</p>
            <ul>
                <li><code>True and True</code> &rarr; <strong>True</strong></li>
                <li><code>True and False</code> &rarr; <strong>False</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


with tab_code:
    st.subheader("🐍 Código Python Representativo")
    st.markdown("Este es el código equivalente en Python generado dinámicamente con las variables actuales:")

    generated_code = f"""# Parametros de entrada
edad = {edad}
tiene_tutor = {tiene_tutor}
saldo = {saldo:.1f}
PRECIO_ENTRADA = {PRECIO_ENTRADA:.1f}

# 1. Evaluacion de condiciones
es_mayor_edad = edad >= 18  # {es_mayor_edad}
puede_entrar_por_edad = es_mayor_edad or tiene_tutor  # {puede_entrar_por_edad}
tiene_dinero_suficiente = saldo >= PRECIO_ENTRADA  # {tiene_dinero_suficiente}

# 2. Condicion combinada
acceso_concedido = puede_entrar_por_edad and tiene_dinero_suficiente  # {acceso_concedido}

# 3. Estructura de control (Flujo)
if acceso_concedido:
    print("Acceso PERMITIDO")
else:
    print("Acceso DENEGADO")
"""

    st.code(generated_code, language="python")