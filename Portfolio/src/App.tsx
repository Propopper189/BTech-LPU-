import React, { useState } from 'react';
import { ArrowUpRight, Award, Crown, X } from 'lucide-react';
import ExperienceSection from './components/ExperienceSection';
import ProjectsSection from './components/ProjectsSection';
import OfferingsSection from './components/OfferingsSection';
import EducationSection from './components/EducationSection';
import InquireSection from './components/InquireSection';
import NinjaSwordCursor from './components/NinjaSwordCursor';
import PopUp from './components/PopUp';
import SectionTransition from './components/SectionTransition';

export default function App() {
  const [menuOpen, setMenuOpen] = useState(false);

  // Section order: Experience -> Projects -> Trainings -> Education -> Contact/Certifications
  const navItems = [
    { name: 'Experience', href: '#experience' },
    { name: 'Projects', href: '#projects' },
    { name: 'Trainings', href: '#offerings' },
    { name: 'Education', href: '#education' },
    { name: 'Contact', href: '#inquire' },
  ];

  const stats = [
    { value: '9.34', label: 'LPU CGPA (B.Tech CSE)' },
    { value: '40+', label: 'VMs Managed (WiSys)' },
    { value: '100/100', label: 'Cloud Compliance Score' },
  ];

  return (
    <div className="min-h-screen w-full bg-black text-white font-inter select-none overflow-x-hidden relative">
      {/* Custom TMNT Ninja Sword Cursor with Spotlight */}
      <NinjaSwordCursor />

      {/* 1. HERO SECTION */}
      <section className="relative min-h-screen w-full overflow-hidden bg-black flex flex-col justify-between">
        {/* Background Video Layer */}
        <video
          autoPlay
          muted
          loop
          playsInline
          className="absolute inset-0 h-full w-full object-cover z-0"
        >
          <source
            src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260606_154941_df1a96e1-a06f-450c-bd02-d863414cc1a0.mp4"
            type="video/mp4"
          />
        </video>

        {/* Dark Overlay Gradient for Readability */}
        <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/45 to-black/65 z-10 pointer-events-none" />

        {/* Top Navbar */}
        <header className="relative z-20 w-full flex items-center justify-between px-6 sm:px-10 lg:px-16 py-3.5 lg:py-4.5">
          {/* Left Brand Name */}
          <a href="#" className="font-podium text-white text-lg sm:text-xl font-bold uppercase tracking-wider hover:text-cyan-300 transition-colors">
            AQUIB JAWAID ANSARI
          </a>

          {/* Center Nav Links (md+) */}
          <nav className="hidden md:flex items-center gap-6 lg:gap-8">
            {navItems.map((item) => (
              <a
                key={item.name}
                href={item.href}
                className="font-inter text-[11px] text-white/80 tracking-widest uppercase hover:text-white transition-colors duration-200"
              >
                {item.name}
              </a>
            ))}
          </nav>

          {/* Right CTA Button (md+) -> Throws user to LinkedIn */}
          <div className="hidden md:flex items-center">
            <a
              href="https://www.linkedin.com/in/akxeeb/"
              target="_blank"
              rel="noopener noreferrer"
              className="border border-white/30 hover:border-white/60 px-4.5 py-2 text-[10px] tracking-widest uppercase hover:bg-white/10 text-white transition-all duration-300 flex items-center gap-1.5 cursor-pointer hover:shadow-[0_0_20px_rgba(255,255,255,0.25)]"
            >
              GET IN TOUCH
              <ArrowUpRight className="w-3.5 h-3.5" />
            </a>
          </div>

          {/* Mobile Hamburger Button (below md) */}
          <button
            onClick={() => setMenuOpen(true)}
            className="flex md:hidden flex-col justify-center items-end space-y-1.5 p-2 cursor-pointer focus:outline-none"
            aria-label="Open Mobile Menu"
          >
            <div className="w-6 h-0.5 bg-white" />
            <div className="w-6 h-0.5 bg-white" />
            <div className="w-4 h-0.5 bg-white" />
          </button>
        </header>

        {/* Mobile Fullscreen Menu Overlay (below md) */}
        <div
          className={`fixed inset-0 z-50 bg-black/95 backdrop-blur-sm flex flex-col justify-between p-6 sm:p-10 transition-all duration-500 ${
            menuOpen ? 'opacity-100 visible pointer-events-auto' : 'opacity-0 invisible pointer-events-none'
          }`}
        >
          {/* Overlay Header Row */}
          <div className="flex items-center justify-between w-full">
            <a href="#" onClick={() => setMenuOpen(false)} className="font-podium text-white text-xl sm:text-2xl font-bold uppercase tracking-wider">
              AQUIB JAWAID ANSARI
            </a>
            <button
              onClick={() => setMenuOpen(false)}
              className="text-white p-2 hover:opacity-70 transition-opacity cursor-pointer"
              aria-label="Close Mobile Menu"
            >
              <X size={28} />
            </button>
          </div>

          {/* Overlay Nav Links */}
          <div className="flex flex-col items-center justify-center gap-6 sm:gap-8 my-auto">
            {navItems.map((item, idx) => (
              <a
                key={item.name}
                href={item.href}
                onClick={() => setMenuOpen(false)}
                style={{
                  transitionDelay: menuOpen ? `${idx * 80 + 100}ms` : '0ms',
                  transform: menuOpen ? 'translateY(0)' : 'translateY(20px)',
                  opacity: menuOpen ? 1 : 0,
                  transition: 'transform 0.5s ease-out, opacity 0.5s ease-out',
                }}
                className="font-podium text-3xl sm:text-4xl text-white uppercase tracking-wide hover:opacity-70 transition-opacity"
              >
                {item.name}
              </a>
            ))}

            {/* GET IN TOUCH button inside mobile overlay -> Throws to LinkedIn */}
            <a
              href="https://www.linkedin.com/in/akxeeb/"
              target="_blank"
              rel="noopener noreferrer"
              onClick={() => setMenuOpen(false)}
              style={{
                transitionDelay: menuOpen ? `${navItems.length * 80 + 100}ms` : '0ms',
                transform: menuOpen ? 'translateY(0)' : 'translateY(20px)',
                opacity: menuOpen ? 1 : 0,
                transition: 'transform 0.5s ease-out, opacity 0.5s ease-out',
              }}
              className="mt-4 border border-white/30 hover:border-white/60 px-6 py-3 text-xs tracking-widest uppercase text-white transition-all duration-300 flex items-center gap-2 cursor-pointer"
            >
              GET IN TOUCH
              <ArrowUpRight className="w-4 h-4" />
            </a>
          </div>

          {/* Overlay Footer text */}
          <div className="text-center text-white/40 text-xs tracking-widest uppercase font-inter">
            &copy; AQUIB JAWAID ANSARI &bull; CLOUD &amp; DEVOPS
          </div>
        </div>

        {/* Main Hero Content Overlay (Optimized Container max-w-3xl) */}
        <main className="relative z-20 flex-1 w-full flex flex-col justify-center px-6 sm:px-10 lg:px-16 py-6 sm:py-10">
          <div className="max-w-3xl">
            {/* 1. Tagline */}
            <PopUp delay={0.1}>
              <div className="flex items-center gap-2 mb-3.5 lg:mb-5">
                <Crown className="w-3.5 h-3.5 text-white/70" />
                <span className="text-white/70 text-[11px] font-inter tracking-[0.25em] uppercase">
                  Cloud &amp; DevOps Engineer
                </span>
              </div>
            </PopUp>

            {/* 2. Main Heading (Scaled down for 100% zoom match) */}
            <PopUp delay={0.25}>
              <div className="flex flex-col">
                <h1 className="font-podium text-white uppercase leading-[0.92] tracking-tight text-[clamp(2.1rem,4.6vw,4.2rem)]">
                  Architect.
                </h1>
                <h1 className="font-podium text-white uppercase leading-[0.92] tracking-tight text-[clamp(2.1rem,4.6vw,4.2rem)]">
                  Automate.
                </h1>
                <h1 className="font-podium text-white uppercase leading-[0.92] tracking-tight text-[clamp(2.1rem,4.6vw,4.2rem)]">
                  Deploy.
                </h1>
              </div>
            </PopUp>

            {/* 3. Subtext */}
            <PopUp delay={0.4}>
              <p className="mt-4 lg:mt-5 text-white/70 text-xs sm:text-sm font-inter leading-relaxed max-w-md">
                Building resilient multi-cloud infrastructure{' '}
                <br className="hidden sm:inline" />
                and automated pipelines that don&apos;t just scale --{' '}
                <strong className="text-white font-bold">they lead.</strong>
              </p>
            </PopUp>

            {/* 4. CTA Row */}
            <PopUp delay={0.55}>
              <div className="mt-5 lg:mt-7 flex flex-wrap items-center gap-4 sm:gap-6">
                <a
                  href="#experience"
                  className="group bg-black hover:bg-neutral-900 px-5 sm:px-6 py-2.5 sm:py-3 text-[11px] tracking-widest uppercase text-white font-medium flex items-center gap-2 transition-all duration-300 shadow-xl cursor-pointer border border-white/10 hover:border-white/30 hover:shadow-[0_0_25px_rgba(255,255,255,0.2)]"
                >
                  SEE MY WORK
                  <ArrowUpRight className="w-3.5 h-3.5 transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                </a>

                <div className="hidden sm:flex items-center gap-3 border-l border-white/20 pl-6">
                  <Award className="w-5 h-5 text-white/50 shrink-0" />
                  <div className="text-white/60 text-[10px] sm:text-xs tracking-wider uppercase flex flex-col leading-tight">
                    <span>AWS Certified</span>
                    <span>Cloud Engineer</span>
                  </div>
                </div>
              </div>
            </PopUp>

            {/* 5. Stats Row */}
            <PopUp delay={0.7}>
              <div className="mt-5 sm:mt-7 lg:mt-9 flex flex-wrap gap-6 sm:gap-10 lg:gap-14 border-t border-white/10 pt-3.5 sm:pt-5">
                {stats.map((stat) => (
                  <div key={stat.label} className="flex flex-col">
                    <span className="font-inter text-white text-lg sm:text-2xl lg:text-3xl font-bold tracking-tight">
                      {stat.value}
                    </span>
                    <span className="text-white/50 text-[9px] sm:text-[10px] tracking-widest uppercase mt-0.5">
                      {stat.label}
                    </span>
                  </div>
                ))}
              </div>
            </PopUp>
          </div>
        </main>
      </section>

      {/* 2. EXPERIENCE SECTION */}
      <SectionTransition direction="left">
        <ExperienceSection />
      </SectionTransition>

      {/* 3. PROJECTS SECTION */}
      <SectionTransition direction="right">
        <ProjectsSection />
      </SectionTransition>

      {/* 4. TRAININGS & TECHNICAL SKILLS SECTION */}
      <SectionTransition direction="left">
        <OfferingsSection />
      </SectionTransition>

      {/* 5. EDUCATION SECTION */}
      <SectionTransition direction="right">
        <EducationSection />
      </SectionTransition>

      {/* 6. CERTIFICATIONS & GET IN TOUCH SECTION */}
      <SectionTransition direction="left">
        <InquireSection />
      </SectionTransition>
    </div>
  );
}
