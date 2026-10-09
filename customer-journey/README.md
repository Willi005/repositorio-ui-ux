# Definitive Customer Journey

Definitive submission provided by the team: **Customer Journey · William.pdf**. It replaces the earlier journey versions. The profile is the cargo driver named William in the UX persona title and Guillermo in its description; the supplied PDF's name and content are preserved.

[View the definitive PDF](Customer%20Journey%20%C2%B7%20William.pdf) · [PNG preview](definitivo.png) · [UX persona](../ux-personas/2.png).

[![William's definitive Customer Journey](definitivo.png)](Customer%20Journey%20%C2%B7%20William.pdf)

## Reading the journey

The English map represents the driver's search for guidance about hours he considers unpaid and his preparation for a Labor Directorate consultation. It contains twelve actions, an emotional curve, and rows for value, barriers, and opportunities.

| Stage | Document actions |
| --- | --- |
| Search | Review payslips; ask a colleague; search online and encounter conflicting sources. |
| Verification | Describe transport, working hours, and payments; review the cited rule and confidence; identify missing information and limits. |
| Guidance | Organize documents; choose a discreet DT channel; prepare the consultation. |
| Follow-up | Contact DT; save the summary and receipt; review pending items and resume guidance. |

The key moment is identifying the applicable working time rule, with its citation and confidence, before interpreting payment. The document explicitly states that the journey is proposed, emotions are hypotheses, and outcomes are not guaranteed.

## Files

The **user-provided PDF is the submission source** and is preserved without modification. `definitivo.png` renders its single page for direct display on GitHub. The Google drawing link and older copies were removed from the current submission; Git preserves their history.

Reproduce the preview with Poppler:

```bash
pdftoppm -png -singlefile -scale-to 2800 'customer-journey/Customer Journey · William.pdf' customer-journey/definitivo
```

Run from the repository root. A new version should replace the PDF and regenerate the image so both represent the same submission.
