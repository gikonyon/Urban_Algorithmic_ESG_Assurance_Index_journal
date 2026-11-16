# 📊 Urban Algorithmic ESG Assurance Index (UAEI)

This repository hosts the forensic verification toolkit and interactive analytics journal accompanying the academic manuscript: **"Algorithmic Urbanism and Sustainability Assurance: Evaluating Artificial Intelligence across Environment, Governance, and Social Inclusion in Nairobi’s Public Services"** (*East African Journal of Business and Economics*, Vol. 9, Issue 4, 2026).

---

## 🌐 Live Interactive Application

Access the deployed Streamlit web application directly in your browser:  
👉 **[Launch UAEI Interactive Journal & Calculator](https://urbanalgorithmicesgassuranceindexjournal-hndwlkgcu3nyd6trmysxo.streamlit.app/)**

---

## 🔬 Framework Overview

To bridge the **Assurance Gap** between smart-city sustainability narratives and verifiable outcomes in Nairobi, the **Urban Algorithmic ESG Assurance Index ($UAEI$)** evaluates public-sector AI deployments across three normalized pillars ($[0.00, 1.00]$):

1. **Environment ($E_{score}$):**  
   $$E_{score} = 0.40(M_r) + 0.30(G_t) + 0.30(R_e)$$  
   Evaluates telemetry ingestion automation ($M_r$), spatial-temporal anchoring ($G_t$), and data center compute/e-waste sustainability ($R_e$).
2. **Governance ($AGIS$):**  
   $$AGIS = 0.35(T_a) + 0.35(D_p) + 0.30(H_o)$$  
   Evaluates algorithmic transparency ($T_a$), compliance with Kenya's *Data Protection Act (2019)* via DPIAs and anonymization ($D_p$), and Section 35 human-in-the-loop oversight ($H_o$).
3. **Social Inclusion ($S_{inc}$):**  
   $$S_{inc} = 0.40(C_m) + 0.30(L_p) + 0.30(W_e)$$  
   Evaluates USSD/SMS multimodal channel parity ($C_m$), Kiswahili/local NLP accessibility ($L_p$), and proportionate deployment across informal wards ($W_e$).

---

## 📁 Repository File Structure

* `journal_app.py`: Interactive Streamlit web application featuring the UAEI ESG Assurance Calculator and research journal logs.
* `uaei_verification.py`: Standalone Python verification suite (`verify_environment`, `verify_governance`, `verify_social_inclusion`, and `evaluate_project_uaei`) with automated diagnostic audit flags.
* `requirements.txt`: Python package dependencies (`streamlit`, `pandas`, `numpy`, `plotly`) for Streamlit Community Cloud deployment.
* `README.md`: Repository documentation and live application link.

---

## 🔭 Future Research Horizon

Subsequent iterations of this framework extend forensic verification to private-sector enterprises via a **County-Adjusted Corporate ESG Variance Model**—benchmarking corporate environmental and social metrics against localized county operating baselines rather than blunt national averages.

---
*Author & Lead Researcher: Gikonyo Ndugu*
