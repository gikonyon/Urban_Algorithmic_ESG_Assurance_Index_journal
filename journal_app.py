# -----------------------------------------------------------------------------
# MODE: UAEI FORENSIC ESG ASSURANCE CALCULATOR
# -----------------------------------------------------------------------------
elif navigation_mode == "📊 UAEI ESG Assurance Calculator":
    st.header("📊 Urban Algorithmic ESG Assurance Index (UAEI) Calculator")
    st.caption("Interactive verification tool for municipal AI and public service deployments in Nairobi.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🌱 Environment (E_score)")
        mr = st.slider("Ingestion Automation (Mr)", 0.0, 1.0, 0.75, 0.05)
        gt = st.slider("Spatial-Temporal Anchoring (Gt)", 0.0, 1.0, 0.80, 0.05)
        re = st.slider("Compute & E-Waste Sustainability (Re)", 0.0, 1.0, 0.65, 0.05)

    with col2:
        st.subheader("🏛️ Governance (AGIS)")
        ta = st.slider("Transparency & Auditability (Ta)", 0.0, 1.0, 0.75, 0.05)
        dp = st.slider("Data Protection / DPIA (Dp)", 0.0, 1.0, 0.90, 0.05)
        ho = st.slider("Human-in-the-Loop Oversight (Ho)", 0.0, 1.0, 0.80, 0.05)

    with col3:
        st.subheader("🤝 Social Inclusion (S_inc)")
        cm = st.slider("Channel Multimodality / USSD (Cm)", 0.0, 1.0, 0.80, 0.05)
        lp = st.slider("Linguistic Parity / Kiswahili (Lp)", 0.0, 1.0, 0.75, 0.05)
        we = st.slider("Ward-Level Equity Allocation (We)", 0.0, 1.0, 0.70, 0.05)

    # Compute scores using our verification logic
    e_score = 0.40 * mr + 0.30 * gt + 0.30 * re
    agis = 0.35 * ta + 0.35 * dp + 0.30 * ho
    s_inc = 0.40 * cm + 0.30 * lp + 0.30 * we
    uaei = (e_score + agis + s_inc) / 3.0

    st.markdown("---")
    res_col1, res_col2, res_col3, res_col4 = st.columns(4)
    res_col1.metric("E_score", f"{e_score:.4f}")
    res_col2.metric("AGIS", f"{agis:.4f}")
    res_col3.metric("S_inc", f"{s_inc:.4f}")
    res_col4.metric("Composite UAEI", f"{uaei:.4f}")

    if uaei >= 0.80:
        st.success("🟢 **Alpha Assurance:** Verified Sustainable Public Infrastructure.")
    elif uaei >= 0.50:
        st.warning("🟡 **Bravo Assurance:** Transitional / Conditionally Compliant.")
    else:
        st.error("🔴 **Charlie Assurance:** Unverified / High Risk Deployment.")
