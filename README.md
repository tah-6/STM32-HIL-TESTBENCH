Modern embedded systems, particularly in safety-critical domains such as automotive and robotics; require not only functional correctness, but deterministic timing behavior.

While firmware is often validated through unit tests or manual interaction, timing characteristics such as command latency and GPIO response are rarely measured in student projects. Small delays or nondeterministic behavior can compound across multiple microcontrollers and peripherals, leading to system instability or failure.

Thats why this project was created to provide a lightweight Hardware-in-the-Loop (HIL) framework for STM32 devices that enables:

Automated firmware regression testing

Host-driven command execution over UART

Precise GPIO/timer instrumentation

Quantitative latency measurement