"""
Database of Realistic India-Specific Legal & Civic Case Studies and Interactive Quizzes.
Covers 16 real-life scenarios spanning 13 civic categories and 4 difficulty levels.
Adheres strictly to Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS),
Bharatiya Sakshya Adhiniyam (BSA), Special Acts, and Constitutional Jurisprudence.
"""

SCENARIO_CATEGORIES = [
    "Personal Safety & Violent Crime",
    "Crimes Against Women",
    "Crimes Against Children",
    "Senior Citizens",
    "Cybercrime & Online Fraud",
    "Financial Scams & Identity Theft",
    "Workplace & College Harassment",
    "Discrimination & Human Rights",
    "Property & Tenancy Disputes",
    "Road Incidents & Transport",
    "Consumer Rights & Medical Negligence",
    "Police Powers & Procedural Rights",
    "Constitutional Rights & State Action"
]

DIFFICULTY_LEVELS = ["Basic", "Intermediate", "Advanced", "Emergency"]

SCENARIOS_DB = {   'case_01_snatching_robbery': {   'category': 'Personal Safety & Violent Crime',
                                     'difficulty': 'Emergency',
                                     'educational_breakdown': {   'case_summary': 'Armed motorcycle-borne snatching '
                                                                                  'resulting in physical injuries and '
                                                                                  'theft of jewellery and electronics, '
                                                                                  'met with illegal police burking.',
                                                                  'common_misconceptions': 'Myth: You must accept a '
                                                                                           "'Lost Item Report' if "
                                                                                           'police say so. Reality: A '
                                                                                           'lost report is for '
                                                                                           'misplaced articles; armed '
                                                                                           'snatching is a serious '
                                                                                           'non-bailable crime '
                                                                                           'requiring an FIR.',
                                                                  'constitutional_analysis': 'Article 21 (Right to '
                                                                                             'life, personal liberty, '
                                                                                             'and physical safety in '
                                                                                             'public spaces). '
                                                                                             'Arbitrary police refusal '
                                                                                             'also impairs statutory '
                                                                                             'rule of law.',
                                                                  'court_precedents': 'Lalita Kumari v. Govt of UP '
                                                                                      '(2014) - Registration of FIR is '
                                                                                      'mandatory under Section 154 '
                                                                                      'CrPC (now S. 173 BNSS) if '
                                                                                      'information discloses a '
                                                                                      'cognizable offence.',
                                                                  'evidence_preservation_protocol': 'Preserve hospital '
                                                                                                    'MLC, IMEI and '
                                                                                                    'device purchase '
                                                                                                    'receipts, gold '
                                                                                                    'chain appraisal '
                                                                                                    'receipt, CCTV '
                                                                                                    'footage from the '
                                                                                                    'metro exit and '
                                                                                                    'shopfronts.',
                                                                  'immediate_action_protocol': '1. Ensure medical '
                                                                                               'safety; 2. Call 112 '
                                                                                               'from the spot; 3. '
                                                                                               'Block SIM and banking '
                                                                                               'apps; 4. Obtain '
                                                                                               'hospital MLC; 5. '
                                                                                               'Demand signed copy of '
                                                                                               'FIR under S. 173 BNSS.',
                                                                  'key_takeaways': [   'Snatching is now an explicit, '
                                                                                       'codified crime under Section '
                                                                                       '304 BNS.',
                                                                                       'Using a deadly weapon elevates '
                                                                                       'robbery to Section 311 BNS '
                                                                                       'with a mandatory minimum of 7 '
                                                                                       'years.',
                                                                                       'Police refusal to file an FIR '
                                                                                       'in cognizable crime is '
                                                                                       'actionable under Section 199 '
                                                                                       'BNS.'],
                                                                  'legal_classification': 'Heinous Cognizable Criminal '
                                                                                          'Offence under Bharatiya '
                                                                                          'Nyaya Sanhita, 2023.',
                                                                  'remedies_against_refusal': 'Section 173(4) BNSS '
                                                                                              '(Complaint to SP/DCP) '
                                                                                              '-> Section 175(3) BNSS '
                                                                                              '(Petition to Judicial '
                                                                                              'Magistrate for '
                                                                                              'investigation order).',
                                                                  'reporting_forums': 'Local Police Station (FIR), '
                                                                                      'Sanchar Saathi CEIR portal '
                                                                                      '(IMEI block), Bank Emergency '
                                                                                      'Fraud Desk (UPI freeze), DLSA '
                                                                                      '(Victim compensation).',
                                                                  'statutory_provisions': 'BNS Section 304 '
                                                                                          '(Snatching), Section 309 '
                                                                                          '(Robbery), Section 311 '
                                                                                          '(Robbery with deadly '
                                                                                          'weapon), BNSS Section 173 '
                                                                                          '(Mandatory FIR).',
                                                                  'victim_support_compensation': 'Eligible for state '
                                                                                                 'victim compensation '
                                                                                                 'under Section 396 '
                                                                                                 'BNSS for physical '
                                                                                                 'injury and trauma '
                                                                                                 'via the District '
                                                                                                 'Legal Services '
                                                                                                 'Authority (DLSA).'},
                                     'id': 'case_01_snatching_robbery',
                                     'questions': [   {   'correct_index': 1,
                                                          'explanation': 'Because the assailants brandished a knife, '
                                                                         'used physical violence, and caused hurt '
                                                                         'during the sudden taking, this constitutes '
                                                                         'Snatching (S. 304 BNS), Robbery (S. 309 '
                                                                         'BNS), and Robbery with attempt to cause hurt '
                                                                         'with a deadly weapon (S. 311 BNS).',
                                                          'options': [   'Simple theft of movable property (Section '
                                                                         '303 BNS)',
                                                                         'Robbery and Snatching using a deadly weapon '
                                                                         '(Sections 304, 309, and 311 BNS)',
                                                                         'Extortion by threat (Section 308 BNS)',
                                                                         'Civil trespass and accidental injury'],
                                                          'question': 'What is the primary criminal offence committed '
                                                                      'against Kavita under the Bharatiya Nyaya '
                                                                      'Sanhita (BNS)?'},
                                                      {   'correct_index': 2,
                                                          'explanation': 'Under Section 173 BNSS and the Constitution '
                                                                         'Bench judgment in Lalita Kumari v. Govt of '
                                                                         'UP, registration of an FIR is mandatory for '
                                                                         "cognizable offences. Suggesting a 'lost "
                                                                         "property' report for violent robbery is "
                                                                         "illegal 'burking' of crime.",
                                                          'options': [   'Yes, police officers have full discretion to '
                                                                         'classify street incidents as lost property',
                                                                         'Yes, because the accused individuals were '
                                                                         'unidentified and escaped',
                                                                         'No. Armed robbery and snatching are '
                                                                         'cognizable offences; under Section 173 BNSS '
                                                                         'and Lalita Kumari, police MUST register an '
                                                                         'FIR immediately',
                                                                         'Only if the shopkeeper refused to become a '
                                                                         'formal witness'],
                                                          'question': 'Was the police officer legally justified in '
                                                                      "refusing to lodge an FIR and advising a 'lost "
                                                                      "property application'?"},
                                                      {   'correct_index': 1,
                                                          'explanation': 'Immediate SIM deactivation prevents OTP '
                                                                         'interception. CEIR portal blocks the IMEI '
                                                                         'across all Indian cellular networks, and '
                                                                         'freezing banking links prevents draining of '
                                                                         'bank accounts.',
                                                          'options': [   'Wait 48 hours to see if the phone turns up '
                                                                         'at the lost-and-found desk',
                                                                         'Block SIM card, block device on DoT CEIR '
                                                                         'portal (ceir.gov.in), and freeze UPI/mobile '
                                                                         'banking',
                                                                         'Post about the theft on Instagram and '
                                                                         'Twitter before doing anything else',
                                                                         'Buy a new phone immediately with the same '
                                                                         'SIM without intimating the bank'],
                                                          'question': 'What should Kavita do IMMEDIATELY regarding her '
                                                                      'banking credentials and stolen smartphone?'},
                                                      {   'correct_index': 1,
                                                          'explanation': 'An MLC (Medico-Legal Certificate) generated '
                                                                         'by examining casualty doctors is '
                                                                         'indispensable forensic evidence to prove '
                                                                         'physical hurt under Section 115/309 BNS.',
                                                          'options': [   'Only the purchase invoice of the gold chain',
                                                                         'A Medico-Legal Certificate (MLC) from a '
                                                                         'government or private hospital detailing '
                                                                         'abrasions and trauma',
                                                                         'A self-declaration on a stamp paper signed '
                                                                         'by the shopkeeper',
                                                                         'Social media screenshots describing the '
                                                                         'pain'],
                                                          'question': 'What physical evidence must be preserved to '
                                                                      'establish the aggravated hurt caused during the '
                                                                      'crime?'},
                                                      {   'correct_index': 1,
                                                          'explanation': 'Section 173(4) BNSS statutorily empowers any '
                                                                         'aggrieved citizen whose FIR is refused to '
                                                                         'send the substance of the information in '
                                                                         'writing by post to the SP/DCP, who must '
                                                                         'investigate or direct an investigation.',
                                                          'options': [   'Approach the local municipal councillor for '
                                                                         'dispute settlement',
                                                                         'Send the written complaint by registered '
                                                                         'post to the Superintendent of Police (SP) '
                                                                         'under Section 173(4) BNSS',
                                                                         'File a civil compensation suit against the '
                                                                         'metro corporation',
                                                                         'Accept the lost report receipt and close the '
                                                                         'matter'],
                                                          'question': 'If the Station House Officer refuses to '
                                                                      'register the FIR despite insistence, what is '
                                                                      "Kavita's statutory next step under the BNSS?"}],
                                     'story': 'Kavita, a 28-year-old software analyst, was walking home from the local '
                                              'metro station around 9:30 PM. In an unlit stretch near her residential '
                                              'colony, two men on a motorbike without a number plate slowed down. The '
                                              "pillion rider jumped off, flashed a 9-inch hunting knife at Kavita's "
                                              'neck, violently grabbed her 18-karat gold chain, and snatched her '
                                              'handbag containing her smartphone, debit cards, and apartment keys. '
                                              'When Kavita shouted, the attacker pushed her forcefully onto the gravel '
                                              'pavement, causing lacerations on her knees and right elbow, before '
                                              'speeding off. A nearby shopkeeper rushed to her aid and she reached the '
                                              'local police station within 30 minutes. However, the Duty Officer at '
                                              "the thana told her: 'Madam, write a simple application for lost "
                                              'property; if we file an FIR for robbery, your case will drag in courts '
                                              "and our beat officers will get bad remarks from the ACP.'",
                                     'title': 'Night-time Chain Snatching at Knifepoint on Return from Metro'},
    'case_02_stalking_intimidation': {   'category': 'Crimes Against Women',
                                         'difficulty': 'Intermediate',
                                         'educational_breakdown': {   'case_summary': 'Persistent physical and online '
                                                                                      'stalking escalating into '
                                                                                      'physical restraint and criminal '
                                                                                      'threats in a parking lot.',
                                                                      'common_misconceptions': "Myth: 'Ignoring a "
                                                                                               'stalker will make him '
                                                                                               "stop.' Reality: "
                                                                                               'Stalking statistically '
                                                                                               'escalates to violent '
                                                                                               'assault if legal '
                                                                                               'boundaries and FIRs '
                                                                                               'are not established '
                                                                                               'early.',
                                                                      'constitutional_analysis': 'Article 15(3) '
                                                                                                 '(Special provisions '
                                                                                                 'protecting women), '
                                                                                                 'Article 21 (Right to '
                                                                                                 'bodily autonomy, '
                                                                                                 'dignity, and freedom '
                                                                                                 'from fear).',
                                                                      'court_precedents': 'State of Punjab v. Major '
                                                                                          'Singh & Dinesh v. State of '
                                                                                          'Rajasthan - Physical '
                                                                                          'restraint and unwanted '
                                                                                          'touches to women constitute '
                                                                                          'criminal assault under '
                                                                                          'outraging modesty '
                                                                                          'provisions.',
                                                                      'evidence_preservation_protocol': 'Unedited '
                                                                                                        'WhatsApp '
                                                                                                        'chats showing '
                                                                                                        'refusal, '
                                                                                                        'screenshots '
                                                                                                        'of fake '
                                                                                                        'profiles with '
                                                                                                        'profile '
                                                                                                        'handles/timestamps, '
                                                                                                        'office '
                                                                                                        'basement '
                                                                                                        'parking CCTV '
                                                                                                        'footage, '
                                                                                                        'colleague '
                                                                                                        'eyewitness '
                                                                                                        'statements.',
                                                                      'immediate_action_protocol': '1. Do not engage '
                                                                                                   'or delete '
                                                                                                   'evidence; 2. '
                                                                                                   'Inform building '
                                                                                                   'security for '
                                                                                                   'parking CCTV '
                                                                                                   'retrieval; 3. Dial '
                                                                                                   '1090/181 or 112; '
                                                                                                   '4. File Zero FIR '
                                                                                                   'before a female '
                                                                                                   'officer.',
                                                                      'key_takeaways': [   'Stalking covers both '
                                                                                           'online monitoring and '
                                                                                           'physical shadowing under '
                                                                                           'Section 78 BNS.',
                                                                                           'Zero FIR guarantees that '
                                                                                           'no woman can be turned '
                                                                                           'away for lack of '
                                                                                           'territorial jurisdiction.',
                                                                                           'Statements must be '
                                                                                           'recorded by a female '
                                                                                           'officer under Section '
                                                                                           '173(1) BNSS.'],
                                                                      'legal_classification': 'Cognizable Criminal '
                                                                                              'Offence under BNS '
                                                                                              '(Sexual Offences '
                                                                                              'Against Women).',
                                                                      'remedies_against_refusal': 'Superintendent of '
                                                                                                  'Police under '
                                                                                                  'Section 173(4) '
                                                                                                  'BNSS, Judicial '
                                                                                                  'Magistrate petition '
                                                                                                  'under Section '
                                                                                                  '175(3) BNSS, NCW '
                                                                                                  'intervention.',
                                                                      'reporting_forums': 'Women Police Station / '
                                                                                          'Local Thana, Women Helpline '
                                                                                          '1090 / 181, National '
                                                                                          'Commission for Women (NCW) '
                                                                                          'online portal.',
                                                                      'statutory_provisions': 'BNS Section 78 '
                                                                                              '(Stalking), Section 74 '
                                                                                              '(Assault outraging '
                                                                                              'modesty), Section 351 '
                                                                                              '(Criminal '
                                                                                              'Intimidation), BNSS '
                                                                                              'Section 173(1) (Woman '
                                                                                              'officer recording).',
                                                                      'victim_support_compensation': 'Free legal aid '
                                                                                                     'through District '
                                                                                                     'Legal Services '
                                                                                                     'Authority (DLSA) '
                                                                                                     'panel advocate '
                                                                                                     'and victim '
                                                                                                     'counseling at '
                                                                                                     'Sakhi One-Stop '
                                                                                                     'Centres.'},
                                         'id': 'case_02_stalking_intimidation',
                                         'questions': [   {   'correct_index': 0,
                                                              'explanation': 'Section 78 BNS codifies stalking, '
                                                                             'encompassing both following a woman '
                                                                             'physically despite disinterest and '
                                                                             'monitoring her internet, email, or '
                                                                             'digital communications.',
                                                              'options': [   'Section 78 BNS (replaces IPC 354D)',
                                                                             'Section 303 BNS (Theft)',
                                                                             'Section 318 BNS (Cheating)',
                                                                             'Section 281 BNS (Rash Driving)'],
                                                              'question': 'Which specific section of the Bharatiya '
                                                                          'Nyaya Sanhita, 2023 deals with physical and '
                                                                          'cyber stalking of a woman?'},
                                                          {   'correct_index': 1,
                                                              'explanation': "Using physical force to grab a woman's "
                                                                             'wrist against her will constitutes an '
                                                                             'assault to outrage modesty (S. 74 BNS), '
                                                                             'and threatening her career is criminal '
                                                                             'intimidation (S. 351 BNS).',
                                                              'options': [   'Nothing, parking lots are private spaces '
                                                                             'outside police jurisdiction',
                                                                             'Grabbing her wrist and issuing threats '
                                                                             'constitutes assault to outrage modesty '
                                                                             '(Section 74 BNS) and criminal '
                                                                             'intimidation (Section 351 BNS)',
                                                                             'It is merely a civil contract dispute '
                                                                             'between former acquaintances',
                                                                             'It is only a violation of the building '
                                                                             'parking bylaws'],
                                                              'question': "What makes Rohit's conduct in the parking "
                                                                          'basement an additional criminal offence '
                                                                          'beyond stalking?'},
                                                          {   'correct_index': 1,
                                                              'explanation': 'The proviso to Section 173(1) BNSS '
                                                                             'mandates that in offences under Sections '
                                                                             '74, 75, 78, etc., the information must '
                                                                             'be recorded by a woman police officer.',
                                                              'options': [   'Any male constable available on night '
                                                                             'duty',
                                                                             'Exclusively a woman police officer or '
                                                                             'woman officer under Section 173(1) BNSS',
                                                                             'A private security guard from the office',
                                                                             'A community panchayat member'],
                                                              'question': "Under the BNSS, who MUST record Sneha's "
                                                                          'statement when she lodges a complaint '
                                                                          'regarding sexual offences?'},
                                                          {   'correct_index': 1,
                                                              'explanation': 'Zero FIR is a statutory right under '
                                                                             'Section 173(1) BNSS. A police station '
                                                                             'cannot reject an FIR on territorial '
                                                                             'grounds; they must register a Zero FIR '
                                                                             'and transfer it to the jurisdictional '
                                                                             'station.',
                                                              'options': [   'No, FIRs can strictly only be filed at '
                                                                             'the police station where the victim '
                                                                             'resides',
                                                                             "Yes, through the mechanism of 'Zero FIR' "
                                                                             'codified under Section 173(1) BNSS, any '
                                                                             'police station must register it and '
                                                                             'transfer it later',
                                                                             'Only if she pays an administrative '
                                                                             'transfer fee',
                                                                             'Only if approved by the State High '
                                                                             'Court'],
                                                              'question': 'Can Sneha file an FIR at a police station '
                                                                          'located near her office, even if she '
                                                                          'resides in a different police precinct?'},
                                                          {   'correct_index': 1,
                                                              'explanation': 'Digital evidence should never be '
                                                                             'deleted. Unedited chat histories, '
                                                                             'profile URLs, call records, and CCTV '
                                                                             'footage backed by Section 63 BSA '
                                                                             'electronic certificates provide '
                                                                             'unassailable proof.',
                                                              'options': [   'Deleting all chats and Instagram '
                                                                             'messages so nobody sees them',
                                                                             'Exporting full unedited WhatsApp chat '
                                                                             'logs, screenshots of fake profiles, '
                                                                             'URLs, and basement CCTV video',
                                                                             'Formatting her mobile device to ensure '
                                                                             'privacy',
                                                                             'Only verbal testimony from her parents'],
                                                              'question': 'What is the crucial digital evidence Sneha '
                                                                          'must preserve to establish a water-tight '
                                                                          'stalking case?'}],
                                         'story': 'Sneha, a 24-year-old graphic designer, noticed an ex-acquaintance, '
                                                  'Rohit, following her daily from her bus stop to her office '
                                                  'building. Despite Sneha explicitly telling him via WhatsApp to '
                                                  'leave her alone and blocking his number, Rohit created multiple '
                                                  "fake Instagram profiles, sending persistent messages such as 'You "
                                                  "cannot ignore me forever' and 'If you don't talk to me, you will "
                                                  "regret it.' Last Friday, Rohit intercepted Sneha in the office "
                                                  'parking basement, grabbed her wrist, and threatened to ruin her '
                                                  'career. Sneha escaped when a colleague arrived. Her family advises '
                                                  "her: 'Don't go to police, society will blame you, just change your "
                                                  "phone number and job.'",
                                         'title': 'Persistent Stalking, Workplace Loitering, and Threatening Messages'},
    'case_03_domestic_violence_eviction': {   'category': 'Crimes Against Women',
                                              'difficulty': 'Basic',
                                              'educational_breakdown': {   'case_summary': 'Matrimonial cruelty, dowry '
                                                                                           'coercion, physical '
                                                                                           'assault, and illegal '
                                                                                           'eviction of woman and '
                                                                                           'child from shared '
                                                                                           'household.',
                                                                           'common_misconceptions': "Myth: 'If the "
                                                                                                    'house is in the '
                                                                                                    "mother-in-law's "
                                                                                                    'name, the wife '
                                                                                                    "has zero rights.' "
                                                                                                    'Reality: Under '
                                                                                                    'Supreme Court '
                                                                                                    'precedent, the '
                                                                                                    'wife has a '
                                                                                                    'statutory right '
                                                                                                    'of residence '
                                                                                                    'regardless of '
                                                                                                    'title.',
                                                                           'constitutional_analysis': 'Article 15(3) '
                                                                                                      '(Protective '
                                                                                                      'discrimination '
                                                                                                      'for women), '
                                                                                                      'Article 21 '
                                                                                                      '(Dignified '
                                                                                                      'life, shelter, '
                                                                                                      'freedom from '
                                                                                                      'domestic '
                                                                                                      'torture).',
                                                                           'court_precedents': 'Satish Chander Ahuja '
                                                                                               'v. Sneha Ahuja (2020) '
                                                                                               'SC - Right to reside '
                                                                                               'in shared household '
                                                                                               'extends to property '
                                                                                               'owned exclusively by '
                                                                                               'in-laws. Prabha Tyagi '
                                                                                               'v. Kamlesh Devi (2022) '
                                                                                               '- Domestic violence '
                                                                                               'remedies available '
                                                                                               'even if residing '
                                                                                               'separately.',
                                                                           'evidence_preservation_protocol': 'Medico-Legal '
                                                                                                             'Certificate '
                                                                                                             '(MLC) of '
                                                                                                             'physical '
                                                                                                             'assault, '
                                                                                                             'photographs '
                                                                                                             'of '
                                                                                                             'locks/belongings '
                                                                                                             'outside, '
                                                                                                             'WhatsApp/SMS '
                                                                                                             'dowry '
                                                                                                             'demands, '
                                                                                                             'marriage '
                                                                                                             'certificate/invitation, '
                                                                                                             'bank '
                                                                                                             'statements '
                                                                                                             'of '
                                                                                                             'gifts.',
                                                                           'immediate_action_protocol': '1. Call 112 / '
                                                                                                        '181 for '
                                                                                                        'immediate '
                                                                                                        'physical '
                                                                                                        'safety and '
                                                                                                        'shelter; 2. '
                                                                                                        'Get MLC '
                                                                                                        'conducted for '
                                                                                                        'physical '
                                                                                                        'assault '
                                                                                                        'bruises; 3. '
                                                                                                        'Approach '
                                                                                                        'Protection '
                                                                                                        'Officer to '
                                                                                                        'file Domestic '
                                                                                                        'Incident '
                                                                                                        'Report (DIR); '
                                                                                                        '4. File '
                                                                                                        'Section 12 '
                                                                                                        'PWDVA '
                                                                                                        'application '
                                                                                                        'for emergency '
                                                                                                        'Residence '
                                                                                                        'Order.',
                                                                           'key_takeaways': [   'PWDVA provides swift, '
                                                                                                'emergency civil '
                                                                                                'protection orders '
                                                                                                'independent of '
                                                                                                'divorce or criminal '
                                                                                                'trials.',
                                                                                                'Illegal eviction from '
                                                                                                'a shared home can be '
                                                                                                'reversed by a '
                                                                                                "Magistrate's "
                                                                                                'same-week residence '
                                                                                                'order.',
                                                                                                'Cruelty for dowry '
                                                                                                'remains a strict, '
                                                                                                'cognizable offence '
                                                                                                'under Section 85/86 '
                                                                                                'BNS.'],
                                                                           'legal_classification': 'Dual Track: '
                                                                                                   'Criminal Offence '
                                                                                                   '(BNS S. 85/86) and '
                                                                                                   'Special '
                                                                                                   'Civil-Protective '
                                                                                                   'Remedy (PWDVA '
                                                                                                   '2005).',
                                                                           'remedies_against_refusal': 'If police '
                                                                                                       'hesitate to '
                                                                                                       'file FIR due '
                                                                                                       'to mediation '
                                                                                                       'guidelines, '
                                                                                                       'invoke the '
                                                                                                       'PWDVA directly '
                                                                                                       'before the '
                                                                                                       'Magistrate, '
                                                                                                       'who has power '
                                                                                                       'to pass '
                                                                                                       'ex-parte '
                                                                                                       'residence '
                                                                                                       'orders within '
                                                                                                       '3 days under '
                                                                                                       'Section 23.',
                                                                           'reporting_forums': 'Protection Officer '
                                                                                               '(District Court / WCD '
                                                                                               'Office), Judicial '
                                                                                               'Magistrate First Class '
                                                                                               '(Section 12 PWDVA), '
                                                                                               'Women Police Station '
                                                                                               '(FIR under S. 85/86 '
                                                                                               'BNS), One Stop Centre.',
                                                                           'statutory_provisions': 'BNS Section 85 & '
                                                                                                   '86 (Cruelty), '
                                                                                                   'PWDVA 2005 '
                                                                                                   'Sections 12, 17, '
                                                                                                   '18, 19, 20, 21; '
                                                                                                   'Dowry Prohibition '
                                                                                                   'Act, 1961 Sections '
                                                                                                   '3 & 4.',
                                                                           'victim_support_compensation': 'Free legal '
                                                                                                          'aid through '
                                                                                                          'DLSA, '
                                                                                                          'monetary '
                                                                                                          'maintenance '
                                                                                                          'for food, '
                                                                                                          'shelter, '
                                                                                                          'and child '
                                                                                                          'upkeep '
                                                                                                          'under '
                                                                                                          'Section 20 '
                                                                                                          'PWDVA, and '
                                                                                                          'state '
                                                                                                          'victim '
                                                                                                          'compensation.'},
                                              'id': 'case_03_domestic_violence_eviction',
                                              'questions': [   {   'correct_index': 1,
                                                                   'explanation': 'In the landmark judgment Satish '
                                                                                  'Chander Ahuja v. Sneha Ahuja '
                                                                                  '(2020), the Supreme Court ruled '
                                                                                  'that a shared household under '
                                                                                  'Section 17 PWDVA includes premises '
                                                                                  'owned by in-laws where the '
                                                                                  'daughter-in-law lived; she cannot '
                                                                                  'be thrown out without due process '
                                                                                  'of law.',
                                                                   'options': [   'Yes, property owners have absolute '
                                                                                  'right to evict anyone at any time '
                                                                                  'without notice',
                                                                                  'No. Under Section 17 of the '
                                                                                  'Protection of Women from Domestic '
                                                                                  'Violence Act, 2005 (PWDVA), every '
                                                                                  'woman in a domestic relationship '
                                                                                  'has an absolute Right to Reside in '
                                                                                  'the Shared Household',
                                                                                  'Only if Pooja contributed at least '
                                                                                  '50% to the house purchase price',
                                                                                  'Yes, but only if they give her 24 '
                                                                                  'hours of advance notice'],
                                                                   'question': "Can Pooja's husband and mother-in-law "
                                                                               'legally evict her from the house '
                                                                               'because the property is registered in '
                                                                               "the mother-in-law's name?"},
                                                               {   'correct_index': 0,
                                                                   'explanation': 'Sections 85 and 86 BNS specifically '
                                                                                  'criminalize cruelty by husband or '
                                                                                  'relatives of husband, including '
                                                                                  'harassment with a view to coercing '
                                                                                  'her or any person related to her to '
                                                                                  'meet any unlawful demand for '
                                                                                  'property or valuable security.',
                                                                   'options': [   'Section 85 & Section 86 BNS '
                                                                                  '(Cruelty by husband or relatives, '
                                                                                  'replacing IPC 498A) and Dowry '
                                                                                  'Prohibition Act',
                                                                                  'Section 303 BNS (Theft)',
                                                                                  'Motor Vehicles Act Section 134',
                                                                                  'Consumer Protection Act Section 35'],
                                                                   'question': 'What criminal provisions under the '
                                                                               'Bharatiya Nyaya Sanhita (BNS) apply to '
                                                                               'the physical abuse and dowry '
                                                                               'harassment?'},
                                                               {   'correct_index': 1,
                                                                   'explanation': 'The PWDVA provides comprehensive '
                                                                                  'immediate civil-protective '
                                                                                  'remedies: restraining abuse, '
                                                                                  'prohibiting dispossession, '
                                                                                  'providing monthly maintenance, and '
                                                                                  'securing interim child custody.',
                                                                   'options': [   'Only a decree of immediate divorce',
                                                                                  'Protection Orders (S. 18), '
                                                                                  'Residence Orders preventing '
                                                                                  'eviction (S. 19), Monetary Relief '
                                                                                  '(S. 20), and Temporary Child '
                                                                                  'Custody (S. 21)',
                                                                                  'An order requiring Pooja to pay '
                                                                                  'rent to her mother-in-law',
                                                                                  "Mandatory arrest of Pooja's "
                                                                                  'parents'],
                                                                   'question': 'What immediate urgent orders can a '
                                                                               'Magistrate grant Pooja under the '
                                                                               'Domestic Violence Act (PWDVA)?'},
                                                               {   'correct_index': 1,
                                                                   'explanation': 'Protection Officers (POs) are '
                                                                                  'statutory officials appointed under '
                                                                                  'Section 8 PWDVA to assist victims '
                                                                                  'in filing Domestic Incident Reports '
                                                                                  '(DIR), obtaining medical exams, and '
                                                                                  'presenting applications to the '
                                                                                  'Magistrate.',
                                                                   'options': [   'Municipal Corporator',
                                                                                  'Protection Officer (PO) and Service '
                                                                                  'Providers',
                                                                                  'Local Bank Manager',
                                                                                  'Traffic Police Warden'],
                                                                   'question': 'Who is the specialized statutory '
                                                                               'official appointed under the PWDVA to '
                                                                               'assist women in drafting domestic '
                                                                               'violence applications free of cost?'},
                                                               {   'correct_index': 0,
                                                                   'explanation': 'One Stop Centres (Sakhi Centres), '
                                                                                  'accessible via Women Helpline 181, '
                                                                                  'provide 24x7 integrated emergency '
                                                                                  'shelter, medical assistance, legal '
                                                                                  'counseling, and police facilitation '
                                                                                  'under one roof.',
                                                                   'options': [   'Nearest One Stop Centre (Sakhi '
                                                                                  'Centre) / Women Helpline 181',
                                                                                  'Private commercial hotel at her own '
                                                                                  'expense',
                                                                                  'Wait until the civil court opens '
                                                                                  'next month',
                                                                                  'Railway station waiting room'],
                                                                   'question': 'If Pooja is stranded without shelter '
                                                                               'or funds right now, where can she seek '
                                                                               'immediate integrated shelter, medical '
                                                                               'care, and legal aid?'}],
                                              'story': 'Pooja, married for 3 years, lives with her husband and in-laws '
                                                       'in New Delhi. For the past year, her husband and mother-in-law '
                                                       'have subjected her to persistent physical beatings and verbal '
                                                       'degradation, demanding an additional Rs. 10 Lakhs and a luxury '
                                                       'car from her retired father. Yesterday, after a violent '
                                                       'assault that left Pooja bruised, her husband locked her out on '
                                                       "the street with her 2-year-old child, declaring: 'The house is "
                                                       "in my mother's name, you have no right to step inside. Go back "
                                                       "to your father or sleep on the road.'",
                                              'title': 'Domestic Abuse, Dowry Demands, and Threatened Eviction from '
                                                       'Shared Household'},
    'case_04_child_sexual_abuse_pocso': {   'category': 'Crimes Against Children',
                                            'difficulty': 'Emergency',
                                            'educational_breakdown': {   'case_summary': 'Child sexual abuse by a '
                                                                                         'tutor in a position of '
                                                                                         'trust, compounded by '
                                                                                         'institutional attempt to '
                                                                                         'suppress reporting.',
                                                                         'common_misconceptions': "Myth: 'Reporting "
                                                                                                  'child abuse brings '
                                                                                                  'public shame to the '
                                                                                                  "family.' Reality: "
                                                                                                  'Under Section 33(7) '
                                                                                                  'and Section 23 '
                                                                                                  'POCSO, media or '
                                                                                                  'public disclosure '
                                                                                                  "of the child's "
                                                                                                  'identity is a '
                                                                                                  'serious punishable '
                                                                                                  'crime; court '
                                                                                                  'hearings are '
                                                                                                  'conducted entirely '
                                                                                                  'in-camera.',
                                                                         'constitutional_analysis': 'Article 21 (Right '
                                                                                                    'to life and '
                                                                                                    'childhood '
                                                                                                    'dignity), Article '
                                                                                                    '39(f) (Directive '
                                                                                                    'Principle: '
                                                                                                    'Children are '
                                                                                                    'given '
                                                                                                    'opportunities and '
                                                                                                    'facilities to '
                                                                                                    'develop in a '
                                                                                                    'healthy manner '
                                                                                                    'and in conditions '
                                                                                                    'of freedom and '
                                                                                                    'dignity).',
                                                                         'court_precedents': 'Independent Thought v. '
                                                                                             'Union of India (2017) SC '
                                                                                             '- Absolute protection of '
                                                                                             'children from sexual '
                                                                                             'exploitation; bodily '
                                                                                             'integrity of minor is '
                                                                                             'non-negotiable.',
                                                                         'evidence_preservation_protocol': "Child's "
                                                                                                           'disclosure '
                                                                                                           'statement '
                                                                                                           'recorded '
                                                                                                           'by child '
                                                                                                           'psychologist '
                                                                                                           '/ '
                                                                                                           'magistrate, '
                                                                                                           'medical '
                                                                                                           'evaluation '
                                                                                                           'report, '
                                                                                                           "tutor's "
                                                                                                           'employment '
                                                                                                           'records, '
                                                                                                           'tuition '
                                                                                                           'communication '
                                                                                                           'logs.',
                                                                         'immediate_action_protocol': '1. Provide '
                                                                                                      'comforting '
                                                                                                      'psychological '
                                                                                                      'safety to '
                                                                                                      'child; 2. Call '
                                                                                                      'Childline 1098 '
                                                                                                      '/ Dial 112; 3. '
                                                                                                      'Undergo medical '
                                                                                                      'examination at '
                                                                                                      'child-friendly '
                                                                                                      'hospital; 4. '
                                                                                                      'Lodge FIR under '
                                                                                                      'POCSO Act at '
                                                                                                      'Special '
                                                                                                      'Juvenile Police '
                                                                                                      'Unit (SJPU).',
                                                                         'key_takeaways': [   'Mandatory reporting '
                                                                                              'under Section 19 POCSO '
                                                                                              'makes covering up abuse '
                                                                                              'a criminal offence.',
                                                                                              'Child identity is '
                                                                                              'strictly confidential '
                                                                                              'by law.',
                                                                                              'Special POCSO Courts '
                                                                                              'provide interim '
                                                                                              'financial compensation '
                                                                                              'even before trial '
                                                                                              'completes.'],
                                                                         'legal_classification': 'Aggravated Sexual '
                                                                                                 'Assault under '
                                                                                                 'Special Criminal '
                                                                                                 'Statute (POCSO Act, '
                                                                                                 '2012).',
                                                                         'remedies_against_refusal': 'Refusal to '
                                                                                                     'register POCSO '
                                                                                                     'case is a direct '
                                                                                                     'criminal offence '
                                                                                                     'under Section 21 '
                                                                                                     'POCSO Act. '
                                                                                                     'Approach '
                                                                                                     'District Special '
                                                                                                     'POCSO Court '
                                                                                                     'directly or '
                                                                                                     'complain to CWC.',
                                                                         'reporting_forums': 'Special Juvenile Police '
                                                                                             'Unit (SJPU) / Local '
                                                                                             'Thana, Childline 1098, '
                                                                                             'Child Welfare Committee '
                                                                                             '(CWC), National '
                                                                                             'Commission for '
                                                                                             'Protection of Child '
                                                                                             'Rights (NCPCR).',
                                                                         'statutory_provisions': 'POCSO Act 2012 '
                                                                                                 'Sections 5 & 6 '
                                                                                                 '(Aggravated '
                                                                                                 'Penetrative Sexual '
                                                                                                 'Assault / Sexual '
                                                                                                 'Assault), Section 19 '
                                                                                                 '(Mandatory '
                                                                                                 'Reporting), Section '
                                                                                                 '21 (Penalty for '
                                                                                                 'failure to report), '
                                                                                                 'BNS Section 65.',
                                                                         'victim_support_compensation': 'Mandatory '
                                                                                                        'immediate '
                                                                                                        'interim '
                                                                                                        'compensation '
                                                                                                        'awarded by '
                                                                                                        'Special POCSO '
                                                                                                        'Court under '
                                                                                                        'Section 33(8) '
                                                                                                        'POCSO Act and '
                                                                                                        'POCSO Rules '
                                                                                                        '2020 for '
                                                                                                        'medical and '
                                                                                                        'psychological '
                                                                                                        'trauma '
                                                                                                        'rehabilitation.'},
                                            'id': 'case_04_child_sexual_abuse_pocso',
                                            'questions': [   {   'correct_index': 0,
                                                                 'explanation': 'The POCSO Act, 2012 is the '
                                                                                'specialized, child-centric law '
                                                                                'enacted to protect children from '
                                                                                'sexual assault, sexual harassment, '
                                                                                'and pornography, treating anyone '
                                                                                'below 18 as a child.',
                                                                 'options': [   'Protection of Children from Sexual '
                                                                                'Offences (POCSO) Act, 2012',
                                                                                'Juvenile Justice Act, 2015 only',
                                                                                'Factories Act, 1948',
                                                                                'Indian Contract Act, 1872'],
                                                                 'question': 'Which dedicated Indian statute governs '
                                                                             'all sexual offences against children '
                                                                             'below 18 years of age?'},
                                                             {   'correct_index': 1,
                                                                 'explanation': 'Section 19 and Section 21 of the '
                                                                                'POCSO Act impose an absolute '
                                                                                'statutory obligation on any person or '
                                                                                'institution who has knowledge of '
                                                                                'sexual abuse of a child to report it '
                                                                                'to police. Failure to report is a '
                                                                                'non-compoundable crime.',
                                                                 'options': [   'Yes, private institutions can resolve '
                                                                                'internal matters confidentially',
                                                                                'No. Under Section 19 and 21 of the '
                                                                                'POCSO Act, reporting is MANDATORY; '
                                                                                'failure to report is a punishable '
                                                                                'criminal offence with imprisonment up '
                                                                                'to one year',
                                                                                'Yes, if the parents agreed in writing',
                                                                                'Only if the tutor promised not to '
                                                                                'teach again'],
                                                                 'question': 'Is the coaching center director legally '
                                                                             "permitted to 'quietly resolve' the "
                                                                             'matter without informing the police?'},
                                                             {   'correct_index': 1,
                                                                 'explanation': 'POCSO mandates child-friendly '
                                                                                'procedures: police in plain clothes, '
                                                                                "statements recorded at child's home, "
                                                                                'video recording, identity completely '
                                                                                'sealed from public/media (S. 33), and '
                                                                                'questions routed through the Special '
                                                                                'Court Judge.',
                                                                 'options': [   'Child must wear school uniform in '
                                                                                'court and testify before public '
                                                                                'gallery',
                                                                                'Police officer must wear civilian '
                                                                                'clothes (not uniform), questioning '
                                                                                "must happen at child's residence, no "
                                                                                'confrontation with accused, and '
                                                                                'identity is strictly confidential (S. '
                                                                                '24 & 33 POCSO)',
                                                                                'Child must be detained in a police '
                                                                                'station lockup for safety',
                                                                                'Accused lawyer can cross-examine the '
                                                                                'child aggressively without magistrate '
                                                                                'oversight'],
                                                                 'question': 'How does the POCSO Act protect the child '
                                                                             'during police investigation and court '
                                                                             'proceedings?'},
                                                             {   'correct_index': 1,
                                                                 'explanation': 'Under POCSO, a minor cannot consent '
                                                                                'to sexual acts. Section 29 reverses '
                                                                                'the burden of proof, presuming the '
                                                                                'accused committed the offence once '
                                                                                'basic prosecution ingredients are '
                                                                                'established.',
                                                                 'options': [   'Consent of child is valid if child is '
                                                                                'above 7 years',
                                                                                "Child's consent is completely "
                                                                                'irrelevant; law presumes absence of '
                                                                                'consent and Section 29/30 establishes '
                                                                                'a statutory presumption of guilt '
                                                                                'against the accused',
                                                                                'Consent must be verified by school '
                                                                                'teachers',
                                                                                'Consent depends on parental approval'],
                                                                 'question': 'What is the legal presumption regarding '
                                                                             'consent of a child under the POCSO Act?'},
                                                             {   'correct_index': 0,
                                                                 'explanation': 'Childline 1098 is the national 24x7 '
                                                                                'emergency helpline dedicated to the '
                                                                                'protection and rescue of children in '
                                                                                'distress.',
                                                                 'options': [   'Childline 1098 (now integrated with '
                                                                                '112)',
                                                                                'Commercial private detective agency',
                                                                                'Tourist helpline 1363',
                                                                                'Traffic challan desk'],
                                                                 'question': 'What immediate emergency helpline should '
                                                                             'be called for child distress, rescue, '
                                                                             'and legal counseling across India?'}],
                                            'story': 'Aarav, a 9-year-old school student, became unusually withdrawn, '
                                                     'terrified of his after-school math tuition, and began wetting '
                                                     'his bed. When gently questioned by his mother, Aarav revealed in '
                                                     'tears that his private tutor, Sharma, had been making him touch '
                                                     'private body parts and threatening to fail him in school if he '
                                                     "told anyone. Aarav's parents confronted the tuition coaching "
                                                     "center director, who said: 'Please do not defame our institute. "
                                                     "We will quietly terminate Mr. Sharma's employment; you should "
                                                     "not ruin your child's life by going to the police.'",
                                            'title': 'Child Sexual Abuse by Private Tutor and Institutional Failure to '
                                                     'Report'},
    'case_05_senior_citizen_property_abandonment': {   'category': 'Senior Citizens',
                                                       'difficulty': 'Intermediate',
                                                       'educational_breakdown': {   'case_summary': 'Elderly widower '
                                                                                                    'evicted by son '
                                                                                                    'after executing a '
                                                                                                    'conditional '
                                                                                                    'property gift '
                                                                                                    'deed, leaving him '
                                                                                                    'destitute and '
                                                                                                    'without '
                                                                                                    'medication.',
                                                                                    'common_misconceptions': 'Myth: '
                                                                                                             "'You "
                                                                                                             'must '
                                                                                                             'file an '
                                                                                                             'expensive '
                                                                                                             'civil '
                                                                                                             'title '
                                                                                                             'suit in '
                                                                                                             'civil '
                                                                                                             'court to '
                                                                                                             'get your '
                                                                                                             'gifted '
                                                                                                             'house '
                                                                                                             "back.' "
                                                                                                             'Reality: '
                                                                                                             'SDM '
                                                                                                             'Maintenance '
                                                                                                             'Tribunal '
                                                                                                             'has '
                                                                                                             'statutory '
                                                                                                             'summary '
                                                                                                             'power '
                                                                                                             'under '
                                                                                                             'Section '
                                                                                                             '23 to '
                                                                                                             'cancel '
                                                                                                             'the gift '
                                                                                                             'deed '
                                                                                                             'within '
                                                                                                             '90 days.',
                                                                                    'constitutional_analysis': 'Article '
                                                                                                               '21 '
                                                                                                               '(Right '
                                                                                                               'to '
                                                                                                               'life '
                                                                                                               'and '
                                                                                                               'dignified '
                                                                                                               'existence '
                                                                                                               'until '
                                                                                                               'natural '
                                                                                                               'death), '
                                                                                                               'Article '
                                                                                                               '41 '
                                                                                                               '(Directive '
                                                                                                               'Principle: '
                                                                                                               'State '
                                                                                                               'shall '
                                                                                                               'make '
                                                                                                               'effective '
                                                                                                               'provision '
                                                                                                               'for '
                                                                                                               'securing '
                                                                                                               'public '
                                                                                                               'assistance '
                                                                                                               'in old '
                                                                                                               'age).',
                                                                                    'court_precedents': 'S. Vanitha v. '
                                                                                                        'Deputy '
                                                                                                        'Commissioner '
                                                                                                        '(2020) SC - '
                                                                                                        'Affirmed '
                                                                                                        'overriding '
                                                                                                        'power of '
                                                                                                        'MWPSC Act to '
                                                                                                        'evict abusive '
                                                                                                        'family '
                                                                                                        'members and '
                                                                                                        'protect '
                                                                                                        'senior '
                                                                                                        "citizens' "
                                                                                                        'shelter. '
                                                                                                        'Sudesh '
                                                                                                        'Chhikara v. '
                                                                                                        'Ramti Devi '
                                                                                                        '(2022) SC - '
                                                                                                        'Property gift '
                                                                                                        'revocation '
                                                                                                        'criteria '
                                                                                                        'under Section '
                                                                                                        '23.',
                                                                                    'evidence_preservation_protocol': 'Registered '
                                                                                                                      'gift '
                                                                                                                      'deed '
                                                                                                                      'copy, '
                                                                                                                      'medical '
                                                                                                                      'prescriptions '
                                                                                                                      'and '
                                                                                                                      'pharmacy '
                                                                                                                      'receipts '
                                                                                                                      'showing '
                                                                                                                      'ongoing '
                                                                                                                      'ailments, '
                                                                                                                      'bank '
                                                                                                                      'statements '
                                                                                                                      'showing '
                                                                                                                      'lack '
                                                                                                                      'of '
                                                                                                                      'independent '
                                                                                                                      'income, '
                                                                                                                      'proof '
                                                                                                                      'of '
                                                                                                                      'lock-out '
                                                                                                                      '(photos/videos).',
                                                                                    'immediate_action_protocol': '1. '
                                                                                                                 'Call '
                                                                                                                 'Elderline '
                                                                                                                 '14567 '
                                                                                                                 'for '
                                                                                                                 'immediate '
                                                                                                                 'shelter/food '
                                                                                                                 'rescue; '
                                                                                                                 '2. '
                                                                                                                 'Call '
                                                                                                                 '112 '
                                                                                                                 'if '
                                                                                                                 'locked '
                                                                                                                 'out '
                                                                                                                 'in '
                                                                                                                 'the '
                                                                                                                 'cold; '
                                                                                                                 '3. '
                                                                                                                 'File '
                                                                                                                 'application '
                                                                                                                 'before '
                                                                                                                 'Sub-Divisional '
                                                                                                                 'Magistrate '
                                                                                                                 '(SDM) '
                                                                                                                 'Maintenance '
                                                                                                                 'Tribunal '
                                                                                                                 'under '
                                                                                                                 'Section '
                                                                                                                 '4 '
                                                                                                                 'and '
                                                                                                                 'Section '
                                                                                                                 '23 '
                                                                                                                 'MWPSC '
                                                                                                                 'Act.',
                                                                                    'key_takeaways': [   'Section 23 '
                                                                                                         'MWPSC Act '
                                                                                                         'can revoke '
                                                                                                         'registered '
                                                                                                         'property '
                                                                                                         'gift deeds '
                                                                                                         'if children '
                                                                                                         'fail to '
                                                                                                         'maintain '
                                                                                                         'parents.',
                                                                                                         'Tribunal '
                                                                                                         'process is '
                                                                                                         'fast-tracked '
                                                                                                         '(statutory '
                                                                                                         'target 90 '
                                                                                                         'days) and '
                                                                                                         'debarred of '
                                                                                                         'lawyer '
                                                                                                         'technicalities.',
                                                                                                         'Elderline '
                                                                                                         '14567 '
                                                                                                         'provides '
                                                                                                         'end-to-end '
                                                                                                         'field '
                                                                                                         'intervention.'],
                                                                                    'legal_classification': 'Special '
                                                                                                            'Statutory '
                                                                                                            'Welfare '
                                                                                                            'and '
                                                                                                            'Summary '
                                                                                                            'Tribunal '
                                                                                                            'Remedy '
                                                                                                            '(MWPSC '
                                                                                                            'Act, '
                                                                                                            '2007).',
                                                                                    'remedies_against_refusal': 'Section '
                                                                                                                '16 '
                                                                                                                'MWPSC '
                                                                                                                'Act '
                                                                                                                'provides '
                                                                                                                'an '
                                                                                                                'Appellate '
                                                                                                                'Tribunal '
                                                                                                                'headed '
                                                                                                                'by '
                                                                                                                'the '
                                                                                                                'District '
                                                                                                                'Magistrate '
                                                                                                                '(DM). '
                                                                                                                'Civil '
                                                                                                                'courts '
                                                                                                                'are '
                                                                                                                'explicitly '
                                                                                                                'barred '
                                                                                                                'under '
                                                                                                                'Section '
                                                                                                                '27 to '
                                                                                                                'prevent '
                                                                                                                'endless '
                                                                                                                'procedural '
                                                                                                                'delays.',
                                                                                    'reporting_forums': 'Maintenance '
                                                                                                        'Tribunal '
                                                                                                        '(Office of '
                                                                                                        'the '
                                                                                                        'Sub-Divisional '
                                                                                                        'Magistrate / '
                                                                                                        'SDM), '
                                                                                                        'Elderline '
                                                                                                        '14567, '
                                                                                                        'District '
                                                                                                        'Social '
                                                                                                        'Welfare '
                                                                                                        'Officer, '
                                                                                                        'Police Thana '
                                                                                                        '(S. 24 '
                                                                                                        'abandonment).',
                                                                                    'statutory_provisions': 'MWPSC Act '
                                                                                                            '2007 '
                                                                                                            'Sections '
                                                                                                            '4 & 9 '
                                                                                                            '(Maintenance '
                                                                                                            'order), '
                                                                                                            'Section '
                                                                                                            '23 '
                                                                                                            '(Revocation '
                                                                                                            'of '
                                                                                                            'property '
                                                                                                            'transfer), '
                                                                                                            'Section '
                                                                                                            '24 '
                                                                                                            '(Criminal '
                                                                                                            'abandonment).',
                                                                                    'victim_support_compensation': 'Interim '
                                                                                                                   'monthly '
                                                                                                                   'maintenance '
                                                                                                                   'order '
                                                                                                                   'under '
                                                                                                                   'Section '
                                                                                                                   '9, '
                                                                                                                   'immediate '
                                                                                                                   'restoration '
                                                                                                                   'of '
                                                                                                                   'physical '
                                                                                                                   'possession '
                                                                                                                   'of '
                                                                                                                   'premises, '
                                                                                                                   'and '
                                                                                                                   'state '
                                                                                                                   'old-age '
                                                                                                                   'home '
                                                                                                                   'shelter '
                                                                                                                   'assistance.'},
                                                       'id': 'case_05_senior_citizen_property_abandonment',
                                                       'questions': [   {   'correct_index': 0,
                                                                            'explanation': 'The MWPSC Act, 2007 is a '
                                                                                           'dedicated summary '
                                                                                           'legislation establishing '
                                                                                           'Senior Citizen Maintenance '
                                                                                           'Tribunals headed by '
                                                                                           'Sub-Divisional Magistrates '
                                                                                           '(SDMs) that must decide '
                                                                                           'cases within 90 days.',
                                                                            'options': [   'Maintenance and Welfare of '
                                                                                           'Parents and Senior '
                                                                                           'Citizens Act, 2007 (MWPSC '
                                                                                           'Act)',
                                                                                           'Arbitration and '
                                                                                           'Conciliation Act, 1996',
                                                                                           'Companies Act, 2013',
                                                                                           'Sale of Goods Act, 1930'],
                                                                            'question': 'Under which specialized law '
                                                                                        'can Rameshwar seek swift '
                                                                                        'relief without having to '
                                                                                        'fight a 10-year civil court '
                                                                                        'trial?'},
                                                                        {   'correct_index': 1,
                                                                            'explanation': 'Section 23 of the MWPSC '
                                                                                           'Act is a landmark '
                                                                                           'protective provision. The '
                                                                                           'SDM Tribunal can declare '
                                                                                           'the transfer of property '
                                                                                           'void as made by fraud or '
                                                                                           'coercion, restoring full '
                                                                                           'ownership to the senior '
                                                                                           'citizen.',
                                                                            'options': [   'No, once a gift deed is '
                                                                                           'registered, it can never '
                                                                                           'be cancelled under any '
                                                                                           'Indian law',
                                                                                           'Yes. Under Section 23 of '
                                                                                           'the MWPSC Act, 2007, if '
                                                                                           'property was transferred '
                                                                                           'on condition of basic care '
                                                                                           'and the transferee fails '
                                                                                           'to provide it, the '
                                                                                           'transfer is deemed '
                                                                                           'fraudulent and void',
                                                                                           'Only if the son is '
                                                                                           'convicted of a criminal '
                                                                                           'murder attempt',
                                                                                           'Only if the Municipal '
                                                                                           'Corporation agrees to '
                                                                                           're-register the land'],
                                                                            'question': 'Can the Maintenance Tribunal '
                                                                                        'declare the gift deed VOID '
                                                                                        'and restore the flat back to '
                                                                                        'Rameshwar?'},
                                                                        {   'correct_index': 1,
                                                                            'explanation': 'Section 17 of the MWPSC '
                                                                                           'Act specifically debars '
                                                                                           'legal practitioners from '
                                                                                           'representing parties, '
                                                                                           'enabling the senior '
                                                                                           'citizen to present '
                                                                                           'grievances directly or '
                                                                                           'through Maintenance '
                                                                                           'Officers without legal '
                                                                                           'costs.',
                                                                            'options': [   'Yes, senior advocates from '
                                                                                           'High Court must appear',
                                                                                           'No. Under Section 17 of '
                                                                                           'the MWPSC Act, legal '
                                                                                           'practitioners are barred '
                                                                                           'from appearing before the '
                                                                                           'Tribunal to keep the '
                                                                                           'process summary, informal, '
                                                                                           'and non-exploitative',
                                                                                           'Only the son can hire a '
                                                                                           'lawyer',
                                                                                           'Only lawyers with 20 years '
                                                                                           'experience can appear'],
                                                                            'question': 'Are lawyers permitted to '
                                                                                        'represent parties before the '
                                                                                        'Senior Citizen Maintenance '
                                                                                        'Tribunal by default?'},
                                                                        {   'correct_index': 1,
                                                                            'explanation': 'Section 24 of the MWPSC '
                                                                                           'Act explicitly makes '
                                                                                           'exposure and abandonment '
                                                                                           'of a senior citizen a '
                                                                                           'cognizable criminal '
                                                                                           'offence.',
                                                                            'options': [   'No, it is strictly a moral '
                                                                                           'family issue',
                                                                                           'Yes. Under Section 24 of '
                                                                                           'the MWPSC Act, anyone '
                                                                                           'having care or protection '
                                                                                           'of a senior citizen who '
                                                                                           'leaves them with intention '
                                                                                           'of wholly abandoning them '
                                                                                           'is punishable with '
                                                                                           'imprisonment up to 3 '
                                                                                           'months or fine',
                                                                                           'Only if the senior citizen '
                                                                                           'is above 90 years of age',
                                                                                           'Only if committed outside '
                                                                                           'state borders'],
                                                                            'question': 'Is abandonment of a senior '
                                                                                        'citizen a punishable criminal '
                                                                                        'offence under the MWPSC Act?'},
                                                                        {   'correct_index': 0,
                                                                            'explanation': 'Elderline (Toll-Free '
                                                                                           '14567) is the Government '
                                                                                           "of India's dedicated "
                                                                                           'senior citizen helpline '
                                                                                           'providing emergency '
                                                                                           'rescue, mediation, and '
                                                                                           'legal facilitation.',
                                                                            'options': [   'National Elderline '
                                                                                           'Helpline 14567',
                                                                                           'Income Tax Helpline 1961',
                                                                                           'Railway Enquiry 139',
                                                                                           'Postal complaint desk'],
                                                                            'question': 'What national government '
                                                                                        'helpline can Rameshwar dial '
                                                                                        'for immediate rescue, food, '
                                                                                        'shelter, and legal '
                                                                                        'assistance?'}],
                                                       'story': 'Rameshwar, a 74-year-old retired clerk suffering from '
                                                                'arthritis, gifted his sole self-acquired two-bedroom '
                                                                'flat in Pune to his son, Vikram, through a registered '
                                                                'gift deed. The gift deed contained a specific '
                                                                'understanding that Vikram would take care of '
                                                                "Rameshwar's food, medical treatment, and shelter for "
                                                                'the rest of his life. Three months after the deed was '
                                                                'registered, Vikram and his wife began starving '
                                                                'Rameshwar, stopped purchasing his heart medication, '
                                                                'and finally changed the entrance door locks while '
                                                                'Rameshwar was at the temple, leaving his clothes in a '
                                                                'garbage bag outside. When Rameshwar pleaded, Vikram '
                                                                "replied: 'The flat is legally mine now. Go live in an "
                                                                "old age home or beg on the streets.'",
                                                       'title': 'Elderly Widower Evicted After Gifting House to Son'},
    'case_06_digital_arrest_scam': {   'category': 'Cybercrime & Online Fraud',
                                       'difficulty': 'Advanced',
                                       'educational_breakdown': {   'case_summary': 'Extortion syndicate posing as '
                                                                                    'CBI/Police executing a fictitious '
                                                                                    "'Digital Arrest' over video call "
                                                                                    'with forged Supreme Court '
                                                                                    'warrants, siphoning life savings.',
                                                                    'common_misconceptions': "Myth: 'Police can arrest "
                                                                                             'you on video call and '
                                                                                             "inspect your funds.' "
                                                                                             'Reality: Law enforcement '
                                                                                             'in India can only arrest '
                                                                                             'in person with proper '
                                                                                             'identification, memo '
                                                                                             'under BNSS Section 36, '
                                                                                             'and production before a '
                                                                                             'Magistrate within 24 '
                                                                                             'hours.',
                                                                    'constitutional_analysis': 'Article 21 (Personal '
                                                                                               'liberty and freedom '
                                                                                               'from unlawful '
                                                                                               'extortion), State '
                                                                                               'Monopoly on Legitimate '
                                                                                               'Force.',
                                                                    'court_precedents': 'In Re: Cyber Frauds & Digital '
                                                                                        'Arrests (High Courts & SC '
                                                                                        'Advisories 2024) - Directing '
                                                                                        'police forces to coordinate '
                                                                                        'with I4C, freeze mule '
                                                                                        'accounts, and sensitize '
                                                                                        'citizens.',
                                                                    'evidence_preservation_protocol': 'Bank transfer '
                                                                                                      'UTR numbers, '
                                                                                                      'account '
                                                                                                      'statement with '
                                                                                                      'exact '
                                                                                                      'timestamps, '
                                                                                                      'Skype/WhatsApp '
                                                                                                      'usernames and '
                                                                                                      'caller phone '
                                                                                                      'numbers, '
                                                                                                      'screenshots of '
                                                                                                      'fake arrest '
                                                                                                      'warrants/ID '
                                                                                                      'cards, call '
                                                                                                      'recordings.',
                                                                    'immediate_action_protocol': '1. Disconnect the '
                                                                                                 'call immediately — '
                                                                                                 'you cannot be '
                                                                                                 'arrested over video; '
                                                                                                 '2. Call 1930 / '
                                                                                                 'cybercrime.gov.in '
                                                                                                 'IMMEDIATELY; 3. '
                                                                                                 "Contact your bank's "
                                                                                                 'emergency fraud desk '
                                                                                                 'to recall RTGS/NEFT; '
                                                                                                 '4. Lodge FIR at '
                                                                                                 'Cyber Crime Police '
                                                                                                 'Station.',
                                                                    'key_takeaways': [   "'Digital arrest' does not "
                                                                                         'exist in Indian '
                                                                                         'jurisprudence.',
                                                                                         'Reporting to 1930 within the '
                                                                                         'Golden Hour freezes money in '
                                                                                         'the banking grid.',
                                                                                         'BSA Section 63 governs the '
                                                                                         'legal admissibility of '
                                                                                         'electronic evidence.'],
                                                                    'legal_classification': 'Organized Cybercrime, '
                                                                                            'Extortion, and Forgery of '
                                                                                            'State Documents under BNS '
                                                                                            '& IT Act.',
                                                                    'remedies_against_refusal': 'Cyber police stations '
                                                                                                'are specialized for '
                                                                                                'these crimes. If '
                                                                                                'funds are frozen in '
                                                                                                'mule accounts, file '
                                                                                                'an application under '
                                                                                                'Section 503 BNSS '
                                                                                                '(disposal of '
                                                                                                'property) before the '
                                                                                                'Magistrate to release '
                                                                                                'the frozen funds back '
                                                                                                'to your account.',
                                                                    'reporting_forums': 'National Cyber Crime '
                                                                                        'Reporting Portal '
                                                                                        '(cybercrime.gov.in / Dial '
                                                                                        '1930), District Cyber Crime '
                                                                                        'Police Station, Sanchar '
                                                                                        'Saathi Chakshu Portal (for '
                                                                                        'disconnecting scammer '
                                                                                        'numbers).',
                                                                    'statutory_provisions': 'BNS Section 204 '
                                                                                            '(Impersonating public '
                                                                                            'servant), Section 308 '
                                                                                            '(Extortion), Section 318 '
                                                                                            '& 319 (Cheating by '
                                                                                            'personation), Section 336 '
                                                                                            '& 338 (Forgery), IT Act '
                                                                                            'Section 66D, BSA Section '
                                                                                            '63.',
                                                                    'victim_support_compensation': 'Inter-bank '
                                                                                                   'automated lien '
                                                                                                   'recovery via 1930 '
                                                                                                   'and victim '
                                                                                                   'compensation claim '
                                                                                                   'for cyber '
                                                                                                   'extortion via '
                                                                                                   'DLSA.'},
                                       'id': 'case_06_digital_arrest_scam',
                                       'questions': [   {   'correct_index': 1,
                                                            'explanation': 'Prime Minister Narendra Modi and the '
                                                                           'Ministry of Home Affairs have explicitly '
                                                                           'issued public advisories: there is NO such '
                                                                           "legal concept as 'Digital Arrest' under "
                                                                           'Indian law. Law enforcement never arrests '
                                                                           'citizens over video calls.',
                                                            'options': [   'Yes, it was introduced in the BNSS 2023 '
                                                                           'for cyber investigations',
                                                                           "No. 'Digital Arrest' is completely "
                                                                           'fictitious and ILLEGAL; no police agency '
                                                                           'or court in India conducts arrests or '
                                                                           'trials over Skype/WhatsApp',
                                                                           'Yes, but only for financial crimes above '
                                                                           'Rs. 10 Lakhs',
                                                                           'Only the CBI has powers of Digital Arrest'],
                                                            'question': "Does the concept of 'Digital Arrest' via "
                                                                        'WhatsApp or Skype video call exist under '
                                                                        'Indian law?'},
                                                        {   'correct_index': 1,
                                                            'explanation': 'Impersonating police officers, forging '
                                                                           'Supreme Court arrest warrants, using '
                                                                           'national emblems, and intimidating victims '
                                                                           'into transferring money constitute '
                                                                           'aggravated cheating, extortion, forgery, '
                                                                           'and cyber impersonation.',
                                                            'options': [   'Only a telemarketing spam violation under '
                                                                           'TRAI rules',
                                                                           'Cheating by personation (S. 319 BNS / 66D '
                                                                           'IT Act), Extortion (S. 308 BNS), Forgery '
                                                                           'of government seals (S. 336/338 BNS), and '
                                                                           'Impersonating a public servant (S. 204 '
                                                                           'BNS)',
                                                                           'Defamation under civil torts',
                                                                           'Breach of contract under Indian Contract '
                                                                           'Act'],
                                                            'question': 'What serious criminal offences have the '
                                                                        'scammers committed under the BNS and IT Act?'},
                                                        {   'correct_index': 1,
                                                            'explanation': "Calling 1930 within the 'Golden Hour' "
                                                                           'triggers the Indian Cyber Crime '
                                                                           'Coordination Centre (I4C) Citizen '
                                                                           'Financial Cyber Fraud Reporting System, '
                                                                           'which electronically freezes the '
                                                                           'transaction trail across beneficiary '
                                                                           'banks.',
                                                            'options': [   'Wait until Monday morning to visit his '
                                                                           'home branch bank manager',
                                                                           'Dial 1930 immediately or log on to '
                                                                           "cybercrime.gov.in within the 'Golden Hour' "
                                                                           'to initiate automated inter-bank lien '
                                                                           'freezing',
                                                                           'Delete Skype and destroy his phone so '
                                                                           'police cannot reach him',
                                                                           'File a civil recovery suit in the District '
                                                                           'Court'],
                                                            'question': 'If Sunil realized the fraud 45 minutes after '
                                                                        'transferring the money, what is the critical '
                                                                        'step he MUST take to recover the funds?'},
                                                        {   'correct_index': 1,
                                                            'explanation': 'Any request to transfer money into an '
                                                                           "account for 'verification', 'safe "
                                                                           "custody', or 'escrow' is a 100% scam. "
                                                                           'Neither the RBI nor the police ever '
                                                                           'operate private escrow accounts for '
                                                                           'individual criminal audits.',
                                                            'options': [   'Yes, that is the standard audit procedure '
                                                                           'in narcotics cases',
                                                                           'No. No government agency, court, police '
                                                                           'department, or RBI ever asks citizens to '
                                                                           "transfer money to 'verify funds' or prove "
                                                                           'innocence',
                                                                           'Yes, but only through RTGS',
                                                                           'Only if approved by an Income Tax '
                                                                           'Inspector'],
                                                            'question': 'Can police or any government department order '
                                                                        "a citizen to transfer money into an 'RBI "
                                                                        "Verification Account' to verify innocence?"},
                                                        {   'correct_index': 1,
                                                            'explanation': 'Under the new Bharatiya Sakshya Adhiniyam, '
                                                                           '2023, Section 63 governs the admissibility '
                                                                           'of electronic records, replacing Section '
                                                                           '65B of the repealed Indian Evidence Act, '
                                                                           '1872.',
                                                            'options': [   'Section 65B Certificate under old Evidence '
                                                                           'Act',
                                                                           'Section 63 Certificate under the Bharatiya '
                                                                           'Sakshya Adhiniyam, 2023',
                                                                           'Notarized property stamp certificate',
                                                                           'Chartered Accountant audit seal'],
                                                            'question': 'Under the Bharatiya Sakshya Adhiniyam, 2023 '
                                                                        '(BSA), what certificate is required to admit '
                                                                        'digital screenshots and video logs as '
                                                                        'evidence in court?'}],
                                       'story': 'Sunil, a 52-year-old school principal, received a call from an '
                                                "automated IVR claiming to be 'FedEx Courier', stating a parcel sent "
                                                'from Mumbai to Thailand containing 5 fake passports, 150 grams of '
                                                "MDMA drugs, and 6 bank credit cards in Sunil's name had been "
                                                'intercepted. The call was immediately transferred to a Skype video '
                                                'call with a man wearing an Indian Police uniform sitting in a room '
                                                "with a 'Cyber Crime Police Headquarter' banner. The caller displayed "
                                                'a forged Supreme Court arrest warrant bearing the National Emblem and '
                                                "Chief Justice's fake signature. The fake officer announced: 'You are "
                                                'under 24-hour Digital Arrest. Do not disconnect the video camera or '
                                                'talk to your family, or commandos will raid your house. To prove your '
                                                'innocence and clear your bank accounts from money laundering, you '
                                                'must immediately transfer your entire mutual fund savings of Rs. 24 '
                                                'Lakhs to the RBI Financial Verification Escrow Account; it will be '
                                                "refunded in 30 minutes after biometric audit.'",
                                       'title': "The 'Digital Arrest' Video Call Scam Impersonating Police & CBI"},
    'case_07_upi_qr_code_scam': {   'category': 'Financial Scams & Identity Theft',
                                    'difficulty': 'Basic',
                                    'educational_breakdown': {   'case_summary': 'Online marketplace seller deceived '
                                                                                 'by fake buyer impersonating military '
                                                                                 'personnel into scanning a QR code '
                                                                                 'and entering UPI PIN, suffering '
                                                                                 'financial loss.',
                                                                 'common_misconceptions': "Myth: 'You need to enter "
                                                                                          'your PIN to receive an '
                                                                                          "advance payment.' Reality: "
                                                                                          'Money is credited directly '
                                                                                          'using your phone number or '
                                                                                          'VPA; you NEVER enter a PIN '
                                                                                          'to receive funds.',
                                                                 'constitutional_analysis': 'Not directly a '
                                                                                            'constitutional dispute '
                                                                                            '(private transaction); '
                                                                                            'governed by criminal '
                                                                                            'fraud provisions and RBI '
                                                                                            'regulatory framework.',
                                                                 'court_precedents': 'State of Maharashtra v. Pradeep '
                                                                                     'Kumar - Cyber frauds involving '
                                                                                     'digital payment gateways '
                                                                                     'constitute offences under both '
                                                                                     'IPC/BNS and Section 66D IT Act.',
                                                                 'evidence_preservation_protocol': 'Screenshots of OLX '
                                                                                                   'chat and user '
                                                                                                   'profile, WhatsApp '
                                                                                                   'conversation '
                                                                                                   'screenshots, QR '
                                                                                                   'code images '
                                                                                                   'received, Bank SMS '
                                                                                                   'and account '
                                                                                                   'statement '
                                                                                                   'displaying '
                                                                                                   'transaction UTR '
                                                                                                   'number.',
                                                                 'immediate_action_protocol': '1. Do NOT scan any '
                                                                                              'second refund QR code; '
                                                                                              '2. Call bank customer '
                                                                                              'care immediately to '
                                                                                              'report unauthorized '
                                                                                              'transaction UTR; 3. '
                                                                                              'Call 1930 or submit '
                                                                                              'complaint on '
                                                                                              'cybercrime.gov.in; 4. '
                                                                                              'Change UPI PIN.',
                                                                 'key_takeaways': [   'UPI PIN is strictly an '
                                                                                      'authorization for DEBIT, never '
                                                                                      'credit.',
                                                                                      'Fake military identity is a '
                                                                                      'standard scam script on '
                                                                                      'OLX/Quikr.',
                                                                                      'Reporting within 3 days '
                                                                                      'triggers RBI customer '
                                                                                      'protection safeguards.'],
                                                                 'legal_classification': 'Cyber Financial Fraud and '
                                                                                         'Cheating by Personation '
                                                                                         'under BNS & IT Act.',
                                                                 'remedies_against_refusal': 'If bank fails to resolve '
                                                                                             'within 30 days or '
                                                                                             'rejects liability '
                                                                                             'arbitrarily, file an '
                                                                                             'online complaint before '
                                                                                             'the RBI Integrated '
                                                                                             'Ombudsman under the '
                                                                                             'Reserve Bank - '
                                                                                             'Integrated Ombudsman '
                                                                                             'Scheme, 2021.',
                                                                 'reporting_forums': 'National Cyber Crime Reporting '
                                                                                     'Portal (cybercrime.gov.in / '
                                                                                     '1930), Bank Banking Ombudsman '
                                                                                     '(rbi.org.in), Local Cyber Cell.',
                                                                 'statutory_provisions': 'BNS Section 318 (Cheating), '
                                                                                         'Section 319 (Cheating by '
                                                                                         'personation), IT Act Section '
                                                                                         '66D, RBI Customer Protection '
                                                                                         'Circular 2017.',
                                                                 'victim_support_compensation': 'Recovery via '
                                                                                                'inter-bank lien '
                                                                                                'freeze on 1930 and '
                                                                                                'statutory '
                                                                                                'compensation claim '
                                                                                                'through RBI '
                                                                                                'Ombudsman.'},
                                    'id': 'case_07_upi_qr_code_scam',
                                    'questions': [   {   'correct_index': 1,
                                                         'explanation': 'A QR code or UPI PIN is ONLY required to '
                                                                        'authorize a payment (debit). Receiving money '
                                                                        'requires zero authorization, PIN, or QR '
                                                                        'scanning.',
                                                         'options': [   'You must enter your UPI PIN to both send and '
                                                                        'receive money',
                                                                        'You NEVER enter your UPI PIN to receive '
                                                                        'money; UPI PIN is used EXCLUSIVELY to '
                                                                        'debit/transfer money from your account',
                                                                        'You only enter PIN if the sender is an army '
                                                                        'officer',
                                                                        'You enter PIN only for transactions above Rs. '
                                                                        '10,000'],
                                                         'question': 'What is the universal rule regarding entering '
                                                                     'your UPI PIN on payment apps?'},
                                                     {   'correct_index': 1,
                                                         'explanation': "This is a classic 'double-dip' scam. The "
                                                                        "scammer exploits the victim's panic to "
                                                                        'trigger a second, larger debit.',
                                                         'options': [   'Yes, scanning it will immediately refund her '
                                                                        'lost Rs. 15,000',
                                                                        'No! Scanning the second QR code and entering '
                                                                        'her PIN will debit ANOTHER Rs. 30,000 from '
                                                                        'her account',
                                                                        'Only if she uses a different banking app',
                                                                        'Only if she restarts her phone first'],
                                                         'question': "Should Meera scan the second 'reverse refund' QR "
                                                                     'code sent by the caller?'},
                                                     {   'correct_index': 1,
                                                         'explanation': 'The RBI Charter on Customer Rights mandates '
                                                                        'that prompt notification within 3 working '
                                                                        'days significantly mitigates or eliminates '
                                                                        'customer liability in unauthorized electronic '
                                                                        'banking frauds.',
                                                         'options': [   '100% customer liability in all circumstances',
                                                                        'Zero liability if the fraud arose from '
                                                                        'third-party breach/system flaw, or limited '
                                                                        'liability depending on circumstances if '
                                                                        'reported within 3 working days',
                                                                        'Mandatory fine payable to the bank',
                                                                        "Customer must pay for the bank's "
                                                                        'investigation costs'],
                                                         'question': "Under RBI's Circular on Limiting Liability of "
                                                                     'Customers in Unauthorized Electronic Banking '
                                                                     "Transactions, what is the customer's liability "
                                                                     'if reported within 3 days?'},
                                                     {   'correct_index': 0,
                                                         'explanation': 'Impersonating military personnel to extract '
                                                                        'money is cheating by personation under '
                                                                        'Section 319 BNS and cyber impersonation under '
                                                                        'Section 66D IT Act.',
                                                         'options': [   'Cheating by personation under Section 319 BNS '
                                                                        'and Section 66D of the IT Act',
                                                                        'Defamation under Section 356 BNS',
                                                                        'Public nuisance under municipal law',
                                                                        'Breach of OLX Terms of Service only'],
                                                         'question': 'What criminal charge applies to the scammer for '
                                                                     'pretending to be an Army Officer and cheating '
                                                                     'Meera?'},
                                                     {   'correct_index': 0,
                                                         'explanation': 'Changing credentials, informing the bank '
                                                                        'fraud desk with the UTR number, and lodging a '
                                                                        'ticket on 1930 blocks further unauthorized '
                                                                        'drains.',
                                                         'options': [   'Change UPI PIN, block debit card on net '
                                                                        'banking app, and report the transaction '
                                                                        'reference number (UTR) to bank fraud helpline '
                                                                        'and 1930',
                                                                        'Throw away her SIM card',
                                                                        'Delete Google Pay without contacting the bank',
                                                                        'Pay the scammer more money'],
                                                         'question': 'What immediate technical step should Meera take '
                                                                     'to secure her bank account?'}],
                                    'story': 'Meera listed her wooden dining table for sale on OLX for Rs. 15,000. '
                                             "Within an hour, a buyer calling himself 'Army Officer Vikram Rathore' "
                                             'called, agreeing to buy the table immediately without bargaining. The '
                                             'caller claimed he was stationed at a military cantonment and would send '
                                             "an army truck to pick it up. He told Meera: 'I am sending an advance of "
                                             'Rs. 15,000 through the Indian Army merchant gateway. I am sending you a '
                                             'QR code on WhatsApp. Just scan it in your Google Pay and enter your UPI '
                                             "PIN to receive the credit balance.' Meera scanned the QR code and "
                                             'entered her UPI PIN. Within seconds, instead of receiving Rs. 15,000, '
                                             'Rs. 15,000 was DEBITED from her account. When she panicked, the caller '
                                             "claimed: 'Madam, it was a system glitch. I am sending a reverse QR code "
                                             'for Rs. 30,000 to refund your money plus the table price; enter your PIN '
                                             "quickly to reverse the transaction.'",
                                    'title': "OLX Furniture Sale Turned UPI QR-Code 'Refund' Scam"},
    'case_08_workplace_posh_retaliation': {   'category': 'Workplace & College Harassment',
                                              'difficulty': 'Basic',
                                              'educational_breakdown': {   'case_summary': 'Senior corporate executive '
                                                                                           'demanding sexual favours '
                                                                                           'in exchange for promotion, '
                                                                                           'followed by retaliatory '
                                                                                           'performance downgrades and '
                                                                                           'HR cover-up.',
                                                                           'common_misconceptions': "Myth: 'HR's job "
                                                                                                    'is to protect '
                                                                                                    "employees.' "
                                                                                                    'Reality: HR '
                                                                                                    'represents the '
                                                                                                    'employer '
                                                                                                    'corporation; the '
                                                                                                    'Internal '
                                                                                                    'Committee (IC) '
                                                                                                    'with an external '
                                                                                                    'NGO member is the '
                                                                                                    'statutory '
                                                                                                    'independent '
                                                                                                    'tribunal mandated '
                                                                                                    'by law.',
                                                                           'constitutional_analysis': 'Article 14 '
                                                                                                      '(Equality in '
                                                                                                      'workplace), '
                                                                                                      'Article '
                                                                                                      '19(1)(g) (Right '
                                                                                                      'to practice '
                                                                                                      'profession '
                                                                                                      'without sexual '
                                                                                                      'subordination), '
                                                                                                      'Article 21 '
                                                                                                      '(Dignity and '
                                                                                                      'safe work '
                                                                                                      'environment).',
                                                                           'court_precedents': 'Vishaka v. State of '
                                                                                               'Rajasthan (1997) SC - '
                                                                                               'Foundation of '
                                                                                               'workplace rights. '
                                                                                               'Aureliano Fernandes v. '
                                                                                               'State of Goa (2023) SC '
                                                                                               '- Supreme Court issued '
                                                                                               'nationwide directions '
                                                                                               'highlighting systemic '
                                                                                               'failures in POSH '
                                                                                               'implementation and '
                                                                                               'mandating strict '
                                                                                               'compliance.',
                                                                           'evidence_preservation_protocol': 'Travel '
                                                                                                             'hotel '
                                                                                                             'booking '
                                                                                                             'records, '
                                                                                                             'WhatsApp '
                                                                                                             '/ text '
                                                                                                             'messages, '
                                                                                                             'prior '
                                                                                                             'positive '
                                                                                                             'appraisal '
                                                                                                             'records '
                                                                                                             'to '
                                                                                                             'disprove '
                                                                                                             'sudden '
                                                                                                             'retaliatory '
                                                                                                             'poor '
                                                                                                             'reviews, '
                                                                                                             'email '
                                                                                                             'correspondence '
                                                                                                             'with HR.',
                                                                           'immediate_action_protocol': '1. Preserve '
                                                                                                        'contemporaneous '
                                                                                                        'notes, '
                                                                                                        'emails, '
                                                                                                        'travel '
                                                                                                        'itineraries, '
                                                                                                        'and Slack '
                                                                                                        'messages; 2. '
                                                                                                        'Submit formal '
                                                                                                        'written '
                                                                                                        'complaint to '
                                                                                                        'the Internal '
                                                                                                        'Committee '
                                                                                                        '(IC) within 3 '
                                                                                                        'months; 3. '
                                                                                                        'Apply for '
                                                                                                        'interim '
                                                                                                        'transfer / '
                                                                                                        'paid leave '
                                                                                                        'under Section '
                                                                                                        '12 POSH Act; '
                                                                                                        '4. Lodge dual '
                                                                                                        'complaint on '
                                                                                                        'SHe-Box '
                                                                                                        'portal.',
                                                                           'key_takeaways': [   'Quid Pro Quo '
                                                                                                'harassment is '
                                                                                                'strictly prohibited '
                                                                                                'under Section 3(2) '
                                                                                                'POSH Act.',
                                                                                                'Interim relief can '
                                                                                                'include up to 3 '
                                                                                                'months of additional '
                                                                                                'paid leave.',
                                                                                                'POSH inquiry and '
                                                                                                'police FIR can run '
                                                                                                'concurrently.'],
                                                                           'legal_classification': 'Statutory '
                                                                                                   'Violation of POSH '
                                                                                                   'Act, 2013 and '
                                                                                                   'Criminal Offence '
                                                                                                   'under Section 75 '
                                                                                                   'BNS.',
                                                                           'remedies_against_refusal': 'If IC acts '
                                                                                                       'with bias or '
                                                                                                       'company fails '
                                                                                                       'to act, appeal '
                                                                                                       'lies to the '
                                                                                                       'Industrial '
                                                                                                       'Tribunal / '
                                                                                                       'Labour Court '
                                                                                                       'under Section '
                                                                                                       '18 POSH Act, '
                                                                                                       'or via a Writ '
                                                                                                       'Petition '
                                                                                                       'before the '
                                                                                                       'High Court.',
                                                                           'reporting_forums': 'Company Internal '
                                                                                               'Committee (IC), '
                                                                                               'Ministry of WCD '
                                                                                               'SHe-Box '
                                                                                               '(shebox.wcd.gov.in), '
                                                                                               'Local Police Station '
                                                                                               '(FIR under S. 75 BNS), '
                                                                                               'Local Committee (LC) '
                                                                                               'at District Magistrate '
                                                                                               'office if company has '
                                                                                               '<10 employees.',
                                                                           'statutory_provisions': 'POSH Act 2013 '
                                                                                                   'Sections 3, 4, 9, '
                                                                                                   '11, 12, 13; BNS '
                                                                                                   'Section 75 (Sexual '
                                                                                                   'Harassment), '
                                                                                                   'Section 79 '
                                                                                                   '(Insulting '
                                                                                                   'modesty).',
                                                                           'victim_support_compensation': 'Compensation '
                                                                                                          'awarded by '
                                                                                                          'IC under '
                                                                                                          'Section '
                                                                                                          '13(3) POSH '
                                                                                                          'Act '
                                                                                                          'deducted '
                                                                                                          'from the '
                                                                                                          "perpetrator's "
                                                                                                          'salary, '
                                                                                                          'considering '
                                                                                                          'mental '
                                                                                                          'trauma, '
                                                                                                          'career '
                                                                                                          'loss, and '
                                                                                                          'medical '
                                                                                                          'expenses.'},
                                              'id': 'case_08_workplace_posh_retaliation',
                                              'questions': [   {   'correct_index': 1,
                                                                   'explanation': 'Section 3(2) of the POSH Act '
                                                                                  'specifically defines Quid Pro Quo '
                                                                                  'harassment: explicit or implicit '
                                                                                  'promise of preferential treatment, '
                                                                                  'or threat of detrimental treatment '
                                                                                  'in employment linked to sexual '
                                                                                  'demands.',
                                                                   'options': [   'Hostile work environment only',
                                                                                  'Quid Pro Quo Sexual Harassment '
                                                                                  '(promising career advancement in '
                                                                                  'exchange for sexual favours, with '
                                                                                  'adverse consequences upon refusal)',
                                                                                  'Casual corporate networking '
                                                                                  'misunderstanding',
                                                                                  'Breach of employment non-disclosure '
                                                                                  'agreement'],
                                                                   'question': 'What specific form of sexual '
                                                                               'harassment did Rajesh engage in under '
                                                                               'the POSH Act, 2013?'},
                                                               {   'correct_index': 1,
                                                                   'explanation': 'Section 4 of the POSH Act mandates '
                                                                                  'that every workplace with 10+ '
                                                                                  'employees must constitute an '
                                                                                  'Internal Committee (IC) with a '
                                                                                  'presiding woman officer and an '
                                                                                  'independent external member from an '
                                                                                  'NGO/legal background.',
                                                                   'options': [   'Corporate Disciplinary Guild',
                                                                                  'Internal Committee (IC), formerly '
                                                                                  'ICC, headed by a senior woman '
                                                                                  'employee and including an '
                                                                                  'independent external member',
                                                                                  "CEO's Grievance Bureau",
                                                                                  'Staff Welfare Club'],
                                                                   'question': 'What is the mandatory internal body '
                                                                               'every organization with 10 or more '
                                                                               'employees MUST establish under the '
                                                                               'POSH Act?'},
                                                               {   'correct_index': 1,
                                                                   'explanation': 'Section 12 of the POSH Act protects '
                                                                                  'the complainant during inquiry: the '
                                                                                  'IC can recommend transfer of either '
                                                                                  'party, or grant up to 3 months of '
                                                                                  'paid leave that is NOT deducted '
                                                                                  'from leave balance.',
                                                                   'options': [   'No, she must continue working '
                                                                                  'directly under the accused until '
                                                                                  'the trial ends',
                                                                                  'Yes. Under Section 12 of the POSH '
                                                                                  'Act, she can demand transfer of '
                                                                                  'herself or the respondent, or paid '
                                                                                  'leave up to 3 months (in addition '
                                                                                  'to normal leave)',
                                                                                  'Only if she pays half her salary '
                                                                                  'into escrow',
                                                                                  'Only if the accused gives written '
                                                                                  'consent'],
                                                                   'question': 'Can Divya request interim relief while '
                                                                               'the POSH inquiry is pending?'},
                                                               {   'correct_index': 1,
                                                                   'explanation': 'POSH proceedings and criminal '
                                                                                  'prosecution under Section 75 BNS '
                                                                                  'are concurrent remedies. Divya has '
                                                                                  'the full legal right to initiate '
                                                                                  'both simultaneously.',
                                                                   'options': [   'Yes, an employee cannot pursue both '
                                                                                  'corporate and criminal remedies '
                                                                                  'simultaneously',
                                                                                  'No. Under Section 9 and Section 28 '
                                                                                  'of the POSH Act, the administrative '
                                                                                  'inquiry is in addition to, and not '
                                                                                  'in derogation of, the right to file '
                                                                                  'an FIR under Section 75 BNS',
                                                                                  'Only if the company IC gives '
                                                                                  'permission in writing',
                                                                                  'Only after she resigns from the '
                                                                                  'company'],
                                                                   'question': 'Does filing a complaint before the '
                                                                               'Internal Committee bar Divya from '
                                                                               'lodging a police FIR under criminal '
                                                                               'law?'},
                                                               {   'correct_index': 0,
                                                                   'explanation': 'SHe-Box (shebox.wcd.gov.in) is the '
                                                                                  'centralized portal launched by the '
                                                                                  'Ministry of Women and Child '
                                                                                  'Development to directly receive and '
                                                                                  'monitor workplace sexual harassment '
                                                                                  'complaints.',
                                                                   'options': [   'Ministry of WCD SHe-Box (Sexual '
                                                                                  'Harassment Electronic Box) at '
                                                                                  'shebox.wcd.gov.in',
                                                                                  'Corporate Affairs Registrar only',
                                                                                  'SEBI SCORES portal',
                                                                                  'Municipal Corporation health desk'],
                                                                   'question': 'If the company fails to constitute an '
                                                                               "IC or suppresses Divya's complaint, "
                                                                               'what central government portal can she '
                                                                               'approach?'}],
                                              'story': 'Divya, a senior product manager at a multinational tech firm '
                                                       'in Bengaluru, was summoned to dinner during an official '
                                                       "business trip by the company's Executive Vice President, "
                                                       "Rajesh. At dinner, Rajesh touched Divya's hand "
                                                       "inappropriately, suggested that they 'spend the night together "
                                                       "in his suite', and stated: 'Your upcoming promotion to "
                                                       "Director is in my hands; be smart and make me happy.' Divya "
                                                       'firmly pulled away, refused his advances, and returned to her '
                                                       'room. Over the next two weeks, Rajesh removed Divya from '
                                                       'high-profile client projects, issued a negative quarterly '
                                                       'performance review rating, and whispered to HR that Divya was '
                                                       "'disruptive and not a team player.' When Divya approached the "
                                                       "HR Director, she was told: 'Rajesh brings in 40% of the firm's "
                                                       "revenue. Think about your career before making a fuss.'",
                                              'title': 'Quid Pro Quo Sexual Harassment by Vice President & Threatened '
                                                       'Appraisals'},
    'case_09_caste_atrocity_temple_entry': {   'category': 'Discrimination & Human Rights',
                                               'difficulty': 'Advanced',
                                               'educational_breakdown': {   'case_summary': 'Assault, casteist '
                                                                                            'humiliation, denial of '
                                                                                            'temple entry, and social '
                                                                                            'boycott imposed on a '
                                                                                            'Scheduled Caste youth and '
                                                                                            'family.',
                                                                            'common_misconceptions': "Myth: 'Temples "
                                                                                                     'are private, '
                                                                                                     'owners can bar '
                                                                                                     'anyone based on '
                                                                                                     "caste.' Reality: "
                                                                                                     'Places of public '
                                                                                                     'worship are open '
                                                                                                     'to all citizens '
                                                                                                     'under Article '
                                                                                                     '15(2) and '
                                                                                                     'Section 3 of the '
                                                                                                     'Protection of '
                                                                                                     'Civil Rights '
                                                                                                     'Act; caste '
                                                                                                     'exclusion is a '
                                                                                                     'non-bailable '
                                                                                                     'crime.',
                                                                            'constitutional_analysis': 'Article 17 '
                                                                                                       '(Abolition of '
                                                                                                       'Untouchability), '
                                                                                                       'Article 15(2) '
                                                                                                       '(No '
                                                                                                       'restriction '
                                                                                                       'regarding '
                                                                                                       'access to '
                                                                                                       'public '
                                                                                                       'places/temples), '
                                                                                                       'Article 21 '
                                                                                                       '(Dignity and '
                                                                                                       'life).',
                                                                            'court_precedents': 'Prathvi Raj Chauhan '
                                                                                                'v. Union of India '
                                                                                                '(2020) SC - Upheld '
                                                                                                'constitutional '
                                                                                                'validity of Section '
                                                                                                '18A barring '
                                                                                                'anticipatory bail and '
                                                                                                'preliminary inquiry. '
                                                                                                'Swaran Singh v. State '
                                                                                                '(2008) SC - Calling '
                                                                                                'caste names in public '
                                                                                                'view is a serious '
                                                                                                'atrocity.',
                                                                            'evidence_preservation_protocol': 'Valid '
                                                                                                              'SC/ST '
                                                                                                              'caste '
                                                                                                              'certificate, '
                                                                                                              'Medico-Legal '
                                                                                                              'Certificate '
                                                                                                              '(MLC) '
                                                                                                              'of '
                                                                                                              'physical '
                                                                                                              'assault, '
                                                                                                              'audio/video '
                                                                                                              'recordings '
                                                                                                              'of '
                                                                                                              'caste '
                                                                                                              'slurs '
                                                                                                              'or '
                                                                                                              'Panchayat '
                                                                                                              'boycott '
                                                                                                              'resolution, '
                                                                                                              'names '
                                                                                                              'of '
                                                                                                              'eyewitnesses.',
                                                                            'immediate_action_protocol': '1. Ensure '
                                                                                                         'personal '
                                                                                                         'physical '
                                                                                                         'safety and '
                                                                                                         'secure '
                                                                                                         'medical '
                                                                                                         'treatment / '
                                                                                                         'MLC for '
                                                                                                         'assault '
                                                                                                         'wounds; 2. '
                                                                                                         'Lodge '
                                                                                                         'written FIR '
                                                                                                         'under SC/ST '
                                                                                                         '(PoA) Act at '
                                                                                                         'jurisdictional '
                                                                                                         'thana; 3. '
                                                                                                         'Demand '
                                                                                                         'DSP-level '
                                                                                                         'investigation; '
                                                                                                         '4. Petition '
                                                                                                         'District '
                                                                                                         'Collector '
                                                                                                         'for '
                                                                                                         'emergency '
                                                                                                         'protection '
                                                                                                         'against '
                                                                                                         'social '
                                                                                                         'boycott and '
                                                                                                         'Rule 12 cash '
                                                                                                         'relief.',
                                                                            'key_takeaways': [   'Article 17 directly '
                                                                                                 'abolishes '
                                                                                                 'untouchability and '
                                                                                                 'makes its '
                                                                                                 'enforcement a crime.',
                                                                                                 'Anticipatory bail is '
                                                                                                 'barred under Section '
                                                                                                 '18A of the SC/ST '
                                                                                                 'Act.',
                                                                                                 'Mandatory '
                                                                                                 'compensation is paid '
                                                                                                 'within 7 days of FIR '
                                                                                                 'registration.'],
                                                                            'legal_classification': 'Aggravated '
                                                                                                    'Non-Bailable '
                                                                                                    'Criminal Offence '
                                                                                                    'under Special '
                                                                                                    'Penal Statute '
                                                                                                    '(SC/ST PoA Act) & '
                                                                                                    'Constitutional '
                                                                                                    'Violation.',
                                                                            'remedies_against_refusal': 'Section 4 of '
                                                                                                        'the SC/ST Act '
                                                                                                        'penalizes '
                                                                                                        'public '
                                                                                                        'servants who '
                                                                                                        'neglect their '
                                                                                                        'duties with '
                                                                                                        'imprisonment '
                                                                                                        'up to 1 year. '
                                                                                                        'Approach the '
                                                                                                        'Special Court '
                                                                                                        'under the '
                                                                                                        'SC/ST Act '
                                                                                                        'directly.',
                                                                            'reporting_forums': 'Jurisdictional Police '
                                                                                                'Station / Special '
                                                                                                'SC/ST Cell, National '
                                                                                                'Commission for '
                                                                                                'Scheduled Castes '
                                                                                                '(NCSC at '
                                                                                                'ncsc.nic.in), '
                                                                                                'District Magistrate '
                                                                                                '(Collector).',
                                                                            'statutory_provisions': 'SC/ST (PoA) Act '
                                                                                                    '1989 Sections '
                                                                                                    '3(1)(r), 3(1)(s), '
                                                                                                    '3(1)(z), '
                                                                                                    '3(1)(za), Section '
                                                                                                    '18A; Protection '
                                                                                                    'of Civil Rights '
                                                                                                    'Act 1955 Sections '
                                                                                                    '3-7; BNS Section '
                                                                                                    '115, 189.',
                                                                            'victim_support_compensation': 'Mandatory '
                                                                                                           'financial '
                                                                                                           'relief '
                                                                                                           'package '
                                                                                                           'under Rule '
                                                                                                           '12 SC/ST '
                                                                                                           'PoA Rules '
                                                                                                           '(Rs. '
                                                                                                           '1,00,000 '
                                                                                                           'to Rs. '
                                                                                                           '8,25,000), '
                                                                                                           'free '
                                                                                                           'ration, '
                                                                                                           'and police '
                                                                                                           'security '
                                                                                                           'escort.'},
                                               'id': 'case_09_caste_atrocity_temple_entry',
                                               'questions': [   {   'correct_index': 0,
                                                                    'explanation': 'Article 17 is absolute and '
                                                                                   "self-executing: 'Untouchability' "
                                                                                   'is abolished and its practice in '
                                                                                   'any form is forbidden. The '
                                                                                   'enforcement of any disability '
                                                                                   "arising out of 'Untouchability' is "
                                                                                   'an offence punishable in '
                                                                                   'accordance with law.',
                                                                    'options': [   'Article 17 of the Constitution of '
                                                                                   'India',
                                                                                   'Article 19(1)(a)',
                                                                                   'Article 356',
                                                                                   'Article 280'],
                                                                    'question': 'Which fundamental constitutional '
                                                                                'article explicitly abolishes '
                                                                                "'Untouchability' and forbids its "
                                                                                'practice in any form?'},
                                                                {   'correct_index': 1,
                                                                    'explanation': 'Section 3 of the SC/ST (PoA) Act '
                                                                                   'specifically criminalizes '
                                                                                   'preventing access to places of '
                                                                                   'public worship, casteist '
                                                                                   'humiliation in public view, '
                                                                                   'assault, and imposing social or '
                                                                                   'economic boycotts.',
                                                                    'options': [   'Only a minor breach of public '
                                                                                   'tranquility',
                                                                                   'Offences of atrocities under '
                                                                                   'Section 3(1)(r) (intentional '
                                                                                   'insult/humiliation in public '
                                                                                   'view), Section 3(1)(za) '
                                                                                   '(preventing entry to public place '
                                                                                   'of worship), and Section 3(1)(z) '
                                                                                   '(social boycott)',
                                                                                   'Breach of private property '
                                                                                   'easements',
                                                                                   'Defamation under civil torts'],
                                                                    'question': 'Under the Scheduled Castes and '
                                                                                'Scheduled Tribes (Prevention of '
                                                                                'Atrocities) Act, 1989, what offences '
                                                                                'were committed by the aggressors?'},
                                                                {   'correct_index': 1,
                                                                    'explanation': 'Parliament enacted Section 18A to '
                                                                                   'explicitly bar anticipatory bail, '
                                                                                   'affirmed by the Supreme Court in '
                                                                                   'Prathvi Raj Chauhan v. Union of '
                                                                                   'India (2020).',
                                                                    'options': [   'Yes, anticipatory bail is '
                                                                                   'automatically granted in all '
                                                                                   'bailable and non-bailable matters',
                                                                                   'No. Section 18 and 18A of the '
                                                                                   'SC/ST (PoA) Act expressly bar '
                                                                                   'anticipatory bail under Section '
                                                                                   '438 CrPC (now S. 482 BNSS) where a '
                                                                                   'prima facie offence is established',
                                                                                   'Only if the village panchayat '
                                                                                   'recommends bail',
                                                                                   'Only if they deposit Rs. 50,000 in '
                                                                                   'court'],
                                                                    'question': 'Can the accused persons obtain '
                                                                                'anticipatory bail under normal '
                                                                                'circumstances for offences under the '
                                                                                'SC/ST (PoA) Act?'},
                                                                {   'correct_index': 1,
                                                                    'explanation': 'Rule 7 of the SC/ST (PoA) Rules, '
                                                                                   '1995 mandates that investigation '
                                                                                   'must be conducted by an officer '
                                                                                   'not below the rank of Deputy '
                                                                                   'Superintendent of Police (DSP).',
                                                                    'options': [   'A junior constable on patrol duty',
                                                                                   'An officer not below the rank of '
                                                                                   'Deputy Superintendent of Police '
                                                                                   '(DSP) / Assistant Commissioner of '
                                                                                   'Police (ACP) under Rule 7',
                                                                                   'A private security officer',
                                                                                   'The local revenue patwari'],
                                                                    'question': 'What mandatory rank of police officer '
                                                                                'must investigate an offence '
                                                                                'registered under the SC/ST (PoA) '
                                                                                'Act?'},
                                                                {   'correct_index': 1,
                                                                    'explanation': 'Rule 12 of the SC/ST (PoA) Rules '
                                                                                   'guarantees mandatory interim '
                                                                                   'relief and rehabilitation '
                                                                                   'disbursed by the District '
                                                                                   'Magistrate/Collector within 7 days '
                                                                                   'of the FIR, independent of '
                                                                                   'conviction.',
                                                                    'options': [   'No, compensation is only paid 10 '
                                                                                   'years later if the accused are '
                                                                                   'convicted',
                                                                                   'Yes. Under Rule 12 of the SC/ST '
                                                                                   '(PoA) Rules, the District '
                                                                                   'Administration must disburse '
                                                                                   'statutory cash relief (ranging '
                                                                                   'from Rs. 85,000 to Rs. 8,25,000 '
                                                                                   'depending on nature) within 7 days '
                                                                                   'of FIR registration',
                                                                                   'Only if they sign a compromise '
                                                                                   'deed',
                                                                                   'Only if they agree to leave the '
                                                                                   'village'],
                                                                    'question': 'Are Sunil and his family entitled to '
                                                                                'immediate government financial relief '
                                                                                'and compensation upon registration of '
                                                                                'the FIR?'}],
                                               'story': 'Sunil, a 22-year-old college student belonging to the '
                                                        'Scheduled Caste (Meghwal) community in a Rajasthan village, '
                                                        'went to offer prayers at the village temple on Diwali. A '
                                                        'group of dominant-caste men blocked his entry, hurled '
                                                        'casteist slurs in front of gathering villagers, forcibly beat '
                                                        "him with wooden sticks, and tore his clothes, shouting: 'How "
                                                        "dare an untouchable step onto our temple steps!' When Sunil's "
                                                        'father complained to the village council (Panchayat), the '
                                                        "dominant elders decreed a 'Social Boycott' (hukka-pani band) "
                                                        "against Sunil's family: village shopkeepers were forbidden "
                                                        'from selling them groceries, and their access to the shared '
                                                        'community water well was blocked.',
                                               'title': 'Casteist Abuse, Social Boycott, and Assault for Entering '
                                                        'Public Village Temple'},
    'case_10_midnight_tenant_lockout': {   'category': 'Property & Tenancy Disputes',
                                           'difficulty': 'Basic',
                                           'educational_breakdown': {   'case_summary': 'Landlord using bouncers, '
                                                                                        'utility severance, and '
                                                                                        'illegal physical lock-in to '
                                                                                        'forcibly evict a tenant '
                                                                                        'during an active registered '
                                                                                        'lease.',
                                                                        'common_misconceptions': "Myth: 'The landlord "
                                                                                                 'owns the house, so '
                                                                                                 'he can throw my '
                                                                                                 'things out whenever '
                                                                                                 "he wants.' Reality: "
                                                                                                 'Lawful possession is '
                                                                                                 'legally protected; '
                                                                                                 'landlords who engage '
                                                                                                 'in forcible '
                                                                                                 'self-help eviction '
                                                                                                 'face criminal '
                                                                                                 'imprisonment and '
                                                                                                 'heavy damages.',
                                                                        'constitutional_analysis': 'Article 21 (Right '
                                                                                                   'to shelter, '
                                                                                                   'personal liberty, '
                                                                                                   'and essential '
                                                                                                   'utilities like '
                                                                                                   'water and '
                                                                                                   'electricity).',
                                                                        'court_precedents': 'Bishan Das v. State of '
                                                                                            'Punjab & Midnapore '
                                                                                            'Zamindary Co. - No person '
                                                                                            'can be dispossessed '
                                                                                            'without due process of '
                                                                                            'law, even by the rightful '
                                                                                            'owner. State cannot '
                                                                                            'tolerate private violence '
                                                                                            'in possession disputes.',
                                                                        'evidence_preservation_protocol': 'Registered '
                                                                                                          'Tenancy '
                                                                                                          'Agreement, '
                                                                                                          'monthly '
                                                                                                          'rent '
                                                                                                          'payment '
                                                                                                          'bank '
                                                                                                          'receipts / '
                                                                                                          'UPI '
                                                                                                          'statements, '
                                                                                                          'video '
                                                                                                          'footage of '
                                                                                                          'padlocks '
                                                                                                          'and '
                                                                                                          'disconnected '
                                                                                                          'wires, '
                                                                                                          'WhatsApp '
                                                                                                          'threat '
                                                                                                          'messages '
                                                                                                          'from '
                                                                                                          'landlord.',
                                                                        'immediate_action_protocol': '1. Call 112 '
                                                                                                     'immediately for '
                                                                                                     'police '
                                                                                                     'intervention to '
                                                                                                     'open locks; 2. '
                                                                                                     'Video record the '
                                                                                                     'disconnected '
                                                                                                     'meters and '
                                                                                                     'locks; 3. File '
                                                                                                     'urgent petition '
                                                                                                     'before Rent '
                                                                                                     'Controller for '
                                                                                                     'restoration of '
                                                                                                     'utilities; 4. '
                                                                                                     'Obtain temporary '
                                                                                                     'injunction under '
                                                                                                     'Order 39 CPC.',
                                                                        'key_takeaways': [   'Cutting off water or '
                                                                                             'electricity to a tenant '
                                                                                             'is strictly illegal '
                                                                                             'under rent laws.',
                                                                                             'Padlocking doors from '
                                                                                             'outside is criminal '
                                                                                             'wrongful confinement '
                                                                                             'under Section 127 BNS.',
                                                                                             'Eviction can only occur '
                                                                                             'through formal court '
                                                                                             'decree.'],
                                                                        'legal_classification': 'Dual: Criminal '
                                                                                                'Offence (Wrongful '
                                                                                                'Confinement & '
                                                                                                'Intimidation) and '
                                                                                                'Civil Tenancy Breach.',
                                                                        'remedies_against_refusal': 'If police dismiss '
                                                                                                    "it as 'purely "
                                                                                                    "civil dispute', "
                                                                                                    'insist that '
                                                                                                    'wrongful '
                                                                                                    'confinement (S. '
                                                                                                    '127 BNS) is a '
                                                                                                    'cognizable '
                                                                                                    'criminal offence. '
                                                                                                    'Submit written '
                                                                                                    'representation to '
                                                                                                    'SP under Section '
                                                                                                    '173(4) BNSS.',
                                                                        'reporting_forums': 'Police Control Room (Dial '
                                                                                            '112) / Local Thana, '
                                                                                            'District Rent Authority / '
                                                                                            'Rent Court, Junior Civil '
                                                                                            'Judge Court (Injunction '
                                                                                            'Suit).',
                                                                        'statutory_provisions': 'BNS Section 126 '
                                                                                                '(Wrongful Restraint), '
                                                                                                'Section 127 (Wrongful '
                                                                                                'Confinement), Section '
                                                                                                '351 (Criminal '
                                                                                                'Intimidation), State '
                                                                                                'Rent Control Acts, '
                                                                                                'CPC Order 39 Rules 1 '
                                                                                                '& 2.',
                                                                        'victim_support_compensation': 'Restoration of '
                                                                                                       'utilities with '
                                                                                                       'statutory '
                                                                                                       'penalties on '
                                                                                                       'landlord and '
                                                                                                       'civil damages '
                                                                                                       'for emotional '
                                                                                                       'distress and '
                                                                                                       'wrongful '
                                                                                                       'confinement.'},
                                           'id': 'case_10_midnight_tenant_lockout',
                                           'questions': [   {   'correct_index': 1,
                                                                'explanation': 'Every state rent control law and the '
                                                                               'Model Tenancy Act strictly prohibit '
                                                                               'landlords from severing essential '
                                                                               'supplies (water, electricity). Rent '
                                                                               'Authorities can impose heavy fines and '
                                                                               'order immediate reconnection.',
                                                                'options': [   'Yes, landlords own the property and '
                                                                               'can disconnect utilities at will',
                                                                               'No. Under Rent Control Acts and Model '
                                                                               'Tenancy law, landlords are STRICTLY '
                                                                               'FORBIDDEN from cutting off essential '
                                                                               'services; doing so carries heavy '
                                                                               'statutory penalties and immediate '
                                                                               'restoration orders',
                                                                               'Only if the tenant is more than 3 days '
                                                                               'late on rent',
                                                                               'Only between 9 AM and 5 PM'],
                                                                'question': 'Can a landlord legally cut off essential '
                                                                            'services like electricity and water to '
                                                                            'force a tenant to vacate?'},
                                                            {   'correct_index': 0,
                                                                'explanation': 'Restraining a person from proceeding '
                                                                               'beyond certain circumscribing limits '
                                                                               'is Wrongful Confinement (Section 127 '
                                                                               'BNS), punishable with imprisonment up '
                                                                               'to one year and fine.',
                                                                'options': [   'Wrongful Confinement under Section 127 '
                                                                               'BNS (replaces IPC 342) and Criminal '
                                                                               'Intimidation under Section 351 BNS',
                                                                               'Simple civil contract renegotiation',
                                                                               'Permissible landlord self-help remedy',
                                                                               'Noise pollution violation only'],
                                                                'question': 'What criminal offence did the landlord '
                                                                            'commit by padlocking the grill and '
                                                                            'trapping the family inside?'},
                                                            {   'correct_index': 1,
                                                                'explanation': 'The Supreme Court in Bishan Das and '
                                                                               'subsequent landmark judgments ruled '
                                                                               'that even a trespasser in settled '
                                                                               'possession cannot be dispossessed '
                                                                               'except by due process of law. Forcible '
                                                                               'extra-judicial eviction is illegal.',
                                                                'options': [   'Hiring private muscle or bouncers to '
                                                                               'throw luggage out',
                                                                               'Only by due process of law: serving a '
                                                                               'formal legal notice and obtaining an '
                                                                               'eviction decree from a competent Rent '
                                                                               'Court / Civil Court',
                                                                               'Publishing an eviction notice in the '
                                                                               'local newspaper',
                                                                               'Locking the entrance door while the '
                                                                               'tenant is outside'],
                                                                'question': 'What is the established legal process for '
                                                                            'evicting a tenant in lawful possession in '
                                                                            'India?'},
                                                            {   'correct_index': 0,
                                                                'explanation': 'An urgent application for temporary '
                                                                               'injunction under Order 39 Rules 1 & 2 '
                                                                               'CPC restrains the landlord from '
                                                                               'disturbing peaceful possession or '
                                                                               'executing forcible eviction without '
                                                                               'court decree.',
                                                                'options': [   'A suit for permanent injunction and an '
                                                                               'urgent ex-parte temporary injunction '
                                                                               'under Order 39 Rules 1 & 2 CPC',
                                                                               'A criminal writ in the Supreme Court '
                                                                               'under Article 32 directly',
                                                                               'An insolvency petition',
                                                                               'A complaint to the Ministry of '
                                                                               'Corporate Affairs'],
                                                                'question': 'What immediate civil court remedy can '
                                                                            'Kiran file to prevent the landlord from '
                                                                            'forcibly evicting them?'},
                                                            {   'correct_index': 0,
                                                                'explanation': 'Dialing 112 brings immediate police '
                                                                               'response to remove the illegal padlock '
                                                                               'and record a complaint of wrongful '
                                                                               'confinement.',
                                                                'options': [   'Call 112 immediately to report '
                                                                               'wrongful confinement and intimidation '
                                                                               'in progress',
                                                                               'Sign whatever document the bouncers '
                                                                               'demand',
                                                                               'Jump out of the balcony window',
                                                                               'Wait 5 days for the lease agreement to '
                                                                               'be scrutinized'],
                                                                'question': 'What emergency action should Kiran take '
                                                                            'while locked inside right now?'}],
                                           'story': 'Kiran, an engineer renting a 2-BHK apartment in Hyderabad with '
                                                    'his pregnant wife, had a disagreement with his landlord, Reddy, '
                                                    'over an unreasonable 35% mid-lease rent hike. The registered '
                                                    '11-month lease agreement was valid for another 5 months. Last '
                                                    'night at 11:30 PM, while Kiran and his wife were sleeping, Reddy '
                                                    'arrived with three bouncers, severed the electricity and '
                                                    'municipal water connections, padlocked the main iron safety grill '
                                                    "from the outside, and shouted: 'Vacate tomorrow morning or I will "
                                                    "throw your wife and luggage onto the street!'",
                                           'title': 'Midnight Lockout, Power Disconnection, and Forcible Eviction by '
                                                    'Landlord'},
    'case_11_hit_and_run_good_samaritan': {   'category': 'Road Incidents & Transport',
                                              'difficulty': 'Intermediate',
                                              'educational_breakdown': {   'case_summary': 'Highway hit-and-run with '
                                                                                           'grievous injuries, '
                                                                                           'bystander providing '
                                                                                           'lifesaving Good Samaritan '
                                                                                           'assistance, met with '
                                                                                           'illegal hospital '
                                                                                           'hesitation.',
                                                                           'common_misconceptions': "Myth: 'If you "
                                                                                                    'take an accident '
                                                                                                    'victim to the '
                                                                                                    'hospital, police '
                                                                                                    'will harass you '
                                                                                                    'and make you pay '
                                                                                                    "bills.' Reality: "
                                                                                                    'Under Section '
                                                                                                    '134A MV Act, Good '
                                                                                                    'Samaritans have '
                                                                                                    'total legal '
                                                                                                    'immunity and '
                                                                                                    'cannot be forced '
                                                                                                    'to pay or stay.',
                                                                           'constitutional_analysis': 'Article 21 '
                                                                                                      '(Right to life '
                                                                                                      'and immediate '
                                                                                                      'emergency '
                                                                                                      'trauma care as '
                                                                                                      'ruled in '
                                                                                                      'Parmanand '
                                                                                                      'Katara and '
                                                                                                      'Paschim Banga '
                                                                                                      'Khet Mazdoor '
                                                                                                      'Samity).',
                                                                           'court_precedents': 'Pt. Parmanand Katara '
                                                                                               'v. Union of India '
                                                                                               '(1989) SC - Mandatory '
                                                                                               'emergency medical care '
                                                                                               'without waiting for '
                                                                                               'police. SaveLIFE '
                                                                                               'Foundation v. Union of '
                                                                                               'India (2016) SC - '
                                                                                               'Comprehensive Good '
                                                                                               'Samaritan guidelines '
                                                                                               'codified into Section '
                                                                                               '134A MV Act.',
                                                                           'evidence_preservation_protocol': 'Hospital '
                                                                                                             'Medico-Legal '
                                                                                                             'Case '
                                                                                                             '(MLC) '
                                                                                                             'report, '
                                                                                                             'photos '
                                                                                                             'of '
                                                                                                             'accident '
                                                                                                             'spot / '
                                                                                                             'vehicle '
                                                                                                             'skid '
                                                                                                             'marks, '
                                                                                                             'traffic '
                                                                                                             'signal '
                                                                                                             'CCTV '
                                                                                                             'footage, '
                                                                                                             'vehicle '
                                                                                                             'registration '
                                                                                                             'notes '
                                                                                                             'from '
                                                                                                             'witnesses.',
                                                                           'immediate_action_protocol': '1. Call 108 / '
                                                                                                        '112 for '
                                                                                                        'emergency '
                                                                                                        'trauma '
                                                                                                        'ambulance; 2. '
                                                                                                        'Hospital must '
                                                                                                        'admit '
                                                                                                        'immediately '
                                                                                                        'under '
                                                                                                        'Parmanand '
                                                                                                        'Katara '
                                                                                                        'protocol; 3. '
                                                                                                        'Good '
                                                                                                        'Samaritan can '
                                                                                                        'leave '
                                                                                                        'immediately '
                                                                                                        'after '
                                                                                                        'admitting '
                                                                                                        'patient; 4. '
                                                                                                        'Police must '
                                                                                                        'lodge FIR '
                                                                                                        'under S. '
                                                                                                        '281/125 BNS.',
                                                                           'key_takeaways': [   'Emergency medical '
                                                                                                'treatment is a '
                                                                                                'non-negotiable '
                                                                                                'constitutional right '
                                                                                                'under Article 21.',
                                                                                                'Good Samaritans have '
                                                                                                'total statutory '
                                                                                                'immunity under '
                                                                                                'Section 134A MV Act.',
                                                                                                'Hit-and-run drivers '
                                                                                                'face up to 10 years '
                                                                                                'imprisonment under '
                                                                                                'Section 106(2) BNS.'],
                                                                           'legal_classification': 'Criminal Offence '
                                                                                                   '(Rash Driving & '
                                                                                                   'Hit-and-Run) and '
                                                                                                   'Special Statutory '
                                                                                                   'Tribunal Claim '
                                                                                                   '(Motor Vehicles '
                                                                                                   'Act).',
                                                                           'remedies_against_refusal': 'If a hospital '
                                                                                                       'refuses '
                                                                                                       'emergency '
                                                                                                       'trauma '
                                                                                                       'treatment, '
                                                                                                       'complain '
                                                                                                       'immediately to '
                                                                                                       'the State '
                                                                                                       'Health '
                                                                                                       'Department and '
                                                                                                       'District '
                                                                                                       'Magistrate; '
                                                                                                       'hospitals risk '
                                                                                                       'cancellation '
                                                                                                       'of clinical '
                                                                                                       'establishment '
                                                                                                       'registration.',
                                                                           'reporting_forums': 'Local Police Station '
                                                                                               '(FIR and Accident '
                                                                                               'Information Report - '
                                                                                               'AIR), Motor Accident '
                                                                                               'Claims Tribunal '
                                                                                               '(MACT), District Legal '
                                                                                               'Services Authority '
                                                                                               '(DLSA).',
                                                                           'statutory_provisions': 'BNS Section 281 '
                                                                                                   '(Rash driving), '
                                                                                                   'Section 125 '
                                                                                                   '(Endangering '
                                                                                                   'life), Section '
                                                                                                   '106(2) (Hit and '
                                                                                                   'run causing '
                                                                                                   'death); Motor '
                                                                                                   'Vehicles Act '
                                                                                                   'Section 134A (Good '
                                                                                                   'Samaritan '
                                                                                                   'Protection), '
                                                                                                   'Section 161 '
                                                                                                   '(Solatium Fund), '
                                                                                                   'Section 166 '
                                                                                                   '(MACT).',
                                                                           'victim_support_compensation': 'Third-party '
                                                                                                          'motor '
                                                                                                          'insurance '
                                                                                                          'claim via '
                                                                                                          'MACT, or '
                                                                                                          'Solatium '
                                                                                                          'Fund for '
                                                                                                          'hit-and-run '
                                                                                                          'cases, plus '
                                                                                                          'interim '
                                                                                                          'medical '
                                                                                                          'relief.'},
                                              'id': 'case_11_hit_and_run_good_samaritan',
                                              'questions': [   {   'correct_index': 1,
                                                                   'explanation': 'The landmark Supreme Court ruling '
                                                                                  'in Pt. Parmanand Katara (1989) '
                                                                                  'established that preservation of '
                                                                                  'human life takes precedence over '
                                                                                  'legal and administrative '
                                                                                  'formalities; all hospitals must '
                                                                                  'treat emergency victims '
                                                                                  'immediately.',
                                                                   'options': [   'Yes, private hospitals are '
                                                                                  'commercial entities with no duty to '
                                                                                  'provide free emergency care',
                                                                                  'No. In Parmanand Katara v. Union of '
                                                                                  'India, the Supreme Court ruled that '
                                                                                  'EVERY doctor and hospital has an '
                                                                                  'absolute professional and '
                                                                                  'constitutional obligation to '
                                                                                  'provide immediate emergency medical '
                                                                                  'treatment without waiting for '
                                                                                  'police clearance',
                                                                                  'Only if the patient is a senior '
                                                                                  'citizen',
                                                                                  'Only if the accident occurred '
                                                                                  'within 500 meters of the hospital'],
                                                                   'question': 'Can a private or government hospital '
                                                                               'legally refuse emergency medical '
                                                                               'treatment to an accident victim '
                                                                               'pending police clearance or financial '
                                                                               'deposit?'},
                                                               {   'correct_index': 1,
                                                                   'explanation': 'Section 134A of the Motor Vehicles '
                                                                                  'Act provides complete civil and '
                                                                                  'criminal immunity to Good '
                                                                                  'Samaritans. Hospitals and police '
                                                                                  'cannot harass, detain, or force '
                                                                                  'them to disclose identity or bear '
                                                                                  'expenses.',
                                                                   'options': [   'None, he is legally responsible for '
                                                                                  "paying the patient's bills",
                                                                                  'Under Section 134A of the Motor '
                                                                                  'Vehicles Act (amended 2019) and '
                                                                                  'Supreme Court guidelines, Good '
                                                                                  'Samaritans cannot be detained at '
                                                                                  'the hospital, forced to disclose '
                                                                                  'personal identity, or compelled to '
                                                                                  'become witnesses',
                                                                                  'He must be placed in civil custody '
                                                                                  'until police verify he was not the '
                                                                                  'driver',
                                                                                  'He must surrender his driving '
                                                                                  'license'],
                                                                   'question': 'What legal protections exist for Vikas '
                                                                               "as a 'Good Samaritan' who helped the "
                                                                               'accident victim?'},
                                                               {   'correct_index': 1,
                                                                   'explanation': 'Section 106(2) BNS specifically '
                                                                                  'provides severe punishment of '
                                                                                  'imprisonment up to 10 years and '
                                                                                  'fine for motorists who cause death '
                                                                                  'by rash or negligent driving and '
                                                                                  'escape without reporting to police.',
                                                                   'options': [   'Simple fine of Rs. 500',
                                                                                  'Imprisonment up to 10 years and '
                                                                                  'fine under Section 106(2) BNS',
                                                                                  'Mandatory 24 hours of traffic '
                                                                                  'community service',
                                                                                  'Suspension of vehicle pollution '
                                                                                  'certificate'],
                                                                   'question': 'What is the newly codified criminal '
                                                                               'punishment under Bharatiya Nyaya '
                                                                               'Sanhita (BNS) for drivers who cause '
                                                                               'fatal accidents by rash driving and '
                                                                               'flee without reporting?'},
                                                               {   'correct_index': 0,
                                                                   'explanation': 'The Motor Accident Claims Tribunal '
                                                                                  '(MACT) is the specialized statutory '
                                                                                  'tribunal established under the '
                                                                                  'Motor Vehicles Act to adjudicate '
                                                                                  'and award third-party compensation '
                                                                                  'to accident victims.',
                                                                   'options': [   'Motor Accident Claims Tribunal '
                                                                                  '(MACT) under the Motor Vehicles '
                                                                                  'Act, 1988',
                                                                                  'Municipal Sanitation Board',
                                                                                  'Telecom Disputes Tribunal (TDSAT)',
                                                                                  'National Green Tribunal'],
                                                                   'question': "Where can the injured motorcyclist's "
                                                                               'family claim financial compensation '
                                                                               'for medical expenses and permanent '
                                                                               'disability?'},
                                                               {   'correct_index': 0,
                                                                   'explanation': 'Section 161 of the Motor Vehicles '
                                                                                  'Act provides statutory compensation '
                                                                                  '(Rs. 2 Lakhs for death, Rs. 50,000 '
                                                                                  'for grievous hurt) under the '
                                                                                  'Solatium Fund for hit-and-run '
                                                                                  'victims where the vehicle cannot be '
                                                                                  'identified.',
                                                                   'options': [   'Hit and Run Compensation Scheme '
                                                                                  '(Solatium Fund) under Section 161 '
                                                                                  'of the Motor Vehicles Act',
                                                                                  'Central Excise Rebate Fund',
                                                                                  'GST Refund Scheme',
                                                                                  'Corporate CSR pool'],
                                                                   'question': 'What government fund provides '
                                                                               'immediate statutory compensation in '
                                                                               'hit-and-run accidents where the '
                                                                               'offending vehicle is untraceable?'}],
                                              'story': 'While driving home along an arterial road at 10 PM, Vikas '
                                                       'witnessed a speeding SUV run a red light, violently smash into '
                                                       'a motorcyclist, and speed away into the night without '
                                                       'stopping. The motorcyclist was thrown onto the asphalt, '
                                                       'bleeding profusely with an open leg fracture and loss of '
                                                       'consciousness. Vikas immediately stopped his car, placed the '
                                                       'injured rider in his rear seat, and rushed him to a nearby '
                                                       'private hospital emergency casualty. At the hospital, the '
                                                       "casualty reception staff told Vikas: 'We cannot treat him "
                                                       'until you pay a Rs. 25,000 cash deposit and wait for the local '
                                                       'police station to clear the Medico-Legal case; furthermore, '
                                                       'you must register your Aadhaar and stay here as a prime '
                                                       "witness.'",
                                              'title': 'Highway Hit-and-Run Collision and Good Samaritan Bystander '
                                                       'Rights'},
    'case_12_medical_negligence_record_refusal': {   'category': 'Consumer Rights & Medical Negligence',
                                                     'difficulty': 'Advanced',
                                                     'educational_breakdown': {   'case_summary': 'Gross surgical '
                                                                                                  'error leaving '
                                                                                                  'foreign body '
                                                                                                  '(sponge) in abdomen '
                                                                                                  'causing '
                                                                                                  'life-threatening '
                                                                                                  'sepsis, followed by '
                                                                                                  'illegal denial of '
                                                                                                  'case papers.',
                                                                                  'common_misconceptions': 'Myth: '
                                                                                                           "'Signing a "
                                                                                                           'consent '
                                                                                                           'form gives '
                                                                                                           'doctors '
                                                                                                           'total '
                                                                                                           'immunity '
                                                                                                           'for '
                                                                                                           "mistakes.' "
                                                                                                           'Reality: '
                                                                                                           'Informed '
                                                                                                           'consent '
                                                                                                           'covers '
                                                                                                           'known '
                                                                                                           'surgical '
                                                                                                           'risks, NOT '
                                                                                                           'negligent '
                                                                                                           'surgical '
                                                                                                           'errors '
                                                                                                           'like '
                                                                                                           'leaving '
                                                                                                           'instruments '
                                                                                                           'or sponges '
                                                                                                           'behind.',
                                                                                  'constitutional_analysis': 'Article '
                                                                                                             '21 '
                                                                                                             '(Right '
                                                                                                             'to '
                                                                                                             'health '
                                                                                                             'and '
                                                                                                             'bodily '
                                                                                                             'integrity '
                                                                                                             'as part '
                                                                                                             'of right '
                                                                                                             'to '
                                                                                                             'life).',
                                                                                  'court_precedents': 'Jacob Mathew v. '
                                                                                                      'State of Punjab '
                                                                                                      '(2005) SC - '
                                                                                                      'Threshold of '
                                                                                                      'gross '
                                                                                                      'negligence for '
                                                                                                      'criminal '
                                                                                                      'culpability. '
                                                                                                      'Indian Medical '
                                                                                                      'Association v. '
                                                                                                      'V.P. Shantha '
                                                                                                      '(1995) SC - '
                                                                                                      'Medical '
                                                                                                      'profession '
                                                                                                      'falls under '
                                                                                                      'Consumer '
                                                                                                      'Protection law. '
                                                                                                      'Achutrao '
                                                                                                      'Haribhau Khodwa '
                                                                                                      'v. State of '
                                                                                                      'Maharashtra - '
                                                                                                      'Leaving '
                                                                                                      'mop/sponge in '
                                                                                                      'abdomen is '
                                                                                                      'classic Res '
                                                                                                      'Ipsa Loquitur.',
                                                                                  'evidence_preservation_protocol': 'Pre-operative '
                                                                                                                    'and '
                                                                                                                    'post-operative '
                                                                                                                    'CT '
                                                                                                                    'scans '
                                                                                                                    '/ '
                                                                                                                    'imaging '
                                                                                                                    'reports, '
                                                                                                                    'extracted '
                                                                                                                    'surgical '
                                                                                                                    'sponge '
                                                                                                                    'preserved '
                                                                                                                    'by '
                                                                                                                    'second '
                                                                                                                    'hospital '
                                                                                                                    'as '
                                                                                                                    'pathological '
                                                                                                                    'evidence, '
                                                                                                                    'second '
                                                                                                                    "hospital's "
                                                                                                                    'emergency '
                                                                                                                    'OT '
                                                                                                                    'notes, '
                                                                                                                    'original '
                                                                                                                    'billing '
                                                                                                                    'receipts.',
                                                                                  'immediate_action_protocol': '1. '
                                                                                                               'Undergo '
                                                                                                               'emergency '
                                                                                                               'corrective '
                                                                                                               'surgery '
                                                                                                               'and '
                                                                                                               'preserve '
                                                                                                               'the '
                                                                                                               'extracted '
                                                                                                               'surgical '
                                                                                                               'foreign '
                                                                                                               'body; '
                                                                                                               '2. '
                                                                                                               'Demand '
                                                                                                               'complete '
                                                                                                               'certified '
                                                                                                               'indoor '
                                                                                                               'case '
                                                                                                               'sheets '
                                                                                                               'in '
                                                                                                               'writing '
                                                                                                               'citing '
                                                                                                               'NMC '
                                                                                                               '72-hour '
                                                                                                               'rule; '
                                                                                                               '3. '
                                                                                                               'File '
                                                                                                               'complaint '
                                                                                                               'before '
                                                                                                               'State '
                                                                                                               'Medical '
                                                                                                               'Council; '
                                                                                                               '4. '
                                                                                                               'File '
                                                                                                               'consumer '
                                                                                                               'compensation '
                                                                                                               'case '
                                                                                                               'on '
                                                                                                               'E-Daakhil.',
                                                                                  'key_takeaways': [   'Hospitals must '
                                                                                                       'provide '
                                                                                                       'complete '
                                                                                                       'medical '
                                                                                                       'records within '
                                                                                                       '72 hours under '
                                                                                                       'NMC '
                                                                                                       'regulations.',
                                                                                                       'Res Ipsa '
                                                                                                       'Loquitur '
                                                                                                       'applies when '
                                                                                                       'foreign bodies '
                                                                                                       'are left '
                                                                                                       'inside '
                                                                                                       'surgical '
                                                                                                       'cavities.',
                                                                                                       'Consumer '
                                                                                                       'Commissions '
                                                                                                       'provide '
                                                                                                       'effective, '
                                                                                                       'substantial '
                                                                                                       'financial '
                                                                                                       'compensation.'],
                                                                                  'legal_classification': 'Deficiency '
                                                                                                          'of Service '
                                                                                                          '(Consumer '
                                                                                                          'Protection '
                                                                                                          'Act), Civil '
                                                                                                          'Tort '
                                                                                                          'Malpractice, '
                                                                                                          'Professional '
                                                                                                          'Misconduct '
                                                                                                          '(NMC).',
                                                                                  'remedies_against_refusal': 'If the '
                                                                                                              'hospital '
                                                                                                              'refuses '
                                                                                                              'case '
                                                                                                              'papers, '
                                                                                                              'file an '
                                                                                                              'urgent '
                                                                                                              'interim '
                                                                                                              'application '
                                                                                                              'before '
                                                                                                              'the '
                                                                                                              'Consumer '
                                                                                                              'Commission '
                                                                                                              'for '
                                                                                                              'immediate '
                                                                                                              'seizure '
                                                                                                              'and '
                                                                                                              'production '
                                                                                                              'of '
                                                                                                              'records, '
                                                                                                              'or '
                                                                                                              'approach '
                                                                                                              'the '
                                                                                                              'High '
                                                                                                              'Court '
                                                                                                              'via '
                                                                                                              'writ.',
                                                                                  'reporting_forums': 'District / '
                                                                                                      'State Consumer '
                                                                                                      'Disputes '
                                                                                                      'Redressal '
                                                                                                      'Commission '
                                                                                                      '(E-Daakhil), '
                                                                                                      'State Medical '
                                                                                                      'Council / NMC '
                                                                                                      'Ethics Board, '
                                                                                                      'Jurisdictional '
                                                                                                      'Police Station '
                                                                                                      '(for Medical '
                                                                                                      'Board '
                                                                                                      'reference).',
                                                                                  'statutory_provisions': 'Consumer '
                                                                                                          'Protection '
                                                                                                          'Act 2019 '
                                                                                                          'Sections '
                                                                                                          '2(42), 35, '
                                                                                                          '84; BNS '
                                                                                                          'Section '
                                                                                                          '106(1) & '
                                                                                                          '125; NMC '
                                                                                                          'Code of '
                                                                                                          'Medical '
                                                                                                          'Ethics '
                                                                                                          'Regulations '
                                                                                                          '2002/2023.',
                                                                                  'victim_support_compensation': 'Substantial '
                                                                                                                 'financial '
                                                                                                                 'compensation '
                                                                                                                 'awarded '
                                                                                                                 'by '
                                                                                                                 'Consumer '
                                                                                                                 'Commissions '
                                                                                                                 'covering '
                                                                                                                 'second '
                                                                                                                 'surgery '
                                                                                                                 'costs, '
                                                                                                                 'loss '
                                                                                                                 'of '
                                                                                                                 'income, '
                                                                                                                 'pain, '
                                                                                                                 'suffering, '
                                                                                                                 'and '
                                                                                                                 'physical '
                                                                                                                 'impairment.'},
                                                     'id': 'case_12_medical_negligence_record_refusal',
                                                     'questions': [   {   'correct_index': 1,
                                                                          'explanation': 'Code of Medical Ethics '
                                                                                         'Regulations framed by the '
                                                                                         'National Medical Commission '
                                                                                         'mandate that every physician '
                                                                                         'and hospital must provide '
                                                                                         'medical records within 72 '
                                                                                         'hours of request.',
                                                                          'options': [   'No, medical records belong '
                                                                                         'strictly to the hospital '
                                                                                         'corporation',
                                                                                         'Yes. Under National Medical '
                                                                                         'Commission (NMC) Regulations '
                                                                                         'and consumer jurisprudence, '
                                                                                         'hospitals MUST provide '
                                                                                         'complete certified case '
                                                                                         'records within 72 hours of '
                                                                                         'request',
                                                                                         'Only if ordered by the Chief '
                                                                                         "Minister's office",
                                                                                         'Only after 5 years have '
                                                                                         'elapsed'],
                                                                          'question': 'Is the hospital legally '
                                                                                      'obligated to provide Anita with '
                                                                                      'complete certified copies of '
                                                                                      'her medical records and OT '
                                                                                      'notes?'},
                                                                      {   'correct_index': 1,
                                                                          'explanation': 'Res Ipsa Loquitur applies '
                                                                                         'directly. Leaving a surgical '
                                                                                         "sponge inside a patient's "
                                                                                         'abdomen is prima facie gross '
                                                                                         'negligence; the burden '
                                                                                         'shifts to the hospital and '
                                                                                         'surgeon to explain how it '
                                                                                         'occurred.',
                                                                          'options': [   'Caveat Emptor (Buyer Beware)',
                                                                                         'Res Ipsa Loquitur (The thing '
                                                                                         'speaks for itself — '
                                                                                         'negligence is obvious on the '
                                                                                         'face of the record without '
                                                                                         'needing complex proof)',
                                                                                         'Force Majeure (Act of God)',
                                                                                         'Doctrine of Frustration'],
                                                                          'question': 'What doctrine in tort law '
                                                                                      'applies to cases where a '
                                                                                      'foreign object '
                                                                                      '(sponge/scissors) is left '
                                                                                      "inside a patient's body during "
                                                                                      'surgery?'},
                                                                      {   'correct_index': 0,
                                                                          'explanation': 'Healthcare services rendered '
                                                                                         'for consideration fall '
                                                                                         "squarely within 'deficiency "
                                                                                         "in service' under the "
                                                                                         'Consumer Protection Act, '
                                                                                         '2019. E-Daakhil enables '
                                                                                         'digital filing of claims.',
                                                                          'options': [   'File an online consumer '
                                                                                         'complaint on E-Daakhil '
                                                                                         '(edaakhil.nic.in) before the '
                                                                                         'Consumer Commission for '
                                                                                         'deficiency in service and '
                                                                                         'medical malpractice',
                                                                                         'Only file a police complaint '
                                                                                         'for simple nuisance',
                                                                                         'Appeal to the World Health '
                                                                                         'Organization',
                                                                                         'Consumer courts have zero '
                                                                                         'jurisdiction over private '
                                                                                         'hospitals'],
                                                                          'question': 'Under the Consumer Protection '
                                                                                      'Act, 2019, what legal redress '
                                                                                      'can Anita pursue?'},
                                                                      {   'correct_index': 1,
                                                                          'explanation': 'Jacob Mathew v. State of '
                                                                                         'Punjab (2005) SC ruled that '
                                                                                         'criminal liability under S. '
                                                                                         '304A IPC (now S. 106 BNS) '
                                                                                         "requires 'gross' negligence, "
                                                                                         'and police must consult an '
                                                                                         'independent medical board '
                                                                                         'before arresting.',
                                                                          'options': [   'Doctors have total immunity '
                                                                                         'and can never be prosecuted '
                                                                                         'under criminal law',
                                                                                         'Police cannot arrest a '
                                                                                         'doctor simply on a '
                                                                                         "complainant's statement; "
                                                                                         'there must be prima facie '
                                                                                         'evidence of GROSS negligence '
                                                                                         'supported by an independent '
                                                                                         'government medical board '
                                                                                         'opinion',
                                                                                         'Any adverse surgical outcome '
                                                                                         'is automatically treated as '
                                                                                         'murder',
                                                                                         'Doctors can only be tried by '
                                                                                         'a jury of their peers'],
                                                                          'question': "What is the Supreme Court's "
                                                                                      'guideline in Jacob Mathew v. '
                                                                                      'State of Punjab regarding '
                                                                                      'criminal prosecution of doctors '
                                                                                      'for medical negligence?'},
                                                                      {   'correct_index': 0,
                                                                          'explanation': 'The State Medical Council '
                                                                                         'and National Medical '
                                                                                         'Commission (NMC) are the '
                                                                                         'statutory regulatory '
                                                                                         'authorities empowered to '
                                                                                         'conduct ethics inquiries and '
                                                                                         'cancel licenses.',
                                                                          'options': [   'State Medical Council / '
                                                                                         'National Medical Commission '
                                                                                         '(NMC)',
                                                                                         'District Collector',
                                                                                         'Consumer Goods Forum',
                                                                                         'Pharmacy Guild'],
                                                                          'question': 'Which regulatory body has the '
                                                                                      'power to suspend or revoke the '
                                                                                      "surgeon's license to practice "
                                                                                      'medicine for professional '
                                                                                      'misconduct?'}],
                                                     'story': 'Anita, a 34-year-old teacher, underwent a laparoscopic '
                                                              'abdominal surgery at a renowned private multi-specialty '
                                                              'hospital. Post-surgery, she suffered unbearable '
                                                              'abdominal pain, vomiting, and high fever for 3 weeks. '
                                                              'The operating surgeon repeatedly dismissed her '
                                                              "complaints as 'routine postoperative gas' and "
                                                              'prescribed painkillers. Unable to bear the agony, Anita '
                                                              'visited another hospital, where an emergency CT scan '
                                                              'revealed a 10 cm surgical gauze sponge (gossypiboma) '
                                                              'left inside her abdominal cavity, which had caused '
                                                              'severe internal infection and intestinal perforation. '
                                                              "She required emergency corrective surgery. When Anita's "
                                                              'husband went back to the first hospital to demand a '
                                                              'certified copy of her indoor case papers, surgical '
                                                              'operation theater notes, and nurse charts, the hospital '
                                                              "medical superintendent refused, saying: 'These are "
                                                              'internal hospital proprietary records; patients are '
                                                              "only entitled to the discharge summary.'",
                                                     'title': 'Surgical Error, Retained Foreign Body, and Hospital '
                                                              'Refusal of Medical Records'},
    'case_13_illegal_detention_police_powers': {   'category': 'Police Powers & Procedural Rights',
                                                   'difficulty': 'Advanced',
                                                   'educational_breakdown': {   'case_summary': 'Midnight pick-up by '
                                                                                                'plainclothes police, '
                                                                                                'secret detention '
                                                                                                'exceeding 36 hours '
                                                                                                'without arrest memo, '
                                                                                                'family intimation, or '
                                                                                                'Magistrate '
                                                                                                'production.',
                                                                                'common_misconceptions': 'Myth: '
                                                                                                         "'Police can "
                                                                                                         'detain '
                                                                                                         'anyone for 3 '
                                                                                                         'or 4 days '
                                                                                                         'for routine '
                                                                                                         'questioning '
                                                                                                         'without '
                                                                                                         'showing an '
                                                                                                         "arrest.' "
                                                                                                         'Reality: Any '
                                                                                                         'involuntary '
                                                                                                         'deprivation '
                                                                                                         'of liberty '
                                                                                                         'is an '
                                                                                                         'arrest; '
                                                                                                         'keeping '
                                                                                                         'someone '
                                                                                                         'beyond 24 '
                                                                                                         'hours '
                                                                                                         'without a '
                                                                                                         "Magistrate's "
                                                                                                         'remand order '
                                                                                                         'is '
                                                                                                         'completely '
                                                                                                         'unconstitutional.',
                                                                                'constitutional_analysis': 'Article 21 '
                                                                                                           '(Right to '
                                                                                                           'life and '
                                                                                                           'liberty), '
                                                                                                           'Article '
                                                                                                           '22(1) '
                                                                                                           '(Right to '
                                                                                                           'know '
                                                                                                           'grounds of '
                                                                                                           'arrest & '
                                                                                                           'consult '
                                                                                                           'lawyer), '
                                                                                                           'Article '
                                                                                                           '22(2) '
                                                                                                           '(Mandatory '
                                                                                                           '24-hour '
                                                                                                           'Magistrate '
                                                                                                           'production).',
                                                                                'court_precedents': 'D.K. Basu v. '
                                                                                                    'State of West '
                                                                                                    'Bengal (1997) SC '
                                                                                                    '- Definitive '
                                                                                                    '11-point arrest '
                                                                                                    'code. Arnesh '
                                                                                                    'Kumar v. State of '
                                                                                                    'Bihar (2014) SC - '
                                                                                                    'Ban on automatic '
                                                                                                    'arrests for '
                                                                                                    'offences '
                                                                                                    'punishable up to '
                                                                                                    '7 years. Nilabati '
                                                                                                    'Behera v. State '
                                                                                                    'of Orissa - State '
                                                                                                    'liability for '
                                                                                                    'custodial '
                                                                                                    'compensation.',
                                                                                'evidence_preservation_protocol': 'CCTV '
                                                                                                                  'footage '
                                                                                                                  'from '
                                                                                                                  'residential '
                                                                                                                  'building '
                                                                                                                  'showing '
                                                                                                                  'midnight '
                                                                                                                  'pick-up, '
                                                                                                                  'call '
                                                                                                                  'records '
                                                                                                                  'to '
                                                                                                                  'thana, '
                                                                                                                  'written '
                                                                                                                  'representation '
                                                                                                                  'submitted '
                                                                                                                  'to '
                                                                                                                  'SP '
                                                                                                                  'with '
                                                                                                                  'postal/stamped '
                                                                                                                  'receipt.',
                                                                                'immediate_action_protocol': '1. '
                                                                                                             'Brother '
                                                                                                             'must '
                                                                                                             'immediately '
                                                                                                             'send '
                                                                                                             'telegram '
                                                                                                             '/ email '
                                                                                                             'to Chief '
                                                                                                             'Judicial '
                                                                                                             'Magistrate '
                                                                                                             '(CJM) '
                                                                                                             'and SP '
                                                                                                             'intimating '
                                                                                                             'illegal '
                                                                                                             'detention; '
                                                                                                             '2. '
                                                                                                             'Approach '
                                                                                                             'High '
                                                                                                             'Court '
                                                                                                             'via '
                                                                                                             'emergency '
                                                                                                             'Habeas '
                                                                                                             'Corpus '
                                                                                                             'Writ '
                                                                                                             'under '
                                                                                                             'Article '
                                                                                                             '226; 3. '
                                                                                                             'Complain '
                                                                                                             'to State '
                                                                                                             'Human '
                                                                                                             'Rights '
                                                                                                             'Commission '
                                                                                                             '(SHRC); '
                                                                                                             '4. '
                                                                                                             'Demand '
                                                                                                             'medical '
                                                                                                             'exam '
                                                                                                             'under S. '
                                                                                                             '53 BNSS '
                                                                                                             'upon '
                                                                                                             'production.',
                                                                                'key_takeaways': [   '24-hour '
                                                                                                     'production '
                                                                                                     'before a '
                                                                                                     'Magistrate under '
                                                                                                     'Article 22(2) is '
                                                                                                     'non-negotiable.',
                                                                                                     'D.K. Basu arrest '
                                                                                                     'memos and '
                                                                                                     'relative '
                                                                                                     'intimation are '
                                                                                                     'mandatory.',
                                                                                                     'Habeas Corpus '
                                                                                                     'writ provides '
                                                                                                     'same-day '
                                                                                                     'judicial '
                                                                                                     'intervention '
                                                                                                     'against secret '
                                                                                                     'custody.'],
                                                                                'legal_classification': 'Gross '
                                                                                                        'Violation of '
                                                                                                        'Constitutional '
                                                                                                        'Procedural '
                                                                                                        'Safeguards '
                                                                                                        'and Criminal '
                                                                                                        'Wrongful '
                                                                                                        'Confinement.',
                                                                                'remedies_against_refusal': 'Filing a '
                                                                                                            'Habeas '
                                                                                                            'Corpus '
                                                                                                            'petition '
                                                                                                            'in the '
                                                                                                            'High '
                                                                                                            'Court '
                                                                                                            'forces '
                                                                                                            'the '
                                                                                                            'police to '
                                                                                                            'produce '
                                                                                                            'the '
                                                                                                            'detainee '
                                                                                                            'before '
                                                                                                            'the bench '
                                                                                                            'within 24 '
                                                                                                            'hours or '
                                                                                                            'face '
                                                                                                            'severe '
                                                                                                            'contempt '
                                                                                                            'proceedings.',
                                                                                'reporting_forums': 'Judicial '
                                                                                                    'Magistrate / '
                                                                                                    'Chief Judicial '
                                                                                                    'Magistrate (CJM), '
                                                                                                    'High Court (Writ '
                                                                                                    'Jurisdiction), '
                                                                                                    'National Human '
                                                                                                    'Rights Commission '
                                                                                                    '(NHRC / SHRC), '
                                                                                                    'District Legal '
                                                                                                    'Services '
                                                                                                    'Authority (DLSA).',
                                                                                'statutory_provisions': 'BNSS Section '
                                                                                                        '35 (Arrest '
                                                                                                        'procedure), '
                                                                                                        'Section 36 '
                                                                                                        '(Arrest '
                                                                                                        'memo), '
                                                                                                        'Section 47 '
                                                                                                        '(Right to '
                                                                                                        'inform '
                                                                                                        'relative), '
                                                                                                        'Section 58 '
                                                                                                        '(24-hour '
                                                                                                        'limit), BNS '
                                                                                                        'Section 127 '
                                                                                                        '(Wrongful '
                                                                                                        'Confinement).',
                                                                                'victim_support_compensation': 'Public '
                                                                                                               'law '
                                                                                                               'compensation '
                                                                                                               'awarded '
                                                                                                               'by the '
                                                                                                               'High '
                                                                                                               'Court '
                                                                                                               '/ '
                                                                                                               'Supreme '
                                                                                                               'Court '
                                                                                                               'for '
                                                                                                               'illegal '
                                                                                                               'detention '
                                                                                                               'under '
                                                                                                               'Article '
                                                                                                               '21 (as '
                                                                                                               'established '
                                                                                                               'in '
                                                                                                               'Rudul '
                                                                                                               'Sah '
                                                                                                               'and '
                                                                                                               'Nilabati '
                                                                                                               'Behera).'},
                                                   'id': 'case_13_illegal_detention_police_powers',
                                                   'questions': [   {   'correct_index': 1,
                                                                        'explanation': 'Article 22(2) of the '
                                                                                       'Constitution of India and '
                                                                                       'Section 58 BNSS (replaces CrPC '
                                                                                       '57) mandate that no person can '
                                                                                       'be detained in custody beyond '
                                                                                       '24 hours without the express '
                                                                                       'authority of a Magistrate.',
                                                                        'options': [   'Within 72 hours',
                                                                                       'Within 24 hours of arrest, '
                                                                                       'excluding journey time, under '
                                                                                       'Article 22(2) and Section 58 '
                                                                                       'BNSS',
                                                                                       'Whenever the investigating '
                                                                                       'officer completes questioning',
                                                                                       'Within 7 days for financial '
                                                                                       'investigations'],
                                                                        'question': 'What is the constitutional and '
                                                                                    'statutory time limit within which '
                                                                                    'an arrested person MUST be '
                                                                                    'produced before the nearest '
                                                                                    'Judicial Magistrate?'},
                                                                    {   'correct_index': 0,
                                                                        'explanation': 'D.K. Basu v. State of West '
                                                                                       'Bengal (1997) SC laid down 11 '
                                                                                       'mandatory procedural '
                                                                                       'safeguards: displaying name '
                                                                                       'tags, preparing an arrest memo '
                                                                                       'signed by a witness, informing '
                                                                                       'relatives within 8-12 hours, '
                                                                                       'and right to meet an advocate.',
                                                                        'options': [   'D.K. Basu v. State of West '
                                                                                       'Bengal (1997)',
                                                                                       'Kesavananda Bharati v. State '
                                                                                       'of Kerala',
                                                                                       'Minerva Mills v. Union of '
                                                                                       'India',
                                                                                       'Indra Sawhney v. Union of '
                                                                                       'India'],
                                                                        'question': 'Which landmark Supreme Court '
                                                                                    'judgment laid down the mandatory '
                                                                                    'guidelines governing arrest, memo '
                                                                                    'preparation, and informing family '
                                                                                    'members?'},
                                                                    {   'correct_index': 1,
                                                                        'explanation': 'Under Section 35(3) BNSS '
                                                                                       '(replaces CrPC 41A) and Arnesh '
                                                                                       'Kumar v. State of Bihar, for '
                                                                                       'offences punishable with up to '
                                                                                       '7 years, arrest is not '
                                                                                       'routine; police must first '
                                                                                       'issue a formal Notice of '
                                                                                       'Appearance.',
                                                                        'options': [   'An execution warrant',
                                                                                       'A Notice of Appearance '
                                                                                       'directing the person to join '
                                                                                       'the investigation',
                                                                                       'A public wanted circular',
                                                                                       'A property attachment seal'],
                                                                        'question': 'Under Section 35(3) BNSS and the '
                                                                                    'Arnesh Kumar guidelines, what '
                                                                                    'must police issue instead of '
                                                                                    'routinely arresting a citizen for '
                                                                                    'offences punishable with '
                                                                                    'imprisonment of less than 7 '
                                                                                    'years?'},
                                                                    {   'correct_index': 1,
                                                                        'explanation': "Habeas Corpus ('produce the "
                                                                                       "body') is the sovereign "
                                                                                       'constitutional remedy against '
                                                                                       'illegal detention. The High '
                                                                                       'Court commands the state to '
                                                                                       'produce the detained person '
                                                                                       'and release them if detention '
                                                                                       'lacks lawful authority.',
                                                                        'options': [   'Writ of Quo Warranto',
                                                                                       'Writ of Habeas Corpus under '
                                                                                       'Article 226 of the '
                                                                                       'Constitution',
                                                                                       'Writ of Certiorari',
                                                                                       'Writ of Prohibition'],
                                                                        'question': 'What extraordinary constitutional '
                                                                                    "writ can Imran's family file in "
                                                                                    'the High Court for his immediate '
                                                                                    'production if police detain him '
                                                                                    'illegally?'},
                                                                    {   'correct_index': 1,
                                                                        'explanation': 'Unlawful detention violates '
                                                                                       'D.K. Basu and constitutes '
                                                                                       'criminal wrongful confinement '
                                                                                       'under Section 127 BNS, '
                                                                                       'exposing delinquent officers '
                                                                                       'to departmental dismissal, '
                                                                                       'contempt of court, and '
                                                                                       'criminal prosecution.',
                                                                        'options': [   'No, police officers enjoy '
                                                                                       'complete immunity for all '
                                                                                       'custodial acts',
                                                                                       'Yes. They commit the offence '
                                                                                       'of Wrongful Confinement under '
                                                                                       'Section 127 BNS and can be '
                                                                                       'prosecuted for contempt of '
                                                                                       'court and human rights '
                                                                                       'violations',
                                                                                       'Only if they sign a confession',
                                                                                       "Only with Governor's prior "
                                                                                       'permission'],
                                                                        'question': 'Are police officers who '
                                                                                    'deliberately detain a citizen '
                                                                                    'beyond 24 hours without '
                                                                                    'magistrate order criminally '
                                                                                    'liable?'}],
                                                   'story': 'At 1:30 AM on a Tuesday, four plainclothes police '
                                                            'personnel banged on the door of Imran, a 26-year-old '
                                                            'freelance accountant. Without showing any identity '
                                                            'badges, written arrest warrant, or explaining the '
                                                            'reasons, they forcibly pulled Imran into an unmarked '
                                                            "vehicle and took him to the police station. When Imran's "
                                                            'brother rushed to the station, the Duty Officer told him: '
                                                            "'He is being questioned in connection with a theft "
                                                            "inquiry; leave immediately or we will lock you up too.' "
                                                            'Imran was held in a lockup cell for 36 hours without '
                                                            'being allowed to call a lawyer, without his family being '
                                                            'informed of his arrest, and without being produced before '
                                                            'any Magistrate.',
                                                   'title': 'Midnight Pick-Up, Unlawful Detention Without Grounds, and '
                                                            'Custodial Rights'},
    'case_14_arbitrary_demolition_due_process': {   'category': 'Constitutional Rights & State Action',
                                                    'difficulty': 'Advanced',
                                                    'educational_breakdown': {   'case_summary': 'Arbitrary '
                                                                                                 'extra-judicial '
                                                                                                 'demolition of '
                                                                                                 'licensed commercial '
                                                                                                 'premises without '
                                                                                                 'notice, violating '
                                                                                                 'natural justice and '
                                                                                                 'Supreme Court '
                                                                                                 'directives.',
                                                                                 'common_misconceptions': "Myth: 'If "
                                                                                                          'authorities '
                                                                                                          'claim '
                                                                                                          'someone is '
                                                                                                          'involved in '
                                                                                                          'a crime, '
                                                                                                          'they can '
                                                                                                          'demolish '
                                                                                                          'their '
                                                                                                          "family's "
                                                                                                          'home or '
                                                                                                          "shop.' "
                                                                                                          'Reality: '
                                                                                                          'The Supreme '
                                                                                                          'Court held '
                                                                                                          'that the '
                                                                                                          'executive '
                                                                                                          'cannot act '
                                                                                                          'as a judge; '
                                                                                                          'punishing '
                                                                                                          'an accused '
                                                                                                          'by '
                                                                                                          'demolishing '
                                                                                                          'property is '
                                                                                                          'a barbaric '
                                                                                                          'negation of '
                                                                                                          'the rule of '
                                                                                                          'law.',
                                                                                 'constitutional_analysis': 'Article '
                                                                                                            '14 '
                                                                                                            '(Protection '
                                                                                                            'against '
                                                                                                            'state '
                                                                                                            'arbitrariness), '
                                                                                                            'Article '
                                                                                                            '19(1)(g) '
                                                                                                            '(Right to '
                                                                                                            'carry on '
                                                                                                            'business), '
                                                                                                            'Article '
                                                                                                            '21 (Right '
                                                                                                            'to '
                                                                                                            'livelihood '
                                                                                                            '- Olga '
                                                                                                            'Tellis), '
                                                                                                            'Article '
                                                                                                            '300A '
                                                                                                            '(Constitutional '
                                                                                                            'Right to '
                                                                                                            'Property).',
                                                                                 'court_precedents': 'In Re: '
                                                                                                     'Directions in '
                                                                                                     'the matter of '
                                                                                                     'Demolition of '
                                                                                                     'Structures '
                                                                                                     '(2024) SC - '
                                                                                                     'Nationwide '
                                                                                                     'binding '
                                                                                                     'guidelines '
                                                                                                     'barring summary '
                                                                                                     'bulldozer '
                                                                                                     'justice; '
                                                                                                     'mandatory 15-day '
                                                                                                     'notice, hearing, '
                                                                                                     'and personal '
                                                                                                     'officer '
                                                                                                     'liability. Olga '
                                                                                                     'Tellis v. BMC '
                                                                                                     '(1985) SC - '
                                                                                                     'Right to '
                                                                                                     'livelihood is '
                                                                                                     'part of Article '
                                                                                                     '21.',
                                                                                 'evidence_preservation_protocol': 'Municipal '
                                                                                                                   'trade '
                                                                                                                   'license, '
                                                                                                                   'electricity '
                                                                                                                   'connection '
                                                                                                                   'bills, '
                                                                                                                   'property '
                                                                                                                   'tax '
                                                                                                                   'receipts, '
                                                                                                                   'video '
                                                                                                                   'and '
                                                                                                                   'photographic '
                                                                                                                   'records '
                                                                                                                   'of '
                                                                                                                   'the '
                                                                                                                   'demolition, '
                                                                                                                   'inventory '
                                                                                                                   'of '
                                                                                                                   'destroyed '
                                                                                                                   'stock '
                                                                                                                   'with '
                                                                                                                   'supplier '
                                                                                                                   'purchase '
                                                                                                                   'bills.',
                                                                                 'immediate_action_protocol': '1. '
                                                                                                              'Video '
                                                                                                              'record '
                                                                                                              'the '
                                                                                                              'demolition, '
                                                                                                              'bulldozer '
                                                                                                              'registration, '
                                                                                                              'and '
                                                                                                              'participating '
                                                                                                              'municipal '
                                                                                                              'officials; '
                                                                                                              '2. '
                                                                                                              'Preserve '
                                                                                                              'all '
                                                                                                              'original '
                                                                                                              'trade '
                                                                                                              'licenses, '
                                                                                                              'tax '
                                                                                                              'receipts, '
                                                                                                              'and '
                                                                                                              'registry '
                                                                                                              'documents; '
                                                                                                              '3. File '
                                                                                                              'emergency '
                                                                                                              'Writ '
                                                                                                              'Petition '
                                                                                                              'under '
                                                                                                              'Article '
                                                                                                              '226 in '
                                                                                                              'the '
                                                                                                              'High '
                                                                                                              'Court; '
                                                                                                              '4. Seek '
                                                                                                              'interim '
                                                                                                              'stay on '
                                                                                                              'further '
                                                                                                              'demolition '
                                                                                                              'and '
                                                                                                              'compensation '
                                                                                                              'inquiry.',
                                                                                 'key_takeaways': [   'Executive '
                                                                                                      'bulldozer '
                                                                                                      'justice without '
                                                                                                      '15-day notice '
                                                                                                      'is completely '
                                                                                                      'unconstitutional.',
                                                                                                      'Officers '
                                                                                                      'executing '
                                                                                                      'illegal '
                                                                                                      'demolitions are '
                                                                                                      'personally '
                                                                                                      'liable for '
                                                                                                      'damages.',
                                                                                                      'Article 226 '
                                                                                                      'writ petitions '
                                                                                                      'provide rapid '
                                                                                                      'high-court '
                                                                                                      'constitutional '
                                                                                                      'redress.'],
                                                                                 'legal_classification': 'Severe '
                                                                                                         'Constitutional '
                                                                                                         'Violation '
                                                                                                         '(Articles '
                                                                                                         '14, 19, 21, '
                                                                                                         '300A) and '
                                                                                                         'Illegal '
                                                                                                         'Administrative '
                                                                                                         'Action.',
                                                                                 'remedies_against_refusal': 'Executive '
                                                                                                             'action '
                                                                                                             'that '
                                                                                                             'defies '
                                                                                                             'Supreme '
                                                                                                             'Court '
                                                                                                             'guidelines '
                                                                                                             'constitutes '
                                                                                                             'criminal '
                                                                                                             'contempt '
                                                                                                             'of '
                                                                                                             'court; '
                                                                                                             'an '
                                                                                                             'application '
                                                                                                             'for '
                                                                                                             'contempt '
                                                                                                             'can be '
                                                                                                             'filed '
                                                                                                             'directly '
                                                                                                             'before '
                                                                                                             'the '
                                                                                                             'Supreme '
                                                                                                             'Court / '
                                                                                                             'High '
                                                                                                             'Court.',
                                                                                 'reporting_forums': 'High Court (Writ '
                                                                                                     'Petition under '
                                                                                                     'Art. 226), '
                                                                                                     'Lokayukta / '
                                                                                                     'State Human '
                                                                                                     'Rights '
                                                                                                     'Commission, '
                                                                                                     'Principal '
                                                                                                     'Secretary (Urban '
                                                                                                     'Development).',
                                                                                 'statutory_provisions': 'State '
                                                                                                         'Municipal '
                                                                                                         'Corporation '
                                                                                                         'Act '
                                                                                                         '(Mandatory '
                                                                                                         'notice '
                                                                                                         'sections), '
                                                                                                         'Article 226 '
                                                                                                         '(High Court '
                                                                                                         'Writ '
                                                                                                         'Jurisdiction), '
                                                                                                         'BNS Section '
                                                                                                         '324 '
                                                                                                         '(Mischief).',
                                                                                 'victim_support_compensation': 'Restitution '
                                                                                                                'of '
                                                                                                                'structure, '
                                                                                                                'full '
                                                                                                                'reimbursement '
                                                                                                                'of '
                                                                                                                'destroyed '
                                                                                                                'inventory, '
                                                                                                                'and '
                                                                                                                'exemplary '
                                                                                                                'public '
                                                                                                                'law '
                                                                                                                'damages '
                                                                                                                'recovered '
                                                                                                                'from '
                                                                                                                'delinquent '
                                                                                                                'officials.'},
                                                    'id': 'case_14_arbitrary_demolition_due_process',
                                                    'questions': [   {   'correct_index': 1,
                                                                         'explanation': 'In November 2024, the Supreme '
                                                                                        'Court laid down nationwide '
                                                                                        'binding guidelines holding '
                                                                                        'that executive demolitions '
                                                                                        'without due process violate '
                                                                                        'the rule of law, separation '
                                                                                        'of powers, and Article 21; '
                                                                                        'authorities must give at '
                                                                                        'least 15 days notice and '
                                                                                        'conduct personal hearings.',
                                                                         'options': [   'Yes, municipal engineers have '
                                                                                        'supreme authority over all '
                                                                                        'urban structures',
                                                                                        'No. In the landmark judgment '
                                                                                        'In Re: Directions in the '
                                                                                        'matter of Demolition of '
                                                                                        'Structures (2024), the '
                                                                                        'Supreme Court ruled that '
                                                                                        "executive 'bulldozer justice' "
                                                                                        'is completely '
                                                                                        'unconstitutional; minimum 15 '
                                                                                        'days written notice and '
                                                                                        'personal hearing are '
                                                                                        'mandatory',
                                                                                        'Only if the owner is given 10 '
                                                                                        'minutes to remove their '
                                                                                        'belongings',
                                                                                        'Yes, if ordered over the '
                                                                                        'telephone by a political '
                                                                                        'official'],
                                                                         'question': 'Can municipal authorities '
                                                                                     "demolish a citizen's house or "
                                                                                     'commercial shop without prior '
                                                                                     'written show-cause notice and a '
                                                                                     'fair hearing?'},
                                                                     {   'correct_index': 0,
                                                                         'explanation': 'Audi Alteram Partem is the '
                                                                                        'foundational principle of '
                                                                                        'natural justice and '
                                                                                        'administrative law: the state '
                                                                                        'cannot take adverse action '
                                                                                        "against a citizen's property "
                                                                                        'or livelihood without prior '
                                                                                        'notice and a genuine '
                                                                                        'opportunity of hearing.',
                                                                         'options': [   'Audi Alteram Partem (Listen '
                                                                                        'to the other side / No person '
                                                                                        'shall be condemned unheard)',
                                                                                        'Nemo Judex In Causa Sua (No '
                                                                                        'one can be a judge in their '
                                                                                        'own cause)',
                                                                                        'Sub Judice',
                                                                                        'Obiter Dicta'],
                                                                         'question': 'Which core principle of natural '
                                                                                     'justice was violated by '
                                                                                     'demolishing the shop without '
                                                                                     'giving Farooq an opportunity to '
                                                                                     'respond?'},
                                                                     {   'correct_index': 0,
                                                                         'explanation': 'Arbitrary state destruction '
                                                                                        'of property directly breaches '
                                                                                        'Article 14 '
                                                                                        '(anti-arbitrariness), Article '
                                                                                        '19(1)(g) (livelihood), '
                                                                                        'Article 21 (Olga Tellis: '
                                                                                        'right to livelihood is part '
                                                                                        'of life), and Article 300A '
                                                                                        '(no deprivation of property '
                                                                                        'except by authority of law).',
                                                                         'options': [   'Article 14 (Equality and '
                                                                                        'protection against '
                                                                                        'arbitrariness), Article '
                                                                                        '19(1)(g) (Right to practice '
                                                                                        'trade/business), Article 21 '
                                                                                        '(Livelihood & dignity), and '
                                                                                        'Article 300A (Right to '
                                                                                        'Property)',
                                                                                        'Only the right to vote under '
                                                                                        'Article 326',
                                                                                        'Article 370',
                                                                                        'No constitutional rights are '
                                                                                        'involved in municipal '
                                                                                        'actions'],
                                                                         'question': 'Which constitutional rights are '
                                                                                     'directly infringed by the '
                                                                                     "arbitrary demolition of Farooq's "
                                                                                     'shop?'},
                                                                     {   'correct_index': 1,
                                                                         'explanation': 'The Supreme Court explicitly '
                                                                                        'ruled that delinquent '
                                                                                        'officers who carry out '
                                                                                        'illegal demolitions without '
                                                                                        'following the prescribed '
                                                                                        'guidelines will be held '
                                                                                        'personally liable for '
                                                                                        'restitution and damages '
                                                                                        'deducted from their salaries.',
                                                                         'options': [   'Complete personal immunity '
                                                                                        'paid by the taxpayer',
                                                                                        'Officers are personally '
                                                                                        'liable to pay '
                                                                                        'restitution/damages from '
                                                                                        'their own salaries, face '
                                                                                        'disciplinary action, and face '
                                                                                        'criminal prosecution for '
                                                                                        'contempt of court',
                                                                                        'Only a verbal reprimand from '
                                                                                        'the mayor',
                                                                                        'An automatic promotion'],
                                                                         'question': 'Under Supreme Court guidelines, '
                                                                                     'what personal liability do '
                                                                                     'municipal officers face if they '
                                                                                     'execute an illegal demolition?'},
                                                                     {   'correct_index': 0,
                                                                         'explanation': 'A Writ Petition under Article '
                                                                                        '226 before the High Court is '
                                                                                        'the primary constitutional '
                                                                                        'remedy to challenge unlawful '
                                                                                        'state action, quash illegal '
                                                                                        'orders, and seek exemplary '
                                                                                        'compensation.',
                                                                         'options': [   'A Writ Petition under Article '
                                                                                        '226 of the Constitution of '
                                                                                        'India seeking compensation '
                                                                                        'and prosecution of delinquent '
                                                                                        'officers',
                                                                                        'A revision petition before '
                                                                                        'the village patwari',
                                                                                        'A consumer complaint for '
                                                                                        'defective goods',
                                                                                        'Wait 3 years for municipal '
                                                                                        're-elections'],
                                                                         'question': 'What judicial remedy should '
                                                                                     'Farooq file in the High Court to '
                                                                                     'claim compensation and hold the '
                                                                                     'officials accountable?'}],
                                                    'story': 'Mohammad Farooq has owned and operated a licensed '
                                                             'grocery store in an urban municipal market for 18 years, '
                                                             'holding a valid municipal trade license, electricity '
                                                             'connection, and property tax receipts. On Monday '
                                                             'morning, following an alleged altercation in the '
                                                             "neighborhood involving Farooq's estranged nephew, a "
                                                             'municipal bulldozer escorted by police arrived at '
                                                             "Farooq's shop without any prior written show-cause "
                                                             'notice, warning, or opportunity of hearing. The '
                                                             "municipal officer stated: 'We have orders from higher "
                                                             "authorities to clear illegal encroachments immediately.' "
                                                             'Within 45 minutes, despite Farooq waving his valid '
                                                             'municipal licenses and tax receipts, the shop was razed '
                                                             'to the ground, destroying stock worth Rs. 15 Lakhs.',
                                                    'title': 'Bulldozer Demolition of Commercial Shop Without Notice '
                                                             'or Hearing'},
    'case_15_sextortion_private_images': {   'category': 'Cybercrime & Online Fraud',
                                             'difficulty': 'Emergency',
                                             'educational_breakdown': {   'case_summary': 'Honeytrap video call '
                                                                                          'resulting in morphed sexual '
                                                                                          'image recording, extortion '
                                                                                          'threats, and cyber '
                                                                                          'blackmail targeting a '
                                                                                          'student.',
                                                                          'common_misconceptions': "Myth: 'Paying Rs. "
                                                                                                   '5,000 once will '
                                                                                                   'make them delete '
                                                                                                   "the video.' "
                                                                                                   'Reality: Paying '
                                                                                                   'proves you have '
                                                                                                   'funds and are '
                                                                                                   'vulnerable; they '
                                                                                                   'will immediately '
                                                                                                   'demand Rs. 50,000.',
                                                                          'constitutional_analysis': 'Article 21 '
                                                                                                     '(Right to '
                                                                                                     'privacy, '
                                                                                                     'dignity, and '
                                                                                                     'bodily autonomy '
                                                                                                     'under K.S. '
                                                                                                     'Puttaswamy v. '
                                                                                                     'Union of India).',
                                                                          'court_precedents': 'K.S. Puttaswamy v. '
                                                                                              'Union of India (2017) '
                                                                                              'SC - Informational '
                                                                                              'privacy and intimate '
                                                                                              'visual privacy are '
                                                                                              'inviolable fundamental '
                                                                                              'rights protected under '
                                                                                              'Article 21.',
                                                                          'evidence_preservation_protocol': 'Screenshots '
                                                                                                            'of the '
                                                                                                            'extortion '
                                                                                                            'chats, '
                                                                                                            'video '
                                                                                                            'thumbnails, '
                                                                                                            "caller's "
                                                                                                            'phone '
                                                                                                            'numbers '
                                                                                                            'and '
                                                                                                            'country '
                                                                                                            'code, UPI '
                                                                                                            'ID '
                                                                                                            'provided '
                                                                                                            'for '
                                                                                                            'payment, '
                                                                                                            'social '
                                                                                                            'media '
                                                                                                            'profile '
                                                                                                            'links of '
                                                                                                            'the '
                                                                                                            'scammer.',
                                                                          'immediate_action_protocol': '1. Do NOT '
                                                                                                       'transfer any '
                                                                                                       'money; 2. Take '
                                                                                                       'screenshots of '
                                                                                                       'threatening '
                                                                                                       'messages, '
                                                                                                       'phone numbers, '
                                                                                                       'and UPI '
                                                                                                       'handles; 3. '
                                                                                                       'Deactivate or '
                                                                                                       'lock social '
                                                                                                       'media accounts '
                                                                                                       'temporarily; '
                                                                                                       '4. Call 1930 / '
                                                                                                       'log complaint '
                                                                                                       'on '
                                                                                                       'cybercrime.gov.in; '
                                                                                                       '5. Create a '
                                                                                                       'hash on '
                                                                                                       'StopNCII.org.',
                                                                          'key_takeaways': [   'Never pay blackmailers '
                                                                                               'in sextortion cases.',
                                                                                               'Platforms must remove '
                                                                                               'intimate images within '
                                                                                               '24 hours under Rule '
                                                                                               '3(2)(b) IT Rules.',
                                                                                               'StopNCII.org prevents '
                                                                                               'image uploads across '
                                                                                               'major platforms.'],
                                                                          'legal_classification': 'Cyber Extortion and '
                                                                                                  'Obscenity Offences '
                                                                                                  'under BNS and IT '
                                                                                                  'Act, 2000.',
                                                                          'remedies_against_refusal': 'Section 67A IT '
                                                                                                      'Act is '
                                                                                                      'non-bailable '
                                                                                                      'and cognizable. '
                                                                                                      'If local police '
                                                                                                      'hesitate, '
                                                                                                      'approach the '
                                                                                                      'District Cyber '
                                                                                                      'Crime Unit or '
                                                                                                      'file directly '
                                                                                                      'on '
                                                                                                      'cybercrime.gov.in '
                                                                                                      'which '
                                                                                                      'auto-assigns '
                                                                                                      'the case to the '
                                                                                                      'nodal officer.',
                                                                          'reporting_forums': 'National Cyber Crime '
                                                                                              'Reporting Portal '
                                                                                              '(cybercrime.gov.in / '
                                                                                              '1930), StopNCII.org, '
                                                                                              'Grievance Officer of '
                                                                                              'Meta / WhatsApp / '
                                                                                              'Instagram under IT '
                                                                                              'Rules 2021.',
                                                                          'statutory_provisions': 'BNS Section 308 '
                                                                                                  '(Extortion), '
                                                                                                  'Section 351 '
                                                                                                  '(Criminal '
                                                                                                  'Intimidation), IT '
                                                                                                  'Act Section 67 & '
                                                                                                  '67A '
                                                                                                  '(Publishing/transmitting '
                                                                                                  'sexually explicit '
                                                                                                  'act), IT Rules 2021 '
                                                                                                  'Rule 3(2)(b).',
                                                                          'victim_support_compensation': 'Mental '
                                                                                                         'health '
                                                                                                         'counseling '
                                                                                                         'through '
                                                                                                         'Tele-MANAS '
                                                                                                         '(14416) and '
                                                                                                         'victim '
                                                                                                         'support '
                                                                                                         'services '
                                                                                                         'through '
                                                                                                         'DLSA.'},
                                             'id': 'case_15_sextortion_private_images',
                                             'questions': [   {   'correct_index': 1,
                                                                  'explanation': 'Paying money NEVER stops sextortion; '
                                                                                 'it signals that the victim is '
                                                                                 'panicked, leading to unending '
                                                                                 'demands for larger sums. Blocking, '
                                                                                 'preserving evidence, and reporting '
                                                                                 'to 1930 is the mandatory protocol.',
                                                                  'options': [   'Pay the demanded amount immediately '
                                                                                 'to ensure they delete the video',
                                                                                 'Do NOT pay any money, block the '
                                                                                 'scammer, do not delete the evidence, '
                                                                                 'and report immediately on '
                                                                                 'cybercrime.gov.in / 1930',
                                                                                 'Apologize to the blackmailer and beg '
                                                                                 'for mercy',
                                                                                 'Delete all social media accounts '
                                                                                 'without saving screenshots'],
                                                                  'question': 'What is the very first rule when '
                                                                              'dealing with a sextortion blackmailer '
                                                                              'demanding money?'},
                                                              {   'correct_index': 0,
                                                                  'explanation': "The 'Report Crime Against "
                                                                                 "Women/Children' category on "
                                                                                 'cybercrime.gov.in allows victims '
                                                                                 '(including male victims of '
                                                                                 'non-consensual intimate '
                                                                                 'imagery/extortion) to report '
                                                                                 'anonymously and request immediate '
                                                                                 'digital takedowns.',
                                                                  'options': [   "'Report Crime Against "
                                                                                 "Women/Children' section",
                                                                                 'Commercial trade dispute desk',
                                                                                 'Income Tax audit portal',
                                                                                 'Telecom billing portal'],
                                                                  'question': 'Under which special category on the '
                                                                              'National Cyber Crime Reporting Portal '
                                                                              '(cybercrime.gov.in) can sextortion '
                                                                              'victims report anonymously?'},
                                                              {   'correct_index': 0,
                                                                  'explanation': 'Extracting money through threats to '
                                                                                 'circulate sexual imagery constitutes '
                                                                                 'Extortion (S. 308 BNS), transmission '
                                                                                 'of explicit pornography (S. 67A IT '
                                                                                 'Act - up to 5 years jail), and '
                                                                                 'Criminal Intimidation (S. 351 BNS).',
                                                                  'options': [   'Extortion (S. 308 BNS), Publishing '
                                                                                 'sexually explicit material (S. '
                                                                                 '67/67A IT Act), and Criminal '
                                                                                 'Intimidation (S. 351 BNS)',
                                                                                 'Simple trespass under civil law',
                                                                                 'Breach of contract under Indian '
                                                                                 'Contract Act',
                                                                                 'Traffic violation under Motor '
                                                                                 'Vehicles Act'],
                                                                  'question': 'What criminal offences under the '
                                                                              'Bharatiya Nyaya Sanhita (BNS) and '
                                                                              'Information Technology Act apply to the '
                                                                              'blackmailer?'},
                                                              {   'correct_index': 0,
                                                                  'explanation': 'StopNCII.org is an internationally '
                                                                                 'recognized platform partnered with '
                                                                                 'tech companies (Meta, TikTok, etc.) '
                                                                                 'that creates a privacy-preserving '
                                                                                 'cryptographic hash of intimate '
                                                                                 'images to prevent them from being '
                                                                                 'uploaded across participating tech '
                                                                                 'platforms.',
                                                                  'options': [   'StopNCII.org (Stop Non-Consensual '
                                                                                 'Intimate Image Abuse)',
                                                                                 'Google Maps',
                                                                                 'Wikipedia',
                                                                                 'LinkedIn Recruiter'],
                                                                  'question': 'Which global platform tool helps '
                                                                              'victims stop intimate images from being '
                                                                              'circulated online by creating a secure '
                                                                              'digital hash?'},
                                                              {   'correct_index': 1,
                                                                  'explanation': 'Rule 3(2)(b) of the Information '
                                                                                 'Technology (Intermediary Guidelines '
                                                                                 'and Digital Media Ethics Code) '
                                                                                 'Rules, 2021 mandates that platforms '
                                                                                 'MUST remove non-consensual nudity or '
                                                                                 'morphed sexual imagery within 24 '
                                                                                 'hours of receiving a complaint.',
                                                                  'options': [   'They can keep the content online for '
                                                                                 '30 days of public discussion',
                                                                                 'Under Rule 3(2)(b) of the IT Rules, '
                                                                                 '2021, platforms MUST take down '
                                                                                 'non-consensual intimate images '
                                                                                 'within 24 hours of receiving a '
                                                                                 'complaint',
                                                                                 'They are not responsible for any '
                                                                                 'user content ever',
                                                                                 'They only respond if the Prime '
                                                                                 'Minister requests it'],
                                                                  'question': 'If the scammer circulates morphed '
                                                                              "photos to Rohan's contacts, what "
                                                                              'statutory responsibility do social '
                                                                              'media intermediaries have under the IT '
                                                                              'Rules, 2021?'}],
                                             'story': 'Rohan, a 21-year-old engineering student, accepted a video call '
                                                      'from an attractive woman on Instagram. Within 10 seconds of '
                                                      'answering, the person on the other end initiated an explicit '
                                                      'striptease and prompted Rohan to undress. The call was abruptly '
                                                      'disconnected after 30 seconds. Minutes later, Rohan received a '
                                                      'WhatsApp message from an unknown number containing a screen '
                                                      "recording of the video call with Rohan's face morphed next to "
                                                      'explicit pornographic footage. The blackmailer demanded Rs. '
                                                      "35,000 via UPI within 30 minutes, threatening: 'If you don't "
                                                      'pay immediately, we will upload this video to YouTube and send '
                                                      "it to your college professors and your mother's Facebook "
                                                      "account.' Terrified of public humiliation, Rohan is "
                                                      'contemplating borrowing money.',
                                             'title': 'Instagram Video Call Honeytrap & Morphed Intimate Image '
                                                      'Blackmail'},
    'case_16_hostel_ragging_torture': {   'category': 'Workplace & College Harassment',
                                          'difficulty': 'Emergency',
                                          'educational_breakdown': {   'case_summary': 'Brutal nighttime hostel '
                                                                                       'ragging causing bone fracture '
                                                                                       'using iron rods, compounded by '
                                                                                       "college administration's "
                                                                                       'illegal threats and '
                                                                                       'suppression.',
                                                                       'common_misconceptions': "Myth: 'Ragging is "
                                                                                                'harmless '
                                                                                                'senior-junior '
                                                                                                "bonding.' Reality: "
                                                                                                'Ragging causing '
                                                                                                'bodily hurt is a '
                                                                                                'non-bailable criminal '
                                                                                                'offence resulting in '
                                                                                                'jail and automatic '
                                                                                                'lifetime cancellation '
                                                                                                'of college degrees.',
                                                                       'constitutional_analysis': 'Article 21 (Right '
                                                                                                  'to life, bodily '
                                                                                                  'security, and human '
                                                                                                  'dignity as affirmed '
                                                                                                  'in Vishwa Jagriti '
                                                                                                  'Mission v. Central '
                                                                                                  'Govt).',
                                                                       'court_precedents': 'Vishwa Jagriti Mission v. '
                                                                                           'Central Govt (2001) SC - '
                                                                                           'Supreme Court framed '
                                                                                           'historic guidelines '
                                                                                           'outlawing ragging and '
                                                                                           'placing institutional '
                                                                                           'liability on colleges.',
                                                                       'evidence_preservation_protocol': 'Hospital '
                                                                                                         'Medico-Legal '
                                                                                                         'Certificate '
                                                                                                         '(MLC) and '
                                                                                                         'X-ray '
                                                                                                         'showing '
                                                                                                         'fractured '
                                                                                                         'bone, photos '
                                                                                                         'of injuries '
                                                                                                         'and torn '
                                                                                                         'clothes, '
                                                                                                         'names and '
                                                                                                         'room numbers '
                                                                                                         'of senior '
                                                                                                         'perpetrators, '
                                                                                                         'call '
                                                                                                         'recordings '
                                                                                                         'of '
                                                                                                         "Principal's "
                                                                                                         'threats.',
                                                                       'immediate_action_protocol': '1. Secure '
                                                                                                    'emergency '
                                                                                                    'orthopedic '
                                                                                                    'medical treatment '
                                                                                                    'and obtain '
                                                                                                    'hospital MLC; 2. '
                                                                                                    'Call National '
                                                                                                    'Anti-Ragging '
                                                                                                    'Helpline '
                                                                                                    '1800-180-5522; 3. '
                                                                                                    'Lodge direct FIR '
                                                                                                    'at jurisdictional '
                                                                                                    'Police Station; '
                                                                                                    '4. Submit written '
                                                                                                    'complaint to '
                                                                                                    'District '
                                                                                                    'Collector & SP.',
                                                                       'key_takeaways': [   'Colleges must file an FIR '
                                                                                            'within 24 hours under '
                                                                                            'Regulation 7 UGC 2009.',
                                                                                            'National Anti-Ragging '
                                                                                            'Helpline 1800-180-5522 '
                                                                                            'triggers administrative '
                                                                                            'probes.',
                                                                                            'Using weapons and '
                                                                                            'breaking bones is '
                                                                                            'punishable up to 10 years '
                                                                                            'under Section 118 BNS.'],
                                                                       'legal_classification': 'Aggravated Criminal '
                                                                                               'Offences (Grievous '
                                                                                               'Hurt & Confinement) '
                                                                                               'and Severe Regulatory '
                                                                                               'Violation (UGC '
                                                                                               'Anti-Ragging '
                                                                                               'Regulations).',
                                                                       'remedies_against_refusal': 'If local thana '
                                                                                                   'hesitates due to '
                                                                                                   'political '
                                                                                                   'pressure, report '
                                                                                                   'directly to the '
                                                                                                   'District '
                                                                                                   'Magistrate and '
                                                                                                   'UGC, who have '
                                                                                                   'power to dispatch '
                                                                                                   'central inquiry '
                                                                                                   'teams and withhold '
                                                                                                   'all university '
                                                                                                   'recognition.',
                                                                       'reporting_forums': 'National Anti-Ragging '
                                                                                           'Helpline (1800-180-5522 / '
                                                                                           'helpline@antiragging.in), '
                                                                                           'Local Police Station (FIR '
                                                                                           'under S. 118 BNS), '
                                                                                           'District Magistrate / '
                                                                                           'Collector, University '
                                                                                           'Grants Commission (UGC).',
                                                                       'statutory_provisions': 'UGC Anti-Ragging '
                                                                                               'Regulations 2009; BNS '
                                                                                               'Section 117 & 118 '
                                                                                               '(Grievous Hurt by '
                                                                                               'weapon), Section 127 '
                                                                                               '(Wrongful '
                                                                                               'Confinement), Section '
                                                                                               '351 (Intimidation); '
                                                                                               'State Anti-Ragging '
                                                                                               'Act.',
                                                                       'victim_support_compensation': 'Victim '
                                                                                                      'compensation '
                                                                                                      'from DLSA under '
                                                                                                      'Section 396 '
                                                                                                      'BNSS, college '
                                                                                                      'refund of fees, '
                                                                                                      'and priority '
                                                                                                      'transfer to '
                                                                                                      'another college '
                                                                                                      'under UGC '
                                                                                                      'directions.'},
                                          'id': 'case_16_hostel_ragging_torture',
                                          'questions': [   {   'correct_index': 0,
                                                               'explanation': 'Regulation 7 of the UGC 2009 '
                                                                              'Regulations mandates that the Head of '
                                                                              'the Institution MUST file an FIR with '
                                                                              'the local police within 24 hours of '
                                                                              'receiving information about a ragging '
                                                                              'incident.',
                                                               'options': [   'Within 24 hours of receiving '
                                                                              'information regarding ragging',
                                                                              'Within 30 days after forming a '
                                                                              'fact-finding committee',
                                                                              'Colleges are not required to file FIRs '
                                                                              'for ragging',
                                                                              'Only after the academic year concludes'],
                                                               'question': 'Under UGC Regulations on Curbing the '
                                                                           'Menace of Ragging in Higher Educational '
                                                                           'Institutions, 2009, what is the mandatory '
                                                                           'time limit for the Principal to file an '
                                                                           'FIR with police?'},
                                                           {   'correct_index': 1,
                                                               'explanation': 'Under Supreme Court directives in '
                                                                              'Vishwa Jagriti Mission and UGC '
                                                                              'Regulations, failure by college '
                                                                              'authorities to report ragging leads to '
                                                                              'cancellation of university grants, loss '
                                                                              'of recognition, and personal criminal '
                                                                              'culpability for abetment/evidence '
                                                                              'concealment.',
                                                               'options': [   'No liability, principals have '
                                                                              'administrative discretion',
                                                                              'Institutional de-recognition, '
                                                                              'withdrawal of UGC funding, and personal '
                                                                              'criminal prosecution under the State '
                                                                              'Anti-Ragging Act and Section 238 BNS '
                                                                              '(causing disappearance of evidence)',
                                                                              'A Rs. 100 library fine',
                                                                              'An award for maintaining campus peace'],
                                                               'question': 'What legal liability does the College '
                                                                           'Principal face for attempting to cover up '
                                                                           'the ragging and suppress the FIR?'},
                                                           {   'correct_index': 0,
                                                               'explanation': 'The National Anti-Ragging Helpline '
                                                                              '(1800-180-5522 / '
                                                                              'helpline@antiragging.in) operates 24x7, '
                                                                              'accepts anonymous complaints, and '
                                                                              'instantly notifies the District '
                                                                              'Collector, SP, and UGC nodal monitoring '
                                                                              'cell.',
                                                               'options': [   'National Anti-Ragging Helpline at '
                                                                              '1800-180-5522 (or email '
                                                                              'helpline@antiragging.in)',
                                                                              'Weather forecast helpline',
                                                                              'Railway reservation desk',
                                                                              'Election Commission helpline 1950'],
                                                               'question': 'What immediate national 24x7 toll-free '
                                                                           'helpline can Prateek call to trigger a '
                                                                           'direct inspection by the District '
                                                                           'Magistrate and UGC?'},
                                                           {   'correct_index': 1,
                                                               'explanation': 'Fracturing a bone is Grievous Hurt (S. '
                                                                              '117 BNS), and using iron rods elevates '
                                                                              'it to Section 118 BNS (punishable up to '
                                                                              '10 years). Locking in rooms is Wrongful '
                                                                              'Confinement (S. 127 BNS).',
                                                               'options': [   'Simple breach of hostel quiet hours',
                                                                              'Voluntarily causing Grievous Hurt by '
                                                                              'dangerous weapons (Section 118 BNS), '
                                                                              'Wrongful Confinement (Section 127 BNS), '
                                                                              'and Rioting (Section 191 BNS)',
                                                                              'Defamation under Section 356 BNS',
                                                                              'Copyright infringement'],
                                                               'question': 'What criminal offences under the BNS apply '
                                                                           'to the senior students who used iron '
                                                                           'curtain rods and caused a collarbone '
                                                                           'fracture?'},
                                                           {   'correct_index': 1,
                                                               'explanation': 'Under Regulation 9 of UGC Regulations, '
                                                                              'proven perpetrators of ragging face '
                                                                              'mandatory rustication, expulsion from '
                                                                              'hostel, and nationwide blacklisting '
                                                                              'across higher education institutions.',
                                                               'options': [   'Written apology letter only',
                                                                              'Immediate suspension, rustication from '
                                                                              'the institution, expulsion from hostel, '
                                                                              'and debarment from admission to any '
                                                                              'other institution for up to 5 years',
                                                                              '50 push-ups on the playground',
                                                                              'Re-allocation to an air-conditioned '
                                                                              'room'],
                                                               'question': 'What statutory administrative punishments '
                                                                           'MUST the college Anti-Ragging Committee '
                                                                           'impose on the guilty students?'}],
                                          'story': 'Prateek, an 18-year-old first-year mechanical engineering student '
                                                   'at a residential engineering college, was summoned to the senior '
                                                   'hostel room at 1:00 AM by a group of third-year students. For '
                                                   'three consecutive nights, Prateek was forced to strip naked, '
                                                   'perform humiliating acts, and was beaten with iron curtain rods '
                                                   'when he refused. On the third night, a blow from a curtain rod '
                                                   'fractured his left collarbone. Prateek was smuggled out to a local '
                                                   "hospital by his roommate. When Prateek's father met the College "
                                                   "Principal and Hostel Warden, the Principal said: 'If you file a "
                                                   "police complaint, our college's NBA accreditation will be "
                                                   "cancelled, your son's engineering career will be destroyed, and "
                                                   'local political leaders backing the senior boys will ensure he '
                                                   'cannot study anywhere. Let us settle this as an internal hostel '
                                                   "brawl.'",
                                          'title': 'Severe College Hostel Ragging, Physical Battery & Administrative '
                                                   'Cover-Up'}}
