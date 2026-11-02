# Fictional intake: Aster Devices

All people, company details, mechanisms, and internal records below are synthetic. They are not evidence of novelty or patentability. Source paragraph identifiers are stable.

## SRC-01 — Inventor intake note, 2026-10-20

### §1
Mira says the company's battery-powered warehouse sensors usually send a reading every minute. During radio congestion, devices retry and consume extra energy. Mira calls the proposed feature "quiet-window batching." She reports designing the sensor-side buffer policy. Theo reportedly designed the gateway scheduling messages.

### §2
The gateway sends each sensor a window start time and a maximum sample count. The sensor stores readings locally and transmits a batch during that window, or when the maximum count is reached. Mira says it should reduce radio wakeups without losing urgent alerts.

### §3
We think battery life will improve by 30%. We have not run a battery test. We plan a public product demo on November 18, 2026, but the exact content of the demo is not decided.

## SRC-02 — Design note, 2026-10-22

### §1
The sensor stores each sample with a timestamp and a priority flag. The gateway sends a window start time and a maximum sample count. This document does not specify clock synchronization or what happens if the gateway's message is missed.

### §2
A high-priority reading bypasses the batching buffer and triggers an immediate transmission attempt. Other samples are sent when the window opens or the maximum count is reached. Congestion can delay delivery even after an immediate attempt.

## SRC-03 — Follow-up transcript excerpt, 2026-10-23

### §1
Mira: "I may have oversimplified the priority behavior. In the prototype everything waits for the next window, even a priority reading. I need Theo to check whether bypass is in a different branch. We haven't selected the production behavior."

### §2
Mira: "By quiet I mean fewer separate sends. It doesn't mean the device stops sampling. We haven't settled whether the count-triggered batch ignores the assigned time window."

## SRC-04 — Optional company context, 2026-10-24

### §1
Technology bucket: Low-power edge telemetry. Responsible team: Embedded Systems. Roadmap initiative: reduce radio activity while preserving alert responsiveness. This is one relevant bucket, not a complete patent strategy or organization chart.

### §2
Portfolio row INT-017 has the internal title "Gateway-coordinated sensor transmission scheduling." It is listed as a pending US application. No application number, claims, family records, filing date, or current official status is supplied. This is the only portfolio row in this example.

### §3
Counsel has not supplied a filing rubric, cost assumptions, or available budget.
