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

**Phase 1: Software Foundation — In Progress**

The project currently includes:

- ROS 2 Jazzy development environment on Ubuntu 24.04 LTS
- Initial ROS 2 workspace and package structure
- `inspection_robot_bringup` package
- `robot_status_node` for publishing robot operating state
- `/robot_status` topic using ROS 2 publisher/subscriber communication
- Initial robot states: `INITIALIZING`, `READY`, `INSPECTING`, `FAULT`, and `SHUTDOWN`
- Automatic `INITIALIZING` → `READY` state transition

### Next Milestone

Develop inter-node robot control so that operating-state transitions can be requested and managed through ROS 2 communication.

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

## Internationalization

The software is being designed with internationalization (i18n) in mind from the beginning rather than treating multilingual support as a later enhancement. This is planned and not completed.

- [Project Languages](docs/LANGUAGES.md)
- [Translation Guide](docs/TRANSLATION_GUIDE.md)

Project goals include:

- Unicode support throughout the application
- External language resource files
- Easy addition of new languages without modifying application code
- Support for both left-to-right and right-to-left languages
- Separation of technical identifiers from user-facing text


### Planned Languages

| Language | Code | Status |
|-----------|------|--------|
| English | en | Primary |
| German | de | Planned |
| Slovak | sk | Planned |
| Spanish | es | Planned |
| Chinese (Simplified) | zh-CN | Planned |
| Japanese | ja | Planned |
| Khmer | km | Planned |
| Tagalog | tl | Planned |
| Hindi | hi | Planned |
| Arabic | ar | Planned |

English is the project's authoritative language. Additional translations will be added as the software and documentation mature. Community review by native speakers is encouraged for future translations.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
