# Social Engineering Attack Scenarios: "JotForm Phishing"

This document outlines several potential attack vectors utilizing the JotForm link:
`https://agent.jotform.com/019c2906ed97722d8c3d0c9ba849e60b3c79`

## Scenario 1: Urgent Policy Update (Authority/Fear)

**Goal:** Harvest credentials or PII by impersonating HR.

**Lure:** An email appearing to be from "Human Resources" or "Compliance Team".

**Subject:** FINAL NOTICE: Employee Handbook Acknowledgement Required Immediately

**Body:**
> "Dear Employee,
> 
> Our records indicate you have not yet signed the updated 2026 Code of Conduct. Failure to complete this form by EOD will result in temporary account suspension pending review.
> 
> Please review and acknowledge here: [Link to Form]
> 
> Regards,
> HR Compliance"

**Why it works:** Leveraging fear of disciplinary action and time pressure.

---

## Scenario 2: Payroll Verification (Greed/Helpfulness)

**Goal:** Financial fraud or identity theft.

**Lure:** An email about a "payroll discrepancy" or "bonus processing".

**Subject:** Action Required: Verify Deposit Information for Bonus Payout

**Body:**
> "Hello,
> 
> We noticed a data mismatch in your direct deposit information for the upcoming bonus cycle. To ensure your payment is processed on time, please verify your details using our secure portal below.
> 
> Verify Here: [Link to Form]
> 
> Thank you,
> Payroll Dept."

**Why it works:** Financial incentive and helpful tone lower suspicion.

---

## Scenario 3: IT Support Ticket (Helpfulness/Curiosity)

**Goal:** Access to internal systems or credentials.

**Lure:** A fake support ticket update or system migration notice.

**Subject:** TICKET #98221: Password Reset Request Update

**Body:**
> "We received a request to reset your password. If this was you, please confirm your identity on the secure validation page to proceed. If this wasn't you, please fill out the form immediately to secure your account.
> 
> Secure Form: [Link to Form]
> 
> IT Security Team"

**Why it works:** Creates confusion and prompts immediate action to "secure" the account.

---

## Detection & Indicators of Compromise (IOCs)

How to identify this specific campaign:

1.  **URL Mismatch**: The link points to `jotform.com` (a third-party form builder) instead of the legitimate company domain (e.g., `company-name.com`).
    *   *Check:* Hover over the link before clicking.
2.  **Generic Greetings**: Use of "Dear Employee" or "Hello" instead of a specific name.
3.  **Urgency cues**: "Immediate action required", "Final Notice", "Account Suspension".
4.  **Mismatched Sender Address**: The email comes from an external address (e.g., `@gmail.com`) or a spoofed domain (e.g., `@c0mpany.com`).
5.  **Request for Sensitive Info**: Legitimate organizations rarely ask for passwords or full SSNs via a simple web form link in an email.
