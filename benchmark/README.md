# Labor rights guidance requires verifiable trust

**The project's opportunity is to help workers understand their situation before starting an official procedure, with visible evidence and an appropriate referral.** Dirección del Trabajo (DT, the Labor Directorate), SUSESO, and ChileAtiende provide complementary patterns: access by profile, preparation and tracking, and explanation by need. Their public screens also show friction relevant to the UX personas: jargon, help far from the decision point, and actions whose prominence does not match the need to understand first. This study compares experiences; it does not determine individual rights or constitute a legal audit of the institutions. The team's proposal remains a concept, and its capabilities are not presented as implemented. The benchmark informs the [Customer Journey](../customer-journey/README.md) and the subsequent prototype.

## Three categories support comparison across different mandates

The research question is how to provide understandable, verifiable guidance about first medical leave, unpaid overtime, and severance settlements without turning an explanation into a legal decision. The observation date is **October 5, 2026**. We reviewed official sources and nine public screenshots, three per service, captured with a visible area of 866 × 922 pixels. This sample supports observations about pages, labels, hierarchy, and an expanded accordion; it does not represent entire flows or all devices. None of the reviewed pages published a product version number. A page's update date is not a product version.

The initial ecosystem considered DT/Mi DT, SUSESO, ChileAtiende, BCN/Ley Chile, and ChatGPT. **DT is the direct functional comparison**, because it offers labor guidance and procedures. SUSESO is a **sector analogue**, because it supports preparation, complaints, and tracking in social security. ChileAtiende is an **information design and referral reference**. These three cover the repository's scenarios and support comparison of public interfaces across distinct responsibilities. DT's consultation center organizes labor topics; SUSESO specifies the institutions and matters under its supervision; ChileAtiende communicates benefits, requirements, and channels. These categories are methodological choices of this study. ([DT](https://www.dt.gob.cl/portal/1628/w3-channel.html), [SUSESO](https://www.suseso.gob.cl/601/w3-propertyvalue-10381.html), [ChileAtiende](https://www.chileatiende.gob.cl/que-es-chileatiende)).

BCN/Ley Chile remains a supplementary legal source, but is excluded from the main matrix because its documentary focus differs from the preparation and referral experience studied; its search interface was not inspected. ChatGPT is acknowledged as a general conversational substitute and excluded from the three institutional experiences because of its different scope. Its documentation acknowledges incorrect answers and the need to verify information. This limitation reinforces the trust problem but does not evaluate its performance on labor questions. The selection establishes neither market leadership nor the absence of commercial alternatives. ([Ley Chile](https://www.bcn.cl/leychile/Consulta/), [OpenAI documentation](https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth)).

The inventory identifies reviewed platforms and destinations; it is not a market census.

| Name | Platform and official URL | Classification | Matrix selection |
| --- | --- | --- | --- |
| Dirección del Trabajo / Mi DT | Institutional website and procedure portal: [dt.gob.cl](https://www.dt.gob.cl/portal/1626/w3-channel.html) | Direct functional comparison | Included: labor guidance and preparation for severance/overtime questions. |
| SUSESO | Institutional website and PAE access: [suseso.gob.cl](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html) | Sector analogue | Included: medical leave, complaint preparation, and tracking. |
| ChileAtiende | Information website: [chileatiende.gob.cl](https://www.chileatiende.gob.cl/que-es-chileatiende) | Design reference | Included: everyday language, actions, and channels. |
| BCN / Ley Chile | Legal information web application: [Ley Chile](https://www.bcn.cl/leychile/Consulta/) | Supplementary source | Excluded: documentary focus; retained as a legal reference. |
| ChatGPT | Web conversational assistant: [official documentation](https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth) | General conversational substitute | Excluded: scope differs from the three institutional services. |

The [comparison matrix](tabla-comparativa.md) applies ten assignment dimensions—identification, profile, value, prioritized features, onboarding, navigation, design, observable accessibility, strengths, and problems—and four domain dimensions: legal traceability, limits and uncertainty, competent referral, and privacy/control. It distinguishes **observed**, **documented**, and **proposed** capabilities. Associations with Nielsen interpret interface evidence; they are not test results or measured severity scores. H2 concerns familiar language; H3, control; H4, consistency; H5, error prevention; H6, recognition; H8, relevant hierarchy; and H10, contextual help. ([Nielsen's heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)).

## DT provides authority, but evidence is distant from the decision

DT is relevant to William and Joseph: it supports labor rights consultation and access to formal services. Features are prioritized here by relevance to these scenarios: topic guidance, procedure preparation, Mi DT access, and human assistance. **Public reading precedes authentication.** Documentation describes RUN and ClaveÚnica for Mi DT access; the account and internal onboarding were not inspected. Employer and worker routes are kept distinct. ([Mi DT access](https://www.dt.gob.cl/portal/1628/w3-article-116464.html), [Documented profiles](https://www.dt.gob.cl/portal/1628/w3-article-116467.html)).

DT01 shows worker and employer cards: the first strength is a recognizable, relevant profile (H6). DT03 shows SUAC and telephone help alongside a legal framework link: the second strength is verifiable assistance (H10). However, a tax credential notice for labor representatives occupies the top of DT01 before the worker entry. For Joseph's guidance goal, this introduces information for another profile ahead of his task (H8). In DT02–DT03, the long page and legal evidence at the bottom require scrolling and connecting that evidence to the initial explanation (H6/H8). These are potential discoverability problems, not evidence of abandonment. ([DT homepage](https://www.dt.gob.cl/portal/1626/w3-channel.html), [Severance page](https://dt.gob.cl/portal/1626/w3-article-117245.html)).

The page explains procedures and documents, but the term for an authorized attesting official remains without a glossary in the observed fragment. An external manual adds instructions without replacing brief contextual help. Institutional blue, large cards, and section headings dominate the visual design. Text size controls are visible, and DT01 shows horizontal scrolling; neither observation establishes full accessibility. The public route observed was homepage → [Workers](https://www.dt.gob.cl/portal/1626/w3-propertyvalue-26864.html) → severance page: three pages. Screenshots cover the homepage and upper/lower parts of the information page. Mi DT's transactional depth remains unknown. ([DT information page](https://dt.gob.cl/portal/1626/w3-article-117245.html)).

![DT01: profile entry and preceding notice](capturas/direccion-trabajo/01-anotada.png)
*DT01. Recognizable profiles; the representatives' notice precedes the worker entry.*

![DT02: severance description and requirements](capturas/direccion-trabajo/02-anotada.png)
*DT02. Description and documents; an external manual does not replace a brief contextual glossary.*

![DT03: support and legal framework at the bottom](capturas/direccion-trabajo/03-anotada.png)
*DT03. Help and legal evidence are available at the end of a long information page.*

## SUSESO separates intentions but requires institutional vocabulary

SUSESO is especially relevant to Benjamin because of its social security services. The relevant functional order is guidance, supporting document preparation, estimated benefit simulation, complaint submission, and tracking. SU01 distinguishes filing a complaint from tracking it: **the first strength is recognizable actions** that separate starting and checking (H6). SU02 offers guidance for workers, families, and other needs: the second strength is classification by profile and situation (H2/H6). No real case file was inspected, and selection time was not measured. ([Users](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html), [Guidance tool](https://www.suseso.gob.cl/606/w3-propertyname-509.html)).

The observed sequence was guidance tool → workers → medical leave → two situations. SU03 presents rejection/modification and the absence of a COMPIN decision. For a first medical leave, the formal wording for an issued decision and the institutional acronym require prior knowledge without a visible definition in that fragment: **the first problem is jargon** (H2). The side text size control also partly covers the Back control in the captured area: the second problem is interference with leaving the screen (H3/H8). Options are large, with apparent blue/white contrast, but contrast was not measured. The overlap applies to the captured window size; it is not generalized to all devices. ([Medical leave guidance](https://www.suseso.gob.cl/606/w3-propertyvalue-586.html)).

The public simulator declares that its result is an estimate and defines which cases it covers. This transferable pattern explains assumptions before presenting a figure. The published complaint lifecycle documents preparation, review, and status checks, but does not establish that current private screens exactly match the tutorial. The login screen offers ClaveÚnica and tax credentials. A historical reference to creating a password is not treated as a verified current personal access option. ([Simulator](https://www.suseso.gob.cl/606/w3-article-711911.html), [Complaint lifecycle](https://www.suseso.gob.cl/606/w3-propertyvalue-562466.html), [PAE login](https://pae.suseso.gob.cl/pae-web/loginCiudadano)).

![SU01: separate complaint and tracking actions](capturas/suseso/01-anotada.png)
*SU01. Starting and tracking a complaint are separate actions; the simulator is presented as an estimate.*

![SU02: guidance organized by profile](capturas/suseso/02-anotada.png)
*SU02. Profile selection prepares the route before authentication is requested.*

![SU03: medical leave situations and overlapping control](capturas/suseso/03-anotada.png)
*SU03. Institutional language and partial overlap of the Back control at the observed window size.*

## ChileAtiende explains actions and must balance help with procedures

ChileAtiende is an information reference, rather than the authority deciding a labor case. Its capabilities are ordered by relevance: explaining the need, requirements and steps, referral to the responsible institution, and channel selection. Joseph's information page supports observation of public reading → expanded ratification section → external DT link or an in-person alternative; the procedure was not completed. **January 27, 2026** appears as the page's last update date. ([Severance information](https://www.chileatiende.gob.cl/fichas/33522)).

The first strength in CA01 is an explanation of the technical term for grounds as a reason: it translates specialized vocabulary (H2). The second strength in CA02 is the separation of obtaining and ratifying a settlement, with expandable information and explicit destinations (H6/H8). Free advice is linked in the description. However, the fixed bar gives ratification more prominence than Help. For Joseph, who seeks understanding before action, that hierarchy deserves review (H8). The issue is the action's priority relative to the scenario's goal. ([Severance page](https://www.chileatiende.gob.cl/fichas/33522)).

CA03 shows remote and in-person channels through explanatory cards. The header and typography change between the information page and the service network: **the second problem is visual consistency** (H4). Social media appears before service channels, another priority poorly aligned with an urgent need (H8). Underlined links and the visible outline of the expanded accordion help identify interaction; keyboard and screen reader behavior were not tested. The portal should not receive credit for deciding cases, uploading documents, or calculating settlements: information pages refer users to the responsible service. ([Service network](https://www.chileatiende.gob.cl/red-de-atencion)).

![CA01: severance explanation and fixed action](capturas/chileatiende/01-anotada.png)
*CA01. Term explanations and date are visible; ratification visually dominates help.*

![CA02: ratification alternatives](capturas/chileatiende/02-anotada.png)
*CA02. The expanded section identifies DT, ClaveÚnica, and an in-person alternative.*

![CA03: service network and channel cards](capturas/chileatiende/03-anotada.png)
*CA03. Channels are explained; social media comes first and the visual treatment differs from the information page.*

## The prototype should prioritize understanding, evidence, and control

**Garrett: Strategy.** The concept is guided by the need to understand with evidence before acting. Its product objective is referral to the appropriate authority with explained confidence. The following priorities are **proposals for team validation, not approved decisions**. Findings refine the [Canvas](../value_proposition.png) and [UX personas](../ux-personas/). For Benjamin, we propose adopting SUSESO's situation entry and progressive preparation, while avoiding jargon at entry or premature complaints. For William, we propose DT's official sources and human support, while avoiding identification requests for initial general guidance or promises of no retaliation. His occupation alone does not establish the applicable working time regime: the route must ask about transport type and available records first. For Joseph, we propose ChileAtiende's everyday explanations and alternatives, while avoiding greater prominence for signing than understanding. These are **design hypotheses**, not preferences confirmed with users. ([DT sector consultation](https://dt.gob.cl/portal/1628/w3-article-60075.html)).

**Garrett: Scope.** We propose a focused prototype route: select the problem, collect minimal context, explain with a source and review date, identify missing information, and prepare a referral. The source should accompany its claim rather than remain at the end of a document. The confidence level proposed in the Canvas should use understandable reasons—source relevance, missing evidence, or discrepancies—without arbitrary percentages or a label implying legal certainty. The feature map summarizes observed, documented, and proposed capabilities.

![Benchmark feature map](feature-map.png)
*Feature map. The team's proposal is a hypothesis; documented capabilities do not equal executed tests.*

A second priority is continuity: a reviewable summary, document checklist, and human guidance alternative. Information should be saved only at the user's explicit choice, with its use explained and deletion available. **Retention policies and deletion controls were not verified** for the three references. Public reading demonstrates that information can be offered without login, but does not prove an absence of tracking. The benchmark does not recommend collecting medical evidence to explain first medical leave or storing employment documents in the first version.

The Canvas proposes automatic referral to the Labor Inspectorate for complex cases. The research requires refining that destination: **referral depends on subject and stage**. DT guides labor matters, while medical leave routes may require COMPIN or SUSESO. A discrepancy between official summaries should not become an individual instruction: show the limit and verify the competent source. Signing or submitting procedures, definitive severance calculations, medical diagnosis, legal determinations, and guarantees of complaint success are excluded from the initial scope. ([DT appeal guidance](https://www.dt.gob.cl/portal/1628/w3-article-95287.html), [SUSESO compendium](https://www.suseso.gob.cl/622/w3-propertyvalue-788701.html)).

## The next evidence should test understanding before action

**The current status is phase 2 documentary research with public interface inspection.** Supervised use of authenticated flows, accessibility checks, and team validation of findings and priorities remain pending. This review is not attributed to meetings, interviews, reviews, or tests that did not occur. To advance, the team should agree on equivalent scenarios for each persona and observe whether participants can explain their situation, locate supporting evidence, and select appropriate help without confusing guidance with an official decision.

The [Customer Journey](../customer-journey/README.md) translates these hypotheses into touchpoints and opportunities; its emotions must be identified as inferred. Later evaluation should especially observe three errors: Benjamin starts a complaint inappropriate to his stage; William applies a working time rule without classifying his work; Joseph interprets an answer as authorization to sign. Reducing these confusions is a more useful criterion for this project than counting features or declaring a winner among portals with different mandates.

## LaTeX submission report

[APA 7 formatted PDF](benchmark.pdf) · [Sources, UFRO cover, and build instructions](latex/README.md). The format revision is dated October 8, 2026; findings and screenshots retain their October 5 observation date. The report includes author-date citations, alphabetical references, five tables, and ten figures. The institutional cover was adapted from the Networks report specified by the user.
