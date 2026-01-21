# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 13:32:08 2026

@author: rjguz
"""

import streamlit as st
import pandas as pd
import numpy as np

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="WorkFlow Pro | Planta Automotriz",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INYECCIÓN DE CSS PERSONALIZADO (Estilo Dark Dashboard)
st.markdown("""
    <style>
    /* Fondo principal y sidebar */
    [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        color: #f8fafc !important;
    }
    
    /* Estilo de las tarjetas (Glassmorphism) */
    .stMetric {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        border-bottom: 4px solid #38bdf8;
    }
    
    /* Botones personalizados */
    .stButton>button {
        background-color: #38bdf8;
        color: white;
        border-radius: 10px;
        border: none;
        width: 100%;
        font-weight: bold;
    }

    /* Títulos y textos */
    h1, h2, h3, p {
        color: #f8fafc !important;
        font-family: 'Inter', sans-serif;
    }

    /* Estilo de tablas */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        background: #1e293b;
        border-radius: 10px;
        overflow: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (Navegación)
with st.sidebar:
    st.title("🏭 WORKFLOW")
    st.markdown("---")
    menu = st.radio(
        "MENÚ DE CONTROL",
        ["Inicio", "Hojas de Trabajo", "Reportes", "Usuarios", "Configuración"],
        index=0
    )
    st.markdown("---")
    st.info("Planta Ramos Arizpe\nTurno: Matutino")

# 4. LÓGICA DE VISTAS
if menu == "Inicio":
    st.header("Dashboard Operativo")
    
    # Widgets de métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Hojas Registradas", "1,250", "12%")
    col2.metric("Órdenes Activas", "35", "-2")
    col3.metric("OEE Planta", "82%", "5%")
    col4.metric("Tiempo Promedio", "45 min", "-5m")

    st.markdown("### Desempeño de Producción (Real vs Meta)")
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['Línea A', 'Línea B']
    )
    st.line_chart(chart_data)

elif menu == "Hojas de Trabajo":
    st.header("Gestión de Hojas de Trabajo")
    
    col_btn1, col_btn2 = st.columns([4, 1])
    with col_btn2:
        if st.button("➕ NUEVA HOJA"):
            st.toast("Abriendo formulario de registro...")

    # Simulación de tarjetas de trabajo
    cols = st.columns(3)
    for i, linea in enumerate(["Carrocería", "Pintura", "Ensamble"]):
        with cols[i]:
            st.markdown(f"""
            <div style="background:#1e293b; padding:20px; border-radius:10px; border-left: 5px solid #4ade80;">
                <h4>Orden #00{i+1}</h4>
                <p style="color:#94a3b8;">Área: {linea}</p>
                <p><b>Estado:</b> En Proceso</p>
            </div>
            """, unsafe_allow_html=True)
            st.progress(65 + (i*10))

elif menu == "Reportes":
    st.header("Analítica y Exportación")
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Eficiencia por Turno")
        df_report = pd.DataFrame({
            'Turno': ['Matutino', 'Vespertino', 'Nocturno'],
            'Eficiencia': [85, 78, 92]
        })
        st.bar_chart(df_report.set_index('Turno'))
    
    with col_right:
        st.subheader("Descargas")
        st.button("📄 Descargar Reporte Semanal (PDF)")
        st.button("📊 Exportar Log de Fallos (CSV)")

elif menu == "Usuarios":
    st.header("Control de Personal")
    data_users = {
        "Nombre": ["Laura Pérez", "Miguel Sánchez", "Carlos Ruiz"],
        "Puesto": ["Supervisor A", "Operario", "Mantenimiento"],
        "Estado": ["En Turno", "Descanso", "En Turno"]
    }
    st.table(pd.DataFrame(data_users))

elif menu == "Configuración":
    st.header("Ajustes del Sistema")
    st.toggle("Notificaciones Push", value=True)
    st.toggle("Modo Auditoría", value=False)
    st.select_slider("Frecuencia de actualización (min)", options=[1, 5, 10, 15])
    if st.button("Guardar Cambios"):
        st.success("Configuración actualizada")