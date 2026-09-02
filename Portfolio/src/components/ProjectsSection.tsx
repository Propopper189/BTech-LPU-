import React, { useState } from 'react';
import { ArrowUpRight } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import FadeIn from './FadeIn';

import wisysImg from '../assets/pics/Wisys.png';
import nebulaImg from '../assets/pics/Nebula.png';
import hotelImg from '../assets/pics/HotelManagement.png';

interface Project {
  id: string;
  title: string;
  client: string;
  category: 'CLOUD' | 'MONITORING' | 'DEVOPS';
  year: string;
  image: string;
  desc: string;
  link: string;
}

const PROJECTS: Project[] = [
  {
    id: 'monitoring',
    title: 'MULTI-CLOUD MONITORING',
    client: 'Cloud Security Audit',
    category: 'MONITORING',
    year: '2026',
    image: wisysImg,
    desc: 'Configured GCP Cloud Monitoring, Huawei Cloud Eye, CTS event logging, and SMN automated alert notifications with Entra ID audit tracking.',
    link: 'https://github.com/Propopper189/Multi-Cloud-Monitoring',
  },
  {
    id: 'nebula',
    title: 'NEBULA CLOUD DRIVE',
    client: 'AWS Architecture Project',
    category: 'CLOUD',
    year: '2026',
    image: nebulaImg,
    desc: 'Scalable AWS cloud storage platform integrating S3 bucket lifecycles, EC2 instances, RDS databases, and ALB load balancing.',
    link: 'https://github.com/Propopper189/Nebula-Cloud-Drive-Version2',
  },
  {
    id: 'hotel',
    title: 'HOTEL & RESTAURANT MANAGEMENT',
    client: 'Full-Stack Enterprise App',
    category: 'DEVOPS',
    year: '2025',
    image: hotelImg,
    desc: 'Full-stack enterprise management system for hotel room reservations, table bookings, food order processing, customer billing workflows, and automated inventory tracking.',
    link: 'https://github.com/Propopper189/Hotel-Restaurant-Management-System',
  },
];

export default function ProjectsSection() {
  const [activeFilter, setActiveFilter] = useState<'ALL' | 'CLOUD' | 'MONITORING' | 'DEVOPS'>('ALL');

  const filteredProjects = activeFilter === 'ALL'
    ? PROJECTS
    : PROJECTS.filter((p) => p.category === activeFilter);

  return (
    <section id="projects" className="relative z-20 w-full bg-black py-12 sm:py-18 lg:py-22 px-6 sm:px-10 lg:px-16 border-t border-white/10 overflow-hidden">
      {/* Background Ambient Glow */}
      <div className="absolute top-1/2 left-1/4 -translate-y-1/2 w-[450px] h-[450px] bg-cyan-500/5 rounded-full blur-[140px] pointer-events-none" />

      <div className="max-w-6xl mx-auto space-y-10 sm:space-y-14 relative z-10">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
          <FadeIn delay={0} y={30}>
            <span className="text-white/60 text-xs sm:text-sm font-inter tracking-[0.3em] uppercase block mb-2">
              // Engineering Portfolio
            </span>
            <h2 className="font-podium text-white text-2xl sm:text-4xl lg:text-5xl uppercase leading-none tracking-tight">
              FEATURED PROJECTS
            </h2>
          </FadeIn>

          {/* PlayStation Sliding Filter Tabs */}
          <FadeIn delay={0.15} y={20}>
            <div className="flex flex-wrap gap-2 sm:gap-2.5 bg-white/5 p-1.5 rounded-full border border-white/10 backdrop-blur-md">
              {(['ALL', 'CLOUD', 'MONITORING', 'DEVOPS'] as const).map((filter) => {
                const isActive = activeFilter === filter;
                return (
                  <button
                    key={filter}
                    onClick={() => setActiveFilter(filter)}
                    className={`relative px-3.5 py-1 text-[10px] font-inter tracking-widest uppercase transition-colors duration-300 rounded-full cursor-pointer ${
                      isActive ? 'text-black font-semibold' : 'text-white/70 hover:text-white'
                    }`}
                  >
                    {isActive && (
                      <motion.div
                        layoutId="activeTabPill"
                        className="absolute inset-0 bg-white rounded-full z-0"
                        transition={{ type: 'spring', stiffness: 380, damping: 30 }}
                      />
                    )}
                    <span className="relative z-10">{filter === 'ALL' ? 'ALL PROJECTS' : filter}</span>
                  </button>
                );
              })}
            </div>
          </FadeIn>
        </div>

        {/* Projects Grid */}
        <motion.div layout className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 sm:gap-7">
          <AnimatePresence>
            {filteredProjects.map((project, idx) => (
              <FadeIn key={project.id} delay={idx * 0.12} y={40}>
                <motion.a
                  href={project.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  whileHover={{ y: -8, scale: 1.02 }}
                  transition={{ type: 'spring', stiffness: 300, damping: 20 }}
                  className="group relative flex flex-col bg-white/5 border border-white/10 hover:border-white/40 hover:shadow-[0_0_35px_rgba(56,189,248,0.25)] rounded-2xl overflow-hidden transition-all duration-300 h-full block"
                >
                  {/* Image Preview Container */}
                  <div className="relative aspect-[16/10] w-full overflow-hidden bg-neutral-950">
                    <img
                      src={project.image}
                      alt={project.title}
                      className="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-108"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent opacity-80 group-hover:opacity-40 transition-opacity" />

                    {/* Top Badges */}
                    <div className="absolute top-3.5 left-3.5 flex gap-2">
                      <span className="bg-black/70 backdrop-blur-md border border-white/20 text-white/90 text-[9px] tracking-widest font-inter px-2.5 py-0.5 uppercase rounded-full">
                        {project.category}
                      </span>
                      <span className="bg-black/70 backdrop-blur-md border border-white/20 text-white/60 text-[9px] tracking-widest font-inter px-2.5 py-0.5 uppercase rounded-full">
                        {project.year}
                      </span>
                    </div>
                  </div>

                  {/* Card Footer Content */}
                  <div className="p-4 sm:p-6 flex flex-col justify-between flex-1 space-y-3.5">
                    <div className="space-y-1.5">
                      <span className="text-white/50 text-[10px] tracking-widest uppercase font-inter block">
                        {project.client}
                      </span>
                      <h3 className="font-podium text-white text-base sm:text-lg uppercase tracking-wide group-hover:text-cyan-300 transition-colors">
                        {project.title}
                      </h3>
                      <p className="text-white/70 text-xs font-inter leading-relaxed line-clamp-3">
                        {project.desc}
                      </p>
                    </div>

                    <div className="pt-3 border-t border-white/10 flex items-center justify-between text-[10px] font-inter tracking-widest uppercase text-white/80 group-hover:text-white">
                      <span>EXPLORE REPOSITORY</span>
                      <div className="w-6.5 h-6.5 rounded-full border border-white/20 flex items-center justify-center group-hover:bg-white group-hover:text-black group-hover:border-white transition-all duration-300 group-hover:scale-110">
                        <ArrowUpRight className="w-3.5 h-3.5" />
                      </div>
                    </div>
                  </div>
                </motion.a>
              </FadeIn>
            ))}
          </AnimatePresence>
        </motion.div>
      </div>
    </section>
  );
}
