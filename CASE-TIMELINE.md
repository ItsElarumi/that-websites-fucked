# Case Timeline

**Case ID:** `ELARUMI-EPIC-2026-001`  
**Subject:** `fortnitecompetitive[.]fun`  
**Timeline opened:** 25 November 2026  
**Status:** Open — registrar blocking confirmed by REG.RU's statement; clarification and Epic Games follow-up remain pending as last recorded.

This timeline records known investigation and reporting milestones in chronological order. Dates are included only where supported by the investigation record. Where an exact time or date is not available, that limitation is stated rather than inferred.

## 22 November 2026 — Investigation opened

- Elarumi began documenting concerns about the Fortnite-themed tournament website `fortnitecompetitive[.]fun`.
- The reported Discord invitation promoted an event described as "FNCS PRO-LEAGUE" and a team called "Falcons".
- The following website paths were recorded:
  - `fortnitecompetitive[.]fun/tournaments/falcons`
  - `fortnitecompetitive[.]fun/tournaments/falcons/login`
- Initial passive research recorded domain registration and DNS information. RDAP data listed REG.RU LLC as registrar and a registration date of 17 November 2026.
- Supplied website screenshots and technical captures were documented. The investigation report notes that their original capture circumstances and completeness were not all independently verified.
- The investigation was classified as **suspected phishing / possible brand impersonation**. Operator identity, Epic Games affiliation and credential theft were not established.
- The initial public investigation documentation was created.

## 23 November 2026 — Documentation and reporting expanded

- The public investigation website and expanded repository documentation were added or updated.
- A separate VirusTotal analysis of the **GitHub investigation repository URL** was documented. This was a scan of the Elarumi repository page, not the reported tournament website.
- Related EpicFishing research and passive third-party website-scan observations were documented, with limitations.
- The investigation report and Epic Games investigation status documentation were updated.
- The SHA-256 integrity manifest was refreshed following documentation changes.

## 25 November 2026 — REG.RU confirms domain blocking

- REG.RU's Abuse Review Department sent the written Russian statement: **"Домен заблокирован."**
- Translation: **"The domain has been blocked."**
- This confirms that REG.RU stated a blocking action had been applied. The response did not specify whether the domain registration itself was suspended, the technical mechanism, duration, legal basis, or whether a final policy finding had been made.
- Elarumi sent a follow-up notification to Epic Games Support informing it of REG.RU's blocking confirmation. The fact that the message was sent is recorded; delivery, reading and any resulting action are not independently established.
- Elarumi sent REG.RU a detailed clarification email under support reference `20261123373000095`. It asked about the type and duration of the restriction, DNS/access effects, whether it related to the abuse report, investigation findings, further action and evidence retention.
- REG.RU's response to that clarification request was pending at the time of this timeline's creation.
- Epic Games' response to the follow-up notification was also pending. Earlier correspondence had indicated that Epic Games was investigating, but no final finding or enforcement outcome was confirmed.
- The repository changelog and evidence register were added or updated to improve auditability and evidence tracking.
- The README and SHA-256 manifest were updated to link and account for the new records.

## Current position — 25 November 2026

| Item | Recorded position |
|---|---|
| REG.RU blocking statement | Confirmed in writing by REG.RU |
| Exact blocking mechanism | Not specified |
| Temporary or permanent | Not specified |
| Domain registration deleted | Not established |
| REG.RU clarification response | Pending |
| Epic Games investigation | Previously reported as ongoing |
| Epic Games follow-up outcome | Pending |
| Website operator identity | Not established |
| Epic Games affiliation | Not established |
| Credential collection or theft | Not established |
| Final phishing determination | Not established |

## Future entries

Add a dated entry when a material event occurs, such as:

- A reply from REG.RU clarifying the blocking action.
- A further response or final finding from Epic Games.
- New independently verifiable technical evidence.
- A material change in the domain's registration, DNS or accessibility status, with the observation date, method and source recorded.
- A correction to an earlier entry.

For each new event, preserve the original source, record the date and time with timezone where available, and distinguish the provider's exact statement from interpretation.

## Related records

- [Full investigation report](THAT-WEBSITES-FUCKED.md)
- [Evidence register](EVIDENCE-REGISTER.md)
- [Repository overview](README.md)
- [Changelog](CHANGELOG.md)
- [SHA-256 manifest](integrity/SHA256SUMS.json)
