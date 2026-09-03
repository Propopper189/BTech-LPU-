import React from 'react';
import { motion } from 'framer-motion';
import FadeIn from './FadeIn';

const SKILLS = [
  {
    num: '1',
    title: 'Cloud Infrastructure & Operations',
    tags: ['GCP', 'Huawei Cloud', 'AWS', 'Linux', 'Bash Scripting', 'Virtual Machines (VMs)'],
    desc: 'Managing multi-cloud environments across GCP, Huawei Cloud, and AWS, automating operational workflows with Bash, and optimizing VM system health.',
  },
  {
    num: '2',
    title: 'Identity & Security Auditing',
    tags: ['Microsoft Entra ID', 'IAM Access Control', 'API Permissions', 'App Registrations', 'CTS Logs'],
    desc: 'Configuring Microsoft Entra ID authentication credentials, application registrations, API permission policies, IAM access, and security audit tracking.',
  },
  {
    num: '3',
    title: 'Cloud Monitoring & Incident Response',
    tags: ['Cloud Monitoring', 'Huawei Cloud Eye', 'SMN Notifications', 'Custom Alerts', 'Troubleshooting'],
    desc: 'Deploying real-time Cloud Eye monitoring, custom alert triggers, SMN automated notifications, and conducting infrastructure incident log resolution.',
  },
  {
    num: '4',
    title: 'Biomedical & Facility Engineering',
    tags: ['Biomedical Equipment', 'Preventive Maintenance', 'Facility Management', 'Equipment Inspection', 'Safety & Compliance'],
    desc: 'Inspecting critical medical diagnostic machinery, executing preventive maintenance schedules, keeping inspection logs, and upholding safety standards.',
  },
  {
    num: '5',
    title: 'Core Technical & Networking Fundamentals',
    tags: ['Computer Networking', 'Technical Documentation', 'C / C++', 'Java', 'Python', 'CompTIA Network+'],
    desc: 'Writing clean code utilities, authoring operational technical documentation, configuring networking protocols, and maintaining system logs.',
  },
];

export default function OfferingsSection() {
  return (
    <section id="offerings" className="relative z-20 w-full bg-neutral-950 py-12 sm:py-18 lg:py-22 px-6 sm:px-10 lg:px-16 border-t border-white/10 overflow-hidden">
      <div className="max-w-6xl mx-auto space-y-10 sm:space-y-14">
        {/* Header */}
        <FadeIn delay={0} y={30} className="space-y-2">
          <span className="text-white/60 text-xs sm:text-sm font-inter tracking-[0.3em] uppercase block">
            // Core Competencies
          </span>
          <h2 className="font-podium text-white text-2xl sm:text-4xl lg:text-5xl uppercase leading-none tracking-tight">
            TECHNICAL SKILLS
          </h2>
        </FadeIn>

        {/* Offerings Vertical List */}
        <div className="divide-y divide-white/10 border-t border-b border-white/10">
          {SKILLS.map((item, idx) => (
            <FadeIn key={item.num} delay={idx * 0.1} y={30}>
              <motion.div
                whileHover={{ x: 6 }}
                transition={{ type: 'spring', stiffness: 300, damping: 25 }}
                className="py-6 sm:py-8 group hover:bg-white/[0.03] transition-colors px-4 -mx-4 rounded-xl flex flex-col lg:flex-row lg:items-center justify-between gap-5 cursor-default"
              >
                {/* Left Title & Index */}
                <div className="flex items-start sm:items-center gap-5 sm:gap-7 lg:w-1/2">
                  <span className="font-inter font-extrabold text-white/30 group-hover:text-cyan-400 text-2xl sm:text-4xl shrink-0 min-w-[1.8rem] transition-colors duration-300">
                    {item.num}
                  </span>
                  <h3 className="font-podium text-white text-lg sm:text-2xl uppercase tracking-wide group-hover:translate-x-2 transition-transform duration-300">
                    {item.title}
                  </h3>
                </div>

                {/* Right Tags & Description */}
                <div className="lg:w-1/2 space-y-2.5">
                  <p className="text-white/70 text-xs sm:text-sm font-inter leading-relaxed">
                    {item.desc}
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {item.tags.map((tag) => (
                      <motion.span
                        key={tag}
                        whileHover={{ scale: 1.08, y: -2 }}
                        className="bg-white/5 border border-white/10 hover:border-cyan-400/50 hover:bg-white/10 text-white/60 hover:text-white text-[10px] tracking-widest font-inter px-2.5 py-0.5 uppercase rounded-full transition-colors cursor-default"
                      >
                        {tag}
                      </motion.span>
                    ))}
                  </div>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
