LOVELY PROFESSIONAL UNIVERSITY

School of Computer Science and Engineering

FINAL INTERNSHIP / ETP REPORT

Course Code: CSE443

Current Term: 26271

Cloud Infrastructure Monitoring and Security Alerting

Using Google Cloud Platform and Huawei Cloud

Student Name

[YOUR FULL NAME]

Registration / UID

[YOUR UID]

Programme

B.Tech. Computer Science and Engineering

Specialization

Artificial Intelligence and Machine Learning

Organization

WiSys, Riyadh, Saudi Arabia

Internship Role

Cloud / IT Infrastructure Trainee

Internship Period

[START DATE] – [END DATE]

University Faculty/Guide

[FACULTY NAME]

Industry Supervisor

[SUPERVISOR NAME]



Submitted in partial fulfillment of the requirements for CSE443 / ETP

August 2026



CERTIFICATE

This section should contain the official internship certificate issued by WiSys. Insert the scanned certificate here before final submission.

[INSERT WI SYS INTERNSHIP CERTIFICATE IMAGE/PDF PAGE HERE]



DECLARATION

I hereby declare that this internship report titled “Cloud Infrastructure Monitoring and Security Alerting Using Google Cloud Platform and Huawei Cloud” presents the work carried out by me during my internship at WiSys, Riyadh, Saudi Arabia. The report has been prepared for academic evaluation under course CSE443. The technical activities described in this report are based on the tasks performed during the internship, subject to the confidentiality and security requirements of the organization.



[YOUR NAME]

[UID] | B.Tech. CSE



ACKNOWLEDGEMENT

I would like to express my sincere gratitude to WiSys, Riyadh, for providing me with the opportunity to work in an enterprise IT infrastructure environment. The internship provided practical exposure to cloud platforms, monitoring, alerting, identity management, security controls and infrastructure operations.

I am thankful to the IT infrastructure and service teams for their guidance, technical discussions and support throughout the internship. I also appreciate the guidance provided by the project and management team, which helped me understand how cloud technologies are applied in real operational environments.

I also thank Lovely Professional University and my faculty guide for providing the academic framework through which the internship experience could be documented and evaluated.



ABSTRACT

Modern organizations depend on cloud infrastructure to host applications, services and critical workloads. As the number of cloud resources increases, manual monitoring becomes difficult and organizations require reliable mechanisms for detecting infrastructure failures, configuration changes and security-related events. During my internship at WiSys, Riyadh, I worked on cloud infrastructure monitoring, alert configuration, security monitoring and operational support across Google Cloud Platform (GCP) and Huawei Cloud environments.

A major part of the work involved identifying monitoring requirements and implementing alerts for events such as virtual-machine deletion, stopping and restarting, failed health checks, high disk utilization, security-group modification, VPC deletion, backup failure, audit-log disabling and monitoring-policy changes. For GCP, I worked with custom metrics and monitoring logic for VM start/stop events where the required information was not directly available as a standard monitoring metric. I also worked with IAM-related monitoring to provide useful information about users, source IP addresses and changes made to cloud resources.

The internship also provided exposure to Huawei Cloud monitoring and alarm configuration, notification topics, subscriptions, templates, audit/event monitoring and multi-account infrastructure operations. In addition, I worked on Microsoft Entra ID application registration and credential configuration for an application environment. The overall experience strengthened my understanding of cloud operations, infrastructure monitoring, security principles, troubleshooting and technical documentation.



TABLE OF CONTENTS

1. Introduction

2. Organization Profile and Internship Environment

3. Internship Objectives

4. Technologies and Tools Used

5. Problem Statement

6. System / Solution Overview

7. Work Performed

8. Implementation and Configuration

9. Testing and Validation

10. Results and Outcomes

11. Challenges and Solutions

12. Skills and Learning Outcomes

13. Conclusion

14. Future Scope

15. References

16. Appendix – Screenshots and Evidence

Tip: In Microsoft Word, right-click the table of contents area after applying Heading styles and choose Update Field if you add an automatic TOC.



1. INTRODUCTION

1.1 Background

Cloud computing has changed the way organizations deploy, operate and secure IT infrastructure. Instead of managing every physical server manually, organizations can provision virtual machines, networks, storage, identity services and monitoring systems through cloud platforms. However, this flexibility also creates a need for continuous monitoring and automated notification.

An infrastructure monitoring system should not only detect service failures but should also identify important administrative and security events. Examples include an unexpected virtual-machine shutdown, deletion of a network, modification of security rules, failure of backups or disabling of audit logging.

1.2 Internship Context

The internship at WiSys provided practical exposure to enterprise cloud operations. My work focused mainly on monitoring and alerting for cloud resources, security-related events, troubleshooting and documentation. The work involved both GCP and Huawei Cloud, along with selected identity-management activities using Microsoft Entra ID.

1.3 Scope of the Report

This report documents the technical activities performed during the internship. It focuses on cloud monitoring, event detection, alerting, security monitoring, identity configuration, testing and operational documentation. Confidential organization-specific information, credentials, private IP addresses and sensitive infrastructure details are intentionally omitted.

2. ORGANIZATION PROFILE AND INTERNSHIP ENVIRONMENT

2.1 Organization

WiSys is the organization where the internship was undertaken in Riyadh, Saudi Arabia. The internship environment provided exposure to enterprise IT infrastructure and cloud-based operations.

2.2 Internship Role

The internship role involved supporting cloud and IT infrastructure activities. My responsibilities included monitoring cloud resources, configuring alerts, investigating configuration and operational events, assisting with infrastructure tasks, preparing technical documentation and supporting the team with assigned operational work.

2.3 Working Environment

Google Cloud Platform (GCP) for cloud infrastructure and monitoring activities.

Huawei Cloud for cloud resource monitoring, alarm configuration and event/audit-related activities.

Microsoft Entra ID for application identity and credential configuration.

Cloud monitoring and notification services for detecting and communicating infrastructure events.

Documentation and ticket/support workflows used by the IT infrastructure team.

3. INTERNSHIP OBJECTIVES

Understand how cloud infrastructure is monitored in an enterprise environment.

Implement and validate useful alerts for infrastructure, availability and security events.

Understand the difference between standard monitoring metrics and custom monitoring requirements.

Gain practical experience with GCP and Huawei Cloud services.

Understand IAM and audit-related monitoring from an operational security perspective.

Develop troubleshooting and incident-analysis skills.

Improve technical documentation and communication skills.

Gain practical exposure to identity and application registration using Microsoft Entra ID.

4. TECHNOLOGIES AND TOOLS USED

Technology / Service

Purpose

Google Cloud Platform

Cloud infrastructure, monitoring and alerting

Cloud Monitoring / Custom Metrics

Monitoring resource events and creating required alert conditions

IAM

Identity, permissions and change visibility

Huawei Cloud

Cloud infrastructure monitoring and alarm configuration

CTS / Audit and event services

Visibility into cloud activity and security-related events

Notification services

Sending alarm notifications to intended recipients

Microsoft Entra ID

Application registration, credentials and identity configuration

AWS (supporting exposure)

General cloud concepts and infrastructure knowledge

Technical Documentation

Recording configurations, procedures and operational knowledge

5. PROBLEM STATEMENT

In a multi-resource cloud environment, important infrastructure and security events can occur at any time. Relying on manual observation is inefficient and can delay response. A suitable monitoring solution must detect important events and generate actionable notifications.

The internship work therefore addressed the following practical problem: how to improve visibility into cloud infrastructure events and configuration changes through appropriately designed monitoring and alerting mechanisms.

5.1 Key Requirements

Detect unexpected virtual-machine state changes.

Detect resource deletion and important network/security configuration changes.

Detect resource-health and storage-utilization problems.

Detect backup and audit/monitoring failures.

Provide useful information about administrative changes where possible.

Deliver notifications through configured notification mechanisms.

Create configurations that can be documented and reproduced across relevant environments.

6. SYSTEM / SOLUTION OVERVIEW

The solution implemented during the internship can be viewed as an event-to-alert pipeline. Cloud resources and administrative actions generate telemetry or audit events. Monitoring and event-processing mechanisms evaluate these events against defined conditions. When a condition is satisfied, an alarm is generated and routed through a notification mechanism.

6.1 High-Level Flow

Cloud resource or user action occurs.

The platform generates a metric, log, audit event or service event.

Monitoring/event services collect or evaluate the information.

A defined condition or custom metric identifies the event of interest.

The corresponding alarm policy is triggered.

The notification mechanism sends an alert to the configured destination.

The event can then be investigated and documented by the infrastructure team.

[INSERT HIGH-LEVEL ARCHITECTURE DIAGRAM HERE: Cloud Resources → Logs/Metrics/Events → Monitoring → Alarm → Notification]

6.2 Security Considerations

Because the work involved production-oriented cloud environments, security and confidentiality were important. No passwords, access tokens, private keys, confidential customer information or sensitive infrastructure details should be included in the academic report.

7. WORK PERFORMED

7.1 GCP Infrastructure Monitoring

I worked on monitoring Google Cloud infrastructure and improving visibility into important virtual-machine and administrative events. The work included reviewing available monitoring capabilities, identifying gaps and configuring monitoring logic to generate useful alerts.

7.2 Custom Monitoring for VM Start/Stop Events

One important requirement was to detect VM start and stop events. The required event information was not directly available in the desired form as a standard monitoring metric, so a custom monitoring approach was used. The implementation involved creating and using a custom metric/event-based mechanism and then associating the result with an alerting condition.

This work provided practical understanding of the difference between a platform's built-in metrics and the custom telemetry that may be required for operational monitoring.

7.3 IAM Change Monitoring

I also worked with IAM-related monitoring to improve visibility into administrative changes. The monitoring approach was designed to provide useful information such as the identity involved in a change, source information where available, and the type of change performed. This is valuable for troubleshooting, accountability and security investigation.

7.4 Huawei Cloud Monitoring

I worked on Huawei Cloud alarm configuration and notification workflows. This included working with notification topics, subscriptions and templates and creating alarm rules for infrastructure events. The work also involved understanding the role of audit/event services in generating information required for certain alerts.

7.5 Multi-Account / Multi-Project Monitoring

The environment included multiple cloud accounts/projects and a significant number of virtual machines. This highlighted the importance of consistent monitoring design and reusable configurations rather than manually checking each server.

7.6 Microsoft Entra ID Work

I worked on identity configuration for an application environment involving Microsoft Entra ID. The activities included application registration, creation/configuration of security credentials and providing the required administrative consent. This provided practical exposure to cloud identity and application authentication concepts.

7.7 Documentation and IT Support

In addition to configuration work, I prepared technical documentation and assisted the infrastructure team with assigned operational activities and ticket-related work. Documentation was important for recording configurations, procedures and troubleshooting information for future reference.

8. IMPLEMENTATION AND CONFIGURATION

8.1 Alert Categories

Category

Alert

Purpose

Compute

VM Instance Deleted

Detect accidental or unauthorized deletion of virtual machines.

Compute

VM Instance Stopped

Detect unexpected shutdown or stopping of virtual machines.

Compute

VM Instance Restarted

Detect unexpected VM restart events.

Compute

VM Health Check Failed

Identify availability or health problems.

Storage

Disk Utilization ≥ 90%

Identify potentially critical storage exhaustion.

Network

Security Group Modified

Detect changes to network access-control configuration.

Network

VPC Deleted

Detect deletion of a virtual private cloud/network.

Backup

Backup Failed

Detect unsuccessful backup operations.

Security

Audit Log Disabled

Detect loss of important audit visibility.

Monitoring

Alarm Policy Deleted / Disabled

Detect changes that could reduce monitoring coverage.

8.2 Example Implementation Sequence

Identify the operational/security event that needs to be detected.

Determine whether a native metric, log, audit event or custom metric is appropriate.

Configure the relevant monitoring or event source.

Create the alert condition and threshold where applicable.

Configure the notification channel/topic/subscription.

Test the condition using a controlled event where permitted.

Confirm that the notification is generated and contains useful information.

Document the final configuration and operational purpose.

8.3 Notification Workflow

For Huawei Cloud activities, notification components such as topics, subscriptions and templates were configured as part of the alarm workflow. The same general principle applies across cloud platforms: an event is detected, an alarm rule evaluates the event, and a notification is routed to the intended recipient.

9. TESTING AND VALIDATION

Testing was performed by checking whether the configured monitoring conditions produced the expected alarm behavior. Where a controlled test event was appropriate and authorized, the event was generated or observed and the resulting alarm/notification was verified.

9.1 Validation Checklist

Verify the monitoring source is receiving the required data.

Verify the alert condition is syntactically and logically correct.

Verify the alert threshold is appropriate.

Verify the alarm changes state when the condition is satisfied.

Verify the notification is delivered to the configured destination.

Verify the notification provides enough information for investigation.

Verify the alert returns to the expected state after the event condition is cleared, where applicable.

Document any limitations or platform-specific behavior.

9.2 Example Test Matrix

Test Case

Expected Result

VM stop event

VM stopped alert is generated and notification is delivered.

VM restart event

Restart alert is generated.

VM deletion event

Deletion alert is generated.

Health check failure

Health-related alert is generated.

Disk utilization reaches threshold

Storage alert is triggered.

Security group modification

Security/network configuration alert is generated.

VPC deletion

Network deletion alert is generated.

Backup failure

Backup failure alert is generated.

Audit logging disabled

Security/audit alert is generated.

Alarm policy disabled/deleted

Monitoring-change alert is generated.

10. RESULTS AND OUTCOMES

The internship work resulted in improved understanding and implementation of cloud monitoring and alerting requirements. The configured alert set provided coverage for several categories of operational and security events.

Improved visibility into virtual-machine state changes.

Improved detection of infrastructure and network configuration changes.

Improved awareness of backup and storage-related problems.

Improved monitoring of audit and monitoring-control changes.

Practical experience with custom metrics for requirements not directly satisfied by native metrics.

Practical understanding of notification and alarm workflows.

Exposure to identity/application registration through Microsoft Entra ID.

Improved ability to document and troubleshoot cloud infrastructure configurations.

10.1 Professional Outcome

The internship helped bridge the gap between academic cloud concepts and real infrastructure operations. Instead of treating cloud services as isolated laboratory exercises, the work demonstrated how monitoring, security, identity, notification and documentation must operate together in an enterprise environment.

11. CHALLENGES AND SOLUTIONS

Challenge

Approach / Learning

Required VM events were not available in the desired native metric form.

Used a custom/event-based monitoring approach and connected it to alerting.

Many different infrastructure events required monitoring.

Grouped alerts into compute, storage, network, backup, security and monitoring categories.

Monitoring required useful context for investigation.

Used logs/audit information and IAM-related visibility to identify change details.

Multiple cloud accounts/projects increased operational complexity.

Focused on consistent, reusable and documented monitoring configurations.

Some alerts depended on audit/event information.

Worked with the appropriate cloud audit/event services before configuring the alarm.

Cloud configurations can be sensitive.

Followed security practices and avoided exposing credentials or confidential infrastructure information.

12. SKILLS AND LEARNING OUTCOMES

12.1 Technical Skills

Cloud infrastructure monitoring

Alert and alarm policy configuration

Custom metrics and event-based monitoring

Cloud IAM concepts

Audit and event monitoring

Network and security monitoring

Backup and storage monitoring

Microsoft Entra ID application registration

Technical troubleshooting

Technical documentation

12.2 Professional Skills

Working with an IT infrastructure team

Understanding operational priorities

Communicating technical issues clearly

Following security and confidentiality requirements

Documenting technical procedures

Investigating problems systematically

Working with senior engineers and managers

13. CONCLUSION

The internship at WiSys provided practical exposure to enterprise cloud infrastructure and IT operations. The central focus of my work was cloud monitoring and alerting, with additional activities in security monitoring, IAM visibility, identity configuration, troubleshooting and documentation.

The implementation and validation of alerts for compute, storage, network, backup, security and monitoring events demonstrated how cloud platforms can be configured to provide timely operational information. The work on custom metrics also demonstrated that real-world monitoring requirements may require solutions beyond standard platform metrics.

Overall, the internship strengthened my practical understanding of cloud computing and infrastructure management and helped me develop the skills required to work in a professional cloud/IT environment.

14. FUTURE SCOPE

Centralize alerts from multiple cloud providers into a common monitoring dashboard.

Introduce automated incident-routing and escalation workflows.

Use Infrastructure as Code to standardize and reproduce monitoring configurations.

Expand anomaly detection beyond fixed thresholds.

Create centralized dashboards for organization-wide infrastructure health.

Integrate monitoring alerts with service-management/ticketing systems.

Develop automated compliance checks for critical security controls.

Use role-based access and least-privilege practices consistently across cloud environments.

15. REFERENCES

Google Cloud documentation – Cloud Monitoring, logging, IAM and compute infrastructure concepts.

Huawei Cloud documentation – Cloud monitoring, alarm management, notification services and audit/event services.

Microsoft documentation – Microsoft Entra ID application registration and identity management.

Internal internship documentation and configuration records maintained during the internship, subject to organizational confidentiality.

16. APPENDIX – SCREENSHOTS AND EVIDENCE

Insert only screenshots that are permitted by WiSys and do not expose passwords, access tokens, private keys, customer information, private IP addresses, confidential project names or other sensitive information.

Screenshot A: GCP monitoring/alert configuration.

[INSERT REDACTED SCREENSHOT HERE]

Screenshot B: GCP custom metric or event-based monitoring configuration.

[INSERT REDACTED SCREENSHOT HERE]

Screenshot C: IAM/audit monitoring example.

[INSERT REDACTED SCREENSHOT HERE]

Screenshot D: Huawei Cloud alarm rule.

[INSERT REDACTED SCREENSHOT HERE]

Screenshot E: Huawei Cloud notification topic/subscription/template.

[INSERT REDACTED SCREENSHOT HERE]

Screenshot F: Example approved alert configuration.

[INSERT REDACTED SCREENSHOT HERE]

Screenshot G: Microsoft Entra ID application registration/credential configuration (redacted).

[INSERT REDACTED SCREENSHOT HERE]

Screenshot H: Relevant documentation or workflow evidence.

[INSERT REDACTED SCREENSHOT HERE]

Screenshot I: Internship certificate.

[INSERT REDACTED SCREENSHOT HERE]



FINAL SUBMISSION CHECKLIST

☐ Replace all [PLACEHOLDER] fields with your actual information.

☐ Insert the official WiSys internship certificate.

☐ Add only approved/redacted screenshots from your internship work.

☐ Add your university/faculty guide and industry supervisor details.

☐ Verify internship dates and organization name exactly as shown on your certificate.

☐ Update the table of contents after final editing.

☐ Export the final document as PDF.

☐ Upload the PDF in UMS under Academics → Project/Dissertation → Upload Research Project → Internship Report with Certificate.

☐ Complete the upload before 20 August 2026.

