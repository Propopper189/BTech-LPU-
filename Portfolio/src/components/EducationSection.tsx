import React from 'react';
import { motion } from 'framer-motion';
import FadeIn from './FadeIn';

const ACADEMICS = [
  {
    num: '1',
    degree: 'B.Tech Computer Science & Engineering',
    institution: 'Lovely Professional University, Phagwara, Punjab',
    period: 'Aug 2025 -- Present',
    score: '9.34 CGPA',
    desc: 'Specializing in Cloud Computing, Computer Networking, Operating Systems, Data Structures & Algorithms, and Distributed Systems.',
  },
  {
    num: '2',
    degree: 'Diploma in Mechanical Engineering',
    institution: 'North Calcutta Polytechnic, Kolkata, West Bengal',
    period: '2021 -- 2024',
    score: '70% Aggregate',
    desc: 'Engineered mechanical systems, thermodynamics, industrial maintenance, and core technical troubleshooting fundamentals.',
  },
  {
    num: '3',
    degree: 'Secondary Education (Class X)',
    institution: 'International Indian School Riyadh, Saudi Arabia',
    period: 'Completed',
    score: '78%',
    desc: 'Built foundation in mathematics, physics, computer fundamentals, and international teamwork.',
  },
];

export default function EducationSection() {
  return (
    <section id="education" className="relative z-20 w-full bg-neutral-950 py-12 sm:py-18 lg:py-22 px-6 sm:px-10 lg:px-16 border-t border-white/10 overflow-hidden">
      <div className="max-w-6xl mx-auto space-y-10 sm:space-y-14">
        {/* Header */}
        <FadeIn delay={0} y={30} className="space-y-2">
          <span className="text-white/60 text-xs sm:text-sm font-inter tracking-[0.3em] uppercase block">
            // Academic Background
          </span>
          <h2 className="font-podium text-white text-2xl sm:text-4xl lg:text-5xl uppercase leading-none tracking-tight">
            EDUCATION
          </h2>
        </FadeIn>

        {/* Education List */}
        <div className="divide-y divide-white/10 border-t border-b border-white/10">
          {ACADEMICS.map((item, idx) => (
            <FadeIn key={item.num} delay={idx * 0.12} y={30}>
              <motion.div
                whileHover={{ x: 6 }}
                transition={{ type: 'spring', stiffness: 300, damping: 25 }}
                className="py-6 sm:py-8 flex flex-col lg:flex-row lg:items-center justify-between gap-5 group hover:bg-white/[0.03] transition-colors px-4 -mx-4 rounded-xl cursor-default"
              >
                {/* Left Number & Degree */}
                <div className="flex items-start sm:items-center gap-5 sm:gap-7 lg:w-7/12">
                  <span className="font-inter font-extrabold text-white/30 group-hover:text-cyan-400 text-2xl sm:text-4xl shrink-0 min-w-[1.8rem] transition-colors duration-300">
                    {item.num}
                  </span>
                  <div className="space-y-1">
                    <h3 className="font-podium text-white text-lg sm:text-xl uppercase tracking-wide group-hover:text-white/90">
                      {item.degree}
                    </h3>
                    <span className="text-white/50 text-xs tracking-widest font-inter uppercase block">
                      {item.institution} &bull; {item.period}
                    </span>
                  </div>
                </div>

                {/* Right Score Badge & Overview */}
                <div className="lg:w-5/12 space-y-2 lg:text-right">
                  <span className="inline-block bg-white/10 group-hover:bg-white/20 border border-white/20 text-white font-mono font-bold text-xs px-3 py-0.5 rounded-full uppercase tracking-wider transition-colors">
                    {item.score}
                  </span>
                  <p className="text-white/70 text-xs sm:text-sm font-inter leading-relaxed">
                    {item.desc}
                  </p>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
