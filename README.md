# THAT WEBSITE'S FUCKED.
## SCAMMERS. WE SEE YOU.

**STOP TARGETING PLAYERS. STOP HIDING BEHIND FAKE TOURNAMENTS.**

This is Elarumi's public anti-scam investigation into a suspicious Fortnite-themed tournament invitation and website.

We are calling out suspicious activity that could put players' accounts and personal information at risk. Players deserve real tournaments, genuine opportunities and safe communities — not suspicious login pages dressed up as esports.

**Case:** ELARUMI-EPIC-2026-001
**Investigation date:** 22 November 2026
**Prepared by:** Elarumi
**Classification:** Suspected phishing / possible brand impersonation


## 🔴 INDEPENDENCE DISCLAIMER

**NO MEMBER OF THE ELARUMI INVESTIGATION TEAM OWNS OR OPERATES THE WEBSITE UNDER INVESTIGATION.**

We are independent investigators. We do not control, develop, endorse, promote or represent the website or its operators.

We strongly oppose deceptive activity that could put players and their accounts at risk. We are documenting concerns and reporting them — **we are not running the website.**

---

**Read the full investigation:** [THAT-WEBSITES-FUCKED.md](THAT-WEBSITES-FUCKED.md)

## WHAT WE'RE CALLING OUT

A Discord invitation promoted a tournament called "FNCS PRO-LEAGUE", encouraged someone to join a team called "Falcons", and directed them towards a Fortnite-themed website.

That combination raised serious concerns about possible phishing and brand impersonation.

**Players: do not enter your Epic Games password into suspicious tournament websites. Verify competitions through official channels.**

## THE EVIDENCE MATTERS

The investigation documents the observed invitation, domain registration information, DNS records, reported certificate details and investigator-supplied captures of a Django debug error response.

These findings justify scrutiny and reporting. They do not independently prove credential theft, identify the website operator or establish an affiliation with Epic Games.

## TECHNICAL SECURITY FINDING

**A PUBLIC DJANGO DEBUG PAGE EXPOSED THE BACKEND CONFIGURATION.**

Investigator-supplied captures show `DEBUG=True` and disclose a backend fingerprint including the `epicfishing` project, its `/home/epicfishing` application path, SQLite database configuration, the `frontend` app, a GeoIP data-file path, permissive host/CORS settings and multiple CSRF trusted origins.

Cloudflare-related headers do not identify the actual origin server. Secret key and password values were masked. This is a serious potential information disclosure and security misconfiguration — not proof of credential theft, database access or successful exploitation.

See the full report for the technical details and limitations.

## ACCOUNTABILITY, NOT GUESSWORK

Relevant organisations and reporting channels are documented in the full report, including REG.RU, Cloudflare, Epic Games and Discord.

Their inclusion does not imply that they operate the website or have confirmed wrongdoing. Reporting outcomes remain subject to confirmation.

No credentials were submitted. No unauthorised access, exploitation or disruption was performed.

## RESPONSIBLE DISCLOSURE

This repository does not publish private correspondence, account identifiers, screenshots supplied by another person or the original evidence archive. The domain is deliberately defanged to reduce accidental visits.

We are here to document, warn and demand responsible action — not to encourage harassment or retaliation.

**SCAMMERS: PLAYERS ARE NOT YOUR TARGET PRACTICE.**

**FUCK SCAMMERS. PROTECT THE PLAYERS.**

— Elarumi
