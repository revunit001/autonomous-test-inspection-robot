# Translation Guide

## Purpose

This project is designed to support multilingual documentation and future multilingual user interfaces.

The goal is to improve accessibility while preserving technical accuracy and maintainability.

## Authoritative Language

English is the authoritative language for:

- Project requirements
- Engineering decisions
- Source code
- API documentation
- Test procedures
- Test results
- Safety-related technical records
- Git commit messages

When a translation differs from the English source, the English version controls until the translation has been reviewed and corrected.

## Supported Languages

| Language | Locale Code | Documentation Status |
|-----------|-------------|----------------------|
| English | en | Authoritative |
| German | de | Planned |
| Slovak | sk | Planned |
| Spanish | es | Planned |
| Chinese, Simplified | zh-CN | Planned |
| Japanese | ja | Planned |
| Khmer | km | Planned |
| Tagalog | tl | Planned |
| Hindi | hi | Planned |
| Arabic | ar | Planned |
| Russion | ru | Planned |

## Translation Principles

1. Preserve technical meaning rather than translating word for word.
2. Do not translate source-code identifiers.
3. Do not translate ROS topic names, class names, function names, filenames, or database identifiers.
4. Keep measurements, limits, warnings, and acceptance criteria technically accurate.
5. Use Unicode text encoding.
6. Clearly identify translations that have not been reviewed.
7. Safety-related translations require review by a fluent or native speaker.
8. Machine translation may be used only as a draft.
9. Do not represent machine-generated translations as professionally certified.
10. Update the translation status when a document changes.

## Translation Status Values

Use one of the following labels at the top of each translated document:

- Authoritative
- Draft
- Machine-translated draft
- Human-reviewed
- Needs update
- Planned

## Folder Structure

```text
docs/
├── en/
├── de/
├── sk/
├── es/
├── zh-CN/
├── ja/
├── km/
├── tl/
├── hi/
├── ar/
└── ru/
