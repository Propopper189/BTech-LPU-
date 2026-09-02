import React from 'react';
import { ArrowUpRight, FileText, CheckCircle2 } from 'lucide-react';
import { motion } from 'framer-motion';
import FadeIn from './FadeIn';

export default function ExperienceSection() {
  return (
    <section id="experience" className="relative z-20 w-full bg-black py-12 sm:py-18 lg:py-22 px-6 sm:px-10 lg:px-16 border-t border-white/10 overflow-hidden">
      {/* Ambient background light spot */}
      <div className="absolute top-1/3 right-10 w-[450px] h-[450px] bg-emerald-500/5 rounded-full blur-[130px] pointer-events-none" />

      <div className="max-w-6xl mx-auto space-y-10 sm:space-y-14 relative z-10">
        {/* Header */}
        <FadeIn delay={0} y={30} className="space-y-2">
          <span className="text-white/60 text-xs sm:text-sm font-inter tracking-[0.3em] uppercase block">
            // Industry Experience
          </span>
          <h2 className="font-podium text-white text-2xl sm:text-4xl lg:text-5xl uppercase leading-none tracking-tight">
            EXPERIENCE
          </h2>
        </FadeIn>

        {/* Experience Cards Stack */}
        <div className="space-y-7 sm:space-y-9">
          {/* Experience Card 1: I.T Trainee */}
          <FadeIn delay={0.15} y={40}>
            <motion.div
              whileHover={{ y: -5 }}
              transition={{ type: 'spring', stiffness: 280, damping: 22 }}
              className="bg-white/5 border border-white/10 hover:border-emerald-500/40 hover:shadow-[0_0_40px_rgba(16,185,129,0.18)] rounded-3xl p-5 sm:p-7 lg:p-8 space-y-5 transition-all duration-300"
            >
              {/* Top Header */}
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/10 pb-4">
                <div>
                  <h3 className="font-podium text-white text-xl sm:text-2xl uppercase tracking-wide">
                    I.T TRAINEE
                  </h3>
                  <span className="text-white/50 text-xs tracking-widest uppercase font-inter block mt-1">
                    Al-Watania Information Systems &bull; Riyadh, Saudi Arabia &bull; (06/2026 -- Present)
                  </span>
                </div>

                {/* Verification Badges / Document Links */}
                <div className="flex flex-wrap gap-2.5">
                  <a
                    href="https://drive.google.com/file/d/1TBBguY5J29-3a_m62H993L_obm3bpzrW/view"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-white/10 hover:bg-white text-white hover:text-black border border-white/20 text-[10px] font-inter tracking-widest uppercase px-3 py-1.5 rounded-full flex items-center gap-1.5 transition-all duration-300 hover:scale-105 cursor-pointer"
                  >
                    <FileText className="w-3.5 h-3.5" />
                    <span>Offer Letter</span>
                    <ArrowUpRight className="w-3 h-3" />
                  </a>

                  <a
                    href="https://drive.google.com/file/d/1p9w9L3wrNRqa5PIeuo2eMo3o4rC8PxKa/view"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-white/10 hover:bg-white text-white hover:text-black border border-white/20 text-[10px] font-inter tracking-widest uppercase px-3 py-1.5 rounded-full flex items-center gap-1.5 transition-all duration-300 hover:scale-105 cursor-pointer"
                  >
                    <FileText className="w-3.5 h-3.5" />
                    <span>Salary Slip</span>
                    <ArrowUpRight className="w-3 h-3" />
                  </a>
                </div>
              </div>

              {/* Bullets */}
              <div className="space-y-3">
                {[
                  'Managed GCP and Huawei Cloud infrastructure across approximately 40 VMs, monitoring resources, alarms, logs, system health, and operational status.',
                  'Configured IAM auditing, custom monitoring alerts, CTS, Cloud Eye, and SMN to improve infrastructure visibility, security monitoring, and automated alert notifications.',
                  'Managed Microsoft Entra ID credentials, application registrations, API permissions, authentication configurations, and technical documentation.',
                  'Assisted with cloud infrastructure troubleshooting and incident resolution, investigating alarms, audit logs, VM status, configuration issues, and infrastructure events.',
                  'Created and maintained technical documentation for cloud monitoring, security auditing, alert configurations, and operational procedures.',
                ].map((bullet, idx) => (
                  <motion.div
                    key={idx}
                    whileHover={{ x: 4 }}
                    transition={{ type: 'spring', stiffness: 400, damping: 25 }}
                    className="flex items-start gap-3 group"
                  >
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5 group-hover:scale-110 transition-transform" />
                    <p className="text-white/80 text-xs sm:text-sm font-inter leading-relaxed">
                      {bullet}
                    </p>
                  </motion.div>
                ))}
              </div>

              {/* Tech Stack Pills */}
              <div className="pt-3 border-t border-white/10 space-y-2">
                <span className="text-white/40 text-[10px] tracking-widest font-inter uppercase block">Tech Stack:</span>
                <div className="flex flex-wrap gap-2">
                  {['GCP', 'Huawei Cloud', 'Microsoft Entra ID', 'AWS', 'Linux', 'Bash', 'IAM', 'Cloud Monitoring', 'CTS', 'Huawei Cloud Eye', 'SMN'].map((tech) => (
                    <motion.span
                      key={tech}
                      whileHover={{ scale: 1.08, y: -2 }}
                      className="bg-white/5 border border-white/10 hover:border-emerald-400/50 hover:bg-emerald-500/10 text-white/70 hover:text-white text-[10px] font-inter px-2.5 py-0.5 uppercase rounded-full transition-colors cursor-default"
                    >
                      {tech}
                    </motion.span>
                  ))}
                </div>
              </div>
            </motion.div>
          </FadeIn>

          {/* Experience Card 2: Junior Biomedical Engineer */}
          <FadeIn delay={0.3} y={40}>
            <motion.div
              whileHover={{ y: -5 }}
              transition={{ type: 'spring', stiffness: 280, damping: 22 }}
              className="bg-white/5 border border-white/10 hover:border-cyan-500/40 hover:shadow-[0_0_40px_rgba(56,189,248,0.18)] rounded-3xl p-5 sm:p-7 lg:p-8 space-y-5 transition-all duration-300"
            >
              {/* Top Header */}
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/10 pb-4">
                <div>
                  <h3 className="font-podium text-white text-xl sm:text-2xl uppercase tracking-wide">
                    JUNIOR BIOMEDICAL ENGINEER
                  </h3>
                  <span className="text-white/50 text-xs tracking-widest uppercase font-inter block mt-1">
                    Sodexo &bull; HLL Infra Tech &bull; (05/2024 -- 06/2024)
                  </span>
                </div>

                {/* Verification Document: Sodexo Letter of Intent */}
                <div className="flex flex-wrap gap-2.5">
                  <a
                    href="https://drive.google.com/file/d/16BavelgcR3Y4HzonV0wJigjzeqzmQSy7/view"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-white/10 hover:bg-white text-white hover:text-black border border-white/20 text-[10px] font-inter tracking-widest uppercase px-3 py-1.5 rounded-full flex items-center gap-1.5 transition-all duration-300 hover:scale-105 cursor-pointer"
                  >
                    <FileText className="w-3.5 h-3.5" />
                    <span>Letter of Intent</span>
                    <ArrowUpRight className="w-3 h-3" />
                  </a>
                </div>
              </div>

              {/* Bullets */}
              <div className="space-y-3">
                {[
                  'Inspected and monitored biomedical equipment to support safe, reliable, and efficient healthcare operations.',
                  'Assisted in preventive maintenance, routine equipment checks, troubleshooting, and identification of operational issues.',
                  'Supported facility management activities, including maintenance coordination, equipment inspections, and service follow-ups.',
                  'Maintained equipment records, maintenance logs, inspection reports, and documentation for operational tracking.',
                  'Followed workplace safety procedures and supported compliance with equipment maintenance and facility management standards.',
                ].map((bullet, idx) => (
                  <motion.div
                    key={idx}
                    whileHover={{ x: 4 }}
                    transition={{ type: 'spring', stiffness: 400, damping: 25 }}
                    className="flex items-start gap-3 group"
                  >
                    <CheckCircle2 className="w-4 h-4 text-cyan-400 shrink-0 mt-0.5 group-hover:scale-110 transition-transform" />
                    <p className="text-white/80 text-xs sm:text-sm font-inter leading-relaxed">
                      {bullet}
                    </p>
                  </motion.div>
                ))}
              </div>

              {/* Tech Stack Pills */}
              <div className="pt-3 border-t border-white/10 space-y-2">
                <span className="text-white/40 text-[10px] tracking-widest font-inter uppercase block">Tech Stack:</span>
                <div className="flex flex-wrap gap-2">
                  {['Biomedical Equipment', 'Preventive Maintenance', 'Facility Management', 'Equipment Inspection', 'Safety & Compliance'].map((tech) => (
                    <motion.span
                      key={tech}
                      whileHover={{ scale: 1.08, y: -2 }}
                      className="bg-white/5 border border-white/10 hover:border-cyan-400/50 hover:bg-cyan-500/10 text-white/70 hover:text-white text-[10px] font-inter px-2.5 py-0.5 uppercase rounded-full transition-colors cursor-default"
                    >
                      {tech}
                    </motion.span>
                  ))}
                </div>
              </div>
            </motion.div>
          </FadeIn>
        </div>
      </div>
    </section>
  );
}
