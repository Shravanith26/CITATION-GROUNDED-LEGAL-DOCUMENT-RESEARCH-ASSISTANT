"""
Database of Real-Life Everyday Situations for 'My Rights in This Situation'.
Covers 38 everyday Indian legal and civic scenarios with current statutory provisions
under Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS),
Bharatiya Sakshya Adhiniyam (BSA), Special Acts, and Constitutional Rights.
"""

SITUATION_CATEGORIES = [
    "Theft & Property Crimes",
    "Cybercrime & Digital Scams",
    "Financial & Consumer Fraud",
    "Safety & Crimes Against Women",
    "Crimes Against Children & Seniors",
    "Violence, Threats & Assault",
    "Workplace & College Harassment",
    "Discrimination & Human Rights",
    "Road Accidents & Transport",
    "Police, Arrest & Legal System",
    "Civil, Property & Documentation",
    "Unsure / General Diagnostic"
]

SITUATIONS_DB = {
    # -------------------------------------------------------------------------
    # 1. THEFT & PROPERTY
    # -------------------------------------------------------------------------
    "theft_belongings": {
        "id": "theft_belongings",
        "title": "Someone stole my phone or belongings",
        "category": "Theft & Property Crimes",
        "is_emergency": False,
        "summary": "You experienced theft of movable property (such as a mobile phone, bag, jewellery, or wallet) without your consent.",
        "legal_issue": "Theft of movable property under Indian criminal law.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [],  # Not directly constitutional unless state action involved
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 303 (replaces IPC 378/379)",
                "deals_with": "Theft and punishment for theft (up to 3 years imprisonment or fine or both).",
                "relevance": "Taking movable property out of your possession with dishonest intent without consent."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 173 (replaces CrPC 154)",
                "deals_with": "Mandatory registration of First Information Report (FIR) for cognizable offences.",
                "relevance": "Theft is a cognizable offence; police are statutorily required to register an FIR and issue a free copy."
            }
        ],
        "immediate_steps": [
            "Block your SIM card immediately and contact your telecom operator to prevent OTP misuse.",
            "Block and track your device on the Central Equipment Identity Register (CEIR) portal (ceir.gov.in).",
            "Freeze mobile banking, UPI apps, and payment cards linked to your stolen device.",
            "Visit the nearest police station to lodge an FIR or file an online lost/theft report.",
            "Obtain a certified stamped copy of the FIR or police acknowledgment receipt free of cost."
        ],
        "evidence_checklist": [
            "IMEI number (found on the mobile box or original invoice)",
            "Purchase bill / invoice of the stolen item with serial numbers",
            "Exact date, time, and location where the property was last seen",
            "Last known location from 'Find My Device' or cloud tracking",
            "CCTV camera locations in the vicinity of the incident"
        ],
        "reporting_channels": [
            {"authority": "Local Police Station / e-FIR Portal", "contact": "Dial 112 or State Police Online Portal", "details": "Lodge an FIR under Section 173 BNSS; demand a free signed copy."},
            {"authority": "CEIR (DoT Portal)", "contact": "ceir.gov.in", "details": "Central portal to block and trace stolen mobile phones across all telecom networks."},
            {"authority": "Bank / UPI Helpline", "contact": "Immediate Bank Customer Care", "details": "Block net banking, debit cards, and UPI links connected to the number."}
        ],
        "police_refusal_escalation": "If the police station refuses to register an FIR, you have the statutory right under Section 173(4) BNSS to send a written complaint by registered post to the Superintendent of Police (SP). If no action is taken, you can petition the Judicial Magistrate under Section 175(3) BNSS for an order directing registration of FIR and investigation.",
        "know_the_difference": "This is primarily a **Criminal Offence** (Theft). It is not a constitutional dispute unless state authorities unlawfully seized property without law.",
        "confidence_level": "Confirmed criminal offence of theft under Section 303 BNS based on the facts provided.",
        "related_issues": ["Identity theft if SIM/phone is unlocked", "Unauthorized UPI/bank transactions", "Burglary if stolen from inside a locked house"],
        "follow_up_questions": [
            {"q": "Was any physical force, weapon, or threat used during the taking?", "options": ["No, it was taken quietly/secretly (Theft)", "Yes, snatching on road (Snatching)", "Yes, weapon or threats used (Robbery)"]},
            {"q": "Where did the theft take place?", "options": ["Public place / transit", "Inside my home / premises", "At workplace / college"]}
        ]
    },

    "chain_bag_snatching": {
        "id": "chain_bag_snatching",
        "title": "Someone snatched my chain/bag",
        "category": "Theft & Property Crimes",
        "is_emergency": True,
        "summary": "An assailant suddenly grabbed and forcibly snatched your chain, purse, mobile phone, or bag in a public space.",
        "legal_issue": "Snatching and use of force to extract property, newly codified as a distinct aggravated offence.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Personal Security", "connection": "Physical assault and violent snatching infringes on bodily security in public spaces."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 304",
                "deals_with": "Snatching (punishable with imprisonment up to 3 years and fine).",
                "relevance": "Specifically codifies sudden grabbing or taking away of property using swift physical force."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 309 (replaces IPC 390)",
                "deals_with": "Robbery (if hurt or wrongful restraint was caused during snatching).",
                "relevance": "If you were pulled down, injured, or restrained, the offence escalates to Robbery."
            }
        ],
        "immediate_steps": [
            "Check for bodily injuries immediately and seek medical attention if hurt.",
            "Dial 112 immediately while at the spot so police can broadcast a flash alert to nearby PCR vans.",
            "Note down the direction of escape, vehicle type, color, and registration number if seen.",
            "Request nearby shopkeepers to preserve their CCTV footage before it is overwritten.",
            "File an FIR at the nearest police station; get an MLC (Medico-Legal Certificate) if injured."
        ],
        "evidence_checklist": [
            "Description of attackers (appearance, clothing, height, helmet)",
            "Vehicle details (two-wheeler model, partial license plate, color)",
            "Medical injury report / Medico-Legal Certificate (MLC)",
            "Photographs of torn clothes, skin abrasions, or broken chain links",
            "CCTV footage from nearby traffic junctions, ATMs, or commercial establishments"
        ],
        "reporting_channels": [
            {"authority": "Emergency Police Response", "contact": "Dial 112", "details": "Immediate PCR dispatch for hot pursuit and cordon-off."},
            {"authority": "Jurisdictional Police Station", "contact": "Nearest Station", "details": "Registration of FIR under Section 304 BNS (Snatching) or Section 309 BNS (Robbery)."}
        ],
        "police_refusal_escalation": "Police cannot dismiss snatching as simple 'loss of item'. If they refuse to register an FIR under Section 304 BNS, escalate to the ACP/DCP or SP under Section 173(4) BNSS. In case of continuing inaction, file under Section 175(3) BNSS before the Magistrate.",
        "know_the_difference": "Snatching is an aggravated **Criminal Offence**. Under the new BNS (Section 304), it is distinguished from ordinary theft by the use of sudden physical force.",
        "confidence_level": "Confirmed criminal offence of Snatching (Section 304 BNS) or Robbery (Section 309 BNS).",
        "related_issues": ["Voluntarily causing hurt during robbery", "Hit-and-run if vehicle dragged victim", "Theft of identity documents in bag"],
        "follow_up_questions": [
            {"q": "Did you suffer physical injury during the incident?", "options": ["Yes, sustained injuries / abrasions", "No physical injury, but shaken", "Property dropped/recovered"]},
            {"q": "Did the offender use or display any weapon?", "options": ["No weapon seen", "Knife / Blade displayed", "Firearm displayed"]}
        ]
    },

    "house_trespass_burglary": {
        "id": "house_trespass_burglary",
        "title": "Someone broke into my house",
        "category": "Theft & Property Crimes",
        "is_emergency": True,
        "summary": "An unauthorized intruder broke into or entered your private home or premises unlawfully to commit theft or harm.",
        "legal_issue": "House-trespass, lurking house-trespass, housebreaking, and burglary.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life, Dignity & Home Privacy", "connection": "The sanctity of private dwelling is an integral dimension of personal liberty."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 329 & 331 (replaces IPC 441/445/457)",
                "deals_with": "Lurking house-trespass and housebreaking, especially by night.",
                "relevance": "Unlawful entry into a human dwelling by breaking locks, doors, or windows to commit theft."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 176 (replaces CrPC 157)",
                "deals_with": "Procedure for police investigation on spot.",
                "relevance": "Police forensic and investigative team must visit the crime scene to inspect points of entry."
            }
        ],
        "immediate_steps": [
            "Do NOT enter the premises alone if you suspect the intruder may still be inside.",
            "Do NOT touch doors, locks, drawers, or surfaces to preserve latent fingerprints and forensic evidence.",
            "Dial 112 immediately to request police and forensic crime team on the spot.",
            "Take photographs and videos from outside showing broken locks, open grills, or forced entry.",
            "Compile a list of missing valuables with receipts and photographs."
        ],
        "evidence_checklist": [
            "Photographs of broken locks, bent window grills, or forced latches",
            "Fingerprint impressions (preserved untouched for police dog/forensic squad)",
            "Building or society gate register entries and visitor logs",
            "CCTV footage from society entrance, lift, and hallway cameras",
            "Itemized inventory of missing jewellery, cash, electronics with bills"
        ],
        "reporting_channels": [
            {"authority": "Emergency Police Response", "contact": "Dial 112", "details": "Request immediate PCR and crime scene unit for spot inspection."},
            {"authority": "Jurisdictional Police Station", "contact": "Local Station", "details": "Registration of FIR under Section 331 BNS (Housebreaking by night)."}
        ],
        "police_refusal_escalation": "Housebreaking is a serious cognizable crime. If police refuse to lodge an FIR or write it as 'missing goods', demand a copy of the spot inspection panchnama and approach the ACP/DCP under Section 173(4) BNSS.",
        "know_the_difference": "This is a serious **Criminal Offence** against property and dwelling security.",
        "confidence_level": "Confirmed criminal offence of Housebreaking under Section 331 BNS.",
        "related_issues": ["Theft of cash/valuables", "Criminal trespass", "Society security negligence"],
        "follow_up_questions": [
            {"q": "Was anyone at home when the break-in happened?", "options": ["No, house was locked/empty", "Yes, family members were present", "Intruder confronted us"]},
            {"q": "Did the break-in happen during the night?", "options": ["Yes, between sunset and sunrise", "No, occurred during daytime", "Unknown time window"]}
        ]
    },

    # -------------------------------------------------------------------------
    # 2. CYBERCRIME & DIGITAL SCAMS
    # -------------------------------------------------------------------------
    "digital_arrest_scam": {
        "id": "digital_arrest_scam",
        "title": "Someone called me pretending to be a police officer / CBI / Customs (Digital Arrest)",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": True,
        "summary": "Fraudsters called via phone or Skype/WhatsApp video posing as CBI, ED, Police, or Customs officers, claiming your Aadhaar/parcel contains drugs/illegal items, placing you under fake 'digital arrest' and demanding money.",
        "legal_issue": "Extortion, impersonation of public servants, criminal intimidation, and cyber fraud.",
        "classification": ["Criminal Offence", "Regulatory Cyber Crime"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Protection of Personal Liberty & Due Process", "connection": "Law enforcement can NEVER arrest or detain citizens over Skype, WhatsApp, or phone calls; due process is mandatory."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 204 (replaces IPC 170) & Section 318 (replaces IPC 420)",
                "deals_with": "Personating a public servant, cheating, and dishonestly inducing delivery of property.",
                "relevance": "Falsely pretending to hold office as police, CBI, or customs officer to defraud."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 308 (replaces IPC 383/384)",
                "deals_with": "Extortion by putting person in fear of injury or false legal prosecution.",
                "relevance": "Coercing funds under threat of immediate arrest or defamation."
            },
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 66D",
                "deals_with": "Cheating by personation by using computer resource or communication device.",
                "relevance": "Using VoIP, WhatsApp video, and forged government seals."
            }
        ],
        "immediate_steps": [
            "DISCONNECT THE CALL IMMEDIATELY. There is NO legal provision for 'digital arrest' anywhere under Indian law.",
            "Do NOT transfer any money, do not disclose bank details, and do not share screen access.",
            "Indian police, CBI, ED, and judges NEVER conduct court trials or demand money via video calls.",
            "Dial 1930 immediately or log on to cybercrime.gov.in to report the numbers and accounts.",
            "Inform family members or a trusted person immediately so you are not isolated by fear."
        ],
        "evidence_checklist": [
            "Phone numbers, WhatsApp numbers, or Skype IDs used by the impostors",
            "Screenshots of fake arrest warrants, CBI/ED letterheads, or court orders sent",
            "Call recordings and screen recordings if captured",
            "Bank account numbers / UPI IDs provided by fraudsters for transfer",
            "Transaction reference IDs (UTR numbers) if any money was unfortunately transferred"
        ],
        "reporting_channels": [
            {"authority": "National Cyber Crime Helpline", "contact": "Dial 1930", "details": "Immediate financial freeze of fraudulent recipient accounts within golden hour."},
            {"authority": "National Cyber Crime Reporting Portal", "contact": "cybercrime.gov.in", "details": "File an online cyber complaint under 'Financial Fraud / Impersonation'."},
            {"authority": "Local Cyber Crime Police Station", "contact": "Nearest Cyber Police Cell", "details": "Lodge an FIR for criminal extortion and impersonation."}
        ],
        "police_refusal_escalation": "Cyber police stations are mandated by MHA guidelines to register digital arrest complaints. If local station hesitates, register directly on cybercrime.gov.in which auto-forwards to jurisdictional nodal officers.",
        "know_the_difference": "This is a serious **Criminal Offence** involving extortion, impersonation, and cyber fraud. Due process under Article 21 strictly forbids phone-based arrests.",
        "confidence_level": "Confirmed criminal extortion and impersonation scam. 'Digital arrest' is completely fictitious.",
        "related_issues": ["Money laundering scam", "Forgery of government seals", "Extortion under threat of prosecution"],
        "follow_up_questions": [
            {"q": "Did you transfer any money to the fraudsters?", "options": ["No, disconnected before paying", "Yes, transferred money within last 24 hours", "Yes, transferred money more than 24 hours ago"]},
            {"q": "Did you grant screen-sharing or install any app (like AnyDesk, TeamViewer)?", "options": ["No apps installed", "Yes, installed app on phone/PC", "Unsure"]}
        ]
    },

    "upi_bank_fraud": {
        "id": "upi_bank_fraud",
        "title": "Money was stolen from my bank/UPI account",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": True,
        "summary": "Unauthorized funds were debited from your bank account or UPI application via fraudulent transfers, skimming, or unauthorized access.",
        "legal_issue": "Unauthorized electronic fund transfer, cyber theft, and identity theft.",
        "classification": ["Criminal Offence", "Regulatory Banking Issue"],
        "constitutional_articles": [],
        "statutory_provisions": [
            {
                "act": "Information Technology Act, 2000",
                "section": "Sections 66C & 66D",
                "deals_with": "Identity theft and cheating by personation using computer resource.",
                "relevance": "Unauthorized electronic fund transfer through compromised credentials."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 318 (replaces IPC 420)",
                "deals_with": "Cheating and dishonestly inducing delivery of property.",
                "relevance": "Deceptive siphoning of bank balances."
            },
            {
                "act": "Reserve Bank of India (RBI) Regulations",
                "section": "Circular on Customer Protection (Limited Liability in Unauthorized Electronic Banking)",
                "deals_with": "Zero liability if customer reports unauthorized transaction within 3 working days.",
                "relevance": "Statutory right to bank reversal if breach is not due to customer negligence."
            }
        ],
        "immediate_steps": [
            "CALL 1930 IMMEDIATELY. The 'Golden Hour' (first 2-3 hours) allows the Indian Cyber Crime Coordination Centre (I4C) to freeze recipient accounts before funds are withdrawn.",
            "Contact your bank's 24/7 fraud helpline immediately to block your debit/credit card, UPI, and net banking.",
            "Request your bank to register an official fraud complaint and obtain a reference/ticket number.",
            "File a formal complaint on the National Cyber Crime Reporting Portal (cybercrime.gov.in).",
            "Under RBI rules, report to your bank within 3 days in writing to claim Zero Liability protection."
        ],
        "evidence_checklist": [
            "Bank account statement highlighting the fraudulent debit entries",
            "Transaction IDs (UTR numbers), UPI transaction reference IDs, and timestamps",
            "SMS notifications and emails received during the unauthorized debits",
            "Beneficiary account details or VPA (UPI ID) where the money was routed",
            "Complaint ticket number issued by your bank"
        ],
        "reporting_channels": [
            {"authority": "National Cyber Crime Helpline (I4C)", "contact": "Dial 1930", "details": "Crucial first step: triggers inter-bank lien marking to stop fund withdrawal."},
            {"authority": "Your Bank's Fraud Desk", "contact": "Bank Helpline (on back of card)", "details": "Mandatory written complaint within 3 days for RBI Zero Liability claim."},
            {"authority": "RBI Banking Ombudsman", "contact": "cms.rbi.org.in", "details": "Escalate if bank fails to resolve or credit refund within 30 days."}
        ],
        "police_refusal_escalation": "Cyber complaints registered on cybercrime.gov.in automatically generate an acknowledgment number that can be escalated to the State Cyber Crime Cell if local station delays FIR.",
        "know_the_difference": "This involves both a **Criminal Offence** (cyber fraud) and a **Regulatory Remedy** under RBI customer protection guidelines for financial recovery.",
        "confidence_level": "Confirmed cyber financial fraud. Rapid reporting within 1930 golden hour dictates recovery probability.",
        "related_issues": ["Phishing / social engineering", "SIM swap fraud", "Bank deficiency of service"],
        "follow_up_questions": [
            {"q": "How long ago did the unauthorized debit happen?", "options": ["Within the last 2 hours (Golden Hour)", "Within the last 24 hours", "More than 2-3 days ago"]},
            {"q": "Did you share an OTP or click on a remote screen-share link?", "options": ["No, money debited without my interaction", "Yes, entered details on a link / shared OTP", "Unsure"]}
        ]
    },

    "sextortion_private_photos": {
        "id": "sextortion_private_photos",
        "title": "Someone is threatening to share my private photos / sextortion",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": True,
        "summary": "A blackmailer or cybercriminal is threatening to leak your intimate pictures, deepfakes, or private video recordings unless you pay money or yield to demands.",
        "legal_issue": "Sextortion, criminal intimidation, non-consensual sharing of intimate images, and extortion.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Privacy & Bodily Dignity (Puttaswamy Ruling)", "connection": "The Supreme Court recognized informational privacy and bodily autonomy as fundamental rights."}
        ],
        "statutory_provisions": [
            {
                "act": "Information Technology Act, 2000",
                "section": "Sections 66E, 67 & 67A",
                "deals_with": "Violation of privacy, publishing or transmitting sexually explicit acts in electronic form.",
                "relevance": "Publishing or threatening to transmit intimate photos without consent is punishable up to 5 years imprisonment."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 77 (replaces IPC 354C) & Section 308 (replaces IPC 384)",
                "deals_with": "Voyeurism, non-consensual capture/distribution of private acts, and extortion.",
                "relevance": "Threatening to circulate private imagery to extract funds or sexual favours."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 351 (replaces IPC 506)",
                "deals_with": "Criminal intimidation to cause injury to person, reputation, or property.",
                "relevance": "Direct threats to ruin social reputation by circulating private media."
            }
        ],
        "immediate_steps": [
            "DO NOT PAY ANY MONEY. Paying money NEVER stops blackmailers; it guarantees they will demand even larger amounts.",
            "Do NOT delete chat history, messages, or payment links. Preserve everything as critical evidence.",
            "Take full screenshots showing the blackmailer's phone number, username, profile link, and threats.",
            "Report immediately on the National Cyber Crime Portal (cybercrime.gov.in) under the 'Report Women/Child Crime Anonymous' option if desired.",
            "Use the 'StopNCII.org' platform to create a cryptographic hash of images to prevent their upload across Facebook, Instagram, and major platforms."
        ],
        "evidence_checklist": [
            "Screenshots of the threatening messages, demands, and countdown timers",
            "Profile URLs, social media handles, phone numbers, and email IDs of the blackmailer",
            "Payment links, UPI IDs, or cryptocurrency addresses provided for extortion",
            "Original images/media with metadata preserved without alteration",
            "Call recordings or voice notes sent by the extortionist"
        ],
        "reporting_channels": [
            {"authority": "National Cyber Crime Reporting Portal", "contact": "cybercrime.gov.in", "details": "Special category for non-consensual intimate imagery and sextortion with takedown protocol."},
            {"authority": "StopNCII.org (Tech Industry Coalition)", "contact": "stopncii.org", "details": "Creates secure image hashes to prevent dissemination on Instagram, Meta, TikTok, etc."},
            {"authority": "Local Cyber Crime Police Unit", "contact": "Nearest Cyber Cell", "details": "Registration of FIR under Sections 66E/67A IT Act and Section 308 BNS."}
        ],
        "police_refusal_escalation": "Cyber police are legally mandated under Section 79(3)(b) of the IT Act to issue takedown notices to platforms within 24 hours of receiving complaints regarding non-consensual sexual content.",
        "know_the_difference": "This is a serious **Criminal Offence**. Victims are protected under privacy jurisprudence (Article 21) and are never blamed under law.",
        "confidence_level": "Confirmed criminal extortion and privacy violation under IT Act and BNS.",
        "related_issues": ["Deepfake creation / identity impersonation", "Blackmail under Section 308 BNS", "Defamation and reputational harm"],
        "follow_up_questions": [
            {"q": "Did the blackmailer already upload or send the content to your contacts?", "options": ["No, currently threatening only", "Yes, shared with friends/family", "Unsure"]},
            {"q": "Is the person an acquaintance or an anonymous online contact?", "options": ["Anonymous online stranger", "Ex-partner / known acquaintance", "Co-worker / classmate"]}
        ]
    },

    "fake_social_profile": {
        "id": "fake_social_profile",
        "title": "Someone created a fake social-media account using my name/photo",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": False,
        "summary": "An unknown individual or acquaintance has cloned your photos, created an impersonating profile on Instagram, Facebook, LinkedIn, or X, and is messaging people or posting content in your name.",
        "legal_issue": "Identity theft, cheating by impersonation, and violation of privacy.",
        "classification": ["Criminal Offence", "Platform Regulatory Violation"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Privacy & Identity Dignity", "connection": "Protects against unlawful misappropriation of individual identity and likeness."}
        ],
        "statutory_provisions": [
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 66C & 66D",
                "deals_with": "Identity theft and cheating by personation using computer resource.",
                "relevance": "Punishable with imprisonment up to 3 years and fine for using another's identity or photos dishonestly."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 319 (replaces IPC 416/419)",
                "deals_with": "Cheating by personation (pretending to be another person).",
                "relevance": "Pretending to be you to deceive friends, family, or the public."
            }
        ],
        "immediate_steps": [
            "Take screenshots of the fake profile showing the exact handle, profile picture, bio, and all posts before reporting.",
            "Copy the exact URL of the impersonating account.",
            "Use the platform's in-app reporting tool: Select 'Report' -> 'Impersonation' -> 'Pretending to be me'.",
            "Ask close friends to also report the profile to trigger platform automated review.",
            "Lodge an online complaint on cybercrime.gov.in under 'Cyber Harassment / Impersonation'."
        ],
        "evidence_checklist": [
            "Exact URL / web link of the fake profile",
            "Screenshots of the fake profile, bio, followers list, and posts",
            "Screenshots of any abusive, inappropriate, or scam messages sent from that account",
            "Proof of your own authentic identity (photo ID or existing original verified handle)"
        ],
        "reporting_channels": [
            {"authority": "Social Media Platform Grievance Officer", "contact": "In-app Report Feature / Platform Grievance Portal", "details": "Mandated under IT Rules 2021 to resolve impersonation complaints within 72 hours."},
            {"authority": "National Cyber Crime Reporting Portal", "contact": "cybercrime.gov.in", "details": "Register under 'Cyber Crime against Women/Citizens' for formal police tracking."}
        ],
        "police_refusal_escalation": "Under the Information Technology (Intermediary Guidelines) Rules, 2021, platforms are legally bound to remove impersonating accounts upon receiving user notice or court order.",
        "know_the_difference": "This involves a **Criminal Offence** (Sections 66C/66D IT Act) and an **Intermediary Regulatory Compliance** duty for social networks.",
        "confidence_level": "Confirmed cyber impersonation and identity theft.",
        "related_issues": ["Defamation", "Online stalking", "Financial fraud using fake profile"],
        "follow_up_questions": [
            {"q": "Is the fake account soliciting money or posting inappropriate photos?", "options": ["Yes, asking money from contacts", "Yes, posting explicit / obscene content", "No, just copying photos/profile"]},
            {"q": "Have you reported it to the social media platform?", "options": ["Yes, but platform hasn't removed it", "Not yet reported to platform", "Platform rejected report"]}
        ]
    },

    # -------------------------------------------------------------------------
    # 3. SAFETY & CRIMES AGAINST WOMEN
    # -------------------------------------------------------------------------
    "stalking_offline_online": {
        "id": "stalking_offline_online",
        "title": "Someone is following or stalking me",
        "category": "Safety & Crimes Against Women",
        "is_emergency": True,
        "summary": "An individual is repeatedly following you physically, monitoring your movements, showing up at your commute/workplace, or persistently tracking your online activities despite disinterest.",
        "legal_issue": "Stalking under criminal law and violation of personal liberty.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life, Personal Liberty & Free Movement", "connection": "Continuous surveillance or pursuit violates the fundamental right to live freely without fear."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 78 (replaces IPC 354D)",
                "deals_with": "Stalking (physical following and electronic monitoring).",
                "relevance": "Follows a woman, attempts to contact despite clear indication of disinterest, or monitors internet/email/electronic communications."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 351 (replaces IPC 506)",
                "deals_with": "Criminal intimidation.",
                "relevance": "If stalking is accompanied by threats of acid, violence, or harm."
            }
        ],
        "immediate_steps": [
            "Prioritize your immediate physical safety. Move into crowded, well-lit spaces, shops, or metro stations if being followed.",
            "Call Emergency 112 or Women Helpline 1091 immediately.",
            "Inform family members, trusted colleagues, or friends about the person and your live location.",
            "Do NOT confront the stalker alone in isolated locations.",
            "Keep an incident log: write down dates, times, locations, vehicles, and conduct of the stalker."
        ],
        "evidence_checklist": [
            "Incident diary detailing dates, times, and exact locations where the stalker appeared",
            "Photographs or videos taken from a safe distance showing the stalker or vehicle",
            "Call logs, text messages, emails, WhatsApp messages, or gifts sent",
            "CCTV footage from residential gate, office reception, or street cameras",
            "Names and contacts of witnesses (guards, co-commuters, colleagues)"
        ],
        "reporting_channels": [
            {"authority": "Emergency Women's Helpline", "contact": "Dial 1091 / Dial 112", "details": "Immediate dispatch of police patrol and assistance."},
            {"authority": "National Commission for Women (NCW)", "contact": "ncw.nic.in / 7827170170", "details": "24/7 helpline for women in distress with institutional monitoring."},
            {"authority": "Jurisdictional Police Station", "contact": "Local Police Station", "details": "Mandatory registration of FIR under Section 78 BNS."}
        ],
        "police_refusal_escalation": "Stalking on first conviction is bailable, but repeat offence is non-bailable. Police are legally bound to register an FIR under Section 173 BNSS. In case of refusal, file a complaint with the ACP/DCP or approach the nearest Mahila Police Station.",
        "know_the_difference": "This is a serious **Criminal Offence** directly endangering the victim's constitutional liberty and physical integrity.",
        "confidence_level": "Confirmed criminal offence of Stalking under Section 78 BNS.",
        "related_issues": ["Sexual harassment", "Criminal intimidation", "Cyber harassment"],
        "follow_up_questions": [
            {"q": "Is the stalking physical, online, or both?", "options": ["Physical following in person", "Online monitoring / persistent messages", "Both physical and online"]},
            {"q": "Has the person issued any explicit threats of violence?", "options": ["Yes, threatened violence/acid/harm", "No overt threats, but relentless pursuit", "Unsure"]}
        ]
    },

    "domestic_violence": {
        "id": "domestic_violence",
        "title": "I am facing domestic violence",
        "category": "Safety & Crimes Against Women",
        "is_emergency": True,
        "summary": "You are subjected to physical assault, verbal abuse, emotional cruelty, sexual abuse, or economic deprivation by a spouse or family member in a domestic relationship.",
        "legal_issue": "Domestic violence, cruelty by spouse/relatives, and right to residence/protection.",
        "classification": ["Criminal Offence", "Civil / Statutory Protection Order"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life with Human Dignity", "connection": "Protection against gender-based violence within domestic relationships is intrinsic to dignity."},
            {"article": "Article 15(3)", "name": "Special Provisions for Women", "connection": "Empowers special legislative measures like the Domestic Violence Act to safeguard women."}
        ],
        "statutory_provisions": [
            {
                "act": "Protection of Women from Domestic Violence Act, 2005 (PWDVA)",
                "section": "Sections 12, 17, 18, 19, 20",
                "deals_with": "Civil remedies: Right to reside in shared household, Protection Orders, Residence Orders, Monetary Relief, and Child Custody.",
                "relevance": "Enables immediate emergency restraining orders preventing abuser from entering the shared house or contacting victim."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 85 & 86 (replaces IPC 498A)",
                "deals_with": "Husband or relative of husband of a woman subjecting her to cruelty.",
                "relevance": "Criminal offence punishable with imprisonment up to 3 years and fine for physical or mental cruelty."
            }
        ],
        "immediate_steps": [
            "If in immediate physical danger, dial 112 or Women Helpline 181 / 1091 right away.",
            "Move to a safe room with a lock, or leave to a trusted neighbour, friend, or relative's place.",
            "If injured, visit a government hospital immediately for medical treatment and ask for an MLC.",
            "You cannot be evicted from your shared household; law protects your right of residence.",
            "Contact a designated Protection Officer (appointed under DV Act) or a legal-aid lawyer."
        ],
        "evidence_checklist": [
            "Medical reports, prescription slips, and Medico-Legal Certificates (MLCs)",
            "Photographs of physical bruises, cuts, or injuries with timestamps",
            "Audio/video recordings, WhatsApp messages, or voicemails containing threats or abuse",
            "Bank statements showing financial deprivation or control of earnings",
            "Past police complaints (DD entries) or protection officer reports"
        ],
        "reporting_channels": [
            {"authority": "National Emergency & Women Helpline", "contact": "Dial 112 / Dial 181", "details": "Immediate emergency rescue and referral to safe shelter homes."},
            {"authority": "Protection Officer (District Level)", "contact": "District Magistrate Office / Women & Child Welfare", "details": "Filing Domestic Incident Report (DIR) before Magistrate under Section 12 PWDVA."},
            {"authority": "NALSA / State Legal Services Authority", "contact": "Dial 15100 (Free Legal Aid)", "details": "Free legal aid advocate assigned to draft DV petitions and maintenance claims."}
        ],
        "police_refusal_escalation": "Under the DV Act, Protection Officers and Service Providers can file applications directly before the Judicial Magistrate without requiring police consent.",
        "know_the_difference": "This unique framework combines a **Criminal Offence** (Section 85 BNS cruelty) with **Civil Statutory Relief** (Protection and Residence orders under PWDVA 2005).",
        "confidence_level": "Confirmed domestic violence matter with parallel criminal and civil protective remedies.",
        "related_issues": ["Dowry prohibition", "Maintenance rights under S. 144 BNSS", "Child custody"],
        "follow_up_questions": [
            {"q": "Is there ongoing physical violence or imminent risk of assault?", "options": ["Yes, currently facing physical danger", "Emotional/verbal/financial abuse", "Threatened with eviction from home"]},
            {"q": "Do you need emergency shelter or medical attention?", "options": ["Yes, need safe shelter and hospital", "Safe for now, need legal protection order", "Seeking guidance only"]}
        ]
    },

    # -------------------------------------------------------------------------
    # 4. CRIMES AGAINST CHILDREN & SENIORS
    # -------------------------------------------------------------------------
    "child_abuse_exploitation": {
        "id": "child_abuse_exploitation",
        "title": "A child is being abused or exploited",
        "category": "Crimes Against Children & Seniors",
        "is_emergency": True,
        "summary": "A minor (under 18 years) is experiencing physical abuse, sexual assault, harassment, neglect, child labour, or exploitation.",
        "legal_issue": "Child sexual abuse under POCSO Act, child cruelty, and mandatory reporting.",
        "classification": ["Criminal Offence", "Child Welfare Protection"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Dignity", "connection": "Children possess absolute right to bodily safety and protection against harm."},
            {"article": "Article 24", "name": "Prohibition of Employment of Children", "connection": "Prohibits child employment in factories, mines, and hazardous occupations."},
            {"article": "Article 39(f)", "name": "Directive Principles for Child Welfare", "connection": "State duty to ensure children develop in a healthy manner with freedom and dignity."}
        ],
        "statutory_provisions": [
            {
                "act": "Protection of Children from Sexual Offences (POCSO) Act, 2012",
                "section": "Sections 3 to 12 & Sections 19/21",
                "deals_with": "Severe penalties for penetrative/aggravated sexual assault and harassment against minors.",
                "relevance": "Section 19 mandates that ANY person who has knowledge of child abuse MUST report it; failure to report is punishable under Section 21."
            },
            {
                "act": "Juvenile Justice (Care and Protection of Children) Act, 2015",
                "section": "Section 75",
                "deals_with": "Punishment for cruelty to child (imprisonment up to 3 years or fine).",
                "relevance": "Assault, abandonment, abuse, or neglect of a child causing suffering."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 95 & Section 143",
                "deals_with": "Hiring or employing children to commit crimes, and human trafficking.",
                "relevance": "Stringent punishment including life imprisonment for trafficking minors."
            }
        ],
        "immediate_steps": [
            "Ensure the child is immediately in a safe, protective environment away from the perpetrator.",
            "DIAL 1098 (Childline) or 112 IMMEDIATELY. Childline coordinates emergency rescue with CWC.",
            "Seek immediate medical attention at a government hospital; medical examination of minors under POCSO is free and prioritized.",
            "Do NOT subject the child to repeated questioning or interrogation by non-professionals.",
            "Under POCSO Section 24, statements of the child are recorded by woman police officers in civil clothing."
        ],
        "evidence_checklist": [
            "Medical examination records from government hospital",
            "Child's statement recorded in friendly, non-threatening conditions",
            "Photographs of any external injuries, burns, or physical marks",
            "Any electronic records, text messages, or videos involving the perpetrator",
            "School attendance records or behavioral observations by teachers/guardians"
        ],
        "reporting_channels": [
            {"authority": "CHILDLINE 24/7 (Emergency Service)", "contact": "Dial 1098", "details": "Direct emergency intervention, rescue, and shelter assistance."},
            {"authority": "Child Welfare Committee (CWC)", "contact": "District CWC Office", "details": "Quasi-judicial authority responsible for care, protection, and rehabilitation of minors."},
            {"authority": "Special Juvenile Police Unit (SJPU)", "contact": "Nearest Police Station / SJPU", "details": "Mandated to record FIR in civil clothes without exposing child to police lockup."}
        ],
        "police_refusal_escalation": "Refusal to register a POCSO complaint is an offence in itself. Section 21 of the POCSO Act criminalizes failure to record or report child abuse by police officers with up to 6 months imprisonment.",
        "know_the_difference": "This is a serious **Criminal Offence** with non-negotiable statutory child protection mandates under POCSO and JJ Act.",
        "confidence_level": "Emergency child protection matter. Mandatory reporting duty applies to all citizens under Section 19 POCSO.",
        "related_issues": ["Mandatory reporting obligations", "CWC foster care", "Criminal trafficking"],
        "follow_up_questions": [
            {"q": "Is the child in immediate physical danger from the offender right now?", "options": ["Yes, child is with/near offender", "No, child is currently in a safe place", "Unsure"]},
            {"q": "What type of abuse is suspected?", "options": ["Sexual abuse / harassment (POCSO)", "Physical beatings / cruelty", "Child labour / trafficking"]}
        ]
    },

    # -------------------------------------------------------------------------
    # 5. POLICE, ARREST & LEGAL REMEDIES
    # -------------------------------------------------------------------------
    "police_refusal_fir": {
        "id": "police_refusal_fir",
        "title": "A police station is refusing to properly record my complaint",
        "category": "Police, Arrest & Legal System",
        "is_emergency": False,
        "summary": "You visited a police station to report a crime (such as theft, assault, fraud, or harassment), but the duty officer refused to register an FIR, told you to compromise, or only accepted a loose paper without acknowledgment.",
        "legal_issue": "Non-registration of mandatory FIR for cognizable offence, and citizen's statutory escalation remedies.",
        "classification": ["Criminal Procedural Violation", "Constitutional Right to Due Process"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Access to Justice & Rule of Law", "connection": "Access to criminal justice machinery is an essential facet of the fundamental right to life."},
            {"article": "Article 14", "name": "Equality Before Law", "connection": "Arbitrary denial of crime registration violates equal protection of laws."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 173(1) (replaces CrPC 154(1))",
                "deals_with": "Mandatory registration of FIR upon receiving information disclosing a cognizable offence.",
                "relevance": "As held by Constitution Bench in Lalita Kumari (2014), registration of FIR is mandatory if a cognizable crime is disclosed."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 173(4) (replaces CrPC 154(3))",
                "deals_with": "Written escalation to the Superintendent of Police (SP / DCP).",
                "relevance": "You can send the complaint substance by registered post to the SP, who must investigate or direct investigation."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 175(3) (replaces CrPC 156(3))",
                "deals_with": "Petition before Judicial Magistrate to order investigation.",
                "relevance": "Magistrate has power to order police to register FIR and monitor the investigation (Sakiri Vasu precedent)."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 199 (replaces IPC 166A)",
                "deals_with": "Public servant disobeying direction under law.",
                "relevance": "Police officers who fail to record complaints regarding offences against women/children can face up to 2 years imprisonment."
            }
        ],
        "immediate_steps": [
            "Politely request the officer to make a General Diary (GD / Daily Diary) entry and provide a GD number.",
            "Note the name, designation, and badge number of the police officer refusing the FIR.",
            "Ask for a written acknowledgment on a duplicate copy of your written complaint.",
            "Concept of Zero FIR: If the police claim the crime occurred outside their jurisdiction, demand a 'Zero FIR', which they must register and transfer.",
            "Draft a detailed complaint and send it via Registered Post with Acknowledgment Due (RPAD) or Speed Post to the District SP/DCP."
        ],
        "evidence_checklist": [
            "Copy of the written complaint submitted to the police station",
            "Postal receipt and tracking report of complaint sent to the Superintendent of Police",
            "General Diary (GD) number or station visitor entry slip if provided",
            "Date, time, and name of the police station and officers interacted with",
            "Underlying evidence of the original crime (injury report, bank statement, CCTV, etc.)"
        ],
        "reporting_channels": [
            {"authority": "Superintendent of Police (SP) / DCP", "contact": "District Police Headquarters", "details": "Statutory escalation under Section 173(4) BNSS via speed post."},
            {"authority": "Jurisdictional Judicial Magistrate", "contact": "District Court", "details": "Section 175(3) BNSS application filed through a lawyer or legal aid advocate."},
            {"authority": "Police Complaints Authority (PCA) / Vigilance", "contact": "State PCA Office", "details": "File complaint against police misconduct and refusal of duty."},
            {"authority": "State Human Rights Commission (SHRC)", "contact": "shrc portal", "details": "Report violation of fundamental rights by police inaction."}
        ],
        "police_refusal_escalation": "This situation IS the escalation protocol: Step 1 (Police Station) -> Step 2 (SP/DCP under S. 173(4) BNSS) -> Step 3 (Magistrate under S. 175(3) BNSS).",
        "know_the_difference": "This is a **Procedural Violation** by law enforcement that touches on **Constitutional Rights** to justice under Article 21.",
        "confidence_level": "Confirmed procedural rights under Section 173 and 175 BNSS.",
        "related_issues": ["Zero FIR statutory entitlement", "Police accountability under Section 199 BNS", "Free legal aid"],
        "follow_up_questions": [
            {"q": "Did the police give you any paper, receipt, or GD number?", "options": ["No, refused completely", "Given an informal stamp on plain paper", "Given a GD / CSR entry number"]},
            {"q": "Does the crime involve violence, women, or children?", "options": ["Yes, crime against woman/child (mandatory S. 199 BNS)", "Yes, violent assault / robbery", "Property or financial dispute"]}
        ]
    },

    "arrest_detention_rights": {
        "id": "arrest_detention_rights",
        "title": "I was arrested or detained and do not understand my rights",
        "category": "Police, Arrest & Legal System",
        "is_emergency": True,
        "summary": "You or an acquaintance has been arrested, detained, or summoned by police officers and need to know statutory safeguards and constitutional protections.",
        "legal_issue": "Arrest procedural safeguards, right to be informed of grounds, right to legal counsel, and production before Magistrate within 24 hours.",
        "classification": ["Constitutional Safeguard", "Criminal Procedural Rights"],
        "constitutional_articles": [
            {"article": "Article 22(1)", "name": "Right to Know Grounds of Arrest & Legal Counsel", "connection": "Absolute constitutional guarantee that no person shall be detained without being informed of grounds and consulting an advocate."},
            {"article": "Article 22(2)", "name": "Production Before Magistrate within 24 Hours", "connection": "Mandatory constitutional duty to produce every arrested person before the nearest Magistrate within 24 hours (excluding journey time)."},
            {"article": "Article 21", "name": "Protection Against Custodial Torture", "connection": "D.K. Basu landmark guidelines establishing mandatory custodial safeguards."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 47 (replaces CrPC 50)",
                "deals_with": "Person arrested to be informed of grounds of arrest and of right to bail.",
                "relevance": "Police must immediately communicate full particulars of the offence and whether it is bailable."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 48 (replaces CrPC 50A)",
                "deals_with": "Obligation of person making arrest to inform friend/relative.",
                "relevance": "Police must immediately inform a designated family member or friend about the arrest and location."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 53 (replaces CrPC 54)",
                "deals_with": "Examination of arrested person by medical officer.",
                "relevance": "Mandatory medical examination at time of arrest to document physical condition and prevent custodial torture."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 58 (replaces CrPC 57)",
                "deals_with": "Person arrested not to be detained more than twenty-four hours.",
                "relevance": "Detention beyond 24 hours without a Magistrate's order of remand is illegal detention."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 35(3) (replaces CrPC 41A)",
                "deals_with": "Notice of appearance before police officer for offences under 7 years (Arnesh Kumar guidelines).",
                "relevance": "For offences punishable with up to 7 years, arrest is not routine; police must first issue a Notice of Appearance."
            }
        ],
        "immediate_steps": [
            "Ask the police officer: 'What are the grounds of my arrest, and is this offence bailable?'",
            "Demand that your family member, friend, or lawyer be informed immediately under Section 48 BNSS.",
            "Demand a copy of the Arrest Memo signed by the arresting officer and an independent witness.",
            "Demand a mandatory medical examination under Section 53 BNSS before being placed in lockup.",
            "Remember: You must be produced before a Judicial Magistrate within 24 hours. Inform the Magistrate if you were mistreated."
        ],
        "evidence_checklist": [
            "Copy of the Arrest Memo containing date, time, and signatures",
            "Inspection Memo documenting any injuries on your body at the time of arrest",
            "Entry in the Police Station General Diary (GD) recording arrival and detention time",
            "Contact number and badge ID of the Investigating Officer (IO)"
        ],
        "reporting_channels": [
            {"authority": "Judicial Magistrate / Remand Court", "contact": "Local District Court", "details": "Tell Magistrate directly during 24-hour production if rights were violated or custody was unlawful."},
            {"authority": "Legal Aid Defense Counsel (NALSA)", "contact": "Duty Counsel at Court / 15100", "details": "Every arrested person is entitled to free legal representation at remand stage."},
            {"authority": "High Court (Habeas Corpus Petition)", "contact": "Article 226 Petition", "details": "Family can file Habeas Corpus if person is missing in police custody past 24 hours."}
        ],
        "police_refusal_escalation": "Detention beyond 24 hours without Magistrate order is unconstitutional. An immediate Habeas Corpus petition can be filed before the High Court under Article 226 or Supreme Court under Article 32.",
        "know_the_difference": "This is a core **Constitutional Right** under Article 22 backed by statutory mandates in the BNSS.",
        "confidence_level": "Confirmed constitutional rights under Articles 21, 22 and Chapter V of BNSS.",
        "related_issues": ["Custodial interrogation rules", "Anticipatory bail under Section 482 BNSS", "D.K. Basu guidelines compliance"],
        "follow_up_questions": [
            {"q": "Has the person been produced before a Magistrate yet?", "options": ["No, currently in police station", "Yes, produced in court", "Detained past 24 hours without court"]},
            {"q": "Were the family members informed about the arrest?", "options": ["Yes, informed", "No, family has not been informed"]}
        ]
    },

    # -------------------------------------------------------------------------
    # 6. ROAD INCIDENTS & CONSUMER RIGHTS
    # -------------------------------------------------------------------------
    "road_accident_hit_and_run": {
        "id": "road_accident_hit_and_run",
        "title": "I was involved in a road accident / hit-and-run",
        "category": "Road Accidents & Transport",
        "is_emergency": True,
        "summary": "You were involved in a vehicular collision, or a vehicle struck you/your vehicle and fled the scene without stopping or rendering medical assistance.",
        "legal_issue": "Rash driving, causing hurt by negligence, hit-and-run, and Good Samaritan legal protections.",
        "classification": ["Criminal Offence", "Motor Accident Claim (Civil Compensation)"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Emergency Medical Care", "connection": "Supreme Court in Parmanand Katara ruled that medical facilities MUST provide immediate emergency care without waiting for police clearance."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 281 & Section 106",
                "deals_with": "Rash driving or riding on a public way, and causing death by negligence.",
                "relevance": "Section 106(2) provides severe punishment (up to 10 years) for motorists who cause fatal accident by rash driving and escape without reporting."
            },
            {
                "act": "Motor Vehicles Act, 1988 (as amended 2019)",
                "section": "Section 134A (Good Samaritan Protection)",
                "deals_with": "Protection of bystanders who render emergency medical assistance to accident victims.",
                "relevance": "Good Samaritans cannot be harassed, detained at hospital, or forced to become witnesses."
            },
            {
                "act": "Motor Vehicles Act, 1988",
                "section": "Section 161 & Section 166",
                "deals_with": "Compensation in hit-and-run motor accidents & MACT claims.",
                "relevance": "Statutory Solatium fund for hit-and-run victims, and Motor Accident Claims Tribunal (MACT) compensation."
            }
        ],
        "immediate_steps": [
            "Check for injuries and call 112 / Ambulance 108 immediately. Medical treatment takes priority over all legal formalities.",
            "Under Supreme Court guidelines (Parmanand Katara), ANY private or government hospital must treat accident victims immediately without waiting for police.",
            "Take photos of the accident scene, vehicle damage, skid marks, and number plates before vehicles are moved.",
            "If the driver fled (hit-and-run), note the vehicle color, make, partial number, and ask nearby shops for CCTV footage.",
            "File an FIR at the jurisdictional police station to ensure eligibility for insurance and MACT compensation."
        ],
        "evidence_checklist": [
            "Photographs and videos of the collision scene, vehicle positions, and damage",
            "Registration number of the offending vehicle",
            "Medico-Legal Certificate (MLC) and hospital emergency admission records",
            "CCTV footage from traffic cameras, toll plazas, or nearby establishments",
            "Contact information of eyewitnesses at the spot"
        ],
        "reporting_channels": [
            {"authority": "Emergency Ambulance & Police", "contact": "Dial 108 (Medical) / Dial 112 (Police)", "details": "Emergency trauma response and accident spot recording."},
            {"authority": "Jurisdictional Police Station", "contact": "Local Police Station", "details": "FIR under Section 281/125 BNS (Rash driving / endangering life)."},
            {"authority": "Motor Accident Claims Tribunal (MACT)", "contact": "District Court MACT Bench", "details": "Claiming financial compensation from motor vehicle third-party insurance."}
        ],
        "police_refusal_escalation": "Police must file an Accident Information Report (AIR) within 90 days to the MACT. If police refuse to register FIR, submit to SP under Section 173(4) BNSS.",
        "know_the_difference": "This incident creates two distinct legal avenues: a **Criminal Case** against the rash driver, and a **Civil Compensation Claim** before the MACT Tribunal.",
        "confidence_level": "Confirmed road accident legal remedies involving BNS criminal provisions and Motor Vehicles Act claims.",
        "related_issues": ["Vehicle insurance claim", "Good Samaritan protections", "Hit-and-run compensation fund"],
        "follow_up_questions": [
            {"q": "Did the offending vehicle stop, or did they flee the spot?", "options": ["Driver fled the scene (Hit and run)", "Driver stopped / vehicle at spot", "Single vehicle self-accident"]},
            {"q": "Were there grievous injuries or loss of life?", "options": ["Severe injuries / hospitalization", "Minor bruises / vehicle damage only", "Fatal incident"]}
        ]
    },

    "consumer_seller_cheated": {
        "id": "consumer_seller_cheated",
        "title": "A company/seller cheated me or gave defective goods",
        "category": "Financial & Consumer Fraud",
        "is_emergency": False,
        "summary": "An online portal, company, or shop seller delivered fake/defective items, refused a legitimate refund, or engaged in misleading advertising and deficiency of service.",
        "legal_issue": "Deficiency in service, unfair trade practices, and consumer protection rights.",
        "classification": ["Consumer Dispute", "Regulatory Complaint", "Potentially Criminal if Fraudulent"],
        "constitutional_articles": [],
        "statutory_provisions": [
            {
                "act": "Consumer Protection Act, 2019",
                "section": "Sections 2(47), 35, 84",
                "deals_with": "Unfair trade practices, consumer complaint before District Commission, and Product Liability.",
                "relevance": "Consumer has statutory right to replacement, full refund with interest, and compensation for mental agony."
            },
            {
                "act": "Consumer Protection (E-Commerce) Rules, 2020",
                "section": "Rule 5 & 6",
                "deals_with": "Obligations of e-commerce platforms regarding returns, refunds, and counterfeit goods.",
                "relevance": "E-commerce platforms cannot refuse refunds for defective products or hide seller details."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 318 (replaces IPC 420)",
                "deals_with": "Cheating (if there was deliberate pre-planned fraudulent intention from the start).",
                "relevance": "If a fake website took money without any intent to deliver goods."
            }
        ],
        "immediate_steps": [
            "Send a formal written notice or email to the seller and marketplace customer support demanding refund/replacement within 7 days.",
            "Do NOT return the defective product without video recording the unboxing and repacking condition.",
            "Register a complaint on the National Consumer Helpline (NCH) portal (consumerhelpline.gov.in) or call 1915.",
            "If unresolved, file an online consumer case on E-Daakhil (edaakhil.nic.in) before the District Consumer Disputes Redressal Commission.",
            "If the seller is a fake website running a scam, register a cyber fraud complaint on cybercrime.gov.in."
        ],
        "evidence_checklist": [
            "Tax invoice / purchase order receipt and order confirmation emails",
            "Unboxing video and high-resolution photographs showing product defect",
            "Chat logs, customer care emails, and written refusal of refund",
            "Bank / credit card payment transaction receipt and debit confirmation",
            "Original product packaging, barcode, and serial number tag"
        ],
        "reporting_channels": [
            {"authority": "National Consumer Helpline (NCH)", "contact": "Dial 1915 / consumerhelpline.gov.in", "details": "Pre-litigation mediation with registered companies."},
            {"authority": "E-Daakhil Portal", "contact": "edaakhil.nic.in", "details": "Official portal to file digital consumer cases before Consumer Commissions without physical court visit."},
            {"authority": "Central Consumer Protection Authority (CCPA)", "contact": "consumeraffairs.nic.in", "details": "Class action regulator for misleading advertisements and unfair trade practices."}
        ],
        "police_refusal_escalation": "Ordinary consumer disputes over defective goods are civil/consumer matters, not police FIRs. However, if the seller was a fake phantom website operating a scam, it is a criminal offence under Section 318 BNS reportable on cybercrime.gov.in.",
        "know_the_difference": "This is primarily a **Consumer Dispute** handled under the Consumer Protection Act, 2019, rather than criminal police law, unless intentional fraudulent deceit is evident.",
        "confidence_level": "Confirmed consumer rights issue under Consumer Protection Act 2019.",
        "related_issues": ["Product liability", "Unfair contract terms", "Cyber financial scam if ghost website"],
        "follow_up_questions": [
            {"q": "Was this a legitimate company delivering defective goods, or a fake scam website?", "options": ["Legitimate company / marketplace with service failure", "Fake ghost website / social media seller that took money and disappeared", "Unsure"]},
            {"q": "What is the financial value involved?", "options": ["Under Rs. 50,000", "Between Rs. 50,000 and Rs. 5,00,000", "Above Rs. 5,00,000"]}
        ]
    }
,

    "robbery_dacoity": {
        "id": "robbery_dacoity",
        "title": "Someone robbed me at gunpoint / knifepoint",
        "category": "Violence, Threats & Assault",
        "is_emergency": True,
        "summary": "Assailants threatened you or used deadly weapons (knife, firearm, acid) to forcibly take your belongings, cash, or vehicle.",
        "legal_issue": "Robbery or Dacoity (if 5 or more persons) involving threat of instant death, hurt, or wrongful restraint.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Personal Liberty", "connection": "Armed violent crime is a direct threat to bodily integrity and personal survival."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 309 & Section 310",
                "deals_with": "Robbery and Dacoity (imprisonment up to 10-14 years, or life imprisonment for dacoity).",
                "relevance": "Theft accompanied by causing or attempting to cause death, hurt, or wrongful restraint."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 311",
                "deals_with": "Robbery or dacoity with attempt to cause death or grievous hurt using deadly weapon.",
                "relevance": "Mandatory minimum imprisonment of not less than seven years."
            },
            {
                "act": "Arms Act, 1959",
                "section": "Section 25 / 27",
                "deals_with": "Illegal possession and use of prohibited arms and ammunition.",
                "relevance": "Carrying unlicensed guns or knives during commission of offences."
            }
        ],
        "immediate_steps": [
            "Ensure immediate physical safety; move into a crowded area, shop, or police booth.",
            "Dial 112 immediately to report the crime in progress and give the assailant escape route/description.",
            "If physically injured, request an ambulance or visit the nearest hospital emergency room for an MLC (Medico-Legal Certificate).",
            "Immediately block all credit/debit cards and SIM cards if your wallet or mobile was taken.",
            "Demand registration of an immediate FIR under Section 173 BNSS with robbery/arms sections."
        ],
        "evidence_checklist": [
            "Physical description of assailants (height, age, clothing, accents, distinct tattoos/marks)",
            "Vehicle details used by robbers (make, color, partial registration number)",
            "Hospital Medico-Legal Certificate (MLC) detailing physical trauma or wounds",
            "CCTV footage from street cameras, traffic signals, ATMs, or shop fronts",
            "Serial numbers/IMEI numbers of stolen devices or cash denominations"
        ],
        "reporting_channels": [
            {"authority": "Police Control Room (Emergency)", "contact": "Dial 112", "details": "Immediate dispatch of police PCR van and wireless alert."},
            {"authority": "Jurisdictional Police Station", "contact": "Local Police Thana", "details": "Registration of formal FIR under Section 309/311 BNS."},
            {"authority": "District Legal Services Authority (DLSA)", "contact": "District Court Complex / NALSA 15100", "details": "Free legal aid and victim compensation scheme under Section 396 BNSS."}
        ],
        "police_refusal_escalation": "Armed robbery is a heinous cognizable offence. Police CANNOT refuse an FIR. If refused, escalate immediately to Deputy Commissioner of Police (DCP) / SP under Section 173(4) BNSS and invoke magistrate intervention under Section 175(3) BNSS.",
        "know_the_difference": "This is a serious **Heinous Criminal Offence**. It is not a civil dispute. State apparatus is legally bound to investigate immediately.",
        "confidence_level": "Confirmed armed criminal offence under Section 309/311 BNS.",
        "related_issues": ["Arms Act violations", "Victim Compensation Scheme under Section 396 BNSS", "Identity and banking theft"],
        "follow_up_questions": [
            {"q": "How many persons were involved in the robbery?", "options": ["1 or 2 persons", "3 to 4 persons", "5 or more persons (Legally classified as Dacoity)"]},
            {"q": "Were deadly weapons (firearms, knives) brandished or used?", "options": ["Yes, firearms / guns", "Yes, knife / bladed weapon", "No weapons, only physical assault"]}
        ]
    },

    "extortion_protection_money": {
        "id": "extortion_protection_money",
        "title": "Someone is demanding extortion money ('hafta') / blackmailing for cash",
        "category": "Violence, Threats & Assault",
        "is_emergency": True,
        "summary": "Local goons, criminals, or individuals are threatening bodily harm, destruction of your business, or false cases unless you pay protection money ('hafta').",
        "legal_issue": "Extortion and putting person in fear of injury in order to commit extortion.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 19(1)(g)", "name": "Right to Practice Any Profession/Trade", "connection": "Extortion rackets illegally impair the citizen's fundamental right to conduct business freely."},
            {"article": "Article 21", "name": "Right to Life & Personal Liberty", "connection": "Intimidation and threat to bodily life or property."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 308",
                "deals_with": "Extortion (punishable with imprisonment up to 3 years or fine or both).",
                "relevance": "Intentionally putting any person in fear of injury and dishonestly inducing delivery of money or valuable property."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 308(4) & (5)",
                "deals_with": "Extortion by putting person in fear of death or grievous hurt (punishable up to 10 years).",
                "relevance": "Aggravated extortion involving life-threatening demands or gang threats."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 398",
                "deals_with": "Witness Protection Scheme.",
                "relevance": "Statutory right to witness and victim protection against retaliation by criminal gangs."
            }
        ],
        "immediate_steps": [
            "Do NOT pay the extortion money, as payments routinely lead to escalating recurring demands.",
            "Record all phone calls, preserve WhatsApp/SMS threats, and do not delete any voice notes.",
            "Immediately notify the local Police Station in writing and meet the Assistant Commissioner of Police (ACP) / SP.",
            "Request police patrol protection for your commercial shop, workplace, or residence.",
            "Request witness and victim protection under the Witness Protection Scheme (Section 398 BNSS)."
        ],
        "evidence_checklist": [
            "Audio call recordings of threatening phone conversations",
            "Screenshots and exported chat transcripts of text messages, WhatsApp, or letters",
            "CCTV footage of extortionists visiting your shop, office, or residence",
            "Bank account / UPI details provided by the extortionist for payment",
            "Statements from staff or neighbors who witnessed the intimidations"
        ],
        "reporting_channels": [
            {"authority": "Senior Police / Anti-Extortion Cell", "contact": "Local Police Commissioner / SP Office", "details": "Specialized Crime Branch / Anti-Extortion Cell handles gang rackets."},
            {"authority": "Police Control Room", "contact": "Dial 112", "details": "Emergency immediate dispatch if extortionists are outside premises."},
            {"authority": "Judicial Magistrate", "contact": "Chief Judicial Magistrate Court", "details": "Complaint under Section 175(3) BNSS for court-monitored investigation."}
        ],
        "police_refusal_escalation": "Extortion with threat of hurt is a non-bailable cognizable offence. If local thana hesitates due to local gang influence, submit written complaint to the Police Commissioner / SP with call recordings, and petition the High Court under Section 528 BNSS (inherent powers) if life is in danger.",
        "know_the_difference": "This is a **Criminal Offence of Extortion**. It is NOT a private debt or civil business misunderstanding.",
        "confidence_level": "Confirmed criminal extortion under Section 308 BNS.",
        "related_issues": ["Organized crime syndicates", "Witness intimidation", "Commercial harassment"],
        "follow_up_questions": [
            {"q": "Is the demand accompanied by threat to life or family safety?", "options": ["Yes, direct threat to kill or harm family", "Threat to vandalize business / shop", "Threat of defamation or false legal cases"]},
            {"q": "Has any money been transferred already?", "options": ["No money paid yet", "Partial payment made under fear", "Multiple payments already coerced"]}
        ]
    },

    "assault_physical_fight": {
        "id": "assault_physical_fight",
        "title": "Someone physically beat or assaulted me / caused injuries",
        "category": "Violence, Threats & Assault",
        "is_emergency": True,
        "summary": "You were physically attacked, beaten, punched, or struck with objects, resulting in bodily pain, bruises, fractures, or bleeding.",
        "legal_issue": "Voluntarily causing hurt or grievous hurt, and criminal assault.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Bodily Integrity", "connection": "Every citizen possesses fundamental right against unlawful physical violence and torture."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 115 & Section 117",
                "deals_with": "Voluntarily causing hurt and voluntarily causing grievous hurt.",
                "relevance": "Grievous hurt includes fractures, dislocation of teeth/bone, loss of sight/hearing, or 20+ days of severe bodily pain."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 118",
                "deals_with": "Voluntarily causing hurt or grievous hurt by dangerous weapons or means.",
                "relevance": "Using sticks, iron rods, glass bottles, sharp objects, or fire."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 189",
                "deals_with": "Unlawful assembly and rioting (if mob or multiple attackers).",
                "relevance": "Every member of unlawful assembly is guilty of offences committed in prosecution of common object."
            }
        ],
        "immediate_steps": [
            "Get to medical safety and visit the nearest government or private hospital casualty immediately.",
            "Ensure the doctor registers an official MLC (Medico-Legal Certificate) recording all injuries.",
            "Take clear, date-stamped photographs of all bruises, cuts, lacerations, and torn clothes.",
            "Call 112 from the hospital or ensure hospital sends police intimation (DD entry).",
            "File an FIR at the police station having jurisdiction over the attack site."
        ],
        "evidence_checklist": [
            "Official Medico-Legal Case (MLC) report and emergency doctor discharge notes",
            "High-resolution photographs of all bodily injuries, fractures, and bloodstains",
            "Torn or bloodstained clothing preserved in paper bags (do not wash)",
            "CCTV video footage of the fight or brawl from surrounding premises",
            "Names and phone numbers of neutral eyewitnesses who witnessed the assault"
        ],
        "reporting_channels": [
            {"authority": "Hospital Casualty / CMO", "contact": "Any Government / Private Hospital", "details": "Mandatory MLC examination and injury profiling under medical protocol."},
            {"authority": "Police Control Room", "contact": "Dial 112", "details": "Emergency response to brawl or assault site."},
            {"authority": "Jurisdictional Police Station", "contact": "Local Police Station", "details": "Registration of FIR under Section 115/117/118 BNS."}
        ],
        "police_refusal_escalation": "Simple hurt without weapons is non-cognizable (NCR), but grievous hurt (fracture, deep wounds) or use of weapons (Section 118 BNS) is STRICTLY COGNIZABLE. If police try to register only an NCR for grievous wounds, produce the MLC report to the SP under Section 173(4) BNSS or Magistrate under Section 175(3) BNSS.",
        "know_the_difference": "This is a **Criminal Offence**. While self-defence exists under Sections 34-44 BNS, aggressive physical battery is punished by criminal courts.",
        "confidence_level": "Confirmed criminal offence of causing hurt / grievous hurt under BNS Chapter VI.",
        "related_issues": ["Private defence boundaries", "Victim Compensation under Section 396 BNSS", "Mob violence / rioting"],
        "follow_up_questions": [
            {"q": "Did the attack involve weapons (rods, bottles, knives, sticks)?", "options": ["Yes, dangerous weapons used", "No weapons, bare hands and feet", "Unsure / blunt objects"]},
            {"q": "Did you suffer bone fractures, disfigurement, or hospital admission?", "options": ["Yes, fracture / cut requiring stitches / admission (Grievous Hurt)", "Minor bruises and pain (Simple Hurt)", "Head injury / concussion"]}
        ]
    },

    "criminal_intimidation_threats": {
        "id": "criminal_intimidation_threats",
        "title": "Someone is threatening to kill or harm me / my family",
        "category": "Violence, Threats & Assault",
        "is_emergency": True,
        "summary": "An individual or group has issued serious verbal, written, or telephonic threats to cause death, rape, grievous hurt, or destruction of your home.",
        "legal_issue": "Criminal Intimidation with threat to cause death or grievous hurt.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Personal Security", "connection": "Threat to life engages state obligation to protect citizens from foreseeable imminent violence."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 351",
                "deals_with": "Criminal intimidation.",
                "relevance": "Threatening any person with injury to person, reputation, or property to compel them to do any act against their will."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 351(3)",
                "deals_with": "Criminal intimidation by threatening to cause death or grievous hurt (punishable up to 7 years).",
                "relevance": "Aggravated criminal intimidation where threat involves death, grievous hurt, rape, or burning property."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 126 & Section 128",
                "deals_with": "Security for keeping peace and good behaviour (Preventive Action).",
                "relevance": "Executive Magistrate can bind down the aggressor on peace bonds with hefty surety."
            }
        ],
        "immediate_steps": [
            "Do NOT confront the aggressor alone; activate call recorders on your phone immediately.",
            "Save and export screenshots of WhatsApp messages, call logs, emails, and voicemail recordings.",
            "Submit a formal written complaint to the Station House Officer (SHO) requesting preventive action and bond under Section 126 BNSS.",
            "Mark a formal copy to the District Superintendent of Police (SP) citing threat to life.",
            "Install security cameras at your residential doorway and avoid secluded routes."
        ],
        "evidence_checklist": [
            "Audio call recordings containing specific threat phrases ('I will kill you', 'I will finish your family')",
            "Screenshots of text messages, chat threads, or threatening letters",
            "Call detail records (CDR) showing repeated calls from offender's number",
            "CCTV footage if threats were delivered at home or workplace entrance",
            "Statements of family members or colleagues who were present"
        ],
        "reporting_channels": [
            {"authority": "Local Police Station (Thana)", "contact": "Station House Officer", "details": "Formal written complaint under Section 351(3) BNS and Section 126 BNSS."},
            {"authority": "Superintendent of Police / DCP", "contact": "District Police Headquarters", "details": "Escalation for threat assessment and preventive police patrol."},
            {"authority": "National / State Human Rights Commission (NHRC)", "contact": "nhrc.nic.in / hrcnet.nic.in", "details": "Intervention if police fail to act despite clear threat to life."}
        ],
        "police_refusal_escalation": "Threats to kill or cause grievous hurt under Section 351(3) BNS are cognizable in several states. Furthermore, police have preventive duties under BNSS Section 168-172. If police ignore, file a Section 175(3) BNSS application before the Magistrate seeking police investigation and protection.",
        "know_the_difference": "This is a **Criminal Matter**. An anticipatory threat to life requires criminal deterrence and preventive surety bonds, not a civil suit.",
        "confidence_level": "Confirmed criminal intimidation under Section 351 BNS.",
        "related_issues": ["Preventive arrest of aggressor", "Peace bonds under BNSS Section 126", "Restraining orders"],
        "follow_up_questions": [
            {"q": "What specific harm was threatened?", "options": ["Threat to kill or murder", "Threat of sexual assault / rape", "Threat to break limbs / assault", "Threat of financial or business ruin"]},
            {"q": "How were the threats communicated?", "options": ["Over phone calls / voice notes", "Via text / WhatsApp / social media", "In person face-to-face with weapons"]}
        ]
    },

    "acid_attack_attempt": {
        "id": "acid_attack_attempt",
        "title": "Threat of acid attack / acid throwing attack",
        "category": "Violence, Threats & Assault",
        "is_emergency": True,
        "summary": "Someone has thrown acid or corrosive substances causing chemical burns, or is threatening to buy acid to disfigure you.",
        "legal_issue": "Acid attack, attempt to throw acid, and illegal sale of unregulated corrosive substances.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life, Dignity & Bodily Integrity", "connection": "Supreme Court in Laxmi v. Union of India established fundamental right to free medical care and state compensation for acid attack survivors."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 124(1)",
                "deals_with": "Voluntarily causing grievous hurt by use of acid (imprisonment not less than 10 years up to life).",
                "relevance": "Fine must be just and reasonable to meet medical expenses of the victim."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 124(2)",
                "deals_with": "Voluntarily throwing or attempting to throw acid (punishable with imprisonment 5 to 7 years).",
                "relevance": "Criminalizes even the attempt or throwing of acid regardless of whether permanent damage was caused."
            },
            {
                "act": "Poisons Act, 1919 & MHA Guidelines",
                "section": "Regulation of Acid Sales",
                "deals_with": "Mandatory ID verification and ban on open over-the-counter sale of acid.",
                "relevance": "Sellers must maintain logbook of buyer Aadhaar and purpose."
            }
        ],
        "immediate_steps": [
            "FIRST AID: Immediately rinse the affected skin under running clean tap water continuously for at least 30-45 minutes. Do NOT apply ointments, oils, or ice.",
            "Rush to the nearest hospital immediately. Under Supreme Court guidelines and Section 397 BNSS, ALL hospitals (government and private) MUST treat acid attack victims FREE OF COST.",
            "Dial 112 and demand immediate police dispatch to the scene and the hospital.",
            "Preserve any clothes, container, bottle, or bike details associated with the attacker.",
            "Apply immediately for interim victim compensation through the District Legal Services Authority (DLSA) under the Central Victim Compensation Fund."
        ],
        "evidence_checklist": [
            "Chemical residue, bottle, or container used to throw the substance",
            "Emergency Medico-Legal Certificate (MLC) detailing burn percentage and depth",
            "CCTV footage from the attack location and nearby acid/chemical shops",
            "Threat messages, stalking records, or previous police complaints against accused",
            "Burned clothing and footwear packed safely in non-reactive containers"
        ],
        "reporting_channels": [
            {"authority": "Emergency Ambulance & Trauma Care", "contact": "Dial 108 / 112", "details": "Immediate emergency burn stabilization."},
            {"authority": "Jurisdictional Police Station", "contact": "Local Police Station", "details": "Immediate FIR under Section 124 BNS (Non-bailable, cognizable)."},
            {"authority": "District Legal Services Authority (DLSA)", "contact": "District Court Complex", "details": "Mandatory interim compensation (minimum Rs. 3 Lakhs) within 15 days."},
            {"authority": "National Commission for Women (NCW)", "contact": "ncw.nic.in / 7827170170", "details": "Dedicated monitoring cell for violence against women."}
        ],
        "police_refusal_escalation": "Refusal to register an FIR in acid attack cases is an express criminal offence for police officers under Section 199 BNS (dereliction of duty). Report directly to the High Court Chief Justice or District Judge if police delay.",
        "know_the_difference": "This is a **Heinous Violent Crime**. Free medical treatment is a non-negotiable statutory obligation for all hospitals.",
        "confidence_level": "Confirmed heinous criminal offence under Section 124 BNS.",
        "related_issues": ["Mandatory free medical care", "Interim compensation from DLSA", "Illegal OTC acid sale prosecution"],
        "follow_up_questions": [
            {"q": "Has acid already been thrown, or is this an imminent threat?", "options": ["Acid has been thrown / injury occurred (Emergency)", "Attacker has threatened / attempted to throw acid", "Stockpiling acid / verbal threat"]},
            {"q": "Has medical emergency treatment been received?", "options": ["At hospital currently", "Received first aid, looking for legal action", "No medical treatment yet"]}
        ]
    },

    "kidnapping_abduction": {
        "id": "kidnapping_abduction",
        "title": "Someone kidnapped / abducted a person or child",
        "category": "Violence, Threats & Assault",
        "is_emergency": True,
        "summary": "A child or adult was unlawfully taken away, confined against their will, or held for ransom or illicit purposes.",
        "legal_issue": "Kidnapping from lawful guardianship, abduction, and kidnapping for ransom.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Personal Liberty", "connection": "Unlawful physical confinement is the gravest deprivation of personal liberty."},
            {"article": "Article 23", "name": "Prohibition of Traffic in Human Beings", "connection": "Abduction for exploitation violates absolute constitutional guarantee against forced captivity."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 137",
                "deals_with": "Kidnapping from India and from lawful guardianship (under 18 years).",
                "relevance": "Taking or enticing any minor out of the keeping of the lawful guardian without consent."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 140",
                "deals_with": "Kidnapping for ransom, etc. (punishable with death or imprisonment for life).",
                "relevance": "Holding any person captive and threatening to cause death or hurt to compel payment of ransom."
            },
            {
                "act": "Standard Operating Procedure (Supreme Court Bachpan Bachao Andolan)",
                "section": "Missing Children Guidelines",
                "deals_with": "Mandatory presumption of kidnapping for any missing minor child.",
                "relevance": "Police must immediately register FIR for kidnapping whenever a child goes missing."
            }
        ],
        "immediate_steps": [
            "Dial 112 immediately. Every second counts in kidnapping cases.",
            "Visit the police station immediately; under Supreme Court directives, police CANNOT declare a missing child 'absent' — they MUST register an FIR for kidnapping immediately.",
            "Provide the victim latest clear photograph, clothes worn, age proof, and physical description to the police.",
            "Request police to initiate emergency mobile tower location tracking of the victim phone.",
            "Alert Childline 1098 if the victim is a minor (below 18 years)."
        ],
        "evidence_checklist": [
            "Recent high-resolution photographs showing face, height, and distinct marks",
            "Accurate time and last known GPS location / mobile signal ping",
            "Call recordings and numbers if ransom or threat calls have been received",
            "CCTV footage from vicinity of the abduction or last seen location",
            "Vehicle details or eyewitness accounts of how the victim was taken"
        ],
        "reporting_channels": [
            {"authority": "Emergency Police Control Room", "contact": "Dial 112", "details": "Immediate state-wide wireless flash and highway naka bandi."},
            {"authority": "Childline India", "contact": "Dial 1098 (24x7)", "details": "Emergency nodal agency for missing and kidnapped children."},
            {"authority": "Track Child Portal", "contact": "trackchild.gov.in", "details": "National portal for missing and vulnerable children."}
        ],
        "police_refusal_escalation": "Refusal to register an FIR for a missing child violates Supreme Court orders (Bachpan Bachao Andolan v. UOI). Approach the Superintendent of Police (SP) or National Commission for Protection of Child Rights (NCPCR) immediately.",
        "know_the_difference": "This is an **Emergency Heinous Crime**. Police have an unconditional statutory obligation to deploy search teams.",
        "confidence_level": "Confirmed grave criminal offence under Section 137/140 BNS.",
        "related_issues": ["Child rescue protocol", "Anti-human trafficking units (AHTU)", "Transit tracking"],
        "follow_up_questions": [
            {"q": "Is the victim a minor child (under 18 years)?", "options": ["Yes, minor child", "No, adult person", "Unsure"]},
            {"q": "Has any ransom demand or communication been received?", "options": ["Yes, ransom demanded", "No communication received yet", "Suspicion of family / custody dispute"]}
        ]
    },

    "human_trafficking": {
        "id": "human_trafficking",
        "title": "Human trafficking / forced labour / commercial sexual exploitation",
        "category": "Discrimination & Human Rights",
        "is_emergency": True,
        "summary": "Persons or children are being recruited, transported, harboured, or transferred by use of force, fraud, or coercion for forced labour, domestic servitude, organ removal, or sexual exploitation.",
        "legal_issue": "Trafficking of persons and bonded / forced labour.",
        "classification": ["Criminal Offence", "Constitutional Violation"],
        "constitutional_articles": [
            {"article": "Article 23", "name": "Prohibition of Traffic in Human Beings & Forced Labour", "connection": "Direct, self-executing constitutional ban on human trafficking, begar, and involuntary servitude."},
            {"article": "Article 24", "name": "Prohibition of Employment of Children in Factories/Hazardous Occupations", "connection": "Absolute constitutional prohibition against child exploitation."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 143",
                "deals_with": "Trafficking of persons (punishable with rigorous imprisonment 7 to 10 years, up to life).",
                "relevance": "Comprehensive definition covering recruitment, transport, harbouring using threat, deception, or abuse of power."
            },
            {
                "act": "Bonded Labour System (Abolition) Act, 1976",
                "section": "Sections 16 to 20",
                "deals_with": "Abolition of bonded debt labour and immediate release/rehabilitation.",
                "relevance": "Statutory extinguishing of all alleged debts and provision of release certificates."
            },
            {
                "act": "Immoral Traffic (Prevention) Act, 1956 (ITPA)",
                "section": "Sections 3 to 9",
                "deals_with": "Suppression of commercial brothels, pimping, and trafficking for prostitution.",
                "relevance": "Criminalizes traffickers and brothel keepers while shielding rescued victims."
            }
        ],
        "immediate_steps": [
            "Contact the dedicated Anti-Human Trafficking Unit (AHTU) through the District Police or Dial 112.",
            "Contact specialized NGOs or NALSA (15100) / Childline (1098) for immediate tactical rescue operations.",
            "Do NOT alert the traffickers or employer before police and District Magistrate raid teams are mobilized.",
            "Ensure the District Magistrate issues formal 'Release Certificates' under the Bonded Labour Act for immediate cash rehabilitation grant.",
            "Victims must be sent to safe government shelter homes (Swadhar Greh / Ujjawala) and provided medical care."
        ],
        "evidence_checklist": [
            "Location of the factory, brick kiln, brothel, or placement agency",
            "Names or aliases of placement agents, contractors (thekedars), or traffickers",
            "Passports, Aadhaar cards, or phones confiscated from victims by exploiters",
            "Records of unpaid wages, wage deductions, or fake debt account books",
            "Photographs or videos of confined conditions and armed guards"
        ],
        "reporting_channels": [
            {"authority": "Anti-Human Trafficking Unit (AHTU)", "contact": "District Police Headquarters", "details": "Specialized nodal wing in every police district for trafficking operations."},
            {"authority": "National Human Rights Commission (NHRC)", "contact": "nhrc.nic.in / Dial 14433", "details": "Direct investigation division for trafficking and bonded labour rescues."},
            {"authority": "National Legal Services Authority (NALSA)", "contact": "Toll-Free 15100", "details": "Free legal aid, counsel representation, and victim rehabilitation funds."}
        ],
        "police_refusal_escalation": "Trafficking is a non-bailable, non-compoundable heinous crime. If local police are complicit with local contractors, alert the State CID, NHRC, and the National Commission for Women (NCW) directly.",
        "know_the_difference": "This is both an aggravated **Criminal Offence** and a direct **Constitutional Violation** of Article 23.",
        "confidence_level": "Confirmed grave criminal and constitutional violation under Section 143 BNS and Article 23.",
        "related_issues": ["Bonded labour rehabilitation grants", "Shelter home protection", "Immigrant worker exploitation"],
        "follow_up_questions": [
            {"q": "What is the nature of the exploitation?", "options": ["Forced labour / bonded debt at factory/brick kiln", "Commercial sexual exploitation / brothel", "Forced domestic servitude / placement agency", "Child begging / organ removal"]},
            {"q": "Are the victims physically confined and documents confiscated?", "options": ["Yes, locked up / documents seized", "Free movement restricted by threats", "Unsure"]}
        ]
    },

    "sexual_harassment_molestation": {
        "id": "sexual_harassment_molestation",
        "title": "Someone sexually touched or harassed me in a public / private place",
        "category": "Safety & Crimes Against Women",
        "is_emergency": True,
        "summary": "You were subjected to unwelcome physical contact, sexual groping, molestation, sexually coloured remarks, or showing of pornography without consent in a public place, transit, or private area.",
        "legal_issue": "Sexual harassment, assault or use of criminal force to woman with intent to outrage her modesty.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 15(1) & (3)", "name": "Prohibition of Discrimination & Special Provisions for Women", "connection": "State obligation to provide non-discriminatory, safe public environments for women."},
            {"article": "Article 21", "name": "Right to Life, Dignity & Bodily Autonomy", "connection": "Right to live with dignity and bodily privacy free from sexual aggression."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 74",
                "deals_with": "Assault or use of criminal force to woman with intent to outrage modesty (punishable 1 to 5 years).",
                "relevance": "Physical groping, grabbing, pulling clothes, or bodily touch with sexual intent."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 75",
                "deals_with": "Sexual harassment (unwelcome contact, demand for favours, showing porn, sexually coloured remarks).",
                "relevance": "Punishable with rigorous imprisonment up to 3 years or fine."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 79",
                "deals_with": "Word, gesture, or act intended to insult modesty of a woman.",
                "relevance": "Lewd gestures, sexual catcalling, or intruding upon privacy."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 173(1) Proviso",
                "deals_with": "Recording of statement by woman police officer.",
                "relevance": "Statement must be recorded exclusively by a woman police officer."
            }
        ],
        "immediate_steps": [
            "Get to immediate safety; raise an alarm to attract public bystanders or transit staff (metro / bus conductor).",
            "Dial 112 or Women Helpline 1090 / 181 immediately.",
            "Demand that your complaint at the police station be recorded by a WOMAN police officer (mandatory under Section 173 BNSS).",
            "Under Section 183(6) BNSS, your statement must also be recorded before a Judicial Magistrate as soon as possible.",
            "Obtain a certified copy of the FIR free of charge."
        ],
        "evidence_checklist": [
            "Exact date, time, and location (metro station, bus route, street corner)",
            "Photographs or video recordings taken on your phone or by co-passengers",
            "CCTV footage from transit authorities (DMRC/metro, bus depot, municipal cameras)",
            "Contact numbers of fellow passengers or witnesses who stepped forward",
            "Text messages, social media chats, or call records if offender is known"
        ],
        "reporting_channels": [
            {"authority": "Women Helpline (Emergency)", "contact": "Dial 1090 / Dial 181 / Dial 112", "details": "Dedicated 24x7 women distress response."},
            {"authority": "Local Police Station / e-FIR", "contact": "Nearest Police Station", "details": "Lodge FIR under Section 74/75 BNS before a woman police officer."},
            {"authority": "National Commission for Women (NCW)", "contact": "ncw.nic.in / 7827170170", "details": "Monitoring of investigation and complaint redressal."}
        ],
        "police_refusal_escalation": "Refusal to register an FIR under Section 74/75 BNS is a punishable crime for the police officer under Section 199 BNS. You can lodge an FIR at ANY police station regardless of jurisdiction (Zero FIR under Section 173 BNSS).",
        "know_the_difference": "This is a **Cognizable Criminal Offence**. Police have zero legal discretion to turn you away or suggest compromise.",
        "confidence_level": "Confirmed criminal offence under Section 74/75 BNS.",
        "related_issues": ["Zero FIR rights", "Mandatory female officer statement", "Free legal counsel from DLSA"],
        "follow_up_questions": [
            {"q": "Was there physical touch/groping or verbal/visual harassment?", "options": ["Physical touching / grabbing / assault (Section 74 BNS)", "Verbal comments / showing porn / gestures (Section 75/79 BNS)", "Both physical and verbal"]},
            {"q": "Where did the incident occur?", "options": ["Public transport (bus, train, metro)", "Road / public street / market", "Private vehicle / taxi / cab", "At home or private room"]}
        ]
    },

    "rape_sexual_assault": {
        "id": "rape_sexual_assault",
        "title": "Sexual assault / rape survivor seeking immediate help and justice",
        "category": "Safety & Crimes Against Women",
        "is_emergency": True,
        "summary": "You or someone you know was subjected to non-consensual sexual penetration, forced sexual acts, or rape.",
        "legal_issue": "Rape and aggravated sexual assault.",
        "classification": ["Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life, Bodily Privacy & Dignity", "connection": "Supreme Court has repeatedly affirmed that sexual assault is the most severe violation of the fundamental right to life and bodily autonomy."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 64 & Section 70",
                "deals_with": "Rape and Gang Rape (rigorous imprisonment not less than 10 years up to life, and 20 years to life for gang rape).",
                "relevance": "Comprehensive statutory definition of non-consensual sexual assault."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 51 & Section 184",
                "deals_with": "Medical examination of rape victim.",
                "relevance": "Must be conducted by a registered female medical practitioner within 24 hours with consent. Two-finger test is strictly illegal and banned."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 183(6) & Section 396",
                "deals_with": "Judicial Magistrate statement and Victim Compensation.",
                "relevance": "Mandatory statement recording before Magistrate and immediate interim financial compensation under Victim Compensation Scheme."
            }
        ],
        "immediate_steps": [
            "Your immediate safety and medical care is paramount. Dial 112 or reach out to a trusted person immediately.",
            "DO NOT shower, bathe, brush teeth, change clothes, or comb hair before medical examination, to preserve critical DNA evidence.",
            "Go immediately to the nearest government or private hospital. All hospitals are legally mandated under Section 397 BNSS to treat rape survivors immediately and free of cost.",
            "Two-finger test is strictly prohibited and illegal under Supreme Court orders. If any doctor attempts it, object immediately.",
            "Statement to police MUST be recorded by a woman police officer at your residence or place of choice.",
            "Contact DLSA (15100) for free female legal representation and an immediate interim compensation grant."
        ],
        "evidence_checklist": [
            "Clothes worn during the incident (stored carefully in clean paper bags, not plastic)",
            "Medico-Legal examination report (MLC) and sexual assault forensic evidence kit (SAEK)",
            "WhatsApp chats, text messages, phone call recordings, or location shares with accused",
            "CCTV footage from hotel, car, premises, or residential entrance",
            "Emergency contraceptive / medical prescription administered by doctor"
        ],
        "reporting_channels": [
            {"authority": "Women Distress Helpline", "contact": "Dial 112 / Dial 1090 / Dial 181", "details": "Emergency trauma dispatch and legal escort."},
            {"authority": "One Stop Centre (Sakhi Centre)", "contact": "Available in every district hospital", "details": "Integrated shelter, medical aid, legal counselling, and police facilitation under one roof."},
            {"authority": "District Legal Services Authority (DLSA)", "contact": "Toll-Free 15100", "details": "Appointment of free female legal counsel and urgent financial compensation under Section 396 BNSS."}
        ],
        "police_refusal_escalation": "Refusal to register an FIR in a rape case is a severe cognizable crime under Section 199 BNS punishable with imprisonment up to 2 years for the police officer. Zero FIR is mandatory under Section 173 BNSS.",
        "know_the_difference": "This is a **Grave Heinous Criminal Offence**. Complete confidentiality of victim identity is legally mandatory under Section 73 BNS (disclosure of victim identity is a crime).",
        "confidence_level": "Confirmed grave criminal offence under Section 64/70 BNS.",
        "related_issues": ["Ban on two-finger test", "Mandatory victim confidentiality under Section 73 BNS", "Free legal counsel and rehabilitation"],
        "follow_up_questions": [
            {"q": "Did the assault occur recently (within last 72 hours)?", "options": ["Yes, within last 72 hours (Critical for DNA evidence kit)", "Occurred past week / month", "Ongoing / historical abuse"]},
            {"q": "Have you visited a hospital for medical examination yet?", "options": ["No, have not undergone medical exam yet", "Yes, medical exam completed", "Currently at hospital"]}
        ]
    },

    "workplace_harassment_posh": {
        "id": "workplace_harassment_posh",
        "title": "Facing sexual harassment or retaliation at workplace (POSH)",
        "category": "Workplace & College Harassment",
        "is_emergency": False,
        "summary": "A colleague, manager, or client made unwelcome sexual advances, sexually suggestive remarks, demanded sexual favours in exchange for promotion, or created a hostile work environment.",
        "legal_issue": "Sexual harassment of women at workplace under POSH Act and criminal law.",
        "classification": ["Regulatory / Statutory Redressal", "Civil Remedy", "Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 14 & Article 19(1)(g)", "name": "Right to Equality & Profession", "connection": "Supreme Court in Vishaka held that safe work environment is fundamental to equality and right to work."},
            {"article": "Article 21", "name": "Right to Life with Dignity", "connection": "Freedom from sexual subjugation at workplace is core to constitutional dignity."}
        ],
        "statutory_provisions": [
            {
                "act": "Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 (POSH Act)",
                "section": "Sections 4, 9, 11, 12, 13",
                "deals_with": "Internal Committee (IC), complaint mechanism within 90 days, interim relief, and inquiry procedure.",
                "relevance": "Every organization with 10+ employees must have an IC with an external member. You can demand paid leave up to 3 months or transfer during inquiry."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 75 & Section 79",
                "deals_with": "Sexual harassment and insulting modesty of a woman.",
                "relevance": "You can pursue BOTH a POSH Internal Committee inquiry AND an independent criminal FIR simultaneously."
            }
        ],
        "immediate_steps": [
            "Document every incident with exact dates, times, words spoken, emails, Slack messages, or witnesses.",
            "Backup all evidence (emails, chat logs, call recordings) to your PERSONAL private device and email.",
            "File a formal written complaint with the Internal Committee (IC) / POSH Committee of your organization within 3 months.",
            "Under Section 12 POSH Act, apply for interim relief: transfer of the accused, transfer of yourself, or up to 3 months paid leave.",
            "If your company has fewer than 10 employees, file your complaint with the Local Committee (LC) set up by the District Officer.",
            "You have the full legal right to ALSO file a police FIR under Section 75 BNS if you choose."
        ],
        "evidence_checklist": [
            "Work emails, Slack / Teams chats, WhatsApp messages containing lewd or inappropriate remarks",
            "Performance appraisals and positive feedback before the incident (to defeat false retaliatory claims)",
            "Names and contemporaneous statements of colleagues you confided in immediately after the incident",
            "Calendar invites, hotel bookings, or flight details if harassment occurred on business travel",
            "Formal written complaint submitted to HR / Internal Committee with stamped/email acknowledgment"
        ],
        "reporting_channels": [
            {"authority": "Internal Complaints Committee (IC)", "contact": "Designated POSH IC Email / Presiding Officer", "details": "Mandatory internal tribunal inside your employer organization."},
            {"authority": "Local Complaints Committee (LC)", "contact": "District Magistrate / Women and Child Welfare Officer", "details": "For firms with fewer than 10 employees or if complaint is against the employer himself."},
            {"authority": "Ministry of WCD SHe-Box", "contact": "shebox.wcd.gov.in", "details": "Centralized government portal directly tracking workplace sexual harassment complaints."}
        ],
        "police_refusal_escalation": "The POSH Act is an independent civil-administrative process that does not prevent you from filing a criminal FIR under Section 75 BNS. If HR retaliates or terminates you, that is illegal victimization actionable under labor law and High Court writ.",
        "know_the_difference": "This is a **Statutory Workplace Violation (POSH Act)** AND potentially a **Criminal Offence (Section 75 BNS)**. You can exercise either or both.",
        "confidence_level": "Confirmed workplace statutory protection under POSH Act 2013 and Section 75 BNS.",
        "related_issues": ["Retaliatory termination protection", "Interim leave rights", "Simultaneous criminal FIR rights"],
        "follow_up_questions": [
            {"q": "Does your company have an active Internal Complaints Committee (IC)?", "options": ["Yes, company has IC", "No IC / fewer than 10 employees", "Complaint is against the founder / employer"]},
            {"q": "Are you facing workplace retaliation (bad reviews, threat of firing)?", "options": ["Yes, facing active retaliation / threat to job", "No retaliation yet, but hostile environment", "Already terminated"]}
        ]
    },

    "college_ragging": {
        "id": "college_ragging",
        "title": "Facing ragging, bullying, or intimidation in college / hostel",
        "category": "Workplace & College Harassment",
        "is_emergency": True,
        "summary": "Seniors, batchmates, or hostel students are subjecting you to physical abuse, forced humiliating acts, verbal abuses, financial extortion, or mental torture under the guise of 'ragging'.",
        "legal_issue": "Ragging, criminal intimidation, wrongful confinement, and institutional liability.",
        "classification": ["Criminal Offence", "Regulatory Violation"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Human Dignity", "connection": "Ragging destroys bodily dignity and psychological health, violating Article 21 (Supreme Court in Vishwa Jagriti Mission)."}
        ],
        "statutory_provisions": [
            {
                "act": "UGC Regulations on Curbing the Menace of Ragging, 2009",
                "section": "Regulations 3, 7, 8, 9",
                "deals_with": "Definition of ragging, mandatory anti-ragging squad, FIR within 24 hours, and institutional de-recognition.",
                "relevance": "Colleges MUST suspend perpetrators and lodge an FIR with police within 24 hours of receiving a complaint."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 115, 126, 351",
                "deals_with": "Hurt, wrongful restraint, and criminal intimidation.",
                "relevance": "Individual student perpetrators face criminal prosecution, jail terms, and rustication."
            },
            {
                "act": "State Anti-Ragging Acts",
                "section": "State Specific Anti-Ragging Acts",
                "deals_with": "Non-bailable provisions for ragging offences.",
                "relevance": "Automatic expulsion from institution and debarment from admission to any other institution for 5 years."
            }
        ],
        "immediate_steps": [
            "Call the National UGC Anti-Ragging 24x7 Helpline at 1800-180-5522 or email helpline@antiragging.in immediately. You can remain ANONYMOUS.",
            "Dial 112 if you are in physical danger or locked inside a hostel room.",
            "Submit a formal written complaint to the College Principal, Anti-Ragging Committee, and Hostel Warden.",
            "By law, the College Principal MUST lodge an FIR with the local police station within 24 hours. Failure to do so makes the head of the institution liable for criminal negligence.",
            "If college attempts to cover up the incident, complain directly to the District Collector and UGC."
        ],
        "evidence_checklist": [
            "Names, branches, years, and room numbers of the senior students involved",
            "WhatsApp group messages, calls, audio recordings of verbal abuse or summons to rooms",
            "Medical hospital report / OPD prescription if any physical harm was inflicted",
            "Photographs of torn clothes, injuries, or vandalized study materials",
            "Copy of the formal complaint submitted to College Anti-Ragging Committee"
        ],
        "reporting_channels": [
            {"authority": "National Anti-Ragging Helpline", "contact": "1800-180-5522 (Toll Free 24x7) / helpline@antiragging.in", "details": "Operated by UGC; notifies District Magistrate and SP directly."},
            {"authority": "College Anti-Ragging Committee & Squad", "contact": "Principal / Dean Office", "details": "Mandatory internal inquiry under UGC 2009 regulations."},
            {"authority": "Local Police Station", "contact": "Dial 112 / Local Thana", "details": "Mandatory FIR under BNS hurt/intimidation sections within 24 hours."}
        ],
        "police_refusal_escalation": "Colleges often try to protect their 'reputation' by suppressing ragging. UGC guidelines mandate that if college administration fails to lodge an FIR, UGC will stop all university funding and withdraw recognition. Complain directly to UGC and SP under Section 173(4) BNSS.",
        "know_the_difference": "Ragging is a **Severe Criminal Offence** and a **Regulatory Violation**. It is not college tradition or innocent fun.",
        "confidence_level": "Confirmed illegal conduct governed by UGC 2009 Regulations and BNS criminal provisions.",
        "related_issues": ["Mandatory institutional FIR duty", "Rustication and admission blacklisting", "Hostel safety"],
        "follow_up_questions": [
            {"q": "Did the ragging involve physical violence, forced stripping, or confinement?", "options": ["Yes, physical assault / locked in room / forced acts", "Verbal abuse / harassment / personal servitude", "Threats of academic or hostel boycott"]},
            {"q": "Have you reported this to the college administration?", "options": ["Yes, but college is trying to hush it up", "Not reported yet out of fear", "Reported and waiting for action"]}
        ]
    },

    "fake_job_offer_scam": {
        "id": "fake_job_offer_scam",
        "title": "Cheated by fake job offer / overseas employment scam",
        "category": "Financial & Consumer Fraud",
        "is_emergency": False,
        "summary": "You received a fake appointment letter, job offer, or overseas work visa guarantee and were duped into paying 'registration fees', 'training charges', 'visa clearance', or 'laptop security deposits'.",
        "legal_issue": "Cheating by personation, cyber fraud, forgery of appointment letters, and unlicensed recruitment.",
        "classification": ["Criminal Offence", "Cybercrime"],
        "constitutional_articles": [],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 318 & Section 319",
                "deals_with": "Cheating and cheating by personation (imprisonment up to 7 years and fine).",
                "relevance": "Inducing job-seekers to part with money by falsely pretending to represent reputed companies."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 336 & Section 338",
                "deals_with": "Forgery for purpose of cheating and using forged documents as genuine.",
                "relevance": "Fabricating fake company letterheads, stamps, appointment contracts, and logos."
            },
            {
                "act": "Emigration Act, 1983",
                "section": "Section 10 & Section 24",
                "deals_with": "Illegal recruiting agents recruiting for foreign employment without MEA registration.",
                "relevance": "Operating an unregistered overseas placement agency is a cognizable criminal offence."
            }
        ],
        "immediate_steps": [
            "Stop all communications and do NOT pay any more money for 'final clearance', 'medical exam', or 'refundable deposit'.",
            "Call 1930 immediately or log on to cybercrime.gov.in to report the fraudulent bank accounts and UPI IDs.",
            "Verify the company directly on its official careers portal or email their genuine HR department.",
            "Check if the recruiter is registered on the Ministry of External Affairs eMigrate portal (emigrate.gov.in) if overseas job.",
            "File an FIR for cheating and forgery at the Cyber Crime Police Station."
        ],
        "evidence_checklist": [
            "Fake offer letters, appointment emails, and WhatsApp / Telegram chat transcripts",
            "Bank transaction receipts, UPI transaction IDs, and beneficiary account numbers",
            "Domain names, fake email addresses (e.g., using @gmail.com instead of official company domain)",
            "Phone numbers used by recruiters and job portal listing screenshots",
            "Forged visa copy or fake flight ticket documents provided by the scammers"
        ],
        "reporting_channels": [
            {"authority": "National Cyber Crime Helpline", "contact": "Dial 1930 / cybercrime.gov.in", "details": "Freeze scammer bank accounts before funds are withdrawn."},
            {"authority": "Cyber Crime Police Station", "contact": "District Cyber Police", "details": "Lodge FIR under Section 318/336 BNS and Section 66D IT Act."},
            {"authority": "Ministry of External Affairs (eMigrate)", "contact": "emigrate.gov.in / Helplines", "details": "Prosecution of illegal overseas recruiting agents under Emigration Act."}
        ],
        "police_refusal_escalation": "This is a criminal offence involving forgery and fraud. If the local thana claims 'you paid voluntarily', remind them that deception is the core definition of Cheating under Section 318 BNS. Submit to SP under Section 173(4) BNSS.",
        "know_the_difference": "This is a **Criminal Fraud and Cybercrime**. Legitimate employers NEVER charge recruitment fees or security deposits from candidates.",
        "confidence_level": "Confirmed criminal fraud under Section 318/336 BNS and Section 66D IT Act.",
        "related_issues": ["Fake interview scams", "Overseas visa fraud", "Money mule accounts"],
        "follow_up_questions": [
            {"q": "Was this a domestic job or an overseas employment offer?", "options": ["Domestic corporate / IT job", "Foreign / Gulf / European visa offer (Emigration Act)", "Part-time work from home / YouTube review job"]},
            {"q": "How was money transferred to the scammers?", "options": ["UPI / Net banking to personal bank accounts", "Credit / debit card on fake payment gateway", "Cryptocurrency / gift cards"]}
        ]
    },

    "investment_crypto_parttime_scam": {
        "id": "investment_crypto_parttime_scam",
        "title": "Lost money in fake investment / stock trading / telegram part-time job scam",
        "category": "Financial & Consumer Fraud",
        "is_emergency": True,
        "summary": "You were lured into a Telegram/WhatsApp group promising massive returns on stock tips, institutional trading, crypto arbitrage, or 'tasks/likes', showed fake profits on a dashboard, and now your funds are frozen.",
        "legal_issue": "Multi-victim cyber investment fraud, cheating, and money laundering via mule accounts.",
        "classification": ["Criminal Offence", "Cybercrime"],
        "constitutional_articles": [],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 318(4)",
                "deals_with": "Cheating and dishonestly inducing delivery of property (imprisonment up to 7 years).",
                "relevance": "Inducing investors to deposit money into shell accounts through fake investment apps."
            },
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 66D",
                "deals_with": "Cheating by personation using computer resource.",
                "relevance": "Impersonating SEBI-registered brokers, international investment houses, or institutional funds."
            },
            {
                "act": "Banning of Unregulated Deposit Schemes Act, 2019 (BUDS Act)",
                "section": "Section 3 & Section 21",
                "deals_with": "Ban on unregulated deposit schemes and fraudulent ponzi setups.",
                "relevance": "Operating unapproved pooled investment programs is a non-bailable criminal offence."
            }
        ],
        "immediate_steps": [
            "GOLDEN HOUR RULE: Call 1930 IMMEDIATELY or report on cybercrime.gov.in. If reported within hours, banks can freeze the fraudulent beneficiary accounts.",
            "Do NOT pay any 'withdrawal tax', 'SEBI clearance fee', or 'liquidity fee' to unlock your funds — that is a secondary trap.",
            "Save and export complete Telegram/WhatsApp group chat history, admin phone numbers, and profile photos.",
            "Download and save bank transaction account statements with UTR numbers showing exact debit timestamps.",
            "Take screenshots of the fake investment app/website dashboard showing your alleged balance before they shut it down."
        ],
        "evidence_checklist": [
            "Bank transaction statements showing debit UTR numbers and recipient account names/IFSC",
            "Complete unedited Telegram / WhatsApp chat exports with recruiter and mentor accounts",
            "Screenshots of the fake trading app / website interface, deposit addresses, and ledger balance",
            "APK installation file or link through which the malicious trading application was installed",
            "Audio recordings of any phone calls with scam group coordinators"
        ],
        "reporting_channels": [
            {"authority": "National Cyber Crime Reporting Portal", "contact": "Dial 1930 / cybercrime.gov.in", "details": "Automated lien marking on scammer bank accounts across Indian banking grid."},
            {"authority": "Cyber Crime Police Station", "contact": "District Cyber Police", "details": "Registration of formal FIR under BNS 318 and IT Act 66D."},
            {"authority": "SEBI Complaints Redress System (SCORES)", "contact": "scores.sebi.gov.in", "details": "Reporting unregistered entities impersonating licensed brokers."}
        ],
        "police_refusal_escalation": "Cyber investment fraud involves organized syndicates. Cyber police stations are specialized to handle these. If a local station refuses, insist on transferring the complaint to the District Cyber Police Station or file directly on cybercrime.gov.in.",
        "know_the_difference": "This is an **Organized Cyber Criminal Scam**. It is NOT a normal stock market investment loss.",
        "confidence_level": "Confirmed cyber financial fraud under Section 318 BNS, IT Act 66D, and BUDS Act.",
        "related_issues": ["Mule account syndicate networks", "Bank lien freeze procedures", "Recovery through Magistrate court"],
        "follow_up_questions": [
            {"q": "How long ago were the transfers made?", "options": ["Within the last 2 to 24 hours (Golden Hour)", "Between 1 and 7 days ago", "More than a month ago"]},
            {"q": "Are the scammers currently demanding 'tax' or 'fees' to release your money?", "options": ["Yes, demanding more money for withdrawal (Do NOT pay!)", "No, they have completely blocked me", "App has stopped working"]}
        ]
    },

    "loan_app_harassment": {
        "id": "loan_app_harassment",
        "title": "Illegal instant loan app harassment, morphed photos & contact shaming",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": True,
        "summary": "You downloaded an instant loan app, repaid or received partial loan, and recovery agents are now blackmailing you by sending morphed obscene photos to your phone contacts and family.",
        "legal_issue": "Extortion, cyber defamation, publishing obscene materials, and illegal lending.",
        "classification": ["Criminal Offence", "Regulatory Violation"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Privacy & Dignity", "connection": "Unlawful extraction of mobile contacts and circulation of fabricated obscene photos breaches the fundamental right to privacy (Puttaswamy)."}
        ],
        "statutory_provisions": [
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 308 & Section 356",
                "deals_with": "Extortion and criminal defamation.",
                "relevance": "Blackmailing for money by threatening to destroy social reputation."
            },
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 67 & Section 67A",
                "deals_with": "Publishing or transmitting obscene or sexually explicit material in electronic form.",
                "relevance": "Circulating morphed nude pictures to contacts carries up to 5 years imprisonment."
            },
            {
                "act": "RBI Fair Practices Code & Digital Lending Guidelines, 2022",
                "section": "Prohibition of Harassment",
                "deals_with": "Recovery agents strictly barred from accessing borrower contacts, calling after hours, or harassing relatives.",
                "relevance": "Unregistered lending apps not partnered with recognized NBFCs are illegal in India."
            }
        ],
        "immediate_steps": [
            "Do NOT pay more money out of panic. Paying only invites greater demands from other linked apps.",
            "Immediately uninstall the rogue app and revoke all app permissions (contacts, photos, storage) on your phone.",
            "Send a broadcast message / status to your contacts informing them: 'My phone was hacked by a fraudulent rogue loan app. Ignore any abusive calls or morphed photos sent from unknown numbers.'",
            "Call 1930 and file a complaint on cybercrime.gov.in under the 'Report Crime Against Women/Children' or 'Financial Fraud' category.",
            "Lodge an FIR at the Cyber Crime Police Station with the harassment call recordings and morphed image evidence."
        ],
        "evidence_checklist": [
            "Screenshots of morphed photos and abusive WhatsApp messages received from recovery agents",
            "Phone numbers, country codes, and Truecaller names of threatening callers",
            "App name, APK download link, and transaction proof showing loan received vs exorbitant repayments made",
            "Screenshots of messages sent to your family members or contacts",
            "Bank account / UPI IDs where extortion payments were directed"
        ],
        "reporting_channels": [
            {"authority": "National Cyber Crime Helpline", "contact": "Dial 1930 / cybercrime.gov.in", "details": "Nodal platform for illegal loan app syndicates."},
            {"authority": "Cyber Police Station", "contact": "District Cyber Cell", "details": "FIR under BNS 308, IT Act 67A for extortion and morphed photos."},
            {"authority": "RBI Sachet Portal", "contact": "sachet.rbi.org.in", "details": "Reserve Bank of India portal for reporting illegal unregistered lending apps."}
        ],
        "police_refusal_escalation": "Morphed obscene photos constitute a non-bailable cognizable offence under Section 67A IT Act and Section 308 BNS. Police have a statutory obligation to register an FIR immediately. Escalate to the DCP Cyber Crime if local staff hesitate.",
        "know_the_difference": "This is a **Criminal Extortion Syndicate** operating in violation of RBI Digital Lending Guidelines. You are a victim of blackmail, not a defaulter.",
        "confidence_level": "Confirmed criminal extortion and IT Act offence under Section 308 BNS and Section 67A IT Act.",
        "related_issues": ["App permission revocation", "Contact broadcast alert", "RBI NBFC verification"],
        "follow_up_questions": [
            {"q": "Have recovery agents sent morphed photos to your contacts already?", "options": ["Yes, photos sent to family/friends", "Threatening to send, but not sent yet", "Only abusive phone calls and threats"]},
            {"q": "Was the loan taken from an authorized bank/NBFC or an APK download link?", "options": ["Unknown APK downloaded from link / web", "App downloaded from Google Play Store", "Registered bank / NBFC app"]}
        ]
    },

    "identity_theft_sim_swap": {
        "id": "identity_theft_sim_swap",
        "title": "Identity theft / SIM swap / fake SIM issued in my name",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": True,
        "summary": "Your mobile network suddenly showed 'No Service', and someone executed a fraudulent SIM swap or used your forged Aadhaar card to obtain multiple SIM cards or loans in your name.",
        "legal_issue": "Identity theft, cheating by personation, and fraudulent activation of telecom services.",
        "classification": ["Criminal Offence", "Cybercrime"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Privacy", "connection": "Misappropriation of personal demographic and biometric identity violates fundamental privacy rights."}
        ],
        "statutory_provisions": [
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 66C & Section 66D",
                "deals_with": "Identity theft and cheating by personation using computer resource.",
                "relevance": "Fraudulently making use of electronic signature, password, or unique identification feature of any other person."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 319 & Section 336",
                "deals_with": "Cheating by personation and forgery.",
                "relevance": "Using someone else's identity documents to obtain goods, credit, or telecom connections."
            },
            {
                "act": "Telecommunications Act, 2023",
                "section": "Section 28 & Section 42",
                "deals_with": "Fraudulent acquisition of SIM cards and misuse of telecom identifiers.",
                "relevance": "Severe penalties for acquiring SIM cards through forged or impersonated credentials."
            }
        ],
        "immediate_steps": [
            "If your phone suddenly loses signal unexpectedly, IMMEDIATELY call your telecom provider from another phone to check if a replacement SIM was issued.",
            "Contact your banks immediately to FREEZE all net banking, UPI, and card transactions linked to the mobile number.",
            "Visit the Department of Telecommunications TAFCOP portal (tafcop.sancharsaathi.gov.in) to see all mobile connections registered against your Aadhaar.",
            "Report any unauthorized mobile numbers on TAFCOP to have them disconnected instantly.",
            "Lodge an FIR at the Cyber Crime Police Station for SIM swap fraud and identity theft."
        ],
        "evidence_checklist": [
            "Timestamp when your genuine SIM card lost cellular network connectivity",
            "Telecom operator confirmation of duplicate SIM issuance at a specific retail store",
            "TAFCOP portal dashboard screenshot listing unauthorized numbers under your Aadhaar",
            "Bank transaction alerts or OTP debit logs received during the outage period",
            "Copy of your genuine identity documents and billing receipts"
        ],
        "reporting_channels": [
            {"authority": "Telecom Operator Emergency Desk", "contact": "Store / Customer Care", "details": "Immediate deactivation of swapped duplicate SIM and reissue to genuine owner."},
            {"authority": "Sanchar Saathi (DoT) TAFCOP", "contact": "tafcop.sancharsaathi.gov.in", "details": "Government portal to check and disconnect fraudulent mobile numbers in your name."},
            {"authority": "National Cyber Crime Reporting Portal", "contact": "Dial 1930 / cybercrime.gov.in", "details": "Lien marking on fraudulent bank transactions."}
        ],
        "police_refusal_escalation": "SIM swap fraud is a recognized cyber crime modus operandi. Police must register FIR under Section 66C/66D IT Act. If local police suggest contacting the telecom company only, submit a written complaint to the Cyber Crime Cell and the DoT TERM cell.",
        "know_the_difference": "This is a **High-Risk Cyber Criminal Offence** that serves as the gateway to complete financial account takeover.",
        "confidence_level": "Confirmed cyber crime under Section 66C/66D IT Act and Section 319 BNS.",
        "related_issues": ["TAFCOP mobile verification", "Aadhaar biometric locking via mAadhaar app", "Bank account security"],
        "follow_up_questions": [
            {"q": "Has your genuine mobile SIM lost network connectivity?", "options": ["Yes, showing 'No Service' suddenly (Emergency SIM Swap indicator)", "No, but discovered unknown numbers registered in my name", "Received OTPs for transactions I never initiated"]},
            {"q": "Have any unauthorized bank withdrawals occurred?", "options": ["Yes, money debited from bank account", "No debits noticed yet, but account at risk", "Unsure"]}
        ]
    },

    "phishing_fake_govt_messages": {
        "id": "phishing_fake_govt_messages",
        "title": "Phishing message / fake electricity bill / fake traffic challan link",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": False,
        "summary": "You received an SMS/WhatsApp claiming: 'Your electricity will be disconnected tonight', 'Traffic challan pending - pay now', or 'e-Challan APK', containing a malicious link or APK file.",
        "legal_issue": "Phishing, computer virus / malware dissemination, and attempted cheating.",
        "classification": ["Cybercrime", "Criminal Offence"],
        "constitutional_articles": [],
        "statutory_provisions": [
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 43 & Section 66",
                "deals_with": "Penalty for damage to computer system and computer related offences.",
                "relevance": "Injecting trojans, malicious APKs, or remote-access spyware into consumer phones."
            },
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 66D",
                "deals_with": "Cheating by personation using computer resource.",
                "relevance": "Impersonating the Electricity Board, Traffic Police, or Income Tax Department."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 318 & Section 62",
                "deals_with": "Attempt to commit cheating.",
                "relevance": "Attempting to siphon money by deceiving victims into clicking malicious links."
            }
        ],
        "immediate_steps": [
            "DO NOT click the link, and under NO circumstances download or install any .apk file sent via SMS/WhatsApp.",
            "If you already installed the APK, turn on 'Airplane Mode' immediately, disconnect Wi-Fi, and boot into Safe Mode to uninstall the rogue app, or factory reset your phone.",
            "Report the scam SMS on the Sanchar Saathi Chakshu portal (sancharsaathi.gov.in/sfc) for suspected fraud communication.",
            "Verify genuine traffic challans ONLY on the official Ministry of Road Transport portal (echallan.parivahan.gov.in).",
            "Verify genuine electricity bills directly on your power discom's official website or consumer app."
        ],
        "evidence_checklist": [
            "Screenshot of the SMS or WhatsApp message showing sender ID / phone number",
            "The exact malicious URL / link address displayed in the message (do not open it)",
            "Timestamp when message was received",
            "If funds were deducted: Bank debit SMS, transaction reference UTR, beneficiary account details"
        ],
        "reporting_channels": [
            {"authority": "Chakshu Portal (DoT Sanchar Saathi)", "contact": "sancharsaathi.gov.in/sfc", "details": "Government platform to report spam and fraud SMS/calls for telecom disconnection."},
            {"authority": "National Cyber Crime Portal", "contact": "Dial 1930 / cybercrime.gov.in", "details": "Immediate reporting if money was debited after clicking link."},
            {"authority": "Telecom Operator Spam Reporting", "contact": "Forward SMS to 1909", "details": "TRAI UCC action."}
        ],
        "police_refusal_escalation": "If no money was lost, police typically do not register an FIR, but DoT Chakshu portal will block the sender's mobile handset and connection. If money was lost, an FIR under Section 66D IT Act and 318 BNS is mandatory.",
        "know_the_difference": "This is a **Cyber Malicious Phishing Campaign**. Genuine utility companies and traffic police never send payment links ending in .apk or shortened bit.ly links.",
        "confidence_level": "Confirmed cyber phishing attempt under Section 66D IT Act.",
        "related_issues": ["Malicious APK malware", "Chakshu scam reporting", "Remote screen sharing tools"],
        "follow_up_questions": [
            {"q": "Did you click the link or install the downloaded application (.apk file)?", "options": ["No, recognized as spam and stopped", "Clicked link, but did not enter card details or install app", "Installed the app / entered banking OTP (High Risk)"]},
            {"q": "Has any unauthorized financial transaction occurred?", "options": ["No money lost", "Money debited from bank account (Emergency 1930 call needed)", "Unsure"]}
        ]
    },

    "medical_negligence": {
        "id": "medical_negligence",
        "title": "Suffered harm due to gross doctor / hospital medical negligence",
        "category": "Financial & Consumer Fraud",
        "is_emergency": False,
        "summary": "A doctor, surgeon, or hospital committed gross surgical error, wrong administration of drugs, surgical instruments left in body, or refusal of emergency treatment resulting in severe disability or death.",
        "legal_issue": "Medical negligence, deficiency of hospital service, and causing hurt/death by rash or negligent act.",
        "classification": ["Consumer Dispute", "Civil Tort", "Criminal Offence (if Gross)"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Health & Emergency Medical Treatment", "connection": "Supreme Court in Parmanand Katara and Paschim Banga Khet Samity established that right to health and emergency medical care is part of Article 21."}
        ],
        "statutory_provisions": [
            {
                "act": "Consumer Protection Act, 2019",
                "section": "Sections 2(42), 35, 84",
                "deals_with": "Deficiency in healthcare service and compensation for medical malpractice.",
                "relevance": "Consumer Commissions award substantial compensation for medical errors, misdiagnosis, and substandard treatment."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 106(1)",
                "deals_with": "Causing death by rash or negligent act.",
                "relevance": "Jacob Mathew v. State of Punjab: Criminal prosecution of doctors requires GROSS negligence supported by an independent expert medical board opinion."
            },
            {
                "act": "National Medical Commission (NMC) Regulations",
                "section": "Code of Medical Ethics",
                "deals_with": "Professional misconduct and suspension of doctor medical license.",
                "relevance": "Complaint to State Medical Council / NMC ethics board for revocation of registration."
            }
        ],
        "immediate_steps": [
            "Immediately request and secure a complete certified set of ALL medical records, case sheets, nursing notes, and lab reports from the hospital under NMC ethics guidelines (hospital MUST provide within 72 hours).",
            "Obtain a detailed independent second medical opinion from a senior government hospital doctor documenting the clinical deviations.",
            "File an official complaint with the State Medical Council / National Medical Commission (NMC) for disciplinary inquiry.",
            "File a consumer compensation claim before the District / State / National Consumer Commission under the Consumer Protection Act, 2019.",
            "If gross criminal conduct caused death, lodge a complaint with police requesting constitution of an expert medical board under Jacob Mathew guidelines."
        ],
        "evidence_checklist": [
            "Complete hospital indoor case records, doctor's daily notes, OT surgical notes, and anesthesia chart",
            "Prescription slips, drug administration records, and pharmacy bills",
            "Pre-operative and post-operative diagnostic imaging (X-rays, CT scans, MRI scans, ultrasound reports)",
            "Discharge summary, death summary, and post-mortem report (if death occurred)",
            "Independent expert medical opinion on standard of care violation"
        ],
        "reporting_channels": [
            {"authority": "State Medical Council / National Medical Commission", "contact": "nmc.org.in / State Council", "details": "Professional misconduct disciplinary action and license cancellation."},
            {"authority": "Consumer Disputes Redressal Commission", "contact": "edaakhil.nic.in / District Consumer Court", "details": "Claiming financial compensation for medical negligence and hospital deficiency."},
            {"authority": "Police Station (for Expert Board formation)", "contact": "Local Police Station", "details": "Investigation under Section 106 BNS with mandatory Medical Board opinion."}
        ],
        "police_refusal_escalation": "Under Supreme Court guidelines in Jacob Mathew, police CANNOT arrest or book a doctor on a simple complaint without first obtaining an independent medical board opinion from a government hospital. The primary and most effective legal remedy is the Consumer Commission.",
        "know_the_difference": "Most medical error claims are **Consumer & Civil Law Claims** requiring expert evidence. Only gross recklessness is treated as a criminal offence.",
        "confidence_level": "Confirmed medical negligence claim under Consumer Protection Act 2019 and NMC Ethics Code.",
        "related_issues": ["Mandatory 72-hour medical record right", "Jacob Mathew medical board rule", "Consumer compensation calculation"],
        "follow_up_questions": [
            {"q": "What was the outcome of the medical incident?", "options": ["Permanent physical disability or bodily injury", "Tragic loss of life / patient deceased", "Corrected by another doctor, financial and emotional trauma"]},
            {"q": "Do you possess the patient's complete certified hospital case records?", "options": ["Yes, have complete records and bills", "Hospital is delaying or refusing to give records", "Only have discharge summary"]}
        ]
    },

    "property_illegal_possession": {
        "id": "property_illegal_possession",
        "title": "Someone illegally occupied or encroached on my land / property",
        "category": "Civil, Property & Documentation",
        "is_emergency": False,
        "summary": "Land grabbers, unauthorized occupants, or powerful individuals have broken boundaries, encroached on your plot, or forcibly occupied your house or land using muscle power.",
        "legal_issue": "Criminal trespass, dispossession, land grabbing, and civil recovery of possession.",
        "classification": ["Civil Dispute", "Criminal Offence (if Force/Threat Used)"],
        "constitutional_articles": [
            {"article": "Article 300A", "name": "Right to Property", "connection": "Constitutional guarantee that no person shall be deprived of their property save by authority of law."}
        ],
        "statutory_provisions": [
            {
                "act": "Specific Relief Act, 1963",
                "section": "Section 6",
                "deals_with": "Suit by person dispossessed of immovable property.",
                "relevance": "Summary civil suit filed within 6 months of illegal dispossession; court restores possession irrespective of title disputes."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 329 & Section 331",
                "deals_with": "Criminal trespass and house-trespass.",
                "relevance": "Unlawfully entering into or upon property in possession of another to commit offence or intimidate."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 164 & Section 165",
                "deals_with": "Procedure where dispute concerning land or water is likely to cause breach of peace.",
                "relevance": "Executive Magistrate / SDM can seal property, determine who was in actual possession, and prevent violent land grabbing."
            }
        ],
        "immediate_steps": [
            "Do NOT resort to private violence, as counter-assault charges may be filed against you.",
            "Gather all original title deeds, sale deeds, mutation registers, Encumbrance Certificate (EC), and recent property tax receipts.",
            "Submit a formal petition to the Sub-Divisional Magistrate (SDM) / Executive Magistrate under Section 164 BNSS to maintain status quo and prevent breach of peace.",
            "Lodge a police complaint for criminal trespass under Section 329 BNS if locks were broken or boundaries destroyed.",
            "File a summary suit under Section 6 of the Specific Relief Act, 1963 in the Civil Court within 6 months for immediate restoration of possession."
        ],
        "evidence_checklist": [
            "Registered Sale Deed, Gift Deed, or Title Certificate showing ownership",
            "Latest Property Tax receipts, electricity/water bills in your name",
            "Revenue records (Patta, Chitta, Khata, Jamabandi, Encumbrance Certificate)",
            "Survey map, demarcation sketch, and photographic evidence of boundary destruction",
            "CCTV footage or eyewitness statements of the illegal entry or lock-breaking"
        ],
        "reporting_channels": [
            {"authority": "Sub-Divisional Magistrate (SDM) Court", "contact": "SDM / Tehsildar Office", "details": "Emergency proceedings under Section 164 BNSS to prevent land grabbing and attach property."},
            {"authority": "Civil Court", "contact": "Jurisdictional Senior Civil Judge Court", "details": "Injunction suit under Order 39 CPC or recovery suit under Section 6 Specific Relief Act."},
            {"authority": "Anti-Land Grabbing Cell / Police Station", "contact": "District SP / Police Thana", "details": "Criminal complaint for trespass and forged documentation."}
        ],
        "police_refusal_escalation": "Police frequently label land disputes as 'purely civil matters' to avoid action. However, forceful physical entry, lock breaking, and threats of violence ARE CRIMINAL OFFENCES under Section 329 BNS and require preventive action under Section 164 BNSS. Escalate to the SDM and SP under Section 173(4) BNSS.",
        "know_the_difference": "Property title is a **Civil Court Matter**, but forceful physical dispossession and boundary breaking is a **Criminal Trespass & Administrative Breach of Peace**.",
        "confidence_level": "Dual track remedy: Civil suit under Specific Relief Act and criminal/preventive proceedings under BNSS Section 164.",
        "related_issues": ["SDM peace proceedings under Section 164 BNSS", "Temporary injunction under Order 39 CPC", "Revenue demarcation"],
        "follow_up_questions": [
            {"q": "When did the illegal dispossession or encroachment occur?", "options": ["Within the last 6 months (Eligible for Section 6 Specific Relief Act summary restoration)", "More than 6 months ago", "Currently in progress / imminent threat"]},
            {"q": "Were threats of violence or deadly weapons used during the entry?", "options": ["Yes, armed goons / threats of violence", "No physical threat, broke boundary/locks quietly", "Dispute over boundary demarcation"]}
        ]
    },

    "landlord_tenant_eviction": {
        "id": "landlord_tenant_eviction",
        "title": "Landlord illegally cut electricity/water or threw belongings out",
        "category": "Civil, Property & Documentation",
        "is_emergency": True,
        "summary": "Your landlord has arbitrarily disconnected your water, electricity, locked you out, or dumped your household belongings on the road without following due legal process of eviction.",
        "legal_issue": "Illegal eviction, wrongful restraint, and cutting off essential services under Rent Control laws.",
        "classification": ["Civil Dispute", "Tenancy Law Violation", "Criminal Offence (Restraint)"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Shelter & Essential Utilities", "connection": "Access to water and electricity is an essential facet of human existence protected under Article 21."}
        ],
        "statutory_provisions": [
            {
                "act": "Model Tenancy Act / State Rent Control Acts",
                "section": "Sections on Essential Services & Eviction",
                "deals_with": "Strict prohibition on landlords cutting off essential services (water, electricity, passage).",
                "relevance": "Landlord CANNOT cut off utilities even if rent is unpaid; Rent Authority can impose heavy financial penalties and restore supply immediately."
            },
            {
                "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
                "section": "Section 126 & Section 329",
                "deals_with": "Wrongful restraint and house-trespass.",
                "relevance": "Locking out a tenant in lawful possession or throwing belongings is criminal wrongful restraint and trespass."
            },
            {
                "act": "Code of Civil Procedure, 1908 (CPC)",
                "section": "Order 39 Rules 1 & 2",
                "deals_with": "Temporary injunction against illegal dispossession.",
                "relevance": "Civil Court can issue an urgent same-day injunction restraining landlord from evicting without due process of law."
            }
        ],
        "immediate_steps": [
            "Call 112 immediately if the landlord has locked your door, dumped your furniture, or is physically preventing you from entering.",
            "Do NOT vacate under pressure. The Supreme Court has repeatedly held that a tenant in possession cannot be evicted except by DUE PROCESS OF LAW (filing a formal eviction suit in court).",
            "Video record the disconnected water meter, tripped power supply, or lock on your entrance.",
            "File an urgent petition before the Rent Authority / Rent Controller for immediate restoration of electricity and water.",
            "File an injunction suit before the Civil Court for an order restraining illegal dispossession."
        ],
        "evidence_checklist": [
            "Valid Tenancy / Rental Agreement and rent payment bank receipts / UPI statements",
            "Video recording of the locked door, displaced luggage, or severed utility connections",
            "WhatsApp chats, text messages, or audio recordings of landlord's threats",
            "Electricity bill / Water bill showing consumer account number",
            "Police complaint copy acknowledging wrongful lockout"
        ],
        "reporting_channels": [
            {"authority": "Police Control Room / Local Thana", "contact": "Dial 112 / Station House Officer", "details": "Immediate intervention to unlock premises and stop wrongful restraint under Section 126 BNS."},
            {"authority": "Rent Authority / Rent Court", "contact": "District Rent Controller", "details": "Mandatory orders under Rent Control Act to restore essential utilities with heavy penalties on landlord."},
            {"authority": "Civil Court", "contact": "Junior Civil Judge Court", "details": "Temporary injunction restraining forcible dispossession without court decree."}
        ],
        "police_refusal_escalation": "Police often say 'this is a civil landlord-tenant dispute'. Emphasize clearly: cutting essential utilities and locking out a residing family is a CRIMINAL ACT of wrongful restraint under Section 126 BNS. Demand registration of an NCR/FIR and immediate key handover.",
        "know_the_difference": "Eviction for non-payment is a **Civil Tenancy Proceeding**, but taking law into one's own hands, cutting utilities, or physical locking is an **Unlawful Criminal Act**.",
        "confidence_level": "Confirmed statutory protection under Rent Control Act and Section 126 BNS.",
        "related_issues": ["Right to essential services", "Due process of eviction", "Security deposit refund dispute"],
        "follow_up_questions": [
            {"q": "What specific illegal action has the landlord taken?", "options": ["Disconnected electricity or water supply", "Put locks on door / threw belongings outside", "Threatened forcible eviction without court notice", "Refusing to refund security deposit after move-out"]},
            {"q": "Do you have a written rental agreement and payment proofs?", "options": ["Yes, registered or written agreement and bank receipts", "Oral tenancy, but paying rent via UPI / bank", "Agreement expired, continuing on verbal understanding"]}
        ]
    },

    "caste_untouchability_discrimination": {
        "id": "caste_untouchability_discrimination",
        "title": "Facing caste discrimination, atrocities or untouchability practices",
        "category": "Discrimination & Human Rights",
        "is_emergency": True,
        "summary": "You belong to a Scheduled Caste (SC) or Scheduled Tribe (ST) and were subjected to casteist slurs, social boycott, denial of access to public places/water/temples, physical assault, or public humiliation by non-SC/ST persons.",
        "legal_issue": "Caste atrocities, practice of untouchability, and hate speech targeting SC/ST communities.",
        "classification": ["Criminal Offence", "Constitutional Violation"],
        "constitutional_articles": [
            {"article": "Article 17", "name": "Abolition of Untouchability", "connection": "Absolute constitutional prohibition against practicing 'untouchability' in any form; enforcement of disability arising from it is a punishable offence."},
            {"article": "Article 15(2)", "name": "Equal Access to Public Places", "connection": "No citizen shall be subjected to restriction regarding access to shops, public restaurants, hotels, water wells, or places of public resort on grounds of caste."}
        ],
        "statutory_provisions": [
            {
                "act": "Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989",
                "section": "Section 3(1) & Section 3(2)",
                "deals_with": "Offences of atrocities including casteist abuses in public view, social boycott, forced tonsuring, wrongful land dispossession, and physical attacks.",
                "relevance": "Strict non-bailable offences. Section 18A bars anticipatory bail; preliminary inquiry is not required prior to FIR."
            },
            {
                "act": "Protection of Civil Rights Act, 1955",
                "section": "Sections 3 to 7",
                "deals_with": "Punishment for enforcing religious and social disabilities on grounds of untouchability.",
                "relevance": "Punishment for preventing entry to temples, public wells, schools, or public transport."
            },
            {
                "act": "SC/ST (PoA) Rules, 1995",
                "section": "Rule 12 (Mandatory Relief & Compensation)",
                "deals_with": "Immediate monetary relief and rehabilitation package.",
                "relevance": "District Administration MUST pay mandatory financial relief (Rs. 85,000 to Rs. 8,25,000) within 7 days of FIR, regardless of conviction."
            }
        ],
        "immediate_steps": [
            "Ensure personal safety and contact trusted community elders or SC/ST organizations.",
            "Lodge a written FIR at the nearest Police Station under Section 3 of the SC/ST (PoA) Act, 1989.",
            "Under Section 18A of the SC/ST Act, police CANNOT demand preliminary inquiry or sanction before registering an FIR.",
            "Investigation MUST be conducted by an officer not below the rank of Deputy Superintendent of Police (DSP) within 60 days.",
            "Demand immediate interim relief and cash compensation under Rule 12 of the SC/ST PoA Rules through the District Magistrate."
        ],
        "evidence_checklist": [
            "Caste Certificate issued by the competent Revenue Authority (Tahsildar / Sub-Collector)",
            "Audio / video recordings of caste slurs, abusive confrontations, or social boycott resolutions",
            "Screenshots of casteist hate speech on social media, WhatsApp groups, or public posters",
            "Names of non-SC/ST witnesses who heard or saw the atrocity in public view",
            "Medico-Legal Certificate (MLC) if physical assault or injuries were caused"
        ],
        "reporting_channels": [
            {"authority": "Special SC/ST Police Cell / DSP", "contact": "District Police Headquarters", "details": "Mandatory DSP-level investigation under the SC/ST (PoA) Act."},
            {"authority": "National Commission for Scheduled Castes (NCSC)", "contact": "ncsc.nic.in / Toll-Free 14566", "details": "Constitutional commission investigating atrocities and recommending police action."},
            {"authority": "District Magistrate (Collector)", "contact": "District Collectorate", "details": "Sanction of mandatory financial compensation and rehabilitation package."}
        ],
        "police_refusal_escalation": "Refusal to register an FIR under the SC/ST Act is a punishable offence for the police officer under Section 4 of the Act (neglect of duty). Complain immediately to the DSP, SP, and submit a petition to the Special Court under the SC/ST Act.",
        "know_the_difference": "This is a **Constitutional Violation (Article 17)** AND an **Aggravated Non-Bailable Criminal Offence (SC/ST PoA Act)**. Anticipatory bail is barred by law.",
        "confidence_level": "Confirmed statutory protection under SC/ST (PoA) Act, 1989 and Article 17.",
        "related_issues": ["Mandatory compensation under Rule 12", "Bar on anticipatory bail", "DSP-level mandatory probe"],
        "follow_up_questions": [
            {"q": "What was the nature of the atrocity?", "options": ["Casteist verbal abuse / humiliation in public view", "Physical assault / bodily injury / tonsuring", "Social boycott / denied water or temple entry", "Illegal dispossession from land / house"]},
            {"q": "Do you possess an official SC/ST Caste Certificate?", "options": ["Yes, valid government caste certificate", "Applied / pending issuance", "Family member holds certificate"]}
        ]
    },

    "disability_discrimination": {
        "id": "disability_discrimination",
        "title": "Denied access, employment, or fair treatment due to disability (RPwD)",
        "category": "Discrimination & Human Rights",
        "is_emergency": False,
        "summary": "You are a person with a benchmark disability and were denied reasonable accommodation, refused admission or employment, mocked/insulted, or denied access to public buildings, transport, or websites.",
        "legal_issue": "Discrimination against persons with disabilities, violation of accessibility mandates, and insult to dignity.",
        "classification": ["Regulatory Violation", "Civil Remedy", "Criminal Offence (for Insults)"],
        "constitutional_articles": [
            {"article": "Article 14 & Article 21", "name": "Right to Equality & Life with Dignity", "connection": "Supreme Court in Vikash Kumar established that reasonable accommodation is a fundamental component of equality and dignity under Articles 14 and 21."}
        ],
        "statutory_provisions": [
            {
                "act": "Rights of Persons with Disabilities Act, 2016 (RPwD Act)",
                "section": "Sections 3, 20, 40 to 46",
                "deals_with": "Non-discrimination in government and private employment, barrier-free accessibility, and reasonable accommodation.",
                "relevance": "No establishment can discriminate against a person with disability in matters of employment or promotion, and all public buildings/transport must be accessible."
            },
            {
                "act": "Rights of Persons with Disabilities Act, 2016",
                "section": "Section 92",
                "deals_with": "Offences of atrocities against persons with disabilities.",
                "relevance": "Intentionally insulting or intimidating with intent to humiliate a person with disability in public view carries imprisonment up to 5 years and fine."
            }
        ],
        "immediate_steps": [
            "Document all instances of discrimination, written refusal of reasonable accommodation, or inaccessible infrastructure.",
            "Submit a formal complaint to the Grievance Redressal Officer of the establishment (mandatory under Section 23 RPwD Act).",
            "File a complaint before the State Commissioner for Persons with Disabilities or the Chief Commissioner (ccdisabilities.nic.in).",
            "If someone intentionally insulted or humiliated you in public view on account of your disability, lodge an FIR under Section 92 RPwD Act.",
            "For education or job denial, approach the High Court under Article 226 for enforcement of fundamental rights."
        ],
        "evidence_checklist": [
            "Unique Disability ID (UDID) Card or Disability Medical Certificate (40%+ benchmark)",
            "Written correspondence, rejection emails, or memos denying job, promotion, or accommodation",
            "Photographs or videos showing physical barriers, lack of ramps, lifts, or accessible toilets",
            "Audio / video evidence or witness statements of public humiliation or abusive remarks"
        ],
        "reporting_channels": [
            {"authority": "Chief Commissioner for Persons with Disabilities", "contact": "ccdisabilities.nic.in / New Delhi", "details": "Quasi-judicial powers of a civil court to summon establishments and enforce accessibility."},
            {"authority": "State Commissioner for Persons with Disabilities", "contact": "State Social Welfare Department", "details": "State-level statutory authority for immediate compliance directives."},
            {"authority": "Local Police Station", "contact": "Police Thana", "details": "FIR under Section 92 RPwD Act for public humiliation or abuse."}
        ],
        "police_refusal_escalation": "Public insults and humiliation under Section 92 RPwD Act are cognizable criminal offences. If police refuse, file a petition before the Special Disability Court established in each district under Section 84 of the RPwD Act.",
        "know_the_difference": "Accessibility and job denial are **Statutory Civil Violations (RPwD Act)**, while public slurs and assaults are **Criminal Offences** under Section 92.",
        "confidence_level": "Confirmed statutory rights under Rights of Persons with Disabilities Act, 2016.",
        "related_issues": ["Mandatory reasonable accommodation", "Special Disability Court jurisdiction", "Accessible public transport"],
        "follow_up_questions": [
            {"q": "What form of discrimination occurred?", "options": ["Denied employment / promotion / reasonable accommodation", "Denied entry / inaccessible building or public transport", "Public insult, abuse, or assault due to disability", "Denied school or college admission"]},
            {"q": "Do you hold a valid UDID Card or Disability Certificate?", "options": ["Yes, have UDID card / certificate (40%+)", "Have medical diagnosis, pending UDID card", "In process of applying"]}
        ]
    },

    "senior_citizen_abandonment": {
        "id": "senior_citizen_abandonment",
        "title": "Elderly parent abandoned, neglected, or property forcibly taken by children",
        "category": "Crimes Against Children & Seniors",
        "is_emergency": True,
        "summary": "An elderly senior citizen is abandoned, refused basic food, shelter, and medical care by adult children, or was deceived into transferring property/flat to children who subsequently mistreated or evicted them.",
        "legal_issue": "Abandonment of senior citizen, maintenance of parents, and revocation of fraudulent property gift deeds.",
        "classification": ["Special Statutory Remedy", "Civil Remedy", "Criminal Offence"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Life & Dignity in Old Age", "connection": "The right to live with dignity extends throughout life; state has duty to protect destitute senior citizens."}
        ],
        "statutory_provisions": [
            {
                "act": "Maintenance and Welfare of Parents and Senior Citizens Act, 2007 (MWPSC Act)",
                "section": "Section 4 & Section 9",
                "deals_with": "Maintenance of parents and senior citizens.",
                "relevance": "Children and legal heirs inheriting property have a mandatory statutory duty to maintain parents."
            },
            {
                "act": "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
                "section": "Section 23",
                "deals_with": "Transfer of property to be void in certain circumstances (Revocation of Gift Deed).",
                "relevance": "If a senior transferred property to children on condition of care and children fail to provide care, the Maintenance Tribunal can DECLARE THE GIFT DEED VOID AND RETURN PROPERTY TO PARENTS."
            },
            {
                "act": "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
                "section": "Section 24",
                "deals_with": "Exposure and abandonment of senior citizen.",
                "relevance": "Abandoning an elderly parent is a criminal offence punishable with imprisonment up to 3 months or fine."
            }
        ],
        "immediate_steps": [
            "Call the National Senior Citizen Helpline at 14567 ('Elderline') for emergency rescue, shelter, and legal guidance.",
            "File an application before the Maintenance Tribunal headed by the Sub-Divisional Magistrate (SDM) under the MWPSC Act, 2007.",
            "If property was gifted to children who now neglect or abuse you, invoke Section 23 of the MWPSC Act to revoke the gift deed and recover title.",
            "The Maintenance Tribunal must decide the application within 90 days; no advocates are required (parties appear in person or via maintenance officers).",
            "If physical assault or lockout occurs, dial 112 for immediate police rescue."
        ],
        "evidence_checklist": [
            "Age proof showing age 60 years or above (Aadhaar, Voter ID, Pension card)",
            "Copy of the registered Gift Deed, Transfer Deed, or Settlement Deed executed in favour of children",
            "Medical prescriptions, hospital bills, and proof of neglected medical treatment",
            "Bank statements showing lack of independent income or maintenance support",
            "Photographs, police complaints, or neighbor statements documenting neglect or eviction"
        ],
        "reporting_channels": [
            {"authority": "National Elderline Helpline", "contact": "Dial 14567 (Toll Free 8 AM - 8 PM)", "details": "Government emergency response, rescue, mediation, and shelter assistance for senior citizens."},
            {"authority": "Maintenance Tribunal (SDM Office)", "contact": "Sub-Divisional Magistrate Court", "details": "Fast-track 90-day statutory tribunal for maintenance orders and property deed cancellations."},
            {"authority": "Local Police Station", "contact": "Dial 112 / Station House Officer", "details": "Intervention under Section 24 MWPSC Act for abandonment and safety."}
        ],
        "police_refusal_escalation": "The primary authority under this law is the Sub-Divisional Magistrate (SDM), NOT the regular civil court or police. Approach the SDM Maintenance Tribunal directly. Civil court jurisdiction is explicitly barred under Section 27 of the MWPSC Act to ensure fast justice.",
        "know_the_difference": "This is a **Fast-Track Special Statutory Remedy** before the SDM. You do NOT have to fight multi-year civil suits to recover your home.",
        "confidence_level": "Confirmed statutory remedy under Maintenance and Welfare of Parents and Senior Citizens Act, 2007.",
        "related_issues": ["Property gift deed cancellation under Section 23", "Fast-track 90-day maintenance award", "Elderline 14567 rescue"],
        "follow_up_questions": [
            {"q": "Did you transfer property (house, flat, land) to your children?", "options": ["Yes, transferred/gifted property and now facing neglect/eviction", "No property transferred, but children refuse maintenance and food", "Facing physical threats and lockouts"]},
            {"q": "Are you currently in physical danger or locked out of your home?", "options": ["Yes, locked out / facing physical abuse (Emergency)", "Facing severe neglect, but living inside home", "Living separately without financial support"]}
        ]
    },

    "privacy_personal_data_leak": {
        "id": "privacy_personal_data_leak",
        "title": "Company leaked my personal / financial data without consent",
        "category": "Cybercrime & Digital Scams",
        "is_emergency": False,
        "summary": "A bank, telecom provider, healthcare app, or e-commerce platform compromised, sold, or leaked your sensitive personal data (Aadhaar, PAN, phone number, health records) without your consent.",
        "legal_issue": "Data breach, failure to protect sensitive personal data, and privacy violations.",
        "classification": ["Regulatory Violation", "Civil Remedy", "Constitutional Violation (if State entity)"],
        "constitutional_articles": [
            {"article": "Article 21", "name": "Right to Privacy", "connection": "Supreme Court in K.S. Puttaswamy held informational privacy and data protection to be an intrinsic part of the right to life under Article 21."}
        ],
        "statutory_provisions": [
            {
                "act": "Digital Personal Data Protection Act, 2023 (DPDP Act)",
                "section": "Sections 4, 6, 8, 27",
                "deals_with": "Obligations of Data Fiduciaries, consent requirements, duty to report breaches, and penalties up to Rs. 250 Crores.",
                "relevance": "Entities must process personal data only with explicit consent and implement reasonable security safeguards."
            },
            {
                "act": "Information Technology Act, 2000",
                "section": "Section 43A",
                "deals_with": "Compensation for failure to protect sensitive personal data or information.",
                "relevance": "Body corporate is liable to pay damages to affected persons for negligence in implementing reasonable security practices."
            },
            {
                "act": "Consumer Protection Act, 2019",
                "section": "Section 2(47)(ix)",
                "deals_with": "Unfair trade practice by disclosing personal information given in confidence.",
                "relevance": "Disclosing consumer personal data without authorization is an actionable unfair trade practice."
            }
        ],
        "immediate_steps": [
            "Send a formal written Data Subject Grievance to the company's designated Data Protection Officer (DPO) demanding breach details.",
            "Lock your Aadhaar biometrics immediately on the UIDAI portal / mAadhaar application.",
            "Change all net banking passwords, enable multi-factor authentication (MFA), and check credit scores (CIBIL) for unauthorized loans.",
            "Lodge a complaint on the CERT-In incident reporting desk (cert-in.org.in).",
            "File a consumer case for deficiency of service and unfair trade practice under Section 2(47) of the Consumer Protection Act."
        ],
        "evidence_checklist": [
            "Screenshots or emails from company acknowledging the security incident / data breach",
            "Public news reports or database dump notices confirming breach of user data",
            "Spam messages, phishing calls, or loan approval alerts triggered immediately post-breach",
            "Proof of your registered account with the breaching company (subscription invoice, user ID)",
            "Copy of grievance email sent to company Data Protection Officer"
        ],
        "reporting_channels": [
            {"authority": "Indian Computer Emergency Response Team (CERT-In)", "contact": "cert-in.org.in / incident@cert-in.org.in", "details": "National nodal agency for monitoring cyber security incidents and major breaches."},
            {"authority": "Data Protection Board of India", "contact": "Under DPDP Act Framework", "details": "Adjudicating body for data breaches and corporate financial penalties."},
            {"authority": "District Consumer Commission", "contact": "edaakhil.nic.in", "details": "Claiming financial compensation for privacy breach and mental distress."}
        ],
        "police_refusal_escalation": "Data breaches are primarily handled through CERT-In, the Data Protection Board, and Consumer Commissions. If personal data was used to commit financial fraud, an FIR under Section 66C/66D IT Act must be filed at the Cyber Police Station.",
        "know_the_difference": "Corporate data negligence is a **Regulatory Violation (DPDP Act) & Consumer Deficiency**. If malicious actors steal funds using leaked data, that creates an independent **Criminal Fraud Case**.",
        "confidence_level": "Confirmed statutory issue under DPDP Act 2023, IT Act Section 43A, and Consumer Protection Act.",
        "related_issues": ["Aadhaar biometric locking", "CIBIL unauthorized inquiry checks", "Corporate liability under DPDP Act"],
        "follow_up_questions": [
            {"q": "What type of data was compromised?", "options": ["Financial data (card details, bank accounts, UPI)", "Identity records (Aadhaar, PAN, Passport)", "Health and medical records", "Contact details (email, phone number, address)"]},
            {"q": "Has any unauthorized financial transaction occurred as a result?", "options": ["Yes, money was debited from account", "No direct debit, but receiving flood of phishing calls", "Unsure"]}
        ]
    },

    "general_diagnostic_unsure": {
        "id": "general_diagnostic_unsure",
        "title": "I don't know what happened legally — help me understand",
        "category": "Unsure / General Diagnostic",
        "is_emergency": False,
        "summary": "You are experiencing a distressing dispute, monetary loss, harassment, or government refusal, but you are not sure what legal category or rights apply to your situation.",
        "legal_issue": "General civic and legal diagnostic assessment under Indian law.",
        "classification": ["Diagnostic Guidance", "Constitutional / Criminal / Civil Triage"],
        "constitutional_articles": [
            {"article": "Article 14 & Article 21", "name": "Equality Before Law & Protection of Life", "connection": "Foundational bedrock ensuring every citizen has access to legal justice, due process, and state protection."}
        ],
        "statutory_provisions": [
            {
                "act": "Legal Services Authorities Act, 1987",
                "section": "Section 12",
                "deals_with": "Criteria for giving legal services.",
                "relevance": "Free legal aid is a statutory right for women, children, SC/ST, custody undertrials, disaster victims, and low-income citizens."
            },
            {
                "act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
                "section": "Section 173 & Section 175",
                "deals_with": "FIR registration and remedies against police non-action.",
                "relevance": "Statutory procedure to activate criminal justice machinery."
            }
        ],
        "immediate_steps": [
            "Check for immediate physical danger: if your bodily safety is threatened, dial 112 immediately without worrying about legal classifications.",
            "Write down a brief chronological timeline: What happened? Who did it? When? Where? What was lost or harmed?",
            "Preserve all physical and digital evidence: take photos, do not delete messages or call logs, and safeguard bills.",
            "Contact the National Legal Services Authority (NALSA) toll-free helpline at 15100 for free professional lawyer consultation.",
            "Select the closest matching category from the options below to see your specific statutory rights."
        ],
        "evidence_checklist": [
            "Chronological timeline of events written down while fresh in memory",
            "All physical receipts, bills, agreements, or medical prescriptions",
            "Digital records (screenshots, chat transcripts, voice recordings, emails)",
            "Identity proofs and government documents relating to the matter",
            "Names and phone numbers of witnesses who can corroborate facts"
        ],
        "reporting_channels": [
            {"authority": "National Legal Services Authority (NALSA)", "contact": "Toll-Free 15100 / nalsa.gov.in", "details": "Free legal counsel and guidance across all District and Taluk courts."},
            {"authority": "Emergency Response Support System (ERSS)", "contact": "Dial 112", "details": "Immediate unified emergency response for police, fire, and ambulance."},
            {"authority": "Citizen Service Centre (CSC) / Legal Aid Clinic", "contact": "District Court Legal Aid Clinic", "details": "Walk-in free legal advice and application drafting."}
        ],
        "police_refusal_escalation": "Whenever police refuse to accept a complaint or register an FIR for a cognizable offence, send the complaint in writing by registered post to the District Superintendent of Police (SP) under Section 173(4) BNSS. You can also approach the District Legal Services Authority (DLSA) for free representation before the Judicial Magistrate under Section 175(3) BNSS.",
        "know_the_difference": "Indian law divides issues into: **Criminal** (theft, assault, cyber scams handled by police and criminal courts), **Civil** (property deeds, contracts, money recovery handled by civil courts), **Consumer** (defective goods, bad services handled by Consumer Commissions), and **Constitutional** (state rights violations handled by High Court / Supreme Court).",
        "confidence_level": "Diagnostic overview providing legal triage across Indian jurisprudence.",
        "related_issues": ["Free legal aid under NALSA", "Zero FIR rights", "District Legal Services Authority"],
        "follow_up_questions": [
            {"q": "What is the primary nature of what occurred?", "options": ["Physical threat, violence, or bodily harm", "Financial loss, cyber scam, or bank fraud", "Dispute over house, land, or property", "Cheated by a company, hospital, or seller", "Harassment at work, college, or home", "Police mistreatment or wrongful arrest"]},
            {"q": "Is the person causing harm a private individual or a government official?", "options": ["Private individual / unknown scammer", "Company or business enterprise", "Police officer or government official", "Family member / relative"]}
        ]
    }

}
