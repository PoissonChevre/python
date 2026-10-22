#!/usr/bin/env python3

# print("Bienvenue dans le calculateur de pourboire !")
# input_total = float(input("Veuillez entrer le montant total de la facture : "))
# tip = float(input("Veuillez entrer le pourcentage de pourboire souhaité (par exemple, 15 pour 15%) : "))
# tip_amount = input_total * (tip / 100)
# total_with_tip = input_total + tip_amount
# print(f"Le montant du pourboire est de {tip_amount:.2f} euros.")
# print(f"Le montant total avec le pourboire est de {total_with_tip/5:.2f} euros.")

# Reads live CPU/memory/disk with psutil and checks each against a threshold.

import psutil

THRESHOLDS = {
    "CPU": 85.0,
    "Memory": 85.0,
    "Disk": 75.0,
}


def collect_metrics():
    return {
        "CPU": psutil.cpu_percent(interval=1),
        "Memory": psutil.virtual_memory().percent,
        "Disk": psutil.disk_usage("/").percent,
    }


def evaluate(name, value, threshold):
    if value > threshold:
        return f"WARNING (above {threshold:.0f}%)", False
    return "Healthy", True


def main():
    try:
        metrics = collect_metrics()
    except Exception as exc:  # psutil can fail on odd platforms/permissions
        print("Could not read system metrics:", exc)
        return

    print("=== System Health Report ===")
    all_healthy = True
    for name, value in metrics.items():
        status, healthy = evaluate(name, value, THRESHOLDS[name])
        all_healthy = all_healthy and healthy
        print(f"{name:7}: {value:5.1f}%  -> {status}")

    print("Overall:", "Healthy" if all_healthy else "NEEDS ATTENTION")


if __name__ == "__main__":
    main()