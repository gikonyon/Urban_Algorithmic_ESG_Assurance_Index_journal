from datetime import datetime
import pandas as pd
import plotly.express as px
import streamlit as st
from uaei_verification import evaluate_project_uaei

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Urban Algorithmic ESG Assurance Index (UAEI)",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Urban Algorithmic ESG Assurance Index (UAEI)")
st.caption(
    "Algorithmic Urbanism and Sustainability Assurance in Nairobi's Public Services | Author: Gikonyo Ndugu"
)

# -----------------------------------------------------------------------------
# 2. INITIALIZE RESEARCH JOURNAL LOGS
# -----------------------------------------------------------------------------
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = [
        {
            "date": "2026-11-16",
            "category": "Pillar I: Environment (E_score)",
            "title": "Predictive Urban Ecology & Sensor Telemetry in Nairobi",
            "content": """
**Core Empirical Focus:**
* **Air Quality & Mobility:** 50+ municipal low-cost sensors (SEI / Breathe Cities initiative) correlating hyper-local $PM_{2.5}$ and $NO_2$ spikes along Mombasa Road, Thika Superhighway, and Outering Road with adaptive Intelligent Traffic Systems (ITS).
* **Water & Circular Waste:** Acoustic and pressure-anomaly models accelerating leak localization across distribution networks; route optimization reducing fuel use in waste collection.
* **Infrastructure Externalities:** AI compute workloads require transparent disclosure of energy and cooling water footprints, alongside certified end-of-life e-waste handling for sensor hardware ($R_e$).
            """,
            "tags": "Environment, Telemetry, AirQuality, Nairobi",
        },
        {
            "date": "2026-11-16",
            "category": "Pillar II: Governance (AGIS)",
            "title": "Algorithmic Accountability under Kenya DPA (2019) & AI Policy (2026)",
            "content": """
**Statutory Guardrails & Compliance:**
* **Data Protection Act (2019) Section 35:** Legal anchor for human-in-the-loop oversight, prohibiting decisions based solely on automated processing that produce legal or significant effects.
* **Section 31 & Regulation 49:** Mandatory Data Protection Impact Assessments (DPIAs) and strict pre-ingestion anonymization of citizen PII.
* **Section 43:** 72-hour breach notification duty to the Office of the Data Protection Commissioner (ODPC).
            """,
            "tags": "Governance, DataProtectionAct, ODPC, Section35",
        },
        {
            "date": "2026-11-16",
            "category": "Pillar III: Social Inclusion (S_inc)",
            "title": "Bridging the Last-Mile Divide Across Nairobi Wards",
            "content": """
**Equitable Public Service Delivery:**
* **Channel Multimodality ($C_m$):** Ensuring USSD (`*xxx#`), SMS, low-bandwidth, and physical service-desk equivalents exist alongside smartphone and web portals.
* **Linguistic Parity ($L_p$):** Incorporating Kiswahili and Sheng natural language processing (NLP) support.
* **Ward Equity ($W_e$):** Deploying sensors and predictive clinic triage/transit tools in proportion to need across high-density informal settlements (Kibera, Mathare, Korogocho, Kariobangi).
            """,
            "tags": "SocialInclusion, USSD, KiswahiliNLP, InformalSettlements",
        },
    ]

# -----------------------------------------------------------------------------
# 3. NAVIGATION SIDEBAR
# -----------------------------------------------------------------------------
st.sidebar.header("Navigation Controls")
navigation_mode = st.sidebar.radio(
    "Select Module:",
    [
        "📊 UAEI ESG Assurance Calculator",
        "📖 Full Research Paper (Revision 2)",
        "📝 Research Journal Logs",
        "🔬 Worked Example (Scenario A vs. B)",
    ],
)

# -----------------------------------------------------------------------------
# MODE 1: UAEI FORENSIC ESG ASSURANCE CALCULATOR
# -----------------------------------------------------------------------------
if navigation_mode == "📊 UAEI ESG Assurance Calculator":
    st.header("📊 Interactive UAEI Verification & Audit Calculator")
    st.markdown(
        "Adjust normalized parameters (`0.00` to `1.00`) across Environment, Governance, and Social Inclusion to compute the **Composite UAEI** and verify gating rules (Legal Floor, Alpha Conditions, and Bravo Cap)."
    )

    project_name = st.text_input(
        "Municipal / Public Service Project Name:",
        value="Citizen Permit-Processing Assistant (Nairobi)",
    )
    affects_inds = st.checkbox(
        "System makes or materially influences decisions about individuals (Triggers Section 35 Legal Floor)?",
        value=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🌱 Environment ($E_{score}$)")
        mr = st.slider(
            "Ingestion Automation ($M_r$)",
            0.0,
            1.0,
            0.75,
            0.05,
            help="0.00 Manual -> 0.50 ETL -> 0.75 Live API -> 1.00 Immutable Log",
        )
        gt = st.slider(
            "Spatial-Temporal Anchoring ($G_t$)",
            0.0,
            1.0,
            0.75,
            0.05,
            help="Cryptographic timestamps + ward-level location",
        )
        re = st.slider(
            "Compute & E-Waste Sustainability ($R_e$)",
            0.0,
            1.0,
            0.50,
            0.05,
            help="Renewable grid alignment + certified e-waste handling",
        )

    with col2:
        st.subheader("🏛️ Governance ($AGIS$)")
        ta = st.slider(
            "Transparency & Auditability ($T_a$)",
            0.0,
            1.0,
            0.75,
            0.05,
            help="Public documentation, retained logs, open data",
        )
        dp = st.slider(
            "Data Protection & DPIA ($D_p$)",
            0.0,
            1.0,
            0.75,
            0.05,
            help="Completed DPIA, anonymization, vendor agreements",
        )
        ho = st.slider(
            "Human-in-the-Loop Oversight ($H_o$)",
            0.0,
            1.0,
            1.00,
            0.05,
            help="0.00 None | 0.50 Informal review | 1.00 Named officer override + citizen appeal",
        )

    with col3:
        st.subheader("🤝 Social Inclusion ($S_{inc}$)")
        cm = st.slider(
            "Channel Multimodality ($C_m$)",
            0.0,
            1.0,
            0.75,
            0.05,
            help="USSD, SMS, low-bandwidth & desk equivalents",
        )
        lp = st.slider(
            "Linguistic Parity ($L_p$)",
            0.0,
            1.0,
            0.50,
            0.05,
            help="Kiswahili, Sheng, and local vernacular support",
        )
        we = st.slider(
            "Ward-Level Equity ($W_e$)",
            0.0,
            1.0,
            0.50,
            0.05,
            help="Proportionate deployment across informal settlements",
        )

    # Evaluate using uaei_verification.py with gating logic
    result = evaluate_project_uaei(
        project_name=project_name,
        env_inputs=(mr, gt, re),
        gov_inputs=(ta, dp, ho),
        soc_inputs=(cm, lp, we),
        affects_individuals=affects_inds,
    )

    st.markdown("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Environment (E_score)", f"{result['E_score']:.4f}", result["Env_Status"])
    m2.metric("Governance (AGIS)", f"{result['AGIS']:.4f}", result["Gov_Status"])
    m3.metric("Social Inclusion (S_inc)", f"{result['S_inc']:.4f}", result["Soc_Status"])
    m4.metric("Composite UAEI", f"{result['UAEI']:.4f}")

    if "Alpha" in result["Assurance_Tier"]:
        st.success(f"🟢 **{result['Assurance_Tier']}**")
    elif "Bravo" in result["Assurance_Tier"]:
        st.warning(f"🟡 **{result['Assurance_Tier']}**")
    else:
        st.error(f"🔴 **{result['Assurance_Tier']}**")

    if result["Gate_Notes"]:
        st.subheader("🛡️ Statutory Gating Rule Activations")
        for note in result["Gate_Notes"]:
            st.warning(note)

    if result["Diagnostic_Flags"]:
        st.subheader("⚠️ Active Audit Flags")
        for flag in result["Diagnostic_Flags"]:
            st.error(flag)
    else:
        st.info("✅ Zero critical statutory audit flags detected.")

# -----------------------------------------------------------------------------
# MODE 2: FULL RESEARCH PAPER (REVISION 2)
# -----------------------------------------------------------------------------
elif navigation_mode == "📖 Full Research Paper (Revision 2)":
    st.header("📖 Manuscript: Algorithmic Urbanism and Sustainability Assurance")
    st.markdown(
        """
**Author:** Gikonyo Ndugu (Independent Researcher/Consultant, Nairobi, Kenya)  
**Target Publication:** *East African Journal of Business and Economics* (EAJBE), Vol. 9, Issue 4 (2026)  

### Abstract
Rapid urbanization in Sub-Saharan Africa strains environmental resources, municipal accountability and equitable public service delivery. In Nairobi, Artificial Intelligence (AI) and Internet of Things (IoT) telemetry are increasingly presented as catalysts for urban sustainability. Without assurance frameworks, however, algorithmic interventions risk producing unverified smart-city narratives, deepening data governance weaknesses and widening socio-economic exclusion. Building on forensic Environmental, Social and Governance (ESG) assurance methods, this paper proposes the **Urban Algorithmic ESG Assurance Index (UAEI)**, a framework for scoring public-sector AI deployments across three pillars: Environment, Governance, and Social Inclusion. The framework is anchored in Kenya's *Data Protection Act (2019)*, the *Nairobi City County Air Quality Action Plan (2025–2029)* and the emerging national AI policy position. It adds minimum-threshold gates so that a strong score in one pillar cannot mask a failure in statutory governance.

---

### 1. Introduction
Metropolitan Nairobi is East Africa's main commercial, diplomatic and technological hub, and its demographic growth has outpaced legacy municipal infrastructure. Persistent deficits in air quality management, non-revenue water, solid waste collection and primary healthcare access make the case for evidence-based urban governance. Kenya has at the same time moved its digital agenda forward through the National AI Strategy 2025–2030, a Draft Kenya Artificial Intelligence and Other Emerging Technologies Policy opened for public comment in July 2026, and a Draft Final National Data Governance Policy published in May 2026. Nairobi City County launched its own Air Quality Action Plan (2025–2029) in November 2025.

Despite public and donor investment in urban analytics, an assurance gap persists between technology deployment and verifiable ESG outcomes. This paper addresses three research questions:
1. **Environmental telemetry:** How can AI and sensor-driven analytics be assessed for their contribution to urban resource efficiency and ecological resilience in Nairobi, and which infrastructure externalities must be accounted for?
2. **Algorithmic governance:** What regulatory, data sovereignty and human-oversight mechanisms are needed to align public-sector AI with Kenya's constitutional and statutory frameworks?
3. **Social inclusion:** How can municipal AI systems be assessed for whether they bridge linguistic, socio-economic and connectivity divides across Nairobi's wards?

---

### 2. Literature Review and Regulatory Context
* **2.1 Urban sustainability and forensic ESG assurance:** Extending forensic ESG assurance from corporate reporting to municipal data pipelines means evaluating three properties: ingestion automation ($M_r$), spatial-temporal integrity ($G_t$) and record immutability ($R_e$). This builds on Ndugu (2026).
* **2.2 Kenya's AI and data governance architecture:** Anchored in the *Constitution of Kenya (2010)*, the *Data Protection Act (2019)*, and its 2021 Regulations. Key statutory provisions include **Section 35** (human-in-the-loop oversight against solely automated decisions), **Section 31 / Regulation 49** (Data Protection Impact Assessments), and **Section 43** (72-hour breach notification).

---

### 3. Methodology: The Urban Algorithmic ESG Assurance Framework
* **E_score = $0.40 \times M_r + 0.30 \times G_t + 0.30 \times R_e$**
* **AGIS = $0.35 \times T_a + 0.35 \times D_p + 0.30 \times H_o$**
* **S_inc = $0.40 \times C_m + 0.30 \times L_p + 0.30 \times W_e$**
* **UAEI = $(E_{score} + AGIS + S_{inc}) / 3$**

#### Minimum-Threshold Gating Rules:
1. **Legal Floor:** Any system influencing individuals with $H_o = 0.00$ is rated Charlie regardless of UAEI, violating Section 35.
2. **Alpha Conditions:** Alpha requires $UAEI \ge 0.80$, $AGIS \ge 0.70$, and no sub-index below $0.60$.
3. **Bravo Cap:** Deployments meeting UAEI $\ge 0.80$ but failing Alpha conditions are capped at Bravo.

---

### 4. Context Analysis: Nairobi's Three Pillars
* **Pillar I (Environment):** 50 municipal low-cost sensors (June 2025 launch) + Air Quality Action Plan (2025–2029) supported by Breathe Cities, SEI Africa, and C40 Cities.
* **Pillar II (Governance):** Operationalizing PII anonymization, DPIAs, and strict audit logging to prevent unlawful external tool data exposure.
* **Pillar III (Social Inclusion):** Ensuring equitable access across informal settlements (Kibera, Mathare, Korogocho, Kariobangi) via USSD/SMS parity and Kiswahili/Sheng NLP support.

---

### 5. Contextual Diagnostic Synthesis
| Pillar | Core Nairobi bottleneck | AI and telemetry intervention | Principal governance or equity risk | Assurance guardrail (UAEI control) |
| :--- | :--- | :--- | :--- | :--- |
| **Environment** | Vehicular $PM_{2.5}$, water loss, dumping | Municipal air sensors, adaptive signals, leak detection | Data centre power/water draw; hazardous e-waste | Live streaming ($M_r \ge 0.75$) + certified e-waste handling ($R_e$) |
| **Governance** | Data silos, procurement opacity | Open data portals, audit logs, sandboxes | Unlawful data transfers; opaque rejections | DPIAs (Sec. 31) and named override officer (Sec. 35) |
| **Social inclusion** | Clinic overcrowding, long commutes | Clinical decision support, route analytics | Exclusion of offline/non-English residents | USSD/SMS parity ($C_m$) + Kiswahili support ($L_p$) |
        """
    )

# -----------------------------------------------------------------------------
# MODE 3: RESEARCH JOURNAL LOGS
# -----------------------------------------------------------------------------
elif navigation_mode == "📝 Research Journal Logs":
    st.header("📝 Thematic Research Journal Logs")
    for entry in st.session_state.journal_entries:
        with st.expander(f"📌 [{entry['date']}] {entry['title']} — {entry['category']}", expanded=True):
            st.markdown(entry["content"])
            st.caption(f"**Keywords:** `{entry['tags']}`")

    st.markdown("---")
    st.subheader("➕ Add New Field Observation or Audit Note")
    with st.form("new_log_form", clear_on_submit=True):
        new_title = st.text_input("Observation Title:")
        new_cat = st.selectbox(
            "Pillar Category:",
            [
                "Pillar I: Environment (E_score)",
                "Pillar II: Governance (AGIS)",
                "Pillar III: Social Inclusion (S_inc)",
                "Future Research: County-Adjusted Corporate ESG",
            ],
        )
        new_content = st.text_area("Notes (Markdown supported):")
        new_tags = st.text_input("Tags:", "Nairobi, ESG, Audit")
        if st.form_submit_button("Save Observation"):
            if new_title.strip() and new_content.strip():
                st.session_state.journal_entries.insert(
                    0,
                    {
                        "date": datetime.today().strftime("%Y-%m-%d"),
                        "category": new_cat,
                        "title": new_title,
                        "content": new_content,
                        "tags": new_tags,
                    },
                )
                st.success("Observation saved!")
                st.rerun()

# -----------------------------------------------------------------------------
# MODE 4: WORKED EXAMPLE (SCENARIO A VS. B)
# -----------------------------------------------------------------------------
elif navigation_mode == "🔬 Worked Example (Scenario A vs. B)":
    st.header("🔬 Section 5 Worked Example: Scenario A vs. Scenario B")
    st.markdown(
        "Demonstrating how the framework behaves before and after sequenced institutional reforms (Hypothetical Data)."
    )

    scenario_a = evaluate_project_uaei(
        project_name="Scenario A: Initial Deployment (Hypothetical)",
        env_inputs=(0.75, 0.50, 0.25),
        gov_inputs=(0.50, 0.50, 0.25),
        soc_inputs=(0.25, 0.25, 0.50),
    )
    scenario_b = evaluate_project_uaei(
        project_name="Scenario B: After Sequenced Reforms (Hypothetical)",
        env_inputs=(0.75, 0.75, 0.50),
        gov_inputs=(0.75, 0.75, 1.00),
        soc_inputs=(0.75, 0.50, 0.50),
    )

    work_df = pd.DataFrame([scenario_a, scenario_b])
    st.dataframe(
        work_df[["Project", "E_score", "AGIS", "S_inc", "UAEI", "Assurance_Tier"]],
        use_container_width=True,
    )

    fig = px.bar(
        work_df,
        x="Project",
        y=["E_score", "AGIS", "S_inc"],
        barmode="group",
        title="Pillar Progression Across Scenario A and Scenario B Reforms",
    )
    st.plotly_chart(fig, use_container_width=True)
