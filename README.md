# Autonomous Test & Inspection Robot

An engineering portfolio project documenting the design and development of an autonomous mobile robot for inspection, data collection, and automated reporting.

## Project Objective

The goal is to design, build, test, and document a mobile robotic platform capable of navigating to inspection locations, collecting sensor and image data, evaluating results against defined criteria, and generating inspection records.

The project is intended to demonstrate a complete engineering workflow, including requirements definition, system architecture, hardware and software integration, robotics software development, test planning, validation, root cause analysis, technical documentation, and responsible AI-assisted engineering.

## Planned Technologies

- Ubuntu Linux
- ROS 2
- C++
- Python
- Raspberry Pi
- OpenCV
- Git and GitHub
- SQLite or another lightweight database

The technology stack may change as engineering decisions are evaluated and documented.

## Current Status

**Phase 0: Project definition and repository setup**

Current work includes establishing the repository structure, documenting the development philosophy and AI-assisted workflow, recording major engineering decisions, and preparing initial requirements and architecture documents.

## Planned Development Phases

1. **Phase 0: Project Definition**: goals, constraints, requirements, architecture, and roadmap.
2. **Phase 1: Environment and Hardware Bring-Up**: ROS 2 environment, platform selection, motors, power, and communications.
3. **Phase 2: Manual Mobile Platform**: manual driving, telemetry, camera streaming, encoders, and battery monitoring.
4. **Phase 3: Autonomous Navigation**: mapping, localization, obstacle detection, and autonomous movement.
5. **Phase 4: Inspection and Data Collection**: station identification, sensor capture, acceptance criteria, and pass/fail logging.
6. **Phase 5: Reporting and Portfolio Completion**: reports, validation, demonstrations, and final presentation.

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── AI_USAGE.md
│   ├── DEVELOPMENT_PHILOSOPHY.md
│   └── ENGINEERING_DECISIONS.md
├── hardware/
├── software/
├── images/
└── reports/
```

Additional directories will be added only when they become useful.

## Documentation

- [AI Usage](docs/AI_USAGE.md)
- [Engineering Decisions](docs/ENGINEERING_DECISIONS.md)
- [Development Philosophy](docs/DEVELOPMENT_PHILOSOPHY.md)

## Project Principles

1. Requirements explain why a feature exists.
2. Design decisions record alternatives and tradeoffs.
3. Code is understood, reviewed, and tested by the project author.
4. Failures and lessons learned are documented honestly.
5. Major milestones produce code, documentation, test evidence, and a demonstration.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
