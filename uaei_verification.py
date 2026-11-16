import numpy as np
import pandas as pd


# ==============================================================================
# MODULE 1: ENVIRONMENT VERIFICATION (E_score)
# Evaluates telemetry ingestion maturity, spatial-temporal anchoring, and compute/e-waste
# ==============================================================================
def verify_environment(mr: float, gt: float, re: float) -> dict:
    """Inputs normalized to [0.00, 1.00]:

    - mr: Ingestion Automation (0.00 Manual -> 0.75 Live API -> 1.00 Immutable Log)
    - gt: Spatial-Temporal Anchoring (Cryptographic timestamp + Ward GPS)
    - re: Compute & E-Waste Sustainability (Renewable grid + EPR recycling)
    """
    e_score = 0.40 * mr + 0.30 * gt + 0.30 * re
    flags = []

    if mr < 0.50:
        flags.append("Ingestion Risk: Manual/batch uploads lack real-time auditability.")
    if gt < 0.75:
        flags.append("Telemetry Risk: Missing cryptographic timestamps or ward GPS anchors.")
    if re < 0.50:
        flags.append("Externality Risk: Unverified renewable power or e-waste recovery.")

    return {
        "E_score": round(e_score, 4),
        "status": "Verified" if (e_score >= 0.75 and not flags) else "Needs Remediation",
        "audit_flags": flags,
    }


# ==============================================================================
# MODULE 2: GOVERNANCE VERIFICATION (AGIS)
# Evaluates transparency, Data Protection Act (2019) compliance, and human oversight
# ==============================================================================
def verify_governance(ta: float, dp: float, ho: float) -> dict:
    """Inputs normalized to [0.00, 1.00]:

    - ta: Transparency & Auditability (Public model cards, open logs)
    - dp: Data Protection & Sovereignty (DPIA Reg. 49, PII anonymization)
    - ho: Human-in-the-Loop Oversight (Sec. 35 officer override & redress)
    """
    agis = 0.35 * ta + 0.35 * dp + 0.30 * ho
    flags = []

    if dp < 0.75:
        flags.append("DPA Risk: Incomplete DPIA (Reg. 49) or un-anonymized citizen PII.")
    if ho < 0.75:
        flags.append("Sec. 35 Risk: Insufficient human-in-the-loop override or citizen redress.")
    if ta < 0.50:
        flags.append("Opacity Risk: Missing public model documentation or audit trail.")

    return {
        "AGIS": round(agis, 4),
        "status": "Compliant" if (agis >= 0.75 and not flags) else "Governance Gap",
        "audit_flags": flags,
    }


# ==============================================================================
# MODULE 3: SOCIAL INCLUSION VERIFICATION (S_inc)
# Evaluates offline channel parity, Kiswahili/local NLP, and informal ward equity
# ==============================================================================
def verify_social_inclusion(cm: float, lp: float, we: float) -> dict:
    """Inputs normalized to [0.00, 1.00]:

    - cm: Channel Multimodality (USSD *xxx#, SMS, and physical desk parity)
    - lp: Linguistic Parity (Kiswahili & local vernacular NLP support)
    - we: Ward-Level Equity Allocation (Deployment in informal settlements)
    """
    s_inc = 0.40 * cm + 0.30 * lp + 0.30 * we
    flags = []

    if cm < 0.75:
        flags.append("Access Risk: Lacks USSD/SMS or physical desk parity for offline residents.")
    if lp < 0.70:
        flags.append("Linguistic Risk: Insufficient Kiswahili/local language NLP support.")
    if we < 0.60:
        flags.append("Equity Risk: Under-allocated across high-density informal wards.")

    return {
        "S_inc": round(s_inc, 4),
        "status": "Inclusive" if (s_inc >= 0.75 and not flags) else "Access Deficit",
        "audit_flags": flags,
    }


# ==============================================================================
# MODULE 4: COMPOSITE UAEI AGGREGATOR
# ==============================================================================
def evaluate_project_uaei(
    project_name: str,
    env_inputs: tuple,
    gov_inputs: tuple,
    soc_inputs: tuple,
) -> dict:
    env_res = verify_environment(*env_inputs)
    gov_res = verify_governance(*gov_inputs)
    soc_res = verify_social_inclusion(*soc_inputs)

    uaei = (env_res["E_score"] + gov_res["AGIS"] + soc_res["S_inc"]) / 3.0

    if uaei >= 0.80:
        tier = "Alpha Assurance (Verified Sustainable Infrastructure)"
    elif uaei >= 0.50:
        tier = "Bravo Assurance (Transitional / Conditionally Compliant)"
    else:
        tier = "Charlie Assurance (Unverified / High Risk)"

    return {
        "Project": project_name,
        "E_score": env_res["E_score"],
        "Env_Status": env_res["status"],
        "AGIS": gov_res["AGIS"],
        "Gov_Status": gov_res["status"],
        "S_inc": soc_res["S_inc"],
        "Soc_Status": soc_res["status"],
        "UAEI": round(uaei, 4),
        "Assurance_Tier": tier,
        "Diagnostic_Flags": (
            env_res["audit_flags"] + gov_res["audit_flags"] + soc_res["audit_flags"]
        ),
    }


if __name__ == "__main__":
    sample_eval = evaluate_project_uaei(
        project_name="Nairobi Corridor Air-Transit AI",
        env_inputs=(0.85, 0.80, 0.65),
        gov_inputs=(0.75, 0.90, 0.80),
        soc_inputs=(0.80, 0.75, 0.70),
    )
    print(pd.DataFrame([sample_eval]).to_string())
