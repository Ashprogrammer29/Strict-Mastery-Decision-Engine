# Strict-Mastery-Decision-Engine

### 🎯 The Philosophy: Precision Over Empathy.
In high-stakes educational environments, "near-misses" are failures. The Strict Mastery Decision Engine is a deterministic state machine designed to eliminate the "Stochastic Fluke"—where a student passes due to lucky guessing or a temporary upward trend without true cognitive retention.

With Skeptical Gatekeeper logic, the engine ensures students progress only when their Weighted Knowledge State meets a rigorous industrial standard.

# 🧠 Core Algorithms & Logic. 

### (i) Weighted Recency Scoring ($S_v$)

Standard averaging is flawed because it treats old, irrelevant failures with the same weight as current performance. Conversely, looking only at the last score ignores historical inconsistency.

SMDE uses a 70/30 Linear Weighting formula:

$$S_v = (Score_{current} \times 0.7) + (Score_{previous} \times 0.3)$$

This creates a "Gravitational Pull" where past performance acts as an anchor, requiring the student to significantly outperform the threshold to overcome a poor history.

### (ii) Volatility Analysis (Standard Deviation $\sigma$)

Stability is the hallmark of mastery. The engine calculates the Standard Deviation of the score sequence to identify 

"The Lucky Gambler."

$$\sigma = \sqrt{\frac{\sum(x_i - \mu)^2}{N}}$$

If the volatility exceeds a predefined coefficient, the engine flags the progress as Stochastic, signaling that while the threshold was met, the performance remains erratic.

### (iii) The Deterministic State Machine

The engine transitions through four immutable states based on the input vector:

PROGRESS: $S_v \ge 85.0$. The user has demonstrated sustained mastery.

RETRY: $S_v < 85.0$ and $Attempts < 3$. The user is granted another iteration to stabilize.

PIVOT: $S_v < 85.0$ and $Attempts \ge 3$. The Circuit Breaker triggers, halting the loop to prevent "Retry Hell" and mandating a foundational reset.

DATA_ERROR: Triggered by out-of-range values or non-numeric noise, ensuring system integrity.

# 🏗️ Technical Architecture

### Production-Grade Engineering

### Zero-Dependency Logic: Built using Python standard libraries (statistics, json, argparse) for maximum portability and zero supply-chain risk.

### Input Sanitization: Robust type-checking and range validation (0-100) to prevent runtime crashes during 3rd-party automated testing.

### JSON-Standardized Output: Optimized for headless integration; results are returned as structured objects for consumption by external dashboards or databases.

### Containerization (Docker)
The engine is delivered as a security-hardened Alpine Linux container. It runs as a non-privileged master_user to follow the principle of least privilege (PoLP).

# 🚀 Execution & Usage

### 1. Build the Image
docker build -t strict-mastery-engine .

### 2. Runtime Argument Injection
The engine accepts a comma-separated string of scores as a CLI argument:

docker run --rm strict-mastery-engine "60,75,86"

### 3. Expected Output (JSON)

{
  "status": "PIVOT",
  "weighted_score": 82.7,
  "volatility": 13.05,
  "attempts": 3,
  "reason": "Threshold not met within 3 attempts. Final S_v: 82.7%."
}

# 🤝 Contribution & Standards
This project follows the PEP 8 style guide and focuses on O(N) time complexity for score processing.

Lead Architect: S Aswin Deivanayagam
