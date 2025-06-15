import random

def get_data_centers():
    return [
        {"name": "Mumbai", "carbon_intensity": 420, "pue": 1.5},
        {"name": "Oregon", "carbon_intensity": 80, "pue": 1.3},
        {"name": "Frankfurt", "carbon_intensity": 150, "pue": 1.4}
    ]

def get_workload_metrics():
    return {
        "cpu": round(random.uniform(20, 80), 2),
        "memory": round(random.uniform(30, 90), 2)
    }

def calculate_energy(cpu, memory):
    return (cpu * 0.5 + memory * 0.3)  # simplified model