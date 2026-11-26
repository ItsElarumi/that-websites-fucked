# Evidence Register

**Case ID:** `ELARUMI-EPIC-2026-001`  
**Subject:** `fortnitecompetitive[.]fun`  
**Register opened:** 25 November 2026  
**Last updated:** 26 November 2026  
**Register status:** Updated to include REG.RU's administrator-only disclosure response; Epic Games follow-up outcome remains pending.

This register indexes evidence and records its provenance and limitations. It is not a finding that the suspected conduct has been proven.

## Handling and verification rules

- Preserve original emails, screenshots, exports and files in their original form. Record collection dates and retain message headers or source metadata where available.
- Use working copies for redaction, annotation, translation or analysis. Do not overwrite originals.
- Do not publish passwords, session tokens, personal data or unnecessary identifiers.
- Distinguish **observed**, **supplied**, **reported**, **third-party result** and **corroborated** evidence. A report that an item exists is not the same as independently verifying its contents.
- Public repository documentation is a summary/index, not a substitute for original evidence. Sensitive or third-party-supplied originals are not published here.
- Record hashes for preserved files where practical. A hash supports later integrity checking; it does not prove authenticity, capture circumstances or truth.
- No credentials were submitted and no intrusive access, exploitation or disruption was performed as part of this investigation.

## Evidence index

| ID | Date / period | Item | Provenance and status | Limitations / handling |
|---|---|---|---|---|
| E-001 | Reported before 22 Nov 2026 | Discord invitation text promoting "FNCS PRO-LEAGUE" and a "Falcons" team | Text reproduced in the investigation report from material supplied to the investigation; **reported / supplied** | Sender identity, intent, account ownership and message authenticity have not been independently established. Preserve the original message or screenshot privately if available. |
| E-002 | By 22 Nov 2026 | Screenshot of the website preview / Fortnite-themed presentation | Report states that a screenshot was supplied by another person and downloaded for preservation; **supplied, not independently authenticated** | Original capture circumstances, completeness and authenticity have not all been independently verified. Not included in this public repository. |
| E-003 | 22 Nov 2026 | Website paths: `fortnitecompetitive[.]fun/tournaments/falcons` and `fortnitecompetitive[.]fun/tournaments/falcons/login` | URLs recorded in the investigation report; **reported observation** | Time-sensitive. Current availability or current page contents are not implied. No credentials were submitted. |
| E-004 | 22 Nov 2026 | Domain RDAP / registration information | Passive RDAP research recorded in the report: registration date 17 Nov 2026; registrar listed as REG.RU LLC; **passive lookup recorded** | Registrar data does not identify the beneficial domain owner or website operator and is not evidence of malicious intent. Retain the original RDAP response/export if available. |
| E-005 | 22 Nov 2026 | DNS lookup results | Passive DNS results recorded in the report, including A, AAAA, NS, SOA and absence of MX/TXT results in that lookup; **passive lookup recorded** | Results are point-in-time observations. Cloudflare-related records do not identify the origin server or operator. Absence in one lookup is not proof that a service or record never existed. |
| E-006 | 22 Nov 2026 | crt.sh certificate-transparency lookup | Lookup returned HTTP 502; **inconclusive third-party response** | Does not establish that no certificate existed or that HTTPS was unavailable. |
| E-007 | By 22 Nov 2026 | SSL/TLS details reported by an unidentified security-details source | Report records a supplied result stating valid certificate, HTTPS enabled and expiry 15 Feb 2027; **source unverified / not independently inspected** | Issuer, subject, SANs and original source output were not provided. Do not treat as independently verified certificate evidence. |
| E-008 | By 22 Nov 2026 | Two text captures of a Django debug error response and settings | Investigator-supplied captures described in the report; **supplied technical evidence, not independently reproduced** | Captures reportedly expose framework, paths, settings and request-environment details. Their original capture circumstances and completeness are not fully verified. Do not infer exploitability or successful access. Keep originals private and redact sensitive values before any sharing. |
| E-009 | 22 Nov 2026 onward | REG.RU abuse report and initial acknowledgement | Correspondence with registrar; support reference `20261123373000095`; **reported correspondence** | Preserve original sent message and full acknowledgement including headers. The acknowledgement alone was not an investigation outcome. |
| E-010 | Received by 25 Nov 2026 | REG.RU response: "Домен заблокирован." | Written response attributed to REG.RU Abuse Review Department; exact Russian text recorded in the report; **registrar action confirmed by its statement** | Translation: "The domain has been blocked." The excerpt does not specify mechanism, duration, legal basis, registration status, policy finding or operator identity. Preserve original email. |
| E-011 | 25 Nov 2026 | Detailed clarification email to REG.RU | User-confirmed sent correspondence in existing support thread `20261123373000095`; **sent, delivery/read status not independently established** | Requests clarification on block type and duration, DNS/access impact, relation to the report, investigation outcome, further action and evidence retention. REG.RU later replied; see E-015. Preserve sent copy. |
| E-012 | Before 25 Nov 2026 | Epic Games Support response | Response quoted in the investigation history: Epic said it was investigating further and would contact the reporter when research was complete or if more information was needed; **reported provider correspondence** | Does not establish a final finding, enforcement action or confirmation of phishing. Preserve original email and headers. |
| E-013 | 25 Nov 2026 | Follow-up notification to Epic Games Support about REG.RU's blocking confirmation | User-confirmed sent correspondence; **sent, delivery/read status not independently established** | No outcome from this follow-up was recorded at the time this register was created. Preserve sent copy and any later reply. |
| E-014 | 23 Nov 2026 | VirusTotal scan of the GitHub repository URL | Separate scan transaction documented in `VIRUSTOTAL-REPOSITORY-ANALYSIS.md`; **third-party scan result** | This scan concerns the Elarumi GitHub repository page, not `fortnitecompetitive[.]fun`. It is not evidence that the reported website is malicious or safe. |
| E-015 | After 25 Nov 2026 follow-up (exact reply timestamp not visible in supplied excerpt) | REG.RU clarification response: current block confirmed; detailed information restricted to domain administrator | Email response attributed to REG.RU's Abuse Review Department, received in the existing support thread; **provider statement supplied by the investigator** | Exact wording: “The domain is currently blocked. Detailed information regarding the block and the reasons for it can only be provided to the domain administrator.” Confirms REG.RU's stated current block and its disclosure limitation. Does not disclose the mechanism, duration, grounds, whether the action was specifically linked to report `20261123373000095`, any policy finding, evidence-retention status or operator identity. The original email and headers should be preserved privately. |

## Evidence storage and custody

The investigation report states that some screenshots and technical captures were supplied. The public repository does not contain all original evidence. This register does not claim that originals, full email headers, raw lookup outputs or cryptographic hashes have all been collected.

For each original item retained privately, add the following custody details when known:

| Field | Record |
|---|---|
| Evidence ID | E-___ |
| Original filename / format | Not yet recorded centrally |
| Collected by | Record the actual person or source |
| Collection date and time (UTC) | Record exact value or mark unknown |
| Original source / URL / sender | Record exact source |
| Storage location | Private, access-controlled location; do not publish sensitive paths |
| SHA-256 | Calculate from the preserved original, if available |
| Redacted working copy | Record filename and relationship to original |
| Verification notes | State what was checked and what remains uncertain |

Do not fill unknown fields by assumption. Mark them **unknown**, **not supplied** or **not yet verified** as appropriate.

## Current evidence assessment

- **Confirmed by provider statement:** REG.RU stated that the domain had been blocked.
- **Reported / supplied, not independently authenticated:** Discord invitation material, website screenshot and Django debug captures.
- **Passive observations:** RDAP and DNS lookup results.
- **Inconclusive:** crt.sh HTTP 502 response.
- **Unverified source:** reported SSL/TLS details.
- **REG.RU clarification:** Response received; detailed block information and reasons are restricted to the domain administrator. The mechanism, duration, grounds and relationship to the abuse report remain undisclosed.
- **Pending:** Epic Games follow-up outcome.
- **Not established:** website operator identity, Epic Games affiliation, credential collection or theft, successful compromise, permanent domain deletion, or a final phishing determination.

## Related records

- [Full investigation report](THAT-WEBSITES-FUCKED.md)
- [Repository overview](README.md)
- [Case changelog](CHANGELOG.md)
- [Separate VirusTotal repository-page analysis](VIRUSTOTAL-REPOSITORY-ANALYSIS.md)
- [SHA-256 manifest](integrity/SHA256SUMS.json)
