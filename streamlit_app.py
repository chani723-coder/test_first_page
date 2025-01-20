import streamlit as st

st.set_page_config(page_title="Autoridad Nacional del Agua",page_icon='img/favicon.ico',layout="wide")






color_fondo="""
<style>
[data-testid="stSidebar"]{
background: linear-gradient(to bottom, #001F3F, #004080, #0B60A7);
}



/* Imágenes */
[data-testid="stImage"] {
    display: flex;
    justify-content: center ;
    padding: 5px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 5px;
    transition: all 0.3s ease;
}

[data-testid="stImage"] img {
    border-radius: 5px;
    max-width: 100%;
    height: auto;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

[data-testid="stImage"]:hover {
    cursor: pointer;
}

[data-testid="stImage"] img:hover {
    transform: scale(0.95);
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
}



[data-testid="stHeadingWithActionElements"] {
    display: flex;
    align-items: center;
    justify-content: space-between;
    /*background: linear-gradient(to bottom, #E8F2FC, #DCE7F3);*/
    background: linear-gradient(to bottom, #001F3F, #004080, #0B60A7);



    padding: 10px 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin: 15px 0;
    transition: all 0.3s ease-in-out;
}
[data-testid="stHeadingWithActionElements"]:hover {
    /*background: linear-gradient(to bottom, #DCE7F3, #CBD6E2);*/
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}
[data-testid="stHeadingWithActionElements"] h1 {
    font-family: "Arial", sans-serif;
    font-size: 28px;
    /*color: #003366;*/
    color:#ffffff;

    font-weight: bold;
    margin: 0;
    line-height: 1.2;
    transition: color 0.3s ease;
}
[data-testid="stHeadingWithActionElements"] h1:hover {
    color: #0B60A7;
    cursor: pointer;
}
[data-testid="stHeadingWithActionElements"] button,
[data-testid="stHeadingWithActionElements"] a {
    background: #0B60A7;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    font-size: 14px;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    text-decoration: none;
}
[data-testid="stHeadingWithActionElements"] button:hover,
[data-testid="stHeadingWithActionElements"] a:hover {
    background: #004080;
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    cursor: pointer;
}








[data-testid="stCaptionContainer"] {
    /*background: linear-gradient(to bottom, #F5F7FA, #E8F2FC);*/
    border-left: 4px solid #0B60A7;
    border-radius: 8px;
    padding: 10px 15px;
    margin: 10px 0;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-in-out;
    /*font-family: "Arial", sans-serif;*/
    font-size: 14px;
    color: #333333;
    line-height: 1.5;
}
[data-testid="stCaptionContainer"]:hover {
    /*background: linear-gradient(to bottom, #E8F2FC, #DCE7F3);*/
    border-left: 4px solid #004080;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
    cursor: default;
}
[data-testid="stCaptionContainer"] p {
    margin: 0;
    color: #004080;
    /*font-weight: bold;*/
    font-size: 14px;
}
</style>
"""
st.markdown(color_fondo,unsafe_allow_html=True)


col1,col2=st.columns([1,3])

col1.image("./img/midagri.png",width=350,use_container_width=True)

col2.image("./img/corte.jpg",width=1100,use_container_width=True)

st.title("Bienvenidos a M.A.D.H")
# st.sidebar.image("img/ANA.webp")

# st.title("Bienvenidos a M.A.D.H")
st.image('./img/MADH.png',width=600)



st.caption(
    """El escaso número de estaciones hidrométricas, la falta de mantenimiento y el déficit en la operación de estos, hace necesario que se modele el régimen del comportamiento de los ríos en nuestro país. Bajo este escenario la Dirección de Administración de Recursos Hídricos (DARH) ha desarrollado una herramienta informática (MADH), en un lenguaje de programación de código abierto, que permita la obtención de la oferta hídrica en cualquier punto de la red hídrica de las cuencas piloto Cunas y Pampas.  
    La base datos de esta herramienta proviene de los caudales generados en los estudios hidrológicos desarrollados por la Dirección de Calidad y Evaluación de Recursos Hídricos(DCERH), en las que utilizaron la herramienta informática WEAP.  
    MADH es una herramienta que simplifica los cálculos hidrológicos para la determinación de la oferta hídrica en un punto en específico dentro de una cuenca, ahorrando tiempo y recursos en el procedimiento de otorgamiento de acreditaciones de disponibilidad hídrica (ADH), a través de un método simple como la transposición de caudales, la cual ha sido automatizada, pero a la vez es efectivo que irá evolucionando en el tiempo. Para el desarrollo de la herramienta MADH se han incluido las demandas hídricas y las licencias de uso otorgadas previamente, además incluye el caudal ecológico. De esta manera la Autoridad Nacional del Agua será el ente que facilite las ofertas de agua en cualquier punto de la red hídrica a nivel nacional. 
""" 
)
a,b,c=st.columns([1,2,1])
with b:
    st.image('img/Presentación1.webp',caption="Método de transposición de caudales")

st.divider()

col1,col2=st.columns(2)

with col1:
    with st.expander("¿Desea saber más sobre cómo se obtienen los caudales?"):

        st.caption("""
        **Ortiz (2001)** refiere que este método consiste en hallar un coeficiente **(C)** que permita llevar la información de un caudal conocido hasta el lugar de interés; considerando la similitud de las cuencas partiendo de  variables como: área de drenaje de la cuenca en estudio **(A1)**, área de drenaje de la cuenca de la cual se tiene información **(A2)**, precipitación media ponderada de la cuenca en estudio **(P1)**, precipitación media ponderada de la cuenca de la que se tienen registros **(P2)**.  
                   
        La transposición de caudales se basa en relaciones entre cuencas similares u homólogas, donde el área de las cuencas desempeña un papel preponderante, así como la precipitación media.

        Según lo señalado, el coeficiente de transposición se calcula mediante la siguiente fórmula:

        """ )
        formula_1="""
        {Q_c \over A_c P_c} = {Q_s \over A_s P_s} 
        """
        formula_2="""
        Q_s = {A_s \over A_c} {P_s \over P_c} Q_c
        """
        a="Qs = Caudal de la cuenca sin información(m3/s)."
        b="Qc = Caudal de la cuenca con información(m3/s)."
        c="As = Área de la cuenca sin información(km2)."
        d="Ac = Área de la cuenca con información(km2)."
        st.latex(formula_1)
        st.latex(formula_2)
        Donde=[a,b,c,d]
        for i in Donde:
            st.caption(i)

with col2:

    st.info('Sobre los desarrolladores',icon=":material/groups:")

    st.image('./img/ANA.webp',width=200,)
    col1, col2, col3,col4 = st.columns(4)

    with col1:
        st.info("Jaime Rivera",icon=":material/psychology:")
        st.image("./img/agricola.webp")
        st.page_link("https://www.linkedin.com/in/jaime-rivera-a8b05b17b/",label='Linkedin',icon=":material/captive_portal:")
    with col2:
        st.info("James Millán",icon=":material/psychology:")
        st.image("./img/agricola.webp")
        st.page_link("https://www.linkedin.com/in/james-millan-24205a92/ ",label='Linkedin',icon=":material/captive_portal:")
    with col3:
        st.info("Cesar Baldoceda",icon=":material/psychology:")
        st.image("./img/agricola.webp")
        st.page_link("https://www.linkedin.com/in/cbaldoceda/ ",label='Linkedin',icon=":material/captive_portal:")
    with col4:
        st.info("Renzo Gonzales",icon=":material/psychology:")
        st.image("./img/agricola.webp")
        st.page_link("https://www.linkedin.com/in/renzo-gonzales-080aa7a5/",label='Linkedin',icon=":material/captive_portal:")

