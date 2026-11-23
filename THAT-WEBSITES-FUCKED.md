# THAT WEBSITE'S FUCKED

## Independent security investigation

**Case ID:** ELARUMI-EPIC-2026-001
**Prepared by:** Elarumi
**Investigation date:** 22 November 2026
**Classification:** Suspected phishing / possible brand impersonation
**Status:** Reports submitted to some relevant parties; outcomes unconfirmed.

---

## 🔴 INDEPENDENCE DISCLAIMER - WE ARE NOT AFFILIATED

> **NO MEMBER OF THE ELARUMI INVESTIGATION TEAM OWNS, OPERATES, CONTROLS, DEVELOPS OR REPRESENTS THE WEBSITE UNDER INVESTIGATION.**
>
> Elarumi and the investigation team are independent of the website and its operators. We do not own it, run it, maintain it, endorse it, promote it or act on behalf of whoever is responsible for it.
>
> **WE DESPISE THE DECEPTION AND THE RISK IT CAN CREATE FOR PLAYERS.** We strongly oppose attempts to mislead people, impersonate trusted gaming brands or put players' accounts and personal information at risk.
>
> Our involvement is to document the available evidence, warn players and report our concerns through appropriate channels. We are not participating in, facilitating or profiting from the activity being investigated.
>
> **WE ARE REPORTING THIS WEBSITE. WE ARE NOT RUNNING IT.**
>
> This investigation uses the classification *suspected phishing / possible brand impersonation*. The identity and actions of the website's operator have not been independently established. Our criticism is directed at the suspicious activity documented in this report, not at an identified individual.

---

## INVESTIGATION DISCLAIMERS AND LIMITATIONS

These disclosures apply to the entire report:

1. **Independence:** Elarumi and the investigation team do not own, operate, control, develop, endorse or represent the website under investigation.
2. **Evidence provenance:** Some screenshots and technical captures were supplied to the investigation. Their original capture circumstances, authenticity and completeness have not all been independently verified. The Django debug response has not been independently reproduced by this investigation.
3. **Unverified identity and affiliation:** The identity of the website operator and any relationship with Epic Games or another organisation have not been established.
4. **Third-party neutrality:** References to Epic Games, Discord, Cloudflare, REG.RU, DNS providers or infrastructure services identify relevant services or reporting channels only. They do not establish that those parties operate, endorse or are responsible for the website.
5. **No credential or access testing:** No credentials were submitted. No attempt was made to gain unauthorised access, exploit the website, access its database or disrupt its operation. Credential theft and successful exploitation have not been demonstrated.
6. **No attribution from network metadata:** Cloudflare-related DNS records and request headers do not establish the origin server, website operator or physical location of the operator.
7. **Time sensitivity:** This report records observations available on 22 November 2026. The website and its configuration may have changed since then. The report is not a guarantee of its current state.
8. **Rating methodology:** The risk score is a provisional investigator-defined heuristic, not a certified security standard, legal finding, statistical probability or proof of criminal conduct. The score is limited by the evidence and assumptions disclosed below.

## PROVISIONAL WEBSITE RISK RATING

**70/100 - HIGH RISK**

**Evidence confidence: Limited.** The score reflects the warning signs documented in this report. It is a structured judgement, not a scientifically validated measurement. Some indicators rely on supplied captures, and the debug disclosure and configuration indicators arise from the same supplied response and may overlap.

### Scoring breakdown

| Indicator | Points | Basis and limitation |
|---|---:|---|
| Public Django debug information disclosure | 25 | Supplied captures show a debug error response containing application and implementation details; not independently reproduced |
| Disclosed configuration settings warranting security review | 15 | Settings shown in the same captures, including permissive host and CORS configuration; effective exploitability was not tested |
| Possible gaming-brand impersonation | 15 | Fortnite-themed presentation raised concern; intentional impersonation and affiliation have not been established |
| Reported tournament invitation | 10 | A supplied Discord message promoted a tournament and directed attention towards the website; the sender's identity and intent have not been established |
| Recent domain registration | 5 | Registration date is contextual information only and is not proof of malicious activity |
| **Total** | **70/100** | **Provisional investigator assessment** |

### Rating scale

| Score | Rating | Interpretation |
|---:|---|---|
| 0–19 | Low | Few documented warning signs |
| 20–39 | Guarded | Some warning signs |
| 40–59 | Elevated | Several concerning indicators |
| 60–79 | High | Multiple significant warning signs |
| 80–100 | Critical | Extensive, strongly substantiated warning signs |

**What this rating does not mean:** 70/100 does not mean a 70% probability of phishing, fraud or compromise. It does not prove credential collection, data theft, successful exploitation, criminal intent, operator identity or Epic Games affiliation.

The score should be revised if independently verified evidence materially changes the assessment. Readers should consider the underlying evidence and limitations rather than relying on the number alone.

---

## 1. Executive summary - SCAMMERS, WE SEE YOU

**This investigation is a public call-out of suspicious activity that could put Fortnite players at risk.**

A Discord invitation promoted a tournament described as "FNCS PRO-LEAGUE" and encouraged the recipient to join a team called "Falcons". It directed attention towards a website presenting itself as a Fortnite competitive or esports destination.

The domain observed was:

`fortnitecompetitive[.]fun`

Let's be clear: players should not have to wonder whether a tournament invitation is genuine or whether a login page is trying to trick them.

The invitation, website presentation and technical observations raised serious concerns about **suspected phishing and possible brand impersonation**. These concerns deserve investigation and responsible action.

**We are calling out the behaviour, warning players and documenting the evidence. We are not going to invent facts to make the case sound bigger.**

The available evidence does not establish that credentials were stolen, that the website successfully collected credentials, or who operated it. Those limitations are stated openly throughout this report.

## 2. What was observed

The Discord invitation included the following message:

> register in 'FNCS PRO-LEAGUE' and join in my team 'Falcons'

The associated website paths observed were:

- `fortnitecompetitive[.]fun/tournaments/falcons`
- `fortnitecompetitive[.]fun/tournaments/falcons/login`

The website preview presented Fortnite-related branding and described itself as a Fortnite competitive or esports destination.

These observations raised a concern that visitors could mistake the site for an official Fortnite service.

A screenshot was supplied by another person and subsequently downloaded for evidence preservation. The screenshot is not included in this public repository.

## 3. Technical observations

### Domain registration

The RDAP information collected during the investigation indicated:

- Registration date: 17 November 2026
- Last changed: 22 November 2026
- Expiration date: 17 November 2027
- Registrar: REG.RU LLC
- Registrar website: https://www.reg.ru/
- Registrar abuse contact: abuse@reg.ru
- Registrar abuse information: https://www.reg.ru/legal/abuse/

Registration information identifies a registrar, not necessarily the website operator or the person responsible for the content.

### DNS observations

The DNS lookup returned the following records:

**A records (IPv4):**
- `104.21.96.131`
- `172.67.180.252`

**AAAA records (IPv6):**
- `2606:4700:3035::6815:6083`
- `2606:4700:3036::ac43:b4fc`

**NS records (nameservers):**
- `ignat.ns.cloudflare.com`
- `ara.ns.cloudflare.com`

**SOA record:**
- Primary nameserver (MNAME): `ara.ns.cloudflare.com.`
- Responsible party field (RNAME): `dns.cloudflare.com.`

**MX records:** No records found in the lookup.

**TXT records:** No records found in the lookup.

The returned IP addresses and nameservers are consistent with Cloudflare infrastructure. This does not establish that Cloudflare operates the website's origin server, owns the domain, or is responsible for its content. The origin server and website operator were not identified.

The absence of MX or TXT records in this lookup does not prove that the operator has no email service or that no other DNS configuration exists.

### Certificate transparency

The crt.sh lookup returned an HTTP 502 error during collection.

This result was inconclusive. It does not establish that the domain had no certificates or that HTTPS was absent.

### Reported SSL/TLS certificate details

A security-details result supplied by the investigator reported the following:

- SSL certificate status: Valid
- HTTPS enabled: Yes
- Reported certificate expiry: 15 February 2027

The source of this security-details result is unknown. The certificate was not independently inspected or verified as part of this investigation. The issuer, certificate subject and Subject Alternative Names were not provided.

A valid certificate and HTTPS connection do not establish that a website is legitimate, safe, or affiliated with Epic Games. Phishing websites can also use HTTPS.

### Django debug and backend configuration disclosure

**A publicly accessible Django debug response exposed substantial details about the application's internal configuration.**

Two investigator-supplied text captures show a detailed Django technical error response for a GET request to the website's root page. The captures display application settings, framework details, internal paths and request-environment information.

The observed backend fingerprint includes:

- Django version: `5.1.7`
- Python version: `3.12.3`
- Django setting `DEBUG`: `True`
- `ALLOWED_HOSTS`: `['*']`
- URL configuration: `epicfishing.urls`
- WSGI application: `epicfishing.wsgi.application`
- Application directory: `/home/epicfishing`
- Installed Django application: `frontend`
- Database engine: Django SQLite backend
- Database path: `/home/epicfishing/db.sqlite3`
- GeoIP data-file path: `/home/epicfishing/static/GeoLite2-Country.mmdb`
- View: `frontend.views.index_page`
- Error: `DoesNotExist`, raised during a database lookup in `price_fishingPage`

#### Exposed configuration and security concerns

The supplied settings output includes:

- `CORS_ALLOW_ALL_ORIGINS=True`
- `CORS_ALLOW_CREDENTIALS=True`
- `CSRF_TRUSTED_ORIGINS` containing `https://fortnite[.]com`, `https://urikclowns[.]shop` and `https://garikfortnite[.]shop`

These values show permissive CORS configuration and multiple configured CSRF trusted origins. They warrant security review. However, the settings alone do not prove that credentialed cross-origin data access is possible, that those domains are controlled by the same operator, or that all of them actively use this application.

The `ALLOWED_HOSTS=['*']` setting is also permissive and should be reviewed for a production deployment.

#### Cloudflare and origin attribution

The supplied request information contains Cloudflare-related headers and metadata. This is consistent with the observed request passing through Cloudflare.

**Cloudflare headers and edge IP information do not establish the actual origin server address.** The IP addresses and request metadata shown in the captures are not treated here as verified origin infrastructure or attribution.

#### Why this matters

Django's `DEBUG=True` setting is inappropriate for a publicly exposed production application. A debug error response can disclose implementation details, configuration values, filesystem paths and other information that should not be publicly available.

The supplied captures show that substantial backend information was exposed. This is consistent with a Django debug information disclosure and potentially unsafe production configuration.

The displayed secret key and password values are masked. The captures do not establish that the Django secret key, passwords or database contents were disclosed.

The captures were supplied by the investigator and have not been independently acquired or reproduced by this report's authoring environment. They do not establish credential theft, successful exploitation, database access, or the identity of the website operator.

### Third-party passive website scan — 23 November 2026

A third party supplied Elarumi with terminal output from a passive investigation of the publicly accessible website at `fortnitecompetitive[.]fun`.

The supplied output reports the following:

- **12 pages/resources checked**
- **164,631 bytes downloaded**
- `robots.txt` returned HTTP 200.
- The requested sitemap, manifest, security policy and other metadata paths returned HTTP 404.
- **0 forms detected** by the scanner.
- **2 external domains** identified; their names were not included in the supplied terminal output.
- **0 webhook references** detected.
- **0 Discord references** detected.
- **0 API references** detected.
- **1 scanning error:** `Invalid IPv6 URL`, encountered while processing the homepage.

**Limitations and attribution:**

These results were supplied by a third party. Elarumi has not independently reproduced or verified this scan. The scanner name, version, configuration and exact execution time were not provided with the output.

The absence of detected forms, webhooks, Discord references or API references does not establish that these features do not exist elsewhere on the website. The HTTP 404 responses apply only to the specific paths requested.

The `Invalid IPv6 URL` message is a reported URL-processing error. It does not, by itself, demonstrate an IPv6 vulnerability or malicious server behaviour.

The results are supplementary observations only. They do not establish the website operator's identity, prove credential theft, confirm successful exploitation or independently establish the website's intent.

## 4. Investigation boundaries

The investigation was limited to passive observation and responsible reporting.

The following actions were not performed:

- No credentials were entered or submitted.
- No credential transmission was tested.
- No unauthorised access was attempted.
- No exploitation was performed.
- No service disruption or denial-of-service activity was performed.
- No attempt was made to identify or expose a private individual behind the website.

Accordingly, this report does not claim confirmed credential theft, confirmed compromise, or confirmed malicious backend activity.

## 5. Reporting and disclosure history

### Epic Games

Official website: https://www.epicgames.com/

Official security and vulnerability reporting: https://www.epicgames.com/site/security?lang=en

An incident report and evidence archive were sent to Epic Games security on 22 November 2026.

The automated response directed vulnerability reports to HackerOne.

The Epic Games HackerOne programme information reviewed during this investigation described a closed scope and excluded social engineering, including phishing, as well as third-party assets not owned by Epic Games.

The suspicious domain was not established to be an Epic-owned asset. No bounty eligibility or Epic investigation is claimed.

#### Epic Games Support follow-up — 23 November 2026

Epic Games Support replied to the earlier contact and directed the reporting party to submit a report about the potentially rule-violating or illegal content or conduct through its official misconduct-reporting form:

https://safety.epicgames.com/policies/reporting-misconduct/submit-report

**Current status:** Epic Support provided the official reporting route. This response does not confirm that the website has been investigated, that a violation has been established, that a formal misconduct report has been submitted, or that any enforcement or remediation action has been taken.

The next reporting step is to submit the available evidence through the form provided by Epic.

### REG.RU

Official website: https://www.reg.ru/

Abuse reporting information: https://www.reg.ru/legal/abuse/

An abuse report and evidence archive were sent to REG.RU on 22 November 2026.

On 22 November 2026, REG.RU issued an automated acknowledgement confirming receipt of a support request.

**Support reference:** `20261123373000095`

The acknowledgement stated that the email was automatically generated and did not require a reply. It did not provide a substantive assessment, confirm that an investigation had begun, establish responsibility for the domain, or confirm any enforcement or remediation action.

**Current status:** Receipt acknowledged. A substantive response and any investigation or remediation outcome remain unconfirmed.

### Discord

The person who originally received the invitation reported the Discord message.

The report reference and outcome were not independently confirmed for this investigation.

### Cloudflare

Official website: https://www.cloudflare.com/

Official abuse-reporting form: https://abuse.cloudflare.com/

Cloudflare's documentation on submitting abuse reports: https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/

Attempts to access the Cloudflare abuse portal resulted in access-block pages.

No Cloudflare abuse report was successfully submitted during this investigation.

An access-support enquiry was drafted but had not been sent when this document was prepared.

No Cloudflare investigation or action is claimed.

## 6. Evidence handling and privacy

The original investigation files are maintained separately from this public repository.

This public version intentionally excludes:

- The original screenshot supplied by another person.
- Discord usernames, account IDs, and message IDs.
- Private messages and correspondence.
- The original evidence ZIP archive.
- Private or identifying information about any suspected individual.

The screenshot's authenticity and original capture date were not independently verified.

The technical observations represent the results of checks performed during this investigation. They should not be interpreted as a guarantee of the website's current state.

## 7. Current conclusion — PLAYERS DESERVE BETTER

**We are not treating suspicious tournament invitations and login pages as harmless.**

The combination of a Fortnite-themed tournament invitation, Fortnite-related website presentation and the observed domain raises a serious concern about suspected phishing and possible brand impersonation.

Players deserve to know when something looks suspicious. They deserve to protect their accounts without being manipulated by fake opportunities.

### What we can say

- A Discord invitation promoted "FNCS PRO-LEAGUE" and a team called "Falcons".
- The invitation directed attention towards a Fortnite-themed website.
- Technical observations included domain registration and DNS information.
- Investigator-supplied captures showed a Django debug error response exposing application settings and implementation details.
- Relevant organisations and reporting channels are documented in this report.

### What remains unproven

- Who operates the website.
- Whether the operator intentionally impersonated Epic Games.
- Whether credentials or other information were collected.
- Whether any visitor was compromised.
- Whether Epic Games, Discord, REG.RU or Cloudflare took action.
- Whether the website has since been disabled or changed.

We will not pretend these unanswered questions have already been resolved. The appropriate evidence-based classification remains **suspected phishing / possible brand impersonation**.

### OUR MESSAGE

**To anyone behind suspicious schemes targeting players: people deserve honesty, not deceptive invitations and suspicious login pages.**

**To players: protect your accounts. Verify tournament invitations. Never hand over credentials to a website just because it looks official.**

**To the relevant service providers: review the evidence through your appropriate reporting channels and take any action warranted by your findings.**

We are documenting this. We are warning people. We are demanding accountability.

**FUCK SCAMMERS. PROTECT THE PLAYERS.**

## 8. Responsible disclosure

If you believe you have encountered this website or a similar invitation, avoid entering passwords or personal information. Use official service-provider reporting channels and preserve relevant evidence without interacting with suspicious login pages.

This report is intended to document observations and encourage responsible handling, not to facilitate retaliation, harassment, or unauthorised access.

---

**FUCK SCAMMERS. GO GET A LIFE. XD <3**

---

## Player Protection

This investigation also aims to help players protect their accounts.

Read the [Elarumi Player Protection Guide](PLAYER-PROTECTION.md) for official Epic Games security resources, general online safety recommendations and personal advice from Elarumi.
