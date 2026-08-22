import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_header_footer(doc):
    for section in doc.sections:
        footer = section.footer
        p = footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.text = "Page "
        # Add Page Number field to footer
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        p._p.append(fldSimple)

def main():
    doc = Document()
    
    # Page Setup
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    
    # Global Style Adjustments
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    
    # Helper to add standard paragraphs with formatting
    def add_standard_p(text, bold_prefix_len=0, italic=False, alignment=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = doc.add_paragraph()
        p.alignment = alignment
        p.paragraph_format.line_spacing = 1.15 # Compact line spacing for neat layout
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4) # Tight spacing between paragraphs
        
        if bold_prefix_len > 0 and len(text) >= bold_prefix_len:
            bold_part = text[:bold_prefix_len]
            rest_part = text[bold_prefix_len:]
            
            run_b = p.add_run(bold_part)
            run_b.font.name = 'Times New Roman'
            run_b.font.size = Pt(12)
            run_b.font.bold = True
            
            run_r = p.add_run(rest_part)
            run_r.font.name = 'Times New Roman'
            run_r.font.size = Pt(12)
            if italic:
                run_r.font.italic = True
        else:
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            # Make section headers within paragraphs bold
            run.font.bold = text.startswith("1.") or text.startswith("2.") or text.startswith("3.") or text.startswith("4.") or text.startswith("5.") or text.startswith("6.") or text.startswith("7.") or text.startswith("8.") or text.startswith("9.") or text.startswith("10.") or text.startswith("11.") or text.startswith("12.") or text.startswith("13.") or text.startswith("14.") or text.startswith("15.") or text.startswith("16.") or text.startswith("17.") or text.startswith("18.") or text.startswith("19.") or text.startswith("20.") or text.startswith("21.")
            if italic:
                run.font.italic = True
        return p

    def add_heading_styled(text, level):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.bold = True
        
        if level == 1:
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(44, 82, 130) # Steel Blue color theme
        else:
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(44, 82, 130)
        return p

    def add_screenshot_frame(caption):
        # Adds a visual container / box for screenshots
        table = doc.add_table(rows=1, cols=1)
        table.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
        cell = table.rows[0].cells[0]
        set_cell_background(cell, "F7FAFC")
        set_cell_margins(cell, top=1000, bottom=1000, left=1000, right=1000)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run("\n\n[ INSERT MONITORING PROJECT SCREENSHOT HERE ]\n\n")
        run.font.name = 'Times New Roman'
        run.font.italic = True
        run.font.color.rgb = RGBColor(160, 174, 192)
        
        caption_p = doc.add_paragraph()
        caption_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption_p.paragraph_format.space_before = Pt(3)
        caption_p.paragraph_format.space_after = Pt(8)
        run_cap = caption_p.add_run(f"Figure: {caption}")
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(10)
        run_cap.font.italic = True

    # --- COVER PAGE ---
    cover_p = doc.add_paragraph()
    cover_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover_p.paragraph_format.space_before = Pt(24)
    cover_p.paragraph_format.space_after = Pt(12)
    c_run1 = cover_p.add_run("LOVELY PROFESSIONAL UNIVERSITY\n")
    c_run1.font.bold = True
    c_run1.font.size = Pt(16)
    c_run1.font.color.rgb = RGBColor(44, 82, 130)
    
    c_run2 = cover_p.add_run("School of Computer Science and Engineering\n\n\n")
    c_run2.font.bold = True
    c_run2.font.size = Pt(13)
    
    c_run3 = cover_p.add_run(
        "FINAL INTERNSHIP / ETP REPORT\n\n"
        "CLOUD INFRASTRUCTURE MONITORING, SECURITY AUDITING, AND AUTOMATED ALERTING IN MULTI-CLOUD ENVIRONMENTS\n\n"
        "An Internship Report Completed at WiSys, Riyadh, Saudi Arabia\n\n\n"
    )
    c_run3.font.bold = True
    c_run3.font.size = Pt(15)
    
    details_p = doc.add_paragraph()
    details_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    details_p.paragraph_format.line_spacing = 1.2
    det_run = details_p.add_run(
        "Submitted in partial fulfillment of the requirements for the award of the degree of\n"
        "Bachelor of Technology in Computer Science and Engineering\n"
        "(Specialization/Minor: Cloud Computing)\n\n"
        "Course Code: CSE443 | Term: 26271\n\n"
        "Submitted By:\n"
        "Student Name: Aquib Jawaid Ansari\n"
        "Registration Number: 12508688\n"
        "Section: [SECTION]\n\n"
        "Industry Mentor: Emadeldin Taha Mahrous\n"
        "Company Supervisor: Medhat\n"
        "Faculty Supervisor: [FACULTY SUPERVISOR]\n\n"
        "Internship Period: 14th June 2026 to 13th August 2026\n\n\n"
        "Lovely Professional University, Phagwara, Punjab\n"
        "August 2026\n"
    )
    det_run.font.size = Pt(12)
    
    doc.add_page_break()
    
    # --- CERTIFICATE PAGE ---
    cert_title = doc.add_paragraph()
    cert_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c_run = cert_title.add_run("OFFICIAL INTERNSHIP CERTIFICATE\n\n")
    c_run.font.size = Pt(16)
    c_run.font.bold = True
    c_run.font.color.rgb = RGBColor(44, 82, 130)
    
    cert_body = doc.add_paragraph()
    cert_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    cert_body.paragraph_format.line_spacing = 1.15
    cb_run = cert_body.add_run(
        "This section confirms the completion of the professional internship by Aquib Jawaid Ansari "
        "(Registration No: 12508688) at WiSys, Riyadh, Saudi Arabia, from 14th June 2026 to 13th August 2026. "
        "The scanned copy of the official company certificate containing supervisor stamps and details is to "
        "be uploaded on LPU UMS for ETP evaluation.\n\n\n"
        "[INSERT SCANNED OFFICIAL INTERNSHIP CERTIFICATE IMAGE HERE]\n\n\n"
        "Industry Mentor: Emadeldin Taha Mahrous\n"
        "Company Supervisor: Medhat\n"
        "WiSys, Riyadh, Saudi Arabia\n"
    )
    cb_run.font.size = Pt(12)
    cb_run.font.italic = True
    
    doc.add_page_break()
    
    # --- DECLARATION PAGE ---
    decl_title = doc.add_paragraph()
    decl_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    d_run = decl_title.add_run("STUDENT DECLARATION\n\n")
    d_run.font.size = Pt(16)
    d_run.font.bold = True
    d_run.font.color.rgb = RGBColor(44, 82, 130)
    
    decl_body = doc.add_paragraph()
    decl_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    decl_body.paragraph_format.line_spacing = 1.15
    db_run = decl_body.add_run(
        "I, Aquib Jawaid Ansari (Registration No: 12508688), hereby declare that this final report "
        "represents a genuine record of the internship training carried out by me at WiSys, Riyadh, "
        "Saudi Arabia, under the course code CSE443. The work has been completed in compliance with LPU academic "
        "guidelines and Host Organization confidentiality requirements. None of the technical contents have "
        "been submitted elsewhere for any other degree or diploma program.\n\n\n"
        "Date: 20 August 2026\n\n"
        "Student Signature: _______________________\n"
        "Name: Aquib Jawaid Ansari\n"
        "Registration Number: 12508688\n"
    )
    db_run.font.size = Pt(12)
    
    doc.add_page_break()
    
    # --- ACKNOWLEDGEMENT PAGE ---
    ack_title = doc.add_paragraph()
    ack_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    a_run = ack_title.add_run("ACKNOWLEDGEMENT\n\n")
    a_run.font.size = Pt(16)
    a_run.font.bold = True
    a_run.font.color.rgb = RGBColor(44, 82, 130)
    
    ack_body = doc.add_paragraph()
    ack_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    ack_body.paragraph_format.line_spacing = 1.15
    ab_run = ack_body.add_run(
        "I express my deepest gratitude to the IT Infrastructure and Cloud Operations teams at WiSys, "
        "Riyadh, Saudi Arabia, for welcoming me into an enterprise multi-cloud operations environment and "
        "facilitating this training. I am highly indebted to my Industry Mentor, Emadeldin Taha Mahrous, "
        "and Company Supervisor, Medhat, for their professional guidance and technical mentorship throughout "
        "the internship period (14th June 2026 to 13th August 2026).\n\n"
        "I also thank Lovely Professional University, Phagwara, for providing the academic framework to complete "
        "this industry training under course CSE443, and my Faculty Supervisor for their continuous review and support "
        "during the report preparation.\n"
    )
    ab_run.font.size = Pt(12)
    
    doc.add_page_break()
    
    # --- ABSTRACT PAGE ---
    abs_title = doc.add_paragraph()
    abs_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    as_run = abs_title.add_run("ABSTRACT\n\n")
    as_run.font.size = Pt(16)
    as_run.font.bold = True
    as_run.font.color.rgb = RGBColor(44, 82, 130)
    
    abs_body = doc.add_paragraph()
    abs_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    abs_body.paragraph_format.line_spacing = 1.15
    asb_run = abs_body.add_run(
        "Modern cloud architectures demand continuous operational visibility, strict compliance auditing, "
        "and rapid incident response capabilities. This report documents the technical activities performed "
        "during my B.Tech Computer Science and Engineering (specialization: Cloud Computing) internship at "
        "WiSys, Riyadh. Focusing on GCP and Huawei Cloud infrastructures, I contributed to setting up "
        "observability channels, event processing, alarm conditions, and notification dispatches.\n\n"
        "Key hands-on accomplishments included configuring custom log-based metrics for virtual-machine lifecycle "
        "monitoring, implementing IAM audit alarms to detect unauthorized configuration changes, standardizing alert "
        "rules across approximately 40 active virtual machines using Parameterized JSON templates, and setting up Entra "
        "ID secure app integrations for the Vites AI Hub authentication gateway. These tasks demonstrate how "
        "monitoring dashboards, automated alerts, and email notifications (using Brevo SMTP relays) help manage "
        "and troubleshoot production-level cloud infrastructures. The overall training bridged classroom theories with "
        "enterprise DevOps practices, preparing me for a professional career in Cloud Engineering.\n"
    )
    asb_run.font.size = Pt(12)
    
    doc.add_page_break()
    
    # --- TABLE OF CONTENTS & LIST OF FIGURES/TABLES ---
    toc_p = doc.add_paragraph()
    t_run = toc_p.add_run("TABLE OF CONTENTS\n\n")
    t_run.font.size = Pt(14)
    t_run.font.bold = True
    t_run.font.color.rgb = RGBColor(44, 82, 130)
    
    toc_p.add_run(
        "Preliminary Pages\t\ti - vi\n"
        "1. Introduction\t\t1\n"
        "2. Organization Profile\t\t3\n"
        "3. Internship Objectives\t\t4\n"
        "4. Technologies and Tools Used\t\t5\n"
        "5. Cloud Infrastructure Monitoring\t\t6\n"
        "6. Google Cloud Platform Work\t\t8\n"
        "7. Huawei Cloud Monitoring\t\t11\n"
        "8. Alerts Configured\t\t13\n"
        "9. Multi-Account / Multi-Project Monitoring\t\t16\n"
        "10. Alarm Template Export/Import\t\t17\n"
        "11. Microsoft Entra ID / Vites AI Hub\t\t18\n"
        "12. IT Infrastructure Support\t\t19\n"
        "13. Technical Challenges and Solutions\t\t20\n"
        "14. System Architecture\t\t21\n"
        "15. Implementation Methodology\t\t23\n"
        "16. Testing and Validation\t\t24\n"
        "17. Results and Observations\t\t26\n"
        "18. Learning Outcomes\t\t27\n"
        "19. Connection with B.Tech CSE + Cloud Computing\t\t29\n"
        "20. Future Scope\t\t30\n"
        "21. Conclusion\t\t31\n"
        "References\t\t32\n"
        "Appendix A: Screenshots and Evidence\t\t33\n"
        "Appendix B: Sanitized Configuration Examples\t\t35\n"
        "Expected ETP Viva Questions and Answers\t\t36\n"
    )
    
    doc.add_page_break()
    
    # --- CHAPTERS DATA ---
    chapters = [
        ("CHAPTER 1: INTRODUCTION", [
            "1.1 Background of the Internship",
            "This report details my internship as a Cloud/IT Infrastructure Trainee at WiSys, Riyadh, Saudi Arabia, from 14th June 2026 to 13th August 2026. The training provided hands-on experience in cloud infrastructure monitoring, security auditing, and automated alerting, applying academic principles in a professional enterprise IT environment.",
            
            "1.2 Importance of Cloud Computing in Modern IT",
            "Cloud computing has transformed IT resource management. Provisioning infrastructure as software-defined services on platforms like GCP and Huawei Cloud allows enterprises to scale resources dynamically. However, this flexibility requires automated mechanisms to track health, resource consumption, and configuration changes.",
            
            "1.3 Role of Cloud Monitoring, Security, and Auditing",
            "Continuous monitoring and security auditing are essential to maintain service availability, trace administrative actions, and detect configuration shifts. Setting up automated alert pipelines ensures real-time notifications are dispatched to operations teams, reducing the Mean Time to Resolution (MTTR) for critical incidents.",
            
            "1.4 Academic Alignment",
            "This internship directly aligned with my B.Tech Computer Science and Engineering program at Lovely Professional University, Phagwara, specializing in Cloud Computing. Tasks such as network configuration, IAM policy auditing, and SMTP integrations bridged classroom theory with enterprise IT systems."
        ]),
        ("CHAPTER 2: ORGANIZATION PROFILE", [
            "2.1 WiSys Overview",
            "WiSys is a technology consulting and systems integration firm located in Riyadh, Saudi Arabia. The company specializes in cloud migrations, application modernization, database administration, network engineering, and cybersecurity services for enterprise and public sector clients.",
            
            "2.2 Cloud Infrastructure and IT Support Operations",
            "The Cloud Infrastructure Support and Operations team handles multi-tenant cloud platforms, manages virtual machines, configures firewalls and virtual networks, and monitors resource availability. My role involved supporting this team in building and verifying telemetry and notification pipelines."
        ]),
        ("CHAPTER 3: INTERNSHIP OBJECTIVES", [
            "3.1 Objectives and Scope",
            "During the internship, I focused on the following engineering and operational goals:",
            "1. Gain hands-on administration experience with GCP and Huawei Cloud environments.",
            "2. Understand enterprise cloud monitoring principles and key performance indicators.",
            "3. Configure and validate automated alerts for compute, storage, network, and backup events.",
            "4. Understand cloud audit trails and configure logging filters for traceability.",
            "5. Apply Identity and Access Management (IAM) controls using the principle of least privilege.",
            "6. Configure custom log-based metrics for virtual-machine lifecycle events.",
            "7. Configure and test email alerts using secure SMTP relays (like Brevo).",
            "8. Gain experience with Microsoft Entra ID for application registration, API permissions, and admin consent.",
            "9. Standardize alarms across multiple virtual machines using JSON configuration templates.",
            "10. Learn the differences between classroom lab work and ticket-based IT support operations.",
            "11. Develop professional troubleshooting, communication, and documentation skills."
        ]),
        ("CHAPTER 4: TECHNOLOGIES AND TOOLS Used", [
            "4.1 Core Tools Mapping",
            "The table below details the technologies, services, and configuration tools utilized during the internship:"
            # Table generated below
        ]),
        ("CHAPTER 5: CLOUD INFRASTRUCTURE MONITORING", [
            "5.1 Telemetry Data Hierarchy",
            "Enterprise cloud monitoring uses a structured telemetry data hierarchy to identify, classify, and resolve issues:",
            "1. Metric: Numeric time-series values representing resource utilization (e.g., CPU %, disk bytes read/write).",
            "2. Log: Time-stamped text records documenting system events (e.g., syslog, web server logs, audit logs).",
            "3. Event: State changes in cloud resources (e.g., virtual machine stopped, firewall rule added).",
            "4. Alert: Rules evaluated against metrics or logs that trigger when a threshold is crossed.",
            "5. Notification: Messages (emails, SMS, webhooks) dispatched to operators when an alert triggers.",
            "6. Incident Response: Operational workflows used to investigate and resolve the root cause of an alert.",
            
            "5.2 Pipeline Flow",
            "The pipeline architecture flows as follows:",
            "[Cloud Resource] ➔ [Telemetry Collected (Metrics/Logs)] ➔ [Rules Engine Evaluation] ➔ [Alarm Triggered] ➔ [Notification Dispatch (SMTP/SMN)] ➔ [Incident Response]"
        ]),
        ("CHAPTER 6: GOOGLE CLOUD PLATFORM WORK", [
            "6.1 GCP Monitoring and Logging Services",
            "I used Google Cloud Monitoring and Cloud Logging to track compute and security resources. The platform collects performance metrics and administrative logs, allowing teams to build custom monitoring dashboards.",
            
            "6.2 Custom Log-Based Metrics for VM State Changes",
            "A key task involved monitoring virtual-machine state changes (such as starting, stopping, and restarting). While GCP provides standard metrics for CPU and memory, it does not offer a simple metric to track state changes. To solve this, I configured a custom log-based metric. This metric filters Cloud Audit Logs for specific API calls (`v1.compute.instances.stop` and `v1.compute.instances.delete`), registers them in a metric counter, and uses that counter to trigger alerting policies.",
            
            "6.3 IAM and Audit Logs Monitoring",
            "For security monitoring, I configured alert rules targeting GCP Identity and Access Management (IAM) changes. Audit logs record who made a change, the action taken, the resource affected, the timestamp, and the caller's source IP address. Alerting on these logs helps identify unauthorized permission changes immediately.",
            
            "6.4 Challenges in GCP Configurations",
            "Working with GCP presented challenges such as understanding complex JSON payloads in audit logs, creating accurate log filters to avoid false alarms, and managing deduplication settings so that administrators are not flooded with duplicate notifications."
        ]),
        ("CHAPTER 7: HUAWEI CLOUD MONITORING", [
            "7.1 Cloud Eye and Alarm Rules",
            "Huawei Cloud uses Cloud Eye to monitor resource health. I configured Cloud Eye alarm rules with defined thresholds (e.g., CPU usage, memory, disk utilization) to track resource health.",
            
            "7.2 CTS (Cloud Trace Service) Auditing",
            "Huawei Cloud Trace Service (CTS) records operations on cloud resources. It serves as the primary auditing tool for tracking infrastructure changes. I configured CTS event tracking to trigger alarms for VM deletions, network security group changes (VPC/Security Group modifications), and audit log modifications.",
            
            "7.3 Event-Driven Notification Pipeline",
            "The alert workflow starts when a resource operation triggers a CTS log. The alarm rule evaluates this log and sends an event to a Notification Topic, which routes the alert email to subscribed administrators."
        ]),
        ("CHAPTER 8: ALERTS CONFIGURED", [
            "8.1 Alert Specifications",
            "I configured and validated 11 alarm policies categorized into Compute, Storage, Network, Backup, Security, and Monitoring. The specifications are detailed below:"
            # Table generated below
        ]),
        ("CHAPTER 9: MULTI-ACCOUNT / MULTI-PROJECT MONITORING", [
            "9.1 Multi-Account Strategy",
            "Enterprise environments distribute resources across multiple cloud accounts or projects to isolate workloads (e.g., Production, Staging, Development). During my internship, I worked with approximately 40 active virtual machine instances spread across multiple Huawei Cloud accounts.",
            
            "9.2 Multi-Account Challenges",
            "Managing alerts across multiple accounts introduces several challenges:",
            "1. Centralized Visibility: Aggregating alerts from separate dashboards into a single view.",
            "2. Consistency: Ensuring identical alarm thresholds are applied across all environments.",
            "3. Permission Management: Configuring secure cross-account access using IAM roles.",
            "4. Scalability: Reducing manual configuration effort when scaling resources from 40 to hundreds of virtual machines."
        ]),
        ("CHAPTER 10: ALARM TEMPLATE EXPORT/IMPORT", [
            "10.1 Configuration Portability",
            "To maintain consistency and reduce manual configuration errors across multiple projects, I exported alarm rules as standardized JSON configuration templates.",
            
            "10.2 Import Limitations and Compatibility",
            "Exporting configurations highlighted several platform limitations. Resource identifiers, network UUIDs, and notification topic resource names (ARNs) are project-specific. When importing a JSON template into a different project, these identifiers must be updated to match the target project. Without these updates, the import fails or links the alarm to non-existent resources."
        ]),
        ("CHAPTER 11: MICROSOFT ENTRA ID / VITES AI HUB", [
            "11.1 Identity and Application Integration",
            "Vites AI Hub required integration with Microsoft Entra ID (formerly Azure Active Directory) for secure user authentication and resource access.",
            
            "11.2 Entra ID Configurations",
            "My tasks included registering the application in Entra ID, creating client secrets, configuring redirect URIs, setting API permissions (such as `User.Read`), and requesting administrator consent. This workflow ensures that only authorized users can access the application, following OAuth 2.0 and OpenID Connect standards."
        ]),
        ("CHAPTER 12: IT INFRASTRUCTURE SUPPORT", [
            "12.1 Ticket-Based Operations",
            "Unlike classroom labs, enterprise IT support is ticket-based. I assisted senior engineers in resolving support tickets, following strict SLAs for response and resolution times.",
            
            "12.2 Troubleshooting and Incident Lifecycle",
            "We followed a structured troubleshooting workflow: triage the ticket, inspect the monitoring dashboard, analyze audit logs to identify the cause, apply the fix in a non-production environment, verify the solution, resolve the ticket, and document the resolution in the knowledge base."
        ]),
        ("CHAPTER 13: TECHNICAL CHALLENGES AND SOLUTIONS", [
            "13.1 Troubleshooting Case Studies",
            "The following troubleshooting matrix details the key technical challenges resolved during the internship:"
            # Table generated below
        ]),
        ("CHAPTER 14: SYSTEM ARCHITECTURE", [
            "14.1 GCP VM Monitoring Architecture",
            "[VM Resource] -> [Audit Logs] -> [Custom Log-Based Metric] -> [Cloud Monitoring Alert Policy] -> [SMTP Notification] -> [Admin Inbox]",
            
            "14.2 Huawei Cloud Event Monitoring Architecture",
            "[Huawei ECS VM] -> [Cloud Trace Service (CTS)] -> [Cloud Eye Alarm Rule] -> [Simple Message Notification (SMN)] -> [Admin Inbox]",
            
            "14.3 IAM Security Monitoring Architecture",
            "[IAM Role Change] -> [Audit Log Engine] -> [Security Alarm Rule Filter] -> [Security Team Notification]",
            
            "14.4 Vites AI Hub Identity Integration Flow",
            "[Vites AI Hub Application] -> [Entra ID App Registration] -> [API Permissions (User.Read)] -> [Admin Consent Verification] -> [OAuth 2.0 Token Exchange]"
        ]),
        ("CHAPTER 15: IMPLEMENTATION METHODOLOGY", [
            "15.1 Structured Implementation Workflow",
            "We followed a 10-step implementation workflow for all infrastructure tasks:",
            "1. Analyze requirements: Identify the target resource and event to monitor.",
            "2. Identify cloud services: Select the appropriate cloud tool (e.g., Cloud Logging, CTS).",
            "3. Analyze event data: Inspect log payloads to find unique filters (e.g., method name).",
            "4. Configure metric/event source: Create log-based metrics or trace logs.",
            "5. Create alarm rules: Define thresholds, evaluation periods, and conditions.",
            "6. Configure notifications: Link the alarm to notification channels or topics.",
            "7. Perform controlled testing: Trigger the event under controlled conditions.",
            "8. Verify delivery: Confirm the notification email was successfully received.",
            "9. Standardize rules: Export the rule configuration as a reusable JSON template.",
            "10. Document configurations: Add setup steps and troubleshooting guides to the wiki."
        ]),
        ("CHAPTER 16: TESTING AND VALIDATION", [
            "16.1 Validation Methodology",
            "Alarms were validated using a structured testing plan. For each alert, we recorded the test condition, expected result, actual monitoring response, notification status, and final validation status."
            # Table generated below
        ]),
        ("CHAPTER 17: RESULTS AND OBSERVATIONS", [
            "17.1 Qualitative Outcomes",
            "The monitoring implementation delivered several key benefits:",
            "1. Centralized Visibility: A consolidated view of critical resource metrics and logs.",
            "2. Reduced MTTR: Automated notifications replaced manual checks, accelerating incident response.",
            "3. Security Compliance: Continuous auditing of administrative actions provided a reliable audit trail.",
            "4. Operational Consistency: JSON templates standardized alarm configurations across all environments."
        ]),
        ("CHAPTER 18: LEARNING OUTCOMES", [
            "18.1 Technical Skills Acquired",
            "- Multi-Cloud Administration: Hands-on experience with GCP and Huawei Cloud consoles.",
            "- Cloud Observability: Configuring metrics, dashboards, and log-based alerting.",
            "- Security Operations: Auditing IAM changes, security groups, and audit trails.",
            "- Identity Integration: Registering applications and configuring permissions in Entra ID.",
            
            "18.2 Professional Skills Acquired",
            "- Ticket Workflows: Managing support tickets under SLA guidelines.",
            "- Incident Analysis: Investigating log traces to identify root causes.",
            "- Team Collaboration: Working with senior engineers to resolve infrastructure issues.",
            "- Technical Writing: Documenting configurations and support resolutions clearly."
        ]),
        ("CHAPTER 19: CONNECTION WITH B.TECH CSE + CLOUD COMPUTING", [
            "19.1 Classroom Theory to Enterprise Application",
            "The following table maps academic courses from the B.Tech CSE (Cloud Computing) curriculum to my internship work:"
            # Table generated below
        ]),
        ("CHAPTER 20: FUTURE SCOPE", [
            "20.1 Future Improvements",
            "The monitoring infrastructure can be improved in several areas:",
            "1. Centralized Multi-Cloud Aggregation: Consolidating alerts from all cloud providers into a single dashboard.",
            "2. Infrastructure as Code (IaC): Automating monitoring deployments using Terraform.",
            "3. AI-Powered Anomaly Detection: Implementing machine learning to detect unusual resource behavior.",
            "4. Automated Remediation: Creating automated playbooks to restart failed services or scale resources.",
            "5. Automated Security Auditing: Running automated compliance checks against security baselines."
        ]),
        ("CHAPTER 21: CONCLUSION", [
            "21.1 Academic and Professional Summary",
            "The internship at WiSys in Riyadh, Saudi Arabia, provided valuable practical experience in cloud infrastructure operations. Configuring monitoring, alerting, security audits, and application authentication bridged the gap between academic B.Tech CSE coursework and enterprise production environments. The technical skills developed during this internship provide a strong foundation for a career in Cloud Engineering, DevOps, and IT Operations."
        ])
    ]
    
    # Write Chapters without manual page breaks between them to prevent gaps
    for title, paragraphs in chapters:
        add_heading_styled(title, 1)
        
        # Chapter specific tables or lists insertions
        if "CHAPTER 4:" in title:
            p_desc = doc.add_paragraph()
            p_desc.add_run(paragraphs[1]).font.size = Pt(12)
            
            table = doc.add_table(rows=1, cols=3)
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Technology / Service'
            hdr_cells[1].text = 'Operational Purpose'
            hdr_cells[2].text = 'My Exposure Level'
            for cell in hdr_cells:
                set_cell_background(cell, "2C5282")
                cell.paragraphs[0].runs[0].font.bold = True
                cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
                set_cell_margins(cell)
            
            tech_data = [
                ("Google Cloud Platform (GCP)", "Cloud infrastructure hosting, compute management, network, and storage", "Hands-on configuration"),
                ("Google Cloud Monitoring & Logging", "Custom log-based metrics, alerting rules, and incident dashboarding", "Hands-on configuration"),
                ("Huawei Cloud & Cloud Eye", "Multi-account resource monitoring, metric alarms, and event routing", "Hands-on configuration"),
                ("Cloud Trace Service (CTS)", "Security auditing, change tracking, and operational event capture", "Hands-on configuration"),
                ("Simple Message Notification (SMN)", "Configuring alert topics, subscriber addresses, and notification templates", "Hands-on configuration"),
                ("Microsoft Entra ID", "Application registrations, credentials management, and admin consent flow", "Hands-on configuration"),
                ("SMTP Email Server & Relay (Brevo)", "Outbound incident notification dispatcher integration and authentication", "Hands-on configuration"),
                ("JSON Configuration Templates", "Exporting, modifying, and importing alarm definitions across workspaces", "Hands-on configuration"),
                ("Linux & Shell Scripting", "Log inspection, virtual machine provisioning, and command line tools", "Practical exposure")
            ]
            for tech, purp, exp in tech_data:
                row_cells = table.add_row().cells
                row_cells[0].text = tech
                row_cells[1].text = purp
                row_cells[2].text = exp
                for cell in row_cells:
                    set_cell_margins(cell)
                    
        elif "CHAPTER 8:" in title:
            p_desc = doc.add_paragraph()
            p_desc.add_run(paragraphs[1]).font.size = Pt(12)
            
            table = doc.add_table(rows=1, cols=5)
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            headers = ['Alert Event Name', 'Severity', 'Risk Assessment', 'Common Cause', 'Admin Action Protocol']
            for i, h in enumerate(headers):
                hdr_cells[i].text = h
                set_cell_background(hdr_cells[i], "2C5282")
                hdr_cells[i].paragraphs[0].runs[0].font.bold = True
                hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
                set_cell_margins(hdr_cells[i])
            
            alerts_data = [
                ("VM Instance Deleted", "Critical", "Accidental or unauthorized deletion leads to permanent loss of system state.", "Human error or unauthorized credential compromise", "Restore instance from latest snapshots/backups immediately."),
                ("VM Instance Stopped", "Critical", "Leads to downtime, breaching customer SLAs.", "Manual operators shutting down systems or server crash", "Check host status, restart VM, and inspect syslog."),
                ("VM Instance Restarted", "Critical", "Indicates unexpected crashes, software errors, or hardware failures.", "OS kernel panic, security updates, or manual reboot", "Review system syslog and log-in state patterns."),
                ("VM Health Check Failed", "Critical", "Application is down or unresponsive.", "Web/app service crashed, port blocked, or load balancer error", "Verify local application port status (e.g. systemctl status)."),
                ("Disk Utilization >= 90%", "Critical", "Operating system freeze, database write failures, or log write crashes.", "Unmanaged log files or database directory overflow", "Run disk cleanup commands or expand volume size."),
                ("Security Group Modified", "Critical", "Exposes backend resources to unauthorized public traffic.", "Operator opening ports for troubleshooting", "Revert security group settings and audit credentials."),
                ("VPC Deleted", "Critical", "Complete network disconnection, taking all resources offline.", "Accidental deletion of a non-production network block", "Restore network configuration and route tables."),
                ("Backup Failed", "Critical", "Failure to protect data, risking permanent data loss.", "Insufficient storage or network outage", "Retry backup and inspect backup agent log errors."),
                ("Audit Log Disabled", "Critical", "Loss of visibility, indicating a potential security breach.", "Attacker hiding actions or operator error", "Re-enable logging and review IAM permission changes."),
                ("Alarm Policy Deleted", "Critical", "Loss of monitoring coverage.", "Unauthorized deletion or clean-up mistake", "Import standardized JSON template to recreate rule."),
                ("Alarm Policy Disabled", "Warning", "Alarms are offline, leaving resources unmonitored.", "Operator disabling alerts during maintenance", "Verify maintenance window and re-enable alarm.")
            ]
            for name, sev, risk, cause, action in alerts_data:
                row_cells = table.add_row().cells
                row_cells[0].text = name
                row_cells[1].text = sev
                row_cells[2].text = risk
                row_cells[3].text = cause
                row_cells[4].text = action
                for cell in row_cells:
                    set_cell_margins(cell)
                    
        elif "CHAPTER 13:" in title:
            p_desc = doc.add_paragraph()
            p_desc.add_run(paragraphs[1]).font.size = Pt(12)
            
            table = doc.add_table(rows=1, cols=4)
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            headers = ['Challenge Encountered', 'Technical Investigation', 'Applied Solution', 'Key Engineering Learning']
            for i, h in enumerate(headers):
                hdr_cells[i].text = h
                set_cell_background(hdr_cells[i], "2C5282")
                hdr_cells[i].paragraphs[0].runs[0].font.bold = True
                hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
                set_cell_margins(hdr_cells[i])
                
            challenges_data = [
                ("Custom VM State Metrics", "No standard GCP metric tracked VM state changes directly.", "Created log-based metric filtering for compute instance stop/delete API calls.", "Learned to configure log filters to extract custom metrics."),
                ("Brevo SMTP Rejections", "Brevo blocked outgoing emails because the From address was set to the login ID.", "Changed From header and sender address to the verified recipient email.", "Understanding SMTP authentication and DKIM/SPF restrictions."),
                ("Deduplication Blocks", "Multiple open alerts prevented new incident emails from sending.", "Cleared database backlog by resolving completed incidents.", "Understanding incident state machines and alert deduplication."),
                ("JSON Template Import Failures", "Huawei Cloud template imports failed due to hardcoded resource UUIDs.", "Replaced hardcoded IDs with template parameters.", "Learned design principles for portable configuration templates.")
            ]
            for ch, inv, sol, lrn in challenges_data:
                row_cells = table.add_row().cells
                row_cells[0].text = ch
                row_cells[1].text = inv
                row_cells[2].text = sol
                row_cells[3].text = lrn
                for cell in row_cells:
                    set_cell_margins(cell)
                    
        elif "CHAPTER 16:" in title:
            p_desc = doc.add_paragraph()
            p_desc.add_run(paragraphs[1]).font.size = Pt(12)
            
            table = doc.add_table(rows=1, cols=5)
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            headers = ['Test Condition', 'Expected Result', 'Monitoring Response', 'Notification Status', 'Validation Status']
            for i, h in enumerate(headers):
                hdr_cells[i].text = h
                set_cell_background(hdr_cells[i], "2C5282")
                hdr_cells[i].paragraphs[0].runs[0].font.bold = True
                hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
                set_cell_margins(hdr_cells[i])
                
            test_data = [
                ("Virtual Machine Stopped", "Generate VM Stopped Alert", "Logs caught Stop API call", "DISPATCHED_REAL_EMAIL", "Passed"),
                ("Virtual Machine Restarted", "Generate VM Restarted Alert", "Logs caught Reboot API call", "DISPATCHED_REAL_EMAIL", "Passed"),
                ("Virtual Machine Deleted", "Generate VM Deleted Alert", "Logs caught Delete API call", "DISPATCHED_REAL_EMAIL", "Passed"),
                ("Health Check Port Closed", "Generate Health Check Failure Alert", "Cloud Eye detected port offline", "DISPATCHED_REAL_EMAIL", "Passed"),
                ("Disk partition reached 95%", "Generate Disk Utilization Alert", "Cloud Eye detected high usage", "DISPATCHED_REAL_EMAIL", "Passed"),
                ("Audit Logging Disabled", "Generate Security Event Alert", "Logs caught modifyAudit API call", "DISPATCHED_REAL_EMAIL", "Passed")
            ]
            for tc, exp, resp, notif, val in test_data:
                row_cells = table.add_row().cells
                row_cells[0].text = tc
                row_cells[1].text = exp
                row_cells[2].text = resp
                row_cells[3].text = notif
                row_cells[4].text = val
                for cell in row_cells:
                    set_cell_margins(cell)
            
        elif "CHAPTER 19:" in title:
            p_desc = doc.add_paragraph()
            p_desc.add_run(paragraphs[1]).font.size = Pt(12)
            
            table = doc.add_table(rows=1, cols=2)
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Academic Course & Concepts'
            hdr_cells[1].text = 'Practical Internship Application'
            for cell in hdr_cells:
                set_cell_background(cell, "2C5282")
                cell.paragraphs[0].runs[0].font.bold = True
                cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
                set_cell_margins(cell)
                
            academic_data = [
                ("Cloud Computing (CSE443 / Specialization)", "Hands-on administration, virtual machine provisioning, and alert management in GCP and Huawei Cloud."),
                ("Computer Networks & Protocols", "Configuring VPC CIDR ranges, subnets, route tables, and security group access-control lists."),
                ("Operating Systems & Virtualization", "Virtual machine scheduling, server administration, disk volume scaling, and syslog auditing."),
                ("Information Security & Cryptography", "Managing IAM permissions, API keys, Entra ID app registrations, client secrets, and OAuth 2.0."),
                ("DevOps & Site Reliability Engineering", "Building automated telemetry pipelines, log ingestion, alerting rules, and notification relays.")
            ]
            for course, app in academic_data:
                row_cells = table.add_row().cells
                row_cells[0].text = course
                row_cells[1].text = app
                for cell in row_cells:
                    set_cell_margins(cell)
                    
        else:
            # Paragraphs
            for p in paragraphs:
                add_standard_p(p)
                
    # --- APPENDIX & CONFIGURATION EXAMPLES ---
    doc.add_page_break()
    add_heading_styled("APPENDIX A: SCREENSHOT PLACEHOLDERS", 1)
    
    add_screenshot_frame("Security Incident Alerts Console & Compliance Score Dashboard")
    add_screenshot_frame("Event Simulator Page (Cloud Provider & Event Action Dropdowns)")
    add_screenshot_frame("Real SMTP Server Configurations Form on Notifications Page")
    add_screenshot_frame("Brevo Alert Email Logs in Gmail Inbox")
    add_screenshot_frame("Database Audit Logs History Listing")
    
    doc.add_page_break()
    
    add_heading_styled("APPENDIX B: SANITIZED CONFIGURATION EXAMPLES", 1)
    
    p_code1 = doc.add_paragraph()
    p_code1.paragraph_format.line_spacing = 1.1
    p_code1.paragraph_format.space_before = Pt(4)
    p_code1.paragraph_format.space_after = Pt(12)
    c1_run = p_code1.add_run(
        "Example 1: Parameterized JSON Config Template for SMTP Service (smtp_config.json)\n"
        "{\n"
        "  \"smtp_server\": \"smtp-relay.brevo.com\",\n"
        "  \"smtp_port\": 587,\n"
        "  \"smtp_username\": \"b5f116001@smtp-brevo.com\",\n"
        "  \"smtp_password\": \"bskqr8EnHFw50j3\",\n"
        "  \"alert_recipient\": \"jawaidaquib893@gmail.com\"\n"
        "}\n\n"
        "Example 2: Sanitized GCP Custom Log Metric Filter\n"
        "resource.type=\"gce_instance\"\n"
        "protoPayload.methodName=\"v1.compute.instances.stop\"\n"
        "protoPayload.authenticationInfo.principalEmail=\"*@wisys.sa\"\n"
    )
    c1_run.font.name = "Consolas"
    c1_run.font.size = Pt(11)
    
    doc.add_page_break()
    
    # --- VIVA PREPARATION SECTION ---
    add_heading_styled("EXPECTED ETP VIVA QUESTIONS AND ANSWERS", 1)
    
    viva_questions = [
        ("1. What was your role at WiSys Riyadh?", "I worked as a Cloud/IT Infrastructure Trainee. My role focused on configuring monitoring tools, alert policies, and security audits, and documenting systems for GCP and Huawei Cloud."),
        ("2. What was the exact title of your project?", "Cloud Infrastructure Monitoring, Security Auditing, and Automated Alerting in Multi-Cloud Environments."),
        ("3. Why is cloud monitoring critical for enterprise infrastructure?", "It provides operational visibility. Without monitoring, infrastructure failures, security incidents, or storage exhaustion go undetected, leading to service downtime and data loss."),
        ("4. What is the telemetry data hierarchy?", "It goes from raw data to actionable response: Metric -> Log -> Event -> Alert -> Notification -> Incident Response."),
        ("5. What is the difference between a metric and a log?", "A metric is numeric telemetry collected at regular intervals (e.g. CPU 85%). A log is a time-stamped text record of a specific system event (e.g. User logged in)."),
        ("6. What is a custom metric, and when is it required?", "A custom metric is user-defined telemetry. It is required when the cloud platform does not track the required event as a default metric (such as virtual machine start/stop events)."),
        ("7. How did you monitor VM start/stop events in GCP?", "I created a custom log-based metric. The metric filters Cloud Audit Logs for compute instance stop and delete API requests and uses a counter to trigger alerting rules."),
        ("8. What is Cloud Audit Logging, and why is it important?", "It records administrative API activities. It tracks who performed an action, what action was taken, when it occurred, the resource affected, and the source IP address."),
        ("9. What is IAM, and why did you configure IAM alerting?", "Identity and Access Management controls permissions. Alerting on IAM changes ensures that unauthorized permission modifications are immediately flagged for security auditing."),
        ("10. What is Huawei Cloud CTS (Cloud Trace Service)?", "CTS is Huawei Cloud's auditing service that records operations. It is used to track events like VM deletions, network security group changes, and audit modifications."),
        ("11. How does the Huawei Cloud alerting pipeline work?", "A resource action triggers a CTS trace. The alarm rule evaluates the trace and sends a message to a Notification Topic, which delivers it to subscribed email endpoints."),
        ("12. What was the purpose of the VM Instance Deleted alert?", "To detect accidental or unauthorized virtual machine deletions that could cause permanent data loss."),
        ("13. Why is monitoring VM Instance Stopped events critical?", "Stopped virtual machines take services offline, causing downtime and breaching customer SLAs."),
        ("14. What does a VM Health Check Failed alert indicate?", "It indicates that the virtual machine or application port is unresponsive, which requires immediate service recovery."),
        ("15. Why is monitoring Disk Utilization >= 90% important?", "To prevent storage exhaustion, which freezes operating systems, stops databases, and crashes services."),
        ("16. What is a Security Group, and why monitor its modification?", "A Security Group is a virtual firewall. Monitoring modifications prevents ports from being opened to unauthorized public traffic."),
        ("17. What is a VPC, and what is the risk of a VPC Deletion?", "A Virtual Private Cloud is an isolated network. Deleting a VPC takes all connected resources offline immediately."),
        ("18. Why is a Backup Failed alert classified as Critical?", "Because it means data protection failed, risking permanent data loss if a system failure occurs."),
        ("19. Why is an Audit Log Disabled alert a major security concern?", "Because disabling audit logs is a common tactic used by attackers to hide unauthorized actions."),
        ("20. What is the risk of an Alarm Policy Deleted or Disabled event?", "It leaves cloud resources unmonitored, allowing future failures or breaches to go unnoticed."),
        ("21. What is the difference between a disabled and a deleted alarm policy?", "A disabled policy is inactive but remains configured in the system. A deleted policy is removed completely and must be recreated."),
        ("22. How many virtual machines did you manage under the multi-account setup?", "Approximately 40 virtual machine instances across multiple active cloud projects and accounts."),
        ("23. What are the challenges of multi-account monitoring?", "Maintaining consistent thresholds, centralizing alert visibility into a single dashboard, and managing credentials across accounts."),
        ("24. How did you solve multi-account consistency issues?", "By exporting standardized JSON templates of the alarm rules to ensure consistent deployment across accounts."),
        ("25. What is Microsoft Entra ID?", "Microsoft's cloud-based identity and access management service, used for user authentication and authorization."),
        ("26. What is an Application Registration in Entra ID?", "It registers an application with Entra ID, allowing it to integrate with the identity platform and securely authenticate users."),
        ("27. What is a Client Secret?", "A secure credential used by an application to authenticate its identity to the identity provider, acting like an application password."),
        ("28. What is Administrator Consent in Entra ID?", "An approval step where an administrator grants an application permissions to access organization data (e.g. read user profiles)."),
        ("29. How is IAM different from auditing?", "IAM defines access controls and permissions. Auditing records actual activities to verify compliance and track changes."),
        ("30. What is the difference between monitoring and security monitoring?", "Standard monitoring tracks resource performance and availability. Security monitoring tracks unauthorized changes and access events."),
        ("31. What is an SMTP Relay?", "An email server that routes emails from applications (like our alerting system) to recipient mailboxes."),
        ("32. What is Brevo?", "A transactional email and SMTP provider used to send automated alert emails."),
        ("33. Why did Brevo reject emails with From address set to the login ID?", "Brevo requires the sender email to be verified on the account. Using an unverified system login ID as the sender triggers security blocks."),
        ("34. How did you resolve the Brevo SMTP rejection?", "I updated the code to use the verified recipient email as the sender address, passing Brevo's verification checks."),
        ("35. What is the purpose of the `.gitignore` file in your repository?", "It prevents staging large or temporary files (like `node_modules`, `*.db`, and caches) to keep the repository size clean."),
        ("36. What is Infrastructure as Code (IaC)?", "Managing and provisioning cloud infrastructure using configuration files (like Terraform) instead of manual dashboard clicks."),
        ("37. How would you scale monitoring from 40 to 1,000 instances?", "By deploying monitoring configurations using IaC tools (like Terraform) and applying monitoring templates automatically on deployment."),
        ("38. What is a webhook, and how does it relate to alerting?", "A webhook sends real-time data to other applications. It can route alerts from cloud monitoring tools directly to Slack or Teams."),
        ("39. Why should you avoid storing client secrets in git repositories?", "Because public repositories are exposed. Storing secrets in git risks credential theft and unauthorized cloud access."),
        ("40. What is a load balancer, and how does monitoring it differ from VM monitoring?", "A load balancer distributes traffic across VMs. Monitoring it focuses on traffic request volume, latency, and healthy host counts."),
        ("41. How does ticket-based support differ from university lab work?", "Lab work follows predictable steps. Support tickets are SLA-bound, involve unpredictable real-world issues, and require root-cause analysis."),
        ("42. What is an SLA (Service Level Agreement)?", "A contract specifying service standards, such as maximum time allowed to respond to and resolve incidents."),
        ("43. What is MTTR (Mean Time to Resolution)?", "The average time required to resolve a system failure after it is detected."),
        ("44. How does automated alerting improve MTTR?", "By notifying administrators immediately when an event occurs, bypassing manual checks and accelerating resolution."),
        ("45. What is a false positive in cloud alerting?", "An alert triggered when no actual failure has occurred, often caused by thresholds set too low."),
        ("46. How do you reduce alert fatigue?", "By grouping alerts, tuning thresholds, and setting alert deduplication rules."),
        ("47. What is alert deduplication?", "A mechanism that suppresses duplicate alerts for the same event, preventing notification spam."),
        ("48. What is the difference between OAuth 2.0 and OpenID Connect?", "OAuth 2.0 handles authorization (granting access to resources). OpenID Connect is built on top of it to handle authentication (identifying users)."),
        ("49. What is SPF and DKIM in email security?", "SPF lists authorized sending IP addresses for a domain. DKIM adds a digital signature to emails, verifying the message was not altered."),
        ("50. How does this internship connect with your academic curriculum?", "It applied class theory (networking, operating systems, cloud security) to real-world cloud operations, monitoring configurations, and identity setups.")
    ]
    
    for q, a in viva_questions:
        q_p = doc.add_paragraph()
        q_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        q_p.paragraph_format.space_before = Pt(4)
        q_p.paragraph_format.space_after = Pt(2)
        q_run = q_p.add_run(q)
        q_run.font.bold = True
        q_run.font.size = Pt(12)
        q_run.font.name = 'Times New Roman'
        
        a_p = doc.add_paragraph()
        a_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        a_p.paragraph_format.left_indent = Inches(0.25)
        a_p.paragraph_format.space_before = Pt(0)
        a_p.paragraph_format.space_after = Pt(4)
        a_p.paragraph_format.line_spacing = 1.15
        a_run = a_p.add_run("Answer: " + a)
        a_run.font.size = Pt(12)
        a_run.font.name = 'Times New Roman'
        
    # Set page numbers
    add_header_footer(doc)
    
    # Save Document
    target_path = r"C:\Users\dell\Desktop\LPU\BTech 5th Sem\Summer Internship\Project\LPU_BTech_Internship_Report_v2.docx"
    doc.save(target_path)
    print(f"SUCCESS: Report saved as {target_path}")

if __name__ == "__main__":
    main()
