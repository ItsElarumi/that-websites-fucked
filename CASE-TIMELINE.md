# Case Timeline

**Case ID:** `ELARUMI-EPIC-2026-001`  
**Subject:** `fortnitecompetitive[.]fun`  
**Timeline opened:** 25 November 2026  
**Last updated:** 26 November 2026  
**Status:** Open — REG.RU says the domain is currently blocked; its clarification response limits detailed disclosure to the domain administrator. Epic Games follow-up remains pending.

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
- REG.RU later replied that the domain was currently blocked and that detailed information about the block and its reasons could only be provided to the domain administrator. The exact timestamp of this reply is not visible in the supplied email excerpt; see evidence item E-015.
- This response does not disclose the block mechanism, duration, grounds, whether the action was specifically linked to support reference `20261123373000095`, whether a policy violation was formally identified, or whether evidence was retained. It does not establish phishing or credential theft.
- Epic Games' response to the follow-up notification remained pending. Earlier correspondence had indicated that Epic Games was investigating, but no final finding or enforcement outcome was confirmed.
- The repository changelog and evidence register were added or updated to improve auditability and evidence tracking.
- The README and SHA-256 manifest were updated to link and account for the new records.

## 26 November 2026 — Cloudflare confirms report receipt

- Elarumi submitted a Phishing report to Cloudflare concerning `fortnitecompetitive.fun`, including the reported URLs and public GitHub investigation documentation.
- Cloudflare emailed confirmation that it had received the report and assigned **Report ID `a5b2a25e9ec2dec5`**.
- Cloudflare cautioned that this may be the only response due to report volume and that a personalised response may not be provided.
- Cloudflare clarified that it is not generally a website hosting provider and cannot remove content hosted by others. Its receipt does not establish that Cloudflare hosts or controls the reported website.
- No investigation finding, forwarding confirmation, removal or enforcement outcome was supplied. This event is recorded as evidence item E-016.

- The investigator supplied the HTML-rendered body of the Cloudflare receipt email for preservation. A text transcription was added as a supplemental E-016 artifact at `evidence/E-016-cloudflare-report-body-rendered.txt`. It is not the original .eml or raw MIME source; the original email and headers remain the authoritative private originals. The preserved body adds no investigation or enforcement outcome.

## Current position — 26 November 2026

| Item | Recorded position |
|---|---|
| REG.RU blocking statement | Confirmed in writing by REG.RU |
| Exact blocking mechanism | Not specified |
| Temporary or permanent | Not specified |
| Domain registration deleted | Not established |
| REG.RU clarification response | Received; detailed block information and reasons restricted to domain administrator |
| Epic Games investigation | Previously reported as ongoing |
| Epic Games follow-up outcome | Pending |
| Cloudflare Phishing report | Received; Report ID `a5b2a25e9ec2dec5` |
| Cloudflare investigation / enforcement outcome | Not provided / not established |
| Website operator identity | Not established |
| Epic Games affiliation | Not established |
| Credential collection or theft | Not established |
| Final phishing determination | Not established |

## Future entries

Add a dated entry when a material event occurs, such as:

- Any further REG.RU information that can be disclosed by the domain administrator or registrar.
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


## Supplemental E-016 email-header authentication

Proton Mail's recorded headers show SPF=pass, DKIM=pass for `notify.cloudflare.com` and `cloudflare-smtp.com`, and DMARC=pass. The message was received over TLS 1.3 from `bg-bc.cloudflare-smtp.com` (104.30.16.12). These results support authorised Cloudflare sending infrastructure but do not establish investigation or enforcement. The message body's reply address (`abusereply@cloudflare.com`) differs from the `Reply-To` header (`noreply@notify.cloudflare.com`); the discrepancy is documented without inferring its cause.
