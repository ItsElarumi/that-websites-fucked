# THAT WEBSITE'S FUCKED.
## SCAMMERS. WE SEE YOU.

**STOP TARGETING PLAYERS. STOP HIDING BEHIND FAKE TOURNAMENTS.**

This is Elarumi's independent cybersecurity, scam-awareness and player-safety investigation project.

## LATEST CASE UPDATE — REG.RU CONFIRMS DOMAIN BLOCKING

REG.RU's Abuse Review Department has subsequently replied to Elarumi's abuse report concerning `fortnitecompetitive[.]fun` with:

> Домен заблокирован.

Translation: "The domain has been blocked."

This confirms that REG.RU applied a blocking action to the domain. The supplied email excerpt does not establish whether the block is temporary or permanent, whether the registration has been deleted, or whether the website operator has been identified. This is a confirmed registrar response, not a conclusive finding of phishing or credential theft.

**Case:** `ELARUMI-EPIC-2026-001`  
**Registrar outcome:** Domain blocking confirmed  
**Epic Games:** Support previously confirmed further investigation; findings and outcomes remain unconfirmed.

See the [full investigation and reporting history](THAT-WEBSITES-FUCKED.md).


We document suspected phishing, possible brand impersonation, suspicious gaming websites, fraudulent tournament invitations, exposed technical information and online scam activity. Our goal is to help players recognise threats, protect their accounts and make safer decisions online.

### OUR MISSION

**Protect players. Expose suspicious activity. Promote safer gaming communities.**

We believe in transparency, responsible research, digital awareness and accountability. We aim to:

- Investigate suspicious websites and online activity using responsible, evidence-led methods.
- Analyse publicly available information and document observable technical findings.
- Preserve a clear record of evidence, reporting attempts and confirmed responses.
- Help gamers recognise phishing attempts, suspicious invitations and deceptive login pages.
- Share practical account-security and online-safety guidance.
- Communicate relevant findings to platforms, service providers and appropriate abuse-reporting organisations.

### RESEARCH AND PUBLICATIONS

This repository contains independent investigation reports, technical observations, security analysis, responsible-disclosure records, evidence-integrity information and player-protection resources.

Our research distinguishes between directly observed information, investigator-supplied material, third-party findings and unverified claims. We document limitations and avoid presenting suspicion as proof.

### RESPONSIBLE RESEARCH PRINCIPLES

- No unauthorised access, exploitation or deliberate disruption.
- No submission of credentials to suspicious websites.
- No unsupported attribution of website ownership or operator identity.
- No publication of passwords, session tokens or unnecessary personal information.
- Responsible reporting and clear documentation of confirmed outcomes.
- No encouragement of harassment, threats or retaliation.

This is an independent project. It is not an official security team, law-enforcement body or representative of any platform mentioned in its research.

**THAT WEBSITE'S FUCKED. SCAMMERS. WE SEE YOU.**

We are calling out suspicious activity that could put players' accounts and personal information at risk. Players deserve real tournaments, genuine opportunities and safe communities — not suspicious login pages dressed up as esports.

**Case:** ELARUMI-EPIC-2026-001
**Investigation date:** 22 November 2026
**Prepared by:** Elarumi
**Classification:** Suspected phishing / possible brand impersonation


## 🔴 INDEPENDENCE DISCLAIMER

**NO MEMBER OF THE ELARUMI INVESTIGATION TEAM OWNS OR OPERATES THE WEBSITE UNDER INVESTIGATION.**

We are independent investigators. We do not control, develop, endorse, promote or represent the website or its operators.

We strongly oppose deceptive activity that could put players and their accounts at risk. We are documenting concerns and reporting them — **we are not running the website.**

## INVESTIGATION DISCLAIMERS

- **Evidence limitation:** Some screenshots and captures were supplied to the investigation by another person or were investigator-supplied materials. They have not all been independently reproduced or authenticated.
- **Identity limitation:** The website operator, domain owner’s real-world identity and any affiliation with Epic Games have not been independently established.
- **Third-party neutrality:** Mentioning Epic Games, Discord, Cloudflare, REG.RU or another service provider does not mean that provider owns, operates, endorses or is responsible for the website.
- **No exploitation:** We did not submit credentials, attempt unauthorised access, exploit the website or deliberately disrupt its operation.
- **Time limitation:** Findings describe observations available on the stated investigation date. Website content, configuration and risk can change.
- **Rating limitation:** The risk score below is an investigator-defined assessment of documented warning signs. It is not a certified industry rating, legal finding, probability of fraud or proof of criminal conduct.

## PROVISIONAL WEBSITE RISK RATING

**70/100 - HIGH RISK**

**Evidence confidence: Limited.** This is a provisional, judgement-based score. Some indicators rely on supplied captures, and certain technical indicators arise from the same debug response. The categories may overlap; the total must not be interpreted as a statistical measurement.

| Documented indicator | Points |
|---|---:|
| Public Django debug response exposing application and implementation details | 25 |
| Disclosed configuration settings that warrant security review | 15 |
| Fortnite-themed presentation raising possible brand-impersonation concerns | 15 |
| Reported Discord tournament invitation directing users towards the site | 10 |
| Recent domain registration — contextual indicator only | 5 |
| **Provisional total** | **70/100** |

**Rating scale:** 0–19 Low · 20–39 Guarded · 40–59 Elevated · 60–79 High · 80–100 Critical.

The score does not establish that credentials were collected or stolen, that the site was operated by a particular person, or that the site is affiliated with Epic Games. A recent registration is not, by itself, evidence of malicious activity.

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

Their inclusion does not imply that they operate the website or have confirmed wrongdoing. REG.RU has confirmed that the reported domain is blocked; the permanence and precise basis of that action are unknown. Epic Games Support previously confirmed further investigation, but its findings and any action remain unconfirmed.

No credentials were submitted. No unauthorised access, exploitation or disruption was performed.

## RESPONSIBLE DISCLOSURE

This repository does not publish private correspondence, account identifiers, screenshots supplied by another person or the original evidence archive. The domain is deliberately defanged to reduce accidental visits.

We are here to document, warn and demand responsible action — not to encourage harassment or retaliation.

**SCAMMERS: PLAYERS ARE NOT YOUR TARGET PRACTICE.**

**FUCK SCAMMERS. PROTECT THE PLAYERS.**

- Elarumi

---

## 🛡️ PLAYER PROTECTION

Your gaming account is worth protecting.

Read our [Player Protection Guide](PLAYER-PROTECTION.md) for official Epic Games security guidance, general player safety advice and a personal message from Elarumi.
