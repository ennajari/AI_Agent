import streamlit as st
from datetime import datetime
import os
import sys
from ennajari.crew import Ennajari
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Ennajari AI Crew", page_icon="🧠", layout="centered")

st.title("🧠 Ennajari AI Crew")
st.markdown("Utilisez l'IA pour générer des synthèses intelligentes par des agents collaboratifs.")

with st.form("crew_form"):
    topic = st.text_input("🎯 Sujet à explorer", value="L’intelligence artificielle dans l’éducation")
    year = st.number_input("📅 Année", value=datetime.now().year, step=1)
    submitted = st.form_submit_button("🚀 Lancer l'IA")

if submitted:
    with st.spinner("💡 Les agents réfléchissent..."):
        try:
            inputs = {
                "topic": topic,
                "current_year": str(year)
            }
            result = Ennajari().crew().kickoff(inputs=inputs)
            st.success("✅ Résultat généré avec succès !")
            st.markdown("### 📄 Résultat :")
            st.markdown(result)
        except Exception as e:
            st.error(f"❌ Une erreur s’est produite : {e}")
