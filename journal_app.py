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
**Core Empirical Findings:**
* **Air Quality & Mobility:** 50+ city-owned sensors (SEI / Breathe Cities) correlate hyper-local $PM_{2.5}$ spikes along Mombasa Road, Thika Superhighway, and Outering Road with adaptive Intelligent Traffic Systems (ITS).
* **Water & Circular Waste:** Acoustic pressure-anomaly detection curbs non-revenue water loss, while fill-level sensors optimize municipal waste fleet routing.
* **Infrastructure Externalities:** Data center workloads must align with Kenya's geothermal/hydro grid and enforce Extended Producer Responsibility (EPR) for retired sensor hardware.
            """,
            "tags": "Environment, Telemetry, AirQuality, Nairobi",
        },
        {
            "date": "2026-11-16",
            "category": "Pillar II: Governance (AGIS)",
            "title": "Algorithmic Accountability under Kenya DPA (2019) & AI Policy (2026)",
            "content": """
**Statutory Guardrails:**
* **Data Protection Act (2019) Section 35:** Protects citizens from decisions based solely on automated processing, mandating human-in-the-loop officer override and redress.
* **Regulation 49 & Section 43:** Requires Data Protection Impact Assessments (DPIAs), strict PII anonymization prior to ingestion, and 72-hour breach reporting to the ODPC.
* **Digital Public Infrastructure (DPI):** Open API standards and national AI regulatory sandboxes prevent municipal vendor lock-in.
            """,
            "tags": "Governance, DataProtectionAct, ODPC, AlgorithmicAudit",
        },
        {
            "date": "2026-11-16",
            "category": "Pillar III: Social Inclusion (S_inc)",
            "title": "Bridging the Last-Mile Divide Across Nairobi Wards",
            "content": """
**Equitable Public Service Delivery:**
* **Channel Multimodality ($C_m$):** Mandating USSD (`*xxx#`), SMS, and physical service-desk equivalents alongside smartphone portals so offline citizens are not excluded.
* **Linguistic Parity ($L_p$):** Fine-tuning civic NLP assistants for Kiswahili and Sheng alongside English.
* **Ward Equity ($W_e$):** Allocating predictive clinic triage and electric BRT/matatu transit analytics proportionately across high-density wards (Kibera, Mathare, Korogocho, Kariobangi).
            """,
            "tags": "SocialInclusion, USSD, KiswahiliNLP, PublicServices",
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
        "📖 Research Paper & Diagnostic Matrix",
        "📝 Research Journal Logs",
        "🔬 Nairobi Pilot Benchmarks",
    ],
)

# -----------------------------------------------------------------------------
# MODE 1: UAEI FORENSIC ESG ASSURANCE CALCULATOR
# -----------------------------------------------------------------------------
if navigation_mode == "📊 UAEI ESG Assurance Calculator":
    st.header("📊 Interactive UAEI Verification & Audit Calculator")
    st.markdown(
        "Adjust the normalized parameters (`0.00` to `1.00`) across the three pillars to compute the **Composite UAEI** and surface statutory audit flags."
    )

    project_name = st.text_input(
        "Municipal / Public Service Project Name:",
        value="Nairobi Corridor Air-Transit AI Pilot",
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
            0.80,
            0.05,
            help="Cryptographic timestamps and ward-level GPS verification",
        )
        re = st.slider(
            "Compute & E-Waste Sustainability ($R_e$)",
            0.0,
            1.0,
            0.65,
            0.05,
            help="Renewable grid alignment and circular e-waste recovery",
        )

    with col2:
        st.subheader("🏛️ Governance ($AGIS$)")
        ta = st.slider(
            "Transparency & Auditability ($T_a$)",
            0.0,
            1.0,
            0.75,
            0.05,
            help="Public model cards, algorithmic decision logs, open portals",
        )
        dp = st.slider(
            "Data Protection & DPIA ($D_p$)",
            0.0,
            1.0,
            0.90,
            0.05,
            help="Reg. 49 DPIA completion, PII anonymization, local residency",
        )
        ho = st.slider(
            "Human-in-the-Loop Oversight ($H_o$)",
            0.0,
            1.0,
            0.80,
            0.05,
            help="Section 35 named officer override and citizen redress mechanism",
        )

    with col3:
        st.subheader("🤝 Social Inclusion ($S_{inc}$)")
        cm = st.slider(
            "Channel Multimodality / USSD ($C_m$)",
            0.0,
            1.0,
            0.80,
            0.05,
            help="Availability of USSD (*xxx#), SMS, and physical service desks",
        )
        lp = st.slider(
            "Linguistic Parity / Kiswahili ($L_p$)",
            0.0,
            1.0,
            0.75,
            0.05,
            help="NLP support for Kiswahili and local vernaculars",
        )
        we = st.slider(
            "Ward-Level Equity Allocation ($W_e$)",
            0.0,
            1.0,
            0.70,
            0.05,
            help="Proportionate deployment across high-density informal wards",
        )

    # Evaluate using the modular verification suite in uaei_verification.py
    result = evaluate_project_uaei(
        project_name=project_name,
        env_inputs=(mr, gt, re),
        gov_inputs=(ta, dp, ho),
        soc_inputs=(cm, lp, we),
    )

    st.markdown("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Environment (E_score)", f"{result['E_score']:.4f}", result["Env_Status"])
    m2.metric("Governance (AGIS)", f"{result['AGIS']:.4f}", result["Gov_Status"])
    m3.metric("Social Inclusion (S_inc)", f"{result['S_inc']:.4f}", result["Soc_Status"])
    m4.metric("Composite UAEI", f"{result['UAEI']:.4f}")

    if result["UAEI"] >= 0.80:
        st.success(f"🟢 **{result['Assurance_Tier']}**")
    elif result["UAEI"] >= 0.50:
        st.warning(f"🟡 **{result['Assurance_Tier']}**")
    else:
        st.error(f"🔴 **{result['Assurance_Tier']}**")

    if result["Diagnostic_Flags"]:
        st.subheader("⚠️ Active Audit Flags")
        for flag in result["Diagnostic_Flags"]:
            st.error(flag)
    else:
        st.info("✅ Zero critical statutory or telemetry audit flags detected.")

# -----------------------------------------------------------------------------
# MODE 2: RESEARCH PAPER & DIAGNOSTIC MATRIX
# -----------------------------------------------------------------------------
elif navigation_mode == "📖 Research Paper & Diagnostic Matrix":
    st.header("📖 Manuscript Summary & Nairobi Diagnostic Matrix")
    st.markdown(
        """
**Title:** *Algorithmic Urbanism and Sustainability Assurance: Evaluating Artificial Intelligence across Environment, Governance, and Social Inclusion in Nairobi’s Public Services*  
**Publication Anchor:** *East African Journal of Business and Economics* (EAJBE), Vol. 9, Issue 4 (2026)  

### Composite Formulation
$$UAEI = \\frac{1}{3}(E_{score} + AGIS + S_{inc})$$
        """
    )

    matrix_df = pd.DataFrame(
        [
            {
                "ESG Pillar": "Environment (E)",
                "Nairobi Urban Bottleneck": "Vehicular PM2.5 spikes, non-revenue water loss, illegal dumping",
                "AI & Telemetry Lever": "50+ municipal air sensors, ITS traffic signals, grid leak detection",
                "Primary Risk": "Data center energy/water draw; informal e-waste toxicity",
                "UAEI Control": "Live API streaming (Mr >= 0.75) + EPR hardware recovery (Re)",
            },
            {
                "ESG Pillar": "Governance (G)",
                "Nairobi Urban Bottleneck": "Departmental data silos, procurement opacity, vendor lock-in",
                "AI & Telemetry Lever": "Open urban data portals, automated audit logs, AI sandboxes",
                "Primary Risk": "Unlawful PII exposure; opaque automated rejections",
                "UAEI Control": "Mandatory DPIAs (Reg. 49) & Sec. 35 human override (Ho)",
            },
            {
                "ESG Pillar": "Social / Public Services (S)",
                "Nairobi Urban Bottleneck": "Clinic overcrowding, long informal-settlement commutes",
                "AI & Telemetry Lever": "Predictive clinic triage, e-mobility routing, multilingual bots",
                "Primary Risk": "Exclusion of offline, low-literacy, and non-English residents",
                "UAEI Control": "USSD/SMS channel parity (Cm) + Kiswahili NLP support (Lp)",
            },
        ]
    )
    st.table(matrix_df)

# -----------------------------------------------------------------------------
# MODE 3: RESEARCH JOURNAL LOGS
# -----------------------------------------------------------------------------
elif navigation_mode == "📝 Research Journal Logs":
    st.header("📝 Thematic Research Logs")
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
# MODE 4: NAIROBI PILOT BENCHMARKS
# -----------------------------------------------------------------------------
elif navigation_mode == "🔬 Nairobi Pilot Benchmarks":
    st.header("🔬 Comparative Benchmark of Simulated Nairobi Pilots")
    pilots = [
        evaluate_project_uaei(
            "Nairobi Corridor Air-Transit AI",
            (0.85, 0.80, 0.65),
            (0.75, 0.90, 0.80),
            (0.80, 0.75, 0.70),
        ),
        evaluate_project_uaei(
            "Informal Settlement Clinic Triage Bot",
            (0.50, 0.60, 0.50),
            (0.65, 0.85, 0.80),
            (0.90, 0.85, 0.85),
        ),
        evaluate_project_uaei(
            "Legacy Batch Revenue Scoring System",
            (0.25, 0.30, 0.40),
            (0.30, 0.45, 0.35),
            (0.40, 0.30, 0.35),
        ),
    ]
    bench_df = pd.DataFrame(pilots)
    st.dataframe(
        bench_df[["Project", "E_score", "AGIS", "S_inc", "UAEI", "Assurance_Tier"]],
        use_container_width=True,
    )

    fig = px.bar(
        bench_df,
        x="Project",
        y=["E_score", "AGIS", "S_inc"],
        barmode="group",
        title="Pillar Comparison Across Simulated Nairobi Public Service Deployments",
    )
    st.plotly_chart(fig, use_container_width=True)
