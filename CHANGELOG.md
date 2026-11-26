# Changelog

All notable documentation, evidence and public-status changes to this repository are recorded here in reverse chronological order. Dates are UTC where commit timestamps are available.

This changelog records repository changes; it does not replace the underlying evidence or establish claims beyond the cited source material.

## [Unreleased]

_No unreleased changes recorded._

## [2026-11-26]

### Added
- Recorded Cloudflare's email confirmation that it received the Phishing report concerning `fortnitecompetitive.fun`; Cloudflare Report ID: `a5b2a25e9ec2dec5`.
- Added evidence item E-016 and updated the main report, evidence register, case timeline, README and public investigation page.
- Recorded Cloudflare's clarification that it is not generally a website hosting provider and cannot remove material hosted by others.
- Refreshed the SHA-256 integrity manifest for updated documents and public page.

### Evidence and status limitations
- Cloudflare's email confirms receipt only. It warns that this may be the only response and supplies no investigation finding, forwarding confirmation, removal or enforcement outcome.
- Cloudflare's clarification does not establish whether it provides any service to the reported domain or who hosts the website.

### Added
- Added evidence item E-015 documenting REG.RU's clarification response that the domain is currently blocked and detailed information about the block and reasons is restricted to the domain administrator.

### Updated
- Updated the evidence register, case timeline and investigation report to distinguish the newly received clarification response from the earlier blocking confirmation.
- Recorded that REG.RU's reply does not disclose the blocking mechanism, duration, grounds, whether the action was specifically linked to the abuse report, a formal policy finding, or evidence-retention status.
- Updated the repository overview and public investigation page so the latest case status no longer describes REG.RU's clarification response as pending.
- Updated the classroom presentation to reflect the new evidence and the remaining uncertainties.
- Refreshed the SHA-256 manifest for the changed repository documents and public page.

### Evidence and status limitations
- REG.RU's administrator-only disclosure statement does not prove phishing, credential collection or theft, operator identity, or the reason for the block.
- The exact timestamp of REG.RU's clarification reply is not visible in the supplied email excerpt.
- Epic Games' follow-up outcome remains unconfirmed.

## [2026-11-25]

### Added
- Added this repository changelog to make material documentation and publication changes auditable.

### Updated
- Recorded REG.RU's written response, **"Домен заблокирован"** ("The domain has been blocked"), concerning `fortnitecompetitive[.]fun`.
- Clarified that the registrar's statement confirms a blocking action but does not disclose its technical scope, duration, legal basis, or whether the domain registration itself was suspended.
- Documented Elarumi's detailed follow-up to REG.RU under support reference `20261123373000095`, requesting clarification about the restriction, investigation and evidence retention. A response was pending at the time of the update.
- Documented Elarumi's follow-up notification to Epic Games Support about REG.RU's blocking confirmation. No outcome from Epic Games was confirmed.
- Updated the main investigation report, repository overview and public investigation website to reflect the latest documented position.
- Refreshed SHA-256 entries for the updated report, README and public website.

### Evidence and status limitations
- No provider confirmation of credential theft, website operator identity, or a final phishing determination was recorded.
- The available REG.RU response did not establish whether blocking was temporary or permanent.
- Epic Games' previously reported statement that it was investigating remained without a confirmed final outcome.

## [2026-11-23]

### Added
- Added the public investigation website and expanded project documentation.
- Added a separate VirusTotal repository security-analysis record, documenting the scan context and its limitations.
- Added documentation of related EpicFishing research findings and passive third-party website-scan observations.

### Updated
- Updated the investigation report and Epic Games investigation status.
- Refreshed the SHA-256 integrity manifest after report changes.

## [2026-11-22]

### Added
- Initial investigation documentation for case `ELARUMI-EPIC-2026-001`, concerning the reported Fortnite-themed tournament website `fortnitecompetitive[.]fun`.
- Initial evidence and reporting context, including the reported tournament and login URLs, responsible-research boundaries, and uncertainty around attribution and suspected credential collection.

---

For the detailed incident chronology, evidence descriptions, reporting correspondence and current case status, see [THAT-WEBSITES-FUCKED.md](THAT-WEBSITES-FUCKED.md).


### Supplemental E-016 email-header authentication
- Recorded recipient-side SPF, DKIM and DMARC pass results, plus TLS 1.3 transport metadata.
- Documented the difference between the email body's stated reply address and the Reply-To header.
- Excluded the recipient address, bounce token, Message-ID and raw signature values from the public repository.
