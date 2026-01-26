import device_sim
import csv
import statistics

from datetime import datetime
from pathlib import Path

def parse_latency(line):
    line = line.strip()
    parts = line.split()

    if not line.startswith("LATENCY_US"):
        raise ValueError(f"Unexpected response: {line}")

    return int(parts[1])


def run_toggle_latency_test(iters: int, pass_max_us: int) -> dict:

    samples: list[int] = []

    for i in range(iters):
        resp = device_sim.handle("TOGGLE")
        lat = parse_latency(resp)
        samples.append(lat)
    
    return {
        "iters": iters,
        "pass_max_us": pass_max_us,
        "min_us": min(samples),
        "max_us": max(samples),
        "mean_us": statistics.mean(samples),
        "stdev_us": statistics.pstdev(samples),
        "pass": max(samples),
        "samples": samples,
    }


def write_csv(path: Path, samples: list[int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["iterations", "latency_us"])
        for i, v in enumerate(samples):
            writer.writerow([i,v])


def write_summary(path: Path, result: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="") as f:
        f.write(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"Iterations: {result['iters']}\n")
        f.write(f"Pass threshold (max): {result['pass_max_us']} us\n")
        f.write(f"Min: {result['min_us']} us\n")
        f.write(f"Max: {result['max_us']} us\n")
        f.write(f"Mean: {result['mean_us']:.2f} us\n")
        f.write(f"Std: {result['stdev_us']:.2f} us\n")
        f.write(f"RESULT: {'PASS' if result['pass'] else 'FAIL'} \n")








def main():
    ITERS = 1000
    PASS_MAX_US = 50


    pong = device_sim.handle("GARBAGE").strip()

    if pong != "OK":
        raise RuntimeError(f"PING failed, got: {pong!r}")
    
    result = run_toggle_latency_test(ITERS, PASS_MAX_US)

    reports_dir = Path("reports")
    csv_path = reports_dir / "sample_latency.csv"
    summary_path = reports_dir / "summary.txt"

    write_csv(csv_path, result["samples"])
    write_summary(summary_path, result)


if __name__ == "__main__":
    main()




