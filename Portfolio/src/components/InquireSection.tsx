import React from 'react';
import { ArrowUpRight, Mail, Phone, Award, FileText } from 'lucide-react';
import { motion } from 'framer-motion';
import FadeIn from './FadeIn';

const LinkedinIcon = () => (
  <svg className="w-5 h-5 fill-current" viewBox="0 0 24 24">
    <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.74a1.62 1.62 0 1 0 0 3.24 1.62 1.62 0 0 0 0-3.24z"/>
  </svg>
);

const GithubIcon = () => (
  <svg className="w-5 h-5 fill-current" viewBox="0 0 24 24">
    <path d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"/>
  </svg>
);

export default function InquireSection() {
  return (
    <section id="inquire" className="relative z-20 w-full bg-black py-12 sm:py-18 lg:py-22 px-6 sm:px-10 lg:px-16 border-t border-white/10 overflow-hidden">
      {/* Background Glow */}
      <div className="absolute bottom-10 left-1/2 -translate-x-1/2 w-[550px] h-[280px] bg-purple-500/5 rounded-full blur-[150px] pointer-events-none" />

      <div className="max-w-6xl mx-auto space-y-10 sm:space-y-14 relative z-10">
        {/* Header */}
        <FadeIn delay={0} y={30} className="space-y-2">
          <span className="text-white/60 text-xs sm:text-sm font-inter tracking-[0.3em] uppercase block">
            // Direct Reach &amp; Credentials
          </span>
          <h2 className="font-podium text-white text-2xl sm:text-4xl lg:text-5xl uppercase leading-none tracking-tight">
            GET IN TOUCH
          </h2>
        </FadeIn>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">
          {/* Left Column: Official Verification Badges */}
          <FadeIn delay={0.15} y={40} className="lg:col-span-6 space-y-4">
            <h3 className="text-white font-podium text-lg sm:text-xl uppercase tracking-wider border-b border-white/10 pb-2.5">
              VERIFIED CERTIFICATIONS
            </h3>

            <div className="space-y-3">
              {[
                {
                  title: 'AWS Cloud Practitioner',
                  sub: 'Amazon Web Services • Credly Badge',
                  link: 'https://www.credly.com/badges/f3458c30-a27a-4c75-9386-e42cb5379375/linked_in_profile',
                  icon: <Award className="w-5.5 h-5.5 text-yellow-400 shrink-0" />,
                  border: 'hover:border-yellow-400/50 hover:shadow-[0_0_30px_rgba(250,204,21,0.2)]',
                },
                {
                  title: 'AWS Academy Graduate',
                  sub: 'AWS Cloud Foundations Training',
                  link: 'https://www.credly.com/badges/b8457fba-5c81-4e4d-823c-fb2bc74c0fb3/linked_in_profile',
                  icon: <Award className="w-5.5 h-5.5 text-cyan-400 shrink-0" />,
                  border: 'hover:border-cyan-400/50 hover:shadow-[0_0_30px_rgba(56,189,248,0.2)]',
                },
                {
                  title: 'CompTIA Network+ Training',
                  sub: 'Abad Network For Training • Certificate',
                  link: 'https://drive.google.com/file/d/1k6E_BsKm0BhrP_ORB0CQ9Ws754oZ-xM_/view',
                  icon: <FileText className="w-5.5 h-5.5 text-emerald-400 shrink-0" />,
                  border: 'hover:border-emerald-400/50 hover:shadow-[0_0_30px_rgba(16,185,129,0.2)]',
                },
              ].map((cert) => (
                <motion.a
                  key={cert.title}
                  href={cert.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  whileHover={{ y: -4, scale: 1.01 }}
                  transition={{ type: 'spring', stiffness: 300, damping: 22 }}
                  className={`bg-white/5 border border-white/10 p-3.5 sm:p-4.5 rounded-2xl flex items-center justify-between transition-all duration-300 group cursor-pointer block ${cert.border}`}
                >
                  <div className="flex items-center gap-3">
                    {cert.icon}
                    <div>
                      <span className="text-white font-podium text-sm sm:text-base uppercase block group-hover:text-white/90">
                        {cert.title}
                      </span>
                      <span className="text-white/60 text-xs font-inter">{cert.sub}</span>
                    </div>
                  </div>
                  <ArrowUpRight className="w-4 h-4 text-white/50 group-hover:text-white group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
                </motion.a>
              ))}
            </div>
          </FadeIn>

          {/* Right Column: Direct Reach & LinkedIn CTA */}
          <FadeIn delay={0.3} y={40} className="lg:col-span-6 space-y-4 flex flex-col justify-between">
            <div className="space-y-4">
              <h3 className="text-white font-podium text-lg sm:text-xl uppercase tracking-wider border-b border-white/10 pb-2.5">
                CONNECT DIRECTLY
              </h3>

              {/* Major LinkedIn Direct Action Button */}
              <motion.a
                href="https://www.linkedin.com/in/akxeeb/"
                target="_blank"
                rel="noopener noreferrer"
                whileHover={{ scale: 1.02, y: -4 }}
                whileTap={{ scale: 0.98 }}
                transition={{ type: 'spring', stiffness: 350, damping: 22 }}
                className="w-full bg-white hover:bg-neutral-100 text-black p-4.5 rounded-2xl font-podium text-base sm:text-lg uppercase tracking-wider flex items-center justify-between transition-all shadow-[0_0_35px_rgba(255,255,255,0.2)] group cursor-pointer"
              >
                <div className="flex items-center gap-3">
                  <LinkedinIcon />
                  <span>CONNECT ON LINKEDIN</span>
                </div>
                <ArrowUpRight className="w-5 h-5 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
              </motion.a>

              {/* Direct Info Links */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-inter tracking-widest uppercase">
                <motion.a
                  href="mailto:aquibjawaid370005@outlook.com"
                  whileHover={{ scale: 1.03, y: -2 }}
                  className="bg-white/5 p-3 rounded-xl border border-white/10 hover:border-white hover:bg-white hover:text-black transition-all flex items-center gap-2.5 truncate cursor-pointer"
                >
                  <Mail className="w-3.5 h-3.5 shrink-0" />
                  <span className="truncate">aquibjawaid370005@outlook.com</span>
                </motion.a>

                <motion.a
                  href="tel:+918276961926"
                  whileHover={{ scale: 1.03, y: -2 }}
                  className="bg-white/5 p-3 rounded-xl border border-white/10 hover:border-white hover:bg-white hover:text-black transition-all flex items-center gap-2.5 cursor-pointer"
                >
                  <Phone className="w-3.5 h-3.5 shrink-0" />
                  <span>+91-8276961926</span>
                </motion.a>

                <motion.a
                  href="tel:+966533199204"
                  whileHover={{ scale: 1.03, y: -2 }}
                  className="bg-white/5 p-3 rounded-xl border border-white/10 hover:border-white hover:bg-white hover:text-black transition-all flex items-center gap-2.5 cursor-pointer"
                >
                  <Phone className="w-3.5 h-3.5 shrink-0" />
                  <span>+966-533199204</span>
                </motion.a>

                <motion.a
                  href="https://github.com/Propopper189"
                  target="_blank"
                  rel="noopener noreferrer"
                  whileHover={{ scale: 1.03, y: -2 }}
                  className="bg-white/5 p-3 rounded-xl border border-white/10 hover:border-white hover:bg-white hover:text-black transition-all flex items-center gap-2.5 cursor-pointer"
                >
                  <GithubIcon />
                  <span>github.com/Propopper189</span>
                </motion.a>

                <motion.a
                  href="https://jawaidaquib893.wixsite.com/aquibjawaid"
                  target="_blank"
                  rel="noopener noreferrer"
                  whileHover={{ scale: 1.03, y: -2 }}
                  className="bg-white/5 p-3 rounded-xl border border-white/10 hover:border-white hover:bg-white hover:text-black transition-all flex items-center gap-2.5 truncate cursor-pointer col-span-1 sm:col-span-2"
                >
                  <ArrowUpRight className="w-3.5 h-3.5 shrink-0" />
                  <span className="truncate">Wix Portfolio Site</span>
                </motion.a>
              </div>
            </div>

            {/* Footer Bottom Info */}
            <div className="pt-5 border-t border-white/10 flex items-center justify-between text-[10px] text-white/40 font-inter tracking-widest uppercase">
              <span>&copy; 2026 AQUIB JAWAID ANSARI</span>
              <span>CLOUD &amp; DEVOPS ENGINEER</span>
            </div>
          </FadeIn>
        </div>
      </div>
    </section>
  );
}
