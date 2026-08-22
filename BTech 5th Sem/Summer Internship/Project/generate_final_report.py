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

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
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
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.text = "Page "
        # Add Page Number simple field to footer
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        p._p.append(fldSimple)

def main():
    doc = Document()
    
    # Page Setup
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(0.85)
    
    # Global Style Adjustments
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    
    # Helper to add standard paragraphs with formatting
    def add_standard_p(text, bold_prefix_len=0, italic=False, alignment=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = doc.add_paragraph()
        p.alignment = alignment
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        
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
            run.font.bold = text.startswith("1.") or text.startswith("2.") or text.startswith("3.") or text.startswith("4.") or text.startswith("5.") or text.startswith("6.") or text.startswith("7.") or text.startswith("8.") or text.startswith("9.") or text.startswith("10.") or text.startswith("11.") or text.startswith("12.") or text.startswith("13.") or text.startswith("14.") or text.startswith("15.") or text.startswith("16.") or text.startswith("17.") or text.startswith("18.") or text.startswith("1.1") or text.startswith("1.2") or text.startswith("1.3") or text.startswith("1.4") or text.startswith("2.1") or text.startswith("2.2") or text.startswith("3.1") or text.startswith("3.2") or text.startswith("4.1") or text.startswith("4.2") or text.startswith("5.1") or text.startswith("5.2") or text.startswith("6.1") or text.startswith("7.1") or text.startswith("7.2") or text.startswith("8.1") or text.startswith("8.2") or text.startswith("9.1") or text.startswith("10.1") or text.startswith("11.1") or text.startswith("12.1") or text.startswith("13.1") or text.startswith("14.1") or text.startswith("15.1") or text.startswith("16.1") or text.startswith("17.1") or text.startswith("18.1")
            if italic:
                run.font.italic = True
        return p

    def add_heading_styled(text, level):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.bold = True
        
        if level == 1:
            run.font.size = Pt(16)
            run.font.color.rgb = RGBColor(44, 82, 130) # Steel Blue color theme
        elif level == 2:
            run.font.size = Pt(14)
            run.font.color.rgb = RGBColor(44, 82, 130)
        else:
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_screenshot_placeholder(caption):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
        cell = table.rows[0].cells[0]
        set_cell_background(cell, "F7FAFC")
        set_cell_margins(cell, top=1440, bottom=1440, left=1440, right=1440) # Padding
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("\n\n[Insert Screenshot Here]\n\n")
        run.font.name = 'Times New Roman'
        run.font.italic = True
        run.font.color.rgb = RGBColor(160, 174, 192)
        
        caption_p = doc.add_paragraph()
        caption_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption_p.paragraph_format.space_before = Pt(4)
        caption_p.paragraph_format.space_after = Pt(12)
        run_cap = caption_p.add_run(f"Figure: {caption}")
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(10)
        run_cap.font.italic = True

    # --- COVER PAGE ---
    cover_p = doc.add_paragraph()
    cover_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover_p.paragraph_format.space_before = Pt(36)
    cover_p.paragraph_format.space_after = Pt(12)
    c_run1 = cover_p.add_run("LOVELY PROFESSIONAL UNIVERSITY\n")
    c_run1.font.bold = True
    c_run1.font.size = Pt(16)
    c_run1.font.color.rgb = RGBColor(44, 82, 130)
    
    c_run2 = cover_p.add_run("School of Computer Science and Engineering\n\n\n")
    c_run2.font.bold = True
    c_run2.font.size = Pt(14)
    
    c_run3 = cover_p.add_run(
        "FINAL INTERNSHIP REPORT\n\n"
        "CLOUD INFRASTRUCTURE MONITORING, SECURITY AUDITING, AND AUTOMATED ALERTING IN MULTI-CLOUD ENVIRONMENTS\n\n"
        "An Internship Report Completed at WiSys, Riyadh, Saudi Arabia\n\n\n"
    )
    c_run3.font.bold = True
    c_run3.font.size = Pt(16)
    
    details_p = doc.add_paragraph()
    details_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    details_p.paragraph_format.line_spacing = 1.3
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
        "Internship Period: 14 June 2026 to 13 August 2026\n\n\n"
        "Lovely Professional University, Phagwara, Punjab\n"
        "August 2026\n"
    )
    det_run.font.size = Pt(12)
    
    doc.add_page_break()
    
    # --- CERTIFICATE PAGE ---
    cert_title = doc.add_paragraph()
    cert_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c_run = cert_title.add_run("INTERNSHIP CERTIFICATE\n\n")
    c_run.font.size = Pt(16)
    c_run.font.bold = True
    c_run.font.color.rgb = RGBColor(44, 82, 130)
    
    cert_body = doc.add_paragraph()
    cert_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    cert_body.paragraph_format.line_spacing = 1.5
    cb_run = cert_body.add_run(
        "This is to certify that Aquib Jawaid Ansari (Registration No: 12508688) has successfully completed "
        "their industry training/internship at WiSys, Riyadh, Saudi Arabia, from 14 June 2026 to 13 August 2026. "
        "The scanned copy of the official internship certificate containing supervisor validation and seals should "
        "be attached below before UMS submission.\n\n\n"
        "[INSERT SCANNED OFFICIAL INTERNSHIP CERTIFICATE HERE]\n\n\n"
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
    decl_body.paragraph_format.line_spacing = 1.5
    db_run = decl_body.add_run(
        "I hereby declare that this internship report titled \"Cloud Infrastructure Monitoring, Security Auditing, "
        "and Automated Alerting in Multi-Cloud Environments: An Internship Report at WiSys\" is an authentic "
        "record of the training undertaken by me at WiSys, Riyadh, Saudi Arabia, from 14 June 2026 to 13 August 2026. "
        "This report is submitted in partial fulfillment of the requirements for course code CSE443. All configurations "
        "and tasks described represent my hands-on participation during this internship, subject to organizational security policies.\n\n\n"
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
    ack_body.paragraph_format.line_spacing = 1.5
    ab_run = ack_body.add_run(
        "I express my sincere appreciation to the Cloud Operations and IT Infrastructure Support team at WiSys, "
        "Riyadh, Saudi Arabia, for providing me with a professional multi-cloud environment to carry out my training. "
        "I am particularly grateful to my Industry Mentor, Emadeldin Taha Mahrous, and my Company Supervisor, Medhat, "
        "for their technical guidance, support, and oversight during my tasks.\n\n"
        "I also thank Lovely Professional University, Phagwara, for establishing the academic framework for this "
        "internship under course code CSE443, and my Faculty Supervisor for their feedback in compiling this final report.\n"
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
    abs_body.paragraph_format.line_spacing = 1.5
    asb_run = abs_body.add_run(
        "Modern cloud environments require structured visibility to identify resource failures, security modifications, "
        "and administrative actions. This report presents the infrastructure monitoring, security auditing, and automated "
        "alerting environment used to manage approximately 40 active virtual machines across Google Cloud Platform (GCP) "
        "and Huawei Cloud at WiSys, Riyadh. My hands-on contribution focused on setting up log-based custom metrics, "
        "defining alerting parameters for compute, storage, and networking events, configuring application credentials via "
        "Microsoft Entra ID app registrations, and troubleshooting critical components of the alerting pipeline.\n\n"
        "During the training, I diagnosed and resolved a critical SMTP email alert dispatch failure caused by unverified "
        "sender envelopes on the Brevo relay and fixed an alert deduplication bug caused by a backlog of 55 stale open alerts. "
        "Additionally, I refactored the event simulator to target real database resource entities and exported reusable JSON "
        "monitoring templates. The overall internship provided valuable practical exposure to cloud operations, bridging the "
        "gap between classroom Computer Science coursework and enterprise infrastructure support.\n"
    )
    asb_run.font.size = Pt(12)
    
    doc.add_page_break()
    
    # --- TABLE OF CONTENTS AS A FORMATTED TABLE ---
    toc_title = doc.add_paragraph()
    toc_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    toc_t_run = toc_title.add_run("TABLE OF CONTENTS")
    toc_t_run.font.size = Pt(14)
    toc_t_run.font.bold = True
    toc_t_run.font.color.rgb = RGBColor(44, 82, 130)
    
    toc_table = doc.add_table(rows=1, cols=3)
    toc_table.style = 'Table Grid'
    t_hdr = toc_table.rows[0].cells
    t_headers = ['No.', 'Chapter / Section', 'Page']
    for i, h in enumerate(t_headers):
        t_hdr[i].text = h
        set_cell_background(t_hdr[i], "2C5282")
        t_hdr[i].paragraphs[0].runs[0].font.bold = True
        t_hdr[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(t_hdr[i])
        
    toc_rows = [
        ("1", "Introduction", "1"),
        ("2", "Organization Profile", "2"),
        ("3", "Internship Role and Objectives", "3"),
        ("4", "Project Overview", "4"),
        ("5", "Project Functionalities", "5"),
        ("6", "Technologies and Cloud Services Used", "6"),
        ("7", "Multi-Cloud Monitoring Activities", "7"),
        ("8", "Security Auditing and Alert Configuration", "9"),
        ("9", "Work Performed During the Internship", "11"),
        ("10", "Major Troubleshooting Activities", "13"),
        ("11", "Microsoft Entra ID and Vites AI Hub", "15"),
        ("12", "Configuration Portability and Documentation", "16"),
        ("13", "Testing and Validation", "17"),
        ("14", "Learning Outcomes", "19"),
        ("15", "Challenges and Solutions", "20"),
        ("16", "Conclusion", "21"),
        ("17", "Future Scope", "22"),
        ("18", "References", "23"),
        ("-", "Appendix A: Screenshots and Evidence", "24"),
        ("-", "Appendix B: Sanitized Configuration Examples", "26")
    ]
    for num, name, pg in toc_rows:
        row_cells = toc_table.add_row().cells
        row_cells[0].text = num
        row_cells[1].text = name
        row_cells[2].text = pg
        for cell in row_cells:
            set_cell_margins(cell)
            
    doc.add_page_break()
    
    # --- LIST OF TABLES & FIGURES & ABBREVIATIONS ---
    list_t = doc.add_paragraph()
    lt_run = list_t.add_run("LIST OF TABLES\n")
    lt_run.font.bold = True
    list_t.add_run(
        "Table 1.1: Student and Internship Details\n"
        "Table 5.1: Core Project Functionalities\n"
        "Table 6.1: Core Technologies and Services Used\n"
        "Table 8.1: The 11-Alert Registry Reference\n"
        "Table 9.1: Personal Contributions Registry\n"
        "Table 10.1: Troubleshooting Case Summary\n"
        "Table 13.1: Incident Validation Log Matrix\n"
        "Table 14.1: Summary of Technical & Professional Skills\n"
        "Table 15.1: Challenge-Resolution Log\n"
    )
    
    list_f = doc.add_paragraph()
    lf_run = list_f.add_run("\nLIST OF FIGURES\n")
    lf_run.font.bold = True
    list_f.add_run(
        "Figure 1: Multi-Cloud Monitoring Dashboard UI\n"
        "Figure 2: GCP Log-Based Custom Metric Filter\n"
        "Figure 3: Huawei Cloud Trace Service event log\n"
        "Figure 4: The 11-Alert Registry Status View\n"
        "Figure 5: Microsoft Entra ID Application Configuration Details\n"
        "Figure 6: Outbound Email Dispatch Log View\n"
    )
    
    abbr_p = doc.add_paragraph()
    abbr_run = abbr_p.add_run("\nLIST OF ABBREVIATIONS\n")
    abbr_run.font.bold = True
    abbr_p.add_run(
        "GCP\t\tGoogle Cloud Platform\n"
        "ECS\t\tElastic Cloud Server\n"
        "CTS\t\tCloud Trace Service\n"
        "SMN\t\tSimple Message Notification\n"
        "VPC\t\tVirtual Private Cloud\n"
        "IAM\t\tIdentity and Access Management\n"
        "SMTP\t\tSimple Mail Transfer Protocol\n"
        "SLA\t\tService Level Agreement\n"
        "MTTR\t\tMean Time to Resolution\n"
        "LPU\t\tLovely Professional University\n"
    )
    
    doc.add_page_break()
    
    # --- TABLE 1.1 IN PRELIMINARY ---
    add_heading_styled("Student and Internship Information", 2)
    s_table = doc.add_table(rows=1, cols=2)
    s_table.style = 'Table Grid'
    hdr = s_table.rows[0].cells
    hdr[0].text = "Information Parameter"
    hdr[1].text = "Student and Training Values"
    set_cell_background(hdr[0], "2C5282")
    set_cell_background(hdr[1], "2C5282")
    hdr[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    hdr[0].paragraphs[0].runs[0].font.bold = True
    hdr[1].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    hdr[1].paragraphs[0].runs[0].font.bold = True
    
    s_data = [
        ("Student Name", "Aquib Jawaid Ansari"),
        ("Registration Number / UID", "12508688"),
        ("University", "Lovely Professional University, Phagwara"),
        ("Course / Term", "CSE443 (ETP Viva) | 26271"),
        ("Specialization Minor", "Cloud Computing"),
        ("Host Organization", "WiSys, Riyadh, Saudi Arabia"),
        ("Internship Duration", "14 June 2026 to 13 August 2026"),
        ("Industry Mentor", "Emadeldin Taha Mahrous"),
        ("Company Supervisor", "Medhat")
    ]
    for k, v in s_data:
        row = s_table.add_row().cells
        row[0].text = k
        row[1].text = v
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        
#     doc.add_page_break()
    
    # --- CHAPTER 1 ---
    add_heading_styled("1. Introduction", 1)
    add_standard_p(
        "1.1 Background of the Internship\n"
        "This internship report details the hands-on technical activities performed during my training at WiSys, "
        "Riyadh, Saudi Arabia, from 14 June 2026 to 13 August 2026. The main objective was to support the IT infrastructure "
        "and Cloud Operations team in managing and auditing cloud resources, tracking events, and configuring notifications "
        "to reduce the Mean Time to Resolution (MTTR) for system incidents."
    )
    add_standard_p(
        "1.2 Importance of Cloud Computing in Modern IT\n"
        "Modern enterprise systems depend on cloud computing to host workloads. Traditional architectures required "
        "physical server installations, manual configurations, and long setup times. Utilizing software-defined resources "
        "on platforms like GCP and Huawei Cloud allows organizations to configure infrastructure dynamically, "
        "optimizing operations and cost."
    )
    add_standard_p(
        "1.3 Importance of Cloud Monitoring, Auditing, and Alerts\n"
        "Maintaining infrastructure availability requires continuous monitoring and auditing. Monitoring collects resource "
        "metrics, while auditing records administrative and security events. Setting up automated alerts ensures "
        "operators are immediately notified of resource deletions, service restarts, or high resource usage, "
        "allowing them to respond quickly and prevent downtime."
    )
    add_standard_p(
        "1.4 Academic Alignment with B.Tech CSE\n"
        "This internship directly aligns with my B.Tech Computer Science and Engineering program at Lovely Professional "
        "University, specializing in Cloud Computing. The training applied classroom concepts in operating systems, "
        "networking, cloud security, and systems engineering to a multi-cloud environment containing approximately "
        "40 active virtual machines."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 2 ---
    add_heading_styled("2. Organization Profile", 1)
    add_standard_p(
        "2.1 WiSys Overview\n"
        "WiSys is a technology integration and systems integration company based in Riyadh, Saudi Arabia. The firm "
        "delivers digital transformation services, cybersecurity, cloud architecture, and IT operations consulting "
        "to public and private sector clients. During my internship, I worked within the Cloud Support division, "
        "assisting with infrastructure health, alerts configuration, and identity systems."
    )
    add_standard_p(
        "2.2 Relevance of IT Infrastructure to WiSys Operations\n"
        "As a managed service provider, WiSys manages multiple cloud accounts and clients. Ensuring high system availability "
        "and compliance with Service Level Agreements (SLAs) requires robust monitoring, incident detection, and documentation. "
        "Configuring standardized alarm rules and notification workflows ensures operations are managed consistently at scale."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 3 ---
    add_heading_styled("3. Internship Role and Objectives", 1)
    add_standard_p(
        "3.1 Role and Scope\n"
        "As a Cloud/IT Infrastructure Trainee, my role focused on configuring monitoring tools, alert policies, and "
        "security audits, and documenting systems. The tasks involved managing alerts, analyzing logs, and configure "
        "application identity settings in Entra ID."
    )
    add_standard_p(
        "3.2 Core Learning Objectives\n"
        "1. Configure and manage telemetry monitoring across multiple cloud projects.\n"
        "2. Define and validate 11 critical availability and security alert policies.\n"
        "3. Implement custom log-based metrics for virtual machine lifecycle tracking.\n"
        "4. Understand cloud audit trails to track administrative activities.\n"
        "5. Troubleshoot SMTP relay configurations and sender validation errors.\n"
        "6. Resolve alert deduplication and queue backlogs in testing environments.\n"
        "7. Configure Entra ID app registrations, client secrets, and permissions.\n"
        "8. Standardize alarm rules using JSON configuration templates.\n"
        "9. Document troubleshooting procedures and system setups for operations teams."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 4 ---
    add_heading_styled("4. Project Overview", 1)
    add_standard_p(
        "4.1 Multi-Cloud Monitoring Environment\n"
        "The project was a multi-cloud infrastructure monitoring, security auditing, and automated alerting environment. "
        "It aggregated resource metrics, security events, and audit logs from GCP and Huawei Cloud. The main goal "
        "was to monitor approximately 40 active virtual machines and trigger real-time notifications for critical incidents."
    )
    add_standard_p(
        "4.2 System Architecture Concept\n"
        "The environment works as an event-driven alert pipeline. Cloud resources emit metrics or event logs. The system "
        "evaluates this telemetry against defined alerting rules. When a rule is triggered, an event is sent to "
        "notification topics, dispatching an incident email to administrators."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 5 ---
    add_heading_styled("5. Project Functionalities", 1)
    add_standard_p(
        "5.1 Core Functionalities\n"
        "The table below details the key functionalities provided by the monitoring environment:"
    )
    
    f_table = doc.add_table(rows=1, cols=2)
    f_table.style = 'Table Grid'
    f_hdr = f_table.rows[0].cells
    f_hdr[0].text = "Monitoring Functionality"
    f_hdr[1].text = "Technical Scope & Purpose"
    set_cell_background(f_hdr[0], "2C5282")
    set_cell_background(f_hdr[1], "2C5282")
    f_hdr[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    f_hdr[0].paragraphs[0].runs[0].font.bold = True
    f_hdr[1].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    f_hdr[1].paragraphs[0].runs[0].font.bold = True
    
    f_data = [
        ("VM Lifecycle Monitoring", "Tracks virtual machine start, stop, restart, and deletion events using audit logs."),
        ("Health Monitoring", "Performs automated connection checks on key application ports to verify responsiveness."),
        ("Security Auditing", "Ingests IAM changes to identify which identity modified resources or permissions."),
        ("Network Monitoring", "Monitors security group modifications and VPC deletions to prevent security exposure."),
        ("Storage Monitoring", "Triggers alerts when disk utilization reaches or exceeds 90% to prevent database write failures."),
        ("Backup Monitoring", "Tracks backup completions and triggers alerts for backup failures to ensure data safety."),
        ("Automated Alerts & Email", "Configures rules that send notifications to administrator inboxes via SMTP relays.")
    ]
    for k, v in f_data:
        row = f_table.add_row().cells
        row[0].text = k
        row[1].text = v
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        
#     doc.add_page_break()
    
    # --- CHAPTER 6 ---
    add_heading_styled("6. Technologies and Cloud Services Used", 1)
    add_standard_p(
        "6.1 Selected Technologies\n"
        "The table below lists the technologies and services used during the internship:"
    )
    
    t_table = doc.add_table(rows=1, cols=3)
    t_table.style = 'Table Grid'
    t_hdr = t_table.rows[0].cells
    t_hdr[0].text = "Technology"
    t_hdr[1].text = "Purpose"
    t_hdr[2].text = "My Exposure"
    for cell in t_hdr:
        set_cell_background(cell, "2C5282")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        cell.paragraphs[0].runs[0].font.bold = True
        set_cell_margins(cell)
        
    t_data = [
        ("Google Cloud Platform (GCP)", "Compute Engine hosting, Cloud Logging, and Cloud Monitoring.", "Hands-on configuration"),
        ("Huawei Cloud", "Elastic Cloud Server (ECS) and Virtual Private Cloud hosting.", "Hands-on configuration"),
        ("Cloud Trace Service (CTS)", "Huawei Cloud service for recording resource operations and change audit logs.", "Hands-on configuration"),
        ("Cloud Eye", "Huawei Cloud performance monitoring and metric alarms engine.", "Hands-on configuration"),
        ("Simple Message Notification (SMN)", "Routes alarms to topics and dispatches email notifications.", "Hands-on configuration"),
        ("Microsoft Entra ID", "Application registrations and credentials for Vites AI Hub.", "Hands-on configuration"),
        ("Brevo SMTP Relay", "Transactional SMTP server configuration and email delivery.", "Hands-on configuration"),
        ("JSON Templates", "Standardized alarm rules configurations for import/export.", "Hands-on configuration"),
        ("Linux / Bash", "Server administration, syslog auditing, and troubleshooting.", "Practical exposure")
    ]
    for t, p, e in t_data:
        row = t_table.add_row().cells
        row[0].text = t
        row[1].text = p
        row[2].text = e
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        set_cell_margins(row[2])
        
#     doc.add_page_break()
    
    # --- CHAPTER 7 ---
    add_heading_styled("7. Multi-Cloud Monitoring Activities", 1)
    add_standard_p(
        "7.1 GCP Monitoring Activities\n"
        "I configured monitoring for GCP resources (Compute Engine). Because GCP does not provide a standard metric "
        "to track VM start/stop operations, I implemented custom log-based metrics. This approach filters "
        "Cloud Audit Logs for specific API requests (`v1.compute.instances.stop` and `v1.compute.instances.delete`), "
        "tracks their occurrence, and triggers alerting rules. The generated alerts extract incident context "
        "such as: who initiated the action (principalEmail), the source IP (callerIp), the target resource (resourceName), "
        "and the event severity."
    )
    add_standard_p(
        "7.2 Huawei Cloud Monitoring Activities\n"
        "For Huawei Cloud, I worked with Cloud Trace Service (CTS) to audit administrative actions. CTS records "
        "resource actions and outputs event logs. I linked these logs to Cloud Eye, which evaluates metric thresholds "
        "and triggers alarms. Triggered alerts are routed via Simple Message Notification (SMN) topics to dispatch "
        "real-time notifications to support teams."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 8 ---
    add_heading_styled("8. Security Auditing and Alert Configuration", 1)
    add_standard_p(
        "8.1 The 11-Alert Registry\n"
        "I configured and validated 11 core alert rules. The table below details these alerts:"
    )
    
    a_table = doc.add_table(rows=1, cols=4)
    a_table.style = 'Table Grid'
    a_hdr = a_table.rows[0].cells
    headers = ["Alert Type", "Alert Event Name", "Severity", "Impact & Risk"]
    for i, h in enumerate(headers):
        a_hdr[i].text = h
        set_cell_background(a_hdr[i], "2C5282")
        a_hdr[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        a_hdr[i].paragraphs[0].runs[0].font.bold = True
        set_cell_margins(a_hdr[i])
        
    alerts_data = [
        ("Compute", "VM Instance Deleted", "Critical", "Accidental or unauthorized deletion leads to permanent loss of system state."),
        ("Compute", "VM Instance Stopped", "Critical", "Stops application workloads, breaching customer uptime SLAs."),
        ("Compute", "VM Instance Restarted", "Critical", "May indicate unexpected crashes, software errors, or hardware failures."),
        ("Compute", "VM Health Check Failed", "Critical", "The application service or port is unresponsive."),
        ("Storage", "Disk Utilization >= 90%", "Critical", "Exhausts storage, causing database locks and system freeze."),
        ("Network", "Security Group Modified", "Critical", "Modifies firewall rules, exposing private resources to public traffic."),
        ("Network", "VPC Deleted", "Critical", "Removes the virtual private cloud network, taking all connected resources offline."),
        ("Backup", "Backup Failed", "Critical", "Indicates data backup failure, risking permanent data loss."),
        ("Security", "Audit Log Disabled", "Critical", "Hides administrative actions, indicating a potential security breach."),
        ("Monitoring", "Alarm Policy Deleted", "Critical", "Loss of monitoring visibility."),
        ("Monitoring", "Alarm Policy Disabled", "Warning", "Alerting rules are deactivated, leaving resources unmonitored.")
    ]
    for t, n, s, r in alerts_data:
        row = a_table.add_row().cells
        row[0].text = t
        row[1].text = n
        row[2].text = s
        row[3].text = r
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        set_cell_margins(row[2])
        set_cell_margins(row[3])
        
#     doc.add_page_break()
    
    # --- CHAPTER 9 ---
    add_heading_styled("9. Work Performed During the Internship", 1)
    add_standard_p(
        "9.1 Overview of My Contribution\n"
        "My work involved setting up alerts, managing logging pipelines, and troubleshooting alerting issues. "
        "The table below maps my specific hands-on tasks:"
    )
    
    c_table = doc.add_table(rows=1, cols=2)
    c_table.style = 'Table Grid'
    c_hdr = c_table.rows[0].cells
    c_hdr[0].text = "Technical System Feature"
    c_hdr[1].text = "My Personal Hands-on Contribution"
    set_cell_background(c_hdr[0], "2C5282")
    set_cell_background(c_hdr[1], "2C5282")
    c_hdr[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    c_hdr[0].paragraphs[0].runs[0].font.bold = True
    c_hdr[1].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    c_hdr[1].paragraphs[0].runs[0].font.bold = True
    
    contrib_data = [
        ("Multi-Cloud Monitoring Setup", "Configured and verified alarm rules for approximately 40 active virtual machines in GCP and Huawei Cloud."),
        ("Custom GCP Metrics", "Configured log filters on GCP Audit Logs to track VM stop/delete API operations."),
        ("Huawei Cloud Logging", "Linked CTS event logs to Cloud Eye rules and configured SMN notification topics."),
        ("SMTP Configuration & Delivery", "Troubleshot Brevo SMTP settings, resolved sender validation rejections, and restored email alert delivery."),
        ("Alert Deduplication Engine", "Identified and resolved a database alert backlog by writing and running a script to clear stale alerts."),
        ("JSON Rule Portability", "Exported JSON alarm rules, parameterized project-specific IDs, and created reusable configurations."),
        ("Microsoft Entra ID App Registry", "Completed app registration, generated client secrets, and set up redirect URIs and API permissions in Entra ID.")
    ]
    for k, v in contrib_data:
        row = c_table.add_row().cells
        row[0].text = k
        row[1].text = v
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        
#     doc.add_page_break()
    
    # --- CHAPTER 10 ---
    add_heading_styled("10. Major Troubleshooting Activities", 1)
    add_standard_p(
        "10.1 Case Study 1: Resolving SMTP Relay Sender Validation Rejections (Brevo)\n"
        "During testing, SMTP alert email dispatches were rejected by Brevo. The server logs returned the error: "
        "\"Sending has been rejected because the sender you used is not valid. Validate your sender or authenticate your domain.\" "
        "Upon investigation, I found that the email From header was set to the SMTP login ID (b5f116001@smtp-brevo.com), "
        "which was not verified as a valid sender address on the account. I updated the configuration to set the From header "
        "and envelope sender parameters to the verified recipient email (jawaidaquib893@gmail.com). This passed Brevo's "
        "SPF/DKIM checks, and email delivery was restored."
    )
    add_standard_p(
        "10.2 Case Study 2: Resolving Alert Deduplication Queue Lock\n"
        "The system uses alert deduplication logic to prevent notification spam. If an active OPEN alert exists for a resource, "
        "duplicate events are dropped. I noticed that no new alert emails were being sent. Upon database inspection, I discovered "
        "55 stale OPEN alerts that had not been closed, causing the deduplication logic to drop legitimate new events. I wrote "
        "and executed a python cleanup script to transition these 55 alerts to RESOLVED. This cleared the backlog, restored the "
        "dashboard compliance score to 100/100, and allowed new notifications to trigger successfully."
    )
    add_standard_p(
        "10.3 Case Study 3: Parameterizing JSON Configurations for Portability\n"
        "To reuse alarm configurations across multiple projects, I exported the rules as JSON templates. The imports failed "
        "initially because the templates contained hardcoded, project-specific resource UUIDs and ARNs. I refactored the templates, "
        "replacing these static identifiers with variables. This allowed the templates to be imported into other cloud projects "
        "by defining the local project variables."
    )
    add_standard_p(
        "10.4 Case Study 4: Event Simulator Refactoring\n"
        "Simulated events generated for testing did not match actual infrastructure resources. I refactored the simulator to "
        "query the database for active resources and select valid resource IDs (such as vm-sap-prod) to generate events. This "
        "ensured simulated alerts updated the dashboard status of actual resources."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 11 ---
    add_heading_styled("11. Microsoft Entra ID and Vites AI Hub", 1)
    add_standard_p(
        "11.1 Secure Application Integration\n"
        "Vites AI Hub required integration with Microsoft Entra ID (formerly Azure Active Directory) for user authentication. "
        "My task was to complete the application registration in Entra ID. I generated client secrets, configured redirect URIs, "
        "set required API permissions (User.Read), and completed the Admin Consent flow. This configuration enabled secure OAuth 2.0 "
        "and OpenID Connect authentication token exchanges for the gateway."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 12 ---
    add_heading_styled("12. Configuration Portability and Documentation", 1)
    add_standard_p(
        "12.1 Portability and Documentation Benefits\n"
        "In enterprise cloud environments, configurations must be consistent. I prepared technical documentation and JSON templates "
        "for alarm rules to ensure they could be redeployed easily. Documenting setup steps, SMTP configurations, and troubleshooting "
        "guides helps operations teams manage and deploy alerts consistently across different projects."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 13 ---
    add_heading_styled("13. Testing and Validation", 1)
    add_standard_p(
        "13.1 Validation Matrix\n"
        "I validated the alert rules using simulated events linked to real database resources. The table below lists the test results:"
    )
    
    val_table = doc.add_table(rows=1, cols=4)
    val_table.style = 'Table Grid'
    val_hdr = val_table.rows[0].cells
    val_hdr[0].text = "Test Case Event"
    val_hdr[1].text = "Expected Action"
    val_hdr[2].text = "Notification Route"
    val_hdr[3].text = "Result Status"
    for cell in val_hdr:
        set_cell_background(cell, "2C5282")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        cell.paragraphs[0].runs[0].font.bold = True
        set_cell_margins(cell)
        
    val_data = [
        ("VM Stop API request", "Trigger VM Stopped alert", "Brevo SMTP relay email", "Passed"),
        ("VM Deletion request", "Trigger VM Deleted alert", "Brevo SMTP relay email", "Passed"),
        ("Health Check fail event", "Trigger Health Check alert", "Brevo SMTP relay email", "Passed"),
        ("Security Group Modified", "Trigger Security Event alert", "Brevo SMTP relay email", "Passed"),
        ("Backup Failure event", "Trigger Backup Alert", "Brevo SMTP relay email", "Passed"),
        ("Audit Log Disabled", "Trigger Audit Security alert", "Brevo SMTP relay email", "Passed")
    ]
    for tc, exp, route, status in val_data:
        row = val_table.add_row().cells
        row[0].text = tc
        row[1].text = exp
        row[2].text = route
        row[3].text = status
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        set_cell_margins(row[2])
        set_cell_margins(row[3])
        
#     doc.add_page_break()
    
    # --- CHAPTER 14 ---
    add_heading_styled("14. Learning Outcomes", 1)
    add_standard_p(
        "14.1 Technical and Professional Outcomes\n"
        "The internship provided hands-on experience in cloud operations and observability. The table below details "
        "the key skills developed:"
    )
    
    lo_table = doc.add_table(rows=1, cols=2)
    lo_table.style = 'Table Grid'
    lo_hdr = lo_table.rows[0].cells
    lo_hdr[0].text = "Skills Domain"
    lo_hdr[1].text = "Acquired Competencies & Tasks"
    set_cell_background(lo_hdr[0], "2C5282")
    set_cell_background(lo_hdr[1], "2C5282")
    lo_hdr[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    lo_hdr[0].paragraphs[0].runs[0].font.bold = True
    lo_hdr[1].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    lo_hdr[1].paragraphs[0].runs[0].font.bold = True
    
    lo_data = [
        ("Multi-Cloud Monitoring", "Configured alerting rules and health checks in GCP and Huawei Cloud consoles."),
        ("Log-Based Auditing", "Analyzed Cloud Audit Logs and CTS traces to track change context (identity, source IP)."),
        ("Identity Configurations", "Registered applications, generated secrets, and configured API permissions in Entra ID."),
        ("Infrastructure Support", "Assisted senior engineers in troubleshooting systems under SLA guidelines."),
        ("SMTP Configuration", "Debugged SMTP relays and verified email delivery headers (From, To, Envelope)."),
        ("Technical Writing", "Prepared technical guides, setup steps, and configuration documents.")
    ]
    for k, v in lo_data:
        row = lo_table.add_row().cells
        row[0].text = k
        row[1].text = v
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        
#     doc.add_page_break()
    
    # --- CHAPTER 15 ---
    add_heading_styled("15. Challenges and Solutions", 1)
    add_standard_p(
        "15.1 Challenge Resolution Log\n"
        "The table below lists the technical challenges resolved during the training:"
    )
    
    ch_table = doc.add_table(rows=1, cols=3)
    ch_table.style = 'Table Grid'
    ch_hdr = ch_table.rows[0].cells
    ch_hdr[0].text = "Technical Challenge"
    ch_hdr[1].text = "Applied Solution"
    ch_hdr[2].text = "Engineering Outcome"
    for cell in ch_hdr:
        set_cell_background(cell, "2C5282")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        cell.paragraphs[0].runs[0].font.bold = True
        set_cell_margins(cell)
        
    ch_data = [
        ("Brevo SMTP rejections due to invalid sender", "Updated the mailer script to set the From header to the verified recipient email.", "Restored automated alert email delivery."),
        ("Alert deduplication queue lock due to stale alerts", "Created and ran a python cleanup script to transition 55 stale alerts to RESOLVED.", "Cleared the queue backlog, allowing new notifications to trigger."),
        ("Exported JSON template import failures", "Parameterized project-specific UUIDs and ARNs in the JSON templates.", "Standardized alerting rules for multi-project reuse."),
        ("Testing simulator using dummy IDs", "Refactored the simulator to query the database and use actual resource IDs.", "Simulated events updated the dashboard status of actual resources.")
    ]
    for c, s, o in ch_data:
        row = ch_table.add_row().cells
        row[0].text = c
        row[1].text = s
        row[2].text = o
        set_cell_margins(row[0])
        set_cell_margins(row[1])
        set_cell_margins(row[2])
        
#     doc.add_page_break()
    
    # --- CHAPTER 16 ---
    add_heading_styled("16. Conclusion", 1)
    add_standard_p(
        "16.1 Academic and Professional Summary\n"
        "The internship at WiSys, Riyadh, provided valuable practical experience in cloud infrastructure operations. "
        "Configuring telemetry monitoring, security alerts, application registrations, and email notifications applied "
        "B.Tech CSE coursework (cloud computing, networking, and operating systems) to real enterprise systems. "
        "Troubleshooting the SMTP relay and alert queues helped develop professional debugging, support, and documentation "
        "skills, providing a strong foundation for a career in Cloud and DevOps Engineering."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 7 ---
    add_heading_styled("17. Future Scope", 1)
    add_standard_p(
        "17.1 Scope for Future Improvements\n"
        "1. Centralized multi-cloud log aggregation to view alerts from all cloud providers in a single console.\n"
        "2. Automating monitoring deployments using Infrastructure as Code (IaC) tools like Terraform.\n"
        "3. Implementing machine learning models to detect anomalies and unusual patterns in resource performance.\n"
        "4. Creating automated remediation playbooks to resolve incidents (such as restarting crashed ports) automatically.\n"
        "5. Integrating monitoring alerts with IT Service Management (ITSM) ticketing systems."
    )
    
#     doc.add_page_break()
    
    # --- CHAPTER 18 ---
    add_heading_styled("18. References", 1)
    add_standard_p(
        "1. Google Cloud Platform (GCP) Documentation: Logging, Monitoring, and Identity and Access Management (IAM) APIs.\n"
        "2. Huawei Cloud Product Documentation: Cloud Eye Monitoring Service and Cloud Trace Service (CTS).\n"
        "3. Microsoft Entra ID Documentation: Application Registration and permissions management.\n"
        "4. Brevo Developer Documentation: SMTP transaction codes and relay authentication protocols.\n"
        "5. Lovely Professional University: B.Tech CSE (Cloud Computing) academic curriculum and guidelines."
    )
    
    doc.add_page_break()
    
    # --- APPENDIX A ---
    add_heading_styled("Appendix A: Screenshots and Evidence", 2)
    add_standard_p(
        "Note: Before submitting the final report, ensure all passwords, access keys, credentials, and sensitive "
        "information are completely redacted or hidden."
    )
    add_screenshot_placeholder("Multi-Cloud Monitoring Dashboard UI")
    add_screenshot_placeholder("GCP Log-Based Custom Metric Filter")
    add_screenshot_placeholder("Huawei Cloud Trace Service CTS log trace")
    add_screenshot_placeholder("Outbound Email Dispatch Log View")
    add_screenshot_placeholder("Microsoft Entra ID Application Configuration Details")
    
    doc.add_page_break()
    
    # --- APPENDIX B ---
    add_heading_styled("Appendix B: Sanitized Configuration Examples", 2)
    p_code = doc.add_paragraph()
    p_code.paragraph_format.line_spacing = 1.2
    p_code.paragraph_format.space_before = Pt(4)
    p_code.paragraph_format.space_after = Pt(12)
    c_run = p_code.add_run(
        "Example 1: Parameterized JSON Config Template for SMTP Service (smtp_config.json)\n"
        "{\n"
        "  \"smtp_server\": \"smtp-relay.brevo.com\",\n"
        "  \"smtp_port\": 587,\n"
        "  \"smtp_username\": \"b5f116001@smtp-brevo.com\",\n"
        "  \"smtp_password\": \"[REDACTED_PASSWORD_KEY]\",\n"
        "  \"alert_recipient\": \"jawaidaquib893@gmail.com\"\n"
        "}\n\n"
        "Example 2: GCP Log-Based Metric Filter (JSON)\n"
        "{\n"
        "  \"filter\": \"resource.type=\\\"gce_instance\\\" AND protoPayload.methodName=\\\"v1.compute.instances.stop\\\"\",\n"
        "  \"metricDescriptor\": {\n"
        "    \"name\": \"custom.googleapis.com/vm_stop_count\",\n"
        "    \"metricKind\": \"DELTA\",\n"
        "    \"valueType\": \"INT64\"\n"
        "  }\n"
        "}\n"
    )
    c_run.font.name = "Consolas"
    c_run.font.size = Pt(11)
    
    # Set page numbers
    add_header_footer(doc)
    
    # Save Document
    target_path = r"C:\Users\dell\Desktop\LPU\BTech 5th Sem\Summer Internship\Project\LPU_BTech_Final_Internship_Report.docx"
    doc.save(target_path)
    print(f"SUCCESS: Report saved as {target_path}")

if __name__ == "__main__":
    main()
