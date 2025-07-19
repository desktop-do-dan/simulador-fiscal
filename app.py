import streamlit as st
from simulador.calculadora import calcular_tributos

st.set_page_config(page_title="Simulador Fiscal", layout="centered")

st.title("🧾 Simulador Fiscal - Loja de Material de Construção")
st.markdown("Preencha os dados da venda abaixo para simular os impostos:")

produto = st.text_input("Produto", "Saco de cimento")
valor_unitario = st.number_input("Valor unitário (R$)", min_value=0.0, step=0.01)
quantidade = st.number_input("Quantidade", min_value=1)
regime = st.selectbox("Regime tributário", ["Simples Nacional", "Lucro Presumido"])

if st.button("Calcular tributos"):
    total, icms, ipi, pis, cofins = calcular_tributos(valor_unitario, quantidade, regime)
    st.success(f"Valor total: R$ {total:.2f}")
    st.write(f"ICMS: R$ {icms:.2f}")
    st.write(f"IPI: R$ {ipi:.2f}")
    st.write(f"PIS: R$ {pis:.2f}")
    st.write(f"COFINS: R$ {cofins:.2f}")
