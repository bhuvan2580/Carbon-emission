import streamlit as st
from data_collector import get_data_centers, get_workload_metrics, calculate_energy
from optimizer import choose_best_dc

st.set_page_config(page_title="Carbon-Aware Data Center Scheduler", page_icon="🌍")

st.title("🌍 Carbon-Aware Data Center Scheduler")

dc_list = get_data_centers()
metrics = get_workload_metrics()

energy = calculate_energy(**metrics)
st.write("### 🔌 Predicted Energy Usage:", round(energy, 2), "Watts")
st.write("#### 📊 Current Workload Metrics:")
st.json(metrics)

best_dc = choose_best_dc(dc_list)

st.success(f"✅ Recommended Data Center: {best_dc['name']}")
st.write(f"🌿 Carbon Intensity: {best_dc['carbon_intensity']} gCO₂/kWh")
st.write(f"🔋 PUE (Power Usage Effectiveness): {best_dc['pue']}")