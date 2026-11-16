import numpy as np
import pandas as pd


def verify_environment(mr: float, gt: float, re: float) -> dict:
    """Pillar I: Environmental Telemetry and Net-Impact Score (E_score)."""
    e_score = 0.40 * mr + 0.30 * gt + 0.30 * re
    flags = []
    if mr < 0.50:
        flags.append("Ingestion Risk: Manual/batch uploads lack real-time auditability.")
    if gt < 0.75:
        flags.append("Telemetry Risk: Missing cryptographic timestamps or ward-level location.")
    if re < 0.50:
        flags.append("Externality Risk: Uncertified or undisclosed compute and e-waste handling.")
    return {
        "E_score": round(e_score, 4),
        "status": "Verified" if (e_score >= 0.75 and not flags) else "Needs Remediation",
        "audit_flags": flags,
    }


def verify_governance(ta: float, dp: float, ho: float) -> dict:
    """Pillar II: Algorithmic Governance Integrity Score (AGIS)."""
    agis = 0.35 * ta + 0.35 * dp + 0.30 * ho
    flags = []
    if dp < 0.75:
        flags.append("DPA Risk: Incomplete DPIA (Sec. 31 / Reg. 49) or missing vendor processing agreement.")
    if ho < 0.75:
        flags.append("Section 35 Risk: Lacks named officer override and documented citizen appeal route.")
    if ta < 0.50:
        flags.append("Opacity Risk: Incomplete public model documentation or retained logs.")
    return {
        "AGIS": round(agis, 4),
        "status": "Compliant" if (agis >= 0.75 and not flags) else "Governance Gap",
        "audit_flags": flags,
    }


def verify_social_inclusion(cm: float, lp: float, we: float) -> dict:
    """Pillar III: Social Inclusion and Public Access Parity Score (S_inc)."""
    s_inc = 0.40 * cm + 0.30 * lp + 0.30 * we
    flags = []
    if cm < 0.75:
        flags.append("Access Risk: Lacks USSD, SMS, or physical service-desk parity.")
    if lp < 0.70:
        flags.append("Linguistic Risk: Insufficient Kiswahili/local language support.")
    if we < 0.60:
        flags.append("Equity Risk: Uneven deployment across informal settlements and peri-urban wards.")
    return {
        "S_inc": round(s_inc, 4),
        "status": "Inclusive" if (s_inc >= 0.75 and not flags) else "Access Deficit",
        "audit_flags": flags,
    }


def evaluate_project_uaei(
    project_name: str,
    env_inputs: tuple,
    gov_inputs: tuple,
    soc_inputs: tuple,
    affects_individuals: bool = True,
) -> dict:
    """Computes composite UAEI and applies Section 3.4 minimum-threshold gating rules."""
    env_res = verify_environment(*env_inputs)
    gov_res = verify_governance(*gov_inputs)
    soc_res = verify_social_inclusion(*soc_inputs)

    e_score = env_res["E_score"]
    agis = gov_res["AGIS"]
    s_inc = soc_res["S_inc"]
    ho = gov_inputs[2]

    uaei = (e_score + agis + s_inc) / 3.0
    gate_notes = []

    # Gate 1: Legal floor (Section 35 human-in-the-loop requirement)
    if affects_individuals and ho == 0.0:
        tier = "Charlie (Capped by Legal Floor: H_o = 0.00 violates Section 35)"
        gate_notes.append("Legal Floor Triggered: Autonomous decision-making without human oversight (H_o = 0.00).")
    # Gate 2 & 3: Alpha conditions vs. Bravo cap
    elif uaei >= 0.80:
        if agis >= 0.70 and min(e_score, agis, s_inc) >= 0.60:
            tier = "Alpha (Verified Sustainable Public Infrastructure)"
        else:
            tier = "Bravo (Capped from Alpha: Failed Pillar Gate Thresholds)"
            gate_notes.append("Bravo Cap Triggered: Alpha requires AGIS >= 0.70 and all sub-indices >= 0.60.")
    elif uaei >= 0.50:
        tier = "Bravo (Transitional, Conditionally Compliant)"
    else:
        tier = "Charlie (Unverified or High-Risk)"

    return {
        "Project": project_name,
        "E_score": round(e_score, 4),
        "Env_Status": env_res["status"],
        "AGIS": round(agis, 4),
        "Gov_Status": gov_res["status"],
        "S_inc": round(s_inc, 4),
        "Soc_Status": soc_res["status"],
        "UAEI": round(uaei, 4),
        "Assurance_Tier": tier,
        "Gate_Notes": gate_notes,
        "Diagnostic_Flags": (
            env_res["audit_flags"] + gov_res["audit_flags"] + soc_res["audit_flags"]
        ),
    }


if __name__ == "__main__":
    # Illustrative Worked Example from Section 5 (Hypothetical Data)
    scenario_a = evaluate_project_uaei(
        project_name="Scenario A: Permit Assistant (Initial Deployment - Hypothetical)",
        env_inputs=(0.75, 0.50, 0.25),
        gov_inputs=(0.50, 0.50, 0.25),
        soc_inputs=(0.25, 0.25, 0.50),
    )
    scenario_b = evaluate_project_uaei(
        project_name="Scenario B: Permit Assistant (After Sequenced Reforms - Hypothetical)",
        env_inputs=(0.75, 0.75, 0.50),
        gov_inputs=(0.75, 0.75, 1.00),
        soc_inputs=(0.75, 0.50, 0.50),
    )
    df = pd.DataFrame([scenario_a, scenario_b])
    print(df[["Project", "E_score", "AGIS", "S_inc", "UAEI", "Assurance_Tier"]].to_string(index=False))
