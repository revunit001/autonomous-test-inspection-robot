# Engineering Decisions

This document records significant technical and project decisions so the reasoning behind choices is preserved.

## Decision Record Template

### EDR-XXX: Decision Title

**Status:** Proposed | Accepted | Superseded | Rejected  
**Date:** YYYY-MM-DD

#### Context
Describe the problem, constraint, or decision.

#### Options Considered
1. Option A
2. Option B
3. Option C

#### Decision
State the selected option.

#### Rationale
Explain why it was selected and the important tradeoffs.

#### Consequences
Describe benefits, limitations, risks, and follow-up actions.

---

## EDR-001: Use GitHub as the Primary Project Repository

**Status:** Accepted  
**Date:** 2026-07-25

### Context
The project requires public version control, documentation storage, issue tracking, milestone history, and a portfolio location for prospective employers.

### Options Considered
1. GitHub
2. GitLab
3. Local-only Git repository
4. Cloud storage without version control

### Decision
Use a public GitHub repository as the primary project repository.

### Rationale
GitHub provides version control, portfolio visibility, issue tracking, releases, documentation rendering, and broad familiarity among engineering teams.

### Consequences
Repository content must remain professional, understandable, and free of confidential information.

---

## EDR-002: Use the MIT License

**Status:** Accepted  
**Date:** 2026-07-25

### Context
The project is intended to be publicly viewable and reusable while preserving attribution and minimizing licensing complexity.

### Options Considered
1. MIT License
2. Apache License 2.0
3. GNU General Public License
4. No license

### Decision
Use the MIT License.

### Rationale
The MIT License is concise, widely recognized, permissive, and suitable for a personal engineering portfolio.

### Consequences
Others may reuse the software, including commercially, provided the license and copyright notice are retained. The software is provided without warranty.

---

## EDR-003: Develop Primarily in WSL Ubuntu

**Status:** Accepted  
**Date:** 2026-07-25

### Context
The planned stack includes ROS 2, C++, Python, CMake, colcon, OpenCV, and Linux-based target hardware.

### Options Considered
1. Native Windows
2. WSL Ubuntu
3. Dedicated Linux workstation
4. Development only on the robot computer

### Decision
Use WSL Ubuntu as the primary development environment during the initial phases.

### Rationale
WSL provides a Linux environment while retaining the existing Windows and VS Code workflow. It also builds practical Linux skills and aligns with the planned ROS 2 and Raspberry Pi environment.

### Consequences
Some graphical simulation, USB, networking, or hardware workflows may require additional configuration. Dedicated Ubuntu may be considered later if WSL becomes restrictive.
