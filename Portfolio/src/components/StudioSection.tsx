import React from 'react';
import FadeIn from './FadeIn';

const PILLARS = [
  {
    num: '01',
    title: 'Uncompromising Vision',
    desc: 'We refuse template-driven mediocrity. Every brand architecture we build is engineered from scratch to dominate its sector.',
  },
  {
    num: '02',
    title: 'Precision Execution',
    desc: 'From custom typographic kerning to WebGL shader physics, our engineering standards leave zero margin for error.',
  },
  {
    num: '03',
    title: 'Cultural Impact',
    desc: 'We do not follow trends; we set the aesthetic benchmark that competitors copy six months later.',
  },
  {
    num: '04',
    title: 'Radical Innovation',
    desc: 'Fusing cutting-edge front-end graphics, real-time 3D, and generative AI into seamless digital experiences.',
  },
];

export default function StudioSection() {
  return (
    <section id="studio" className="relative z-20 w-full bg-neutral-950 py-24 sm:py-32 px-6 sm:px-10 lg:px-16 border-t border-white/10">
      <div className="max-w-7xl mx-auto space-y-16 lg:space-y-24">
        {/* Header & Manifesto */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-end">
          <FadeIn delay={0} y={30} className="lg:col-span-5 space-y-3">
            <span className="text-white/60 text-xs sm:text-sm font-inter tracking-[0.3em] uppercase block">
              // Agency Manifesto
            </span>
            <h2 className="font-podium text-white text-4xl sm:text-6xl lg:text-7xl uppercase leading-none tracking-tight">
              THE STUDIO
            </h2>
          </FadeIn>

          <FadeIn delay={0.2} y={30} className="lg:col-span-7">
            <p className="text-white/90 font-podium text-xl sm:text-3xl lg:text-4xl uppercase leading-snug tracking-wide">
              &quot;WE OPERATE AT THE INTERSECTION OF RADICAL DESIGN AND TECHNOLOGICAL DISRUPTION.&quot;
            </p>
          </FadeIn>
        </div>

        {/* Video / Banner Graphic */}
        <FadeIn delay={0.3} y={40}>
          <div className="relative w-full aspect-[21/9] rounded-3xl overflow-hidden border border-white/10 bg-black group">
            <img
              src="https://motionsites.ai/assets/hero-stellar-ai-v2-preview-DjvxjG3C.gif"
              alt="VANGUARD Studio Creative Space"
              loading="lazy"
              className="w-full h-full object-cover opacity-70 group-hover:scale-105 transition-transform duration-700"
            />
            <div className="absolute inset-0 bg-gradient-to-r from-black/80 via-transparent to-black/80" />
            <div className="absolute bottom-6 left-6 sm:bottom-10 sm:left-10 z-10 max-w-lg space-y-2">
              <span className="text-white/50 text-xs tracking-widest font-inter uppercase">
                Global Creative Direction
              </span>
              <h3 className="font-podium text-white text-xl sm:text-3xl uppercase tracking-wider">
                HEADQUARTERS &bull; NEW YORK / LONDON / TOKYO
              </h3>
            </div>
          </div>
        </FadeIn>

        {/* 4 Pillars Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 divide-y sm:divide-y-0 sm:divide-x divide-white/10 border-t border-b border-white/10 py-12">
          {PILLARS.map((pillar, idx) => (
            <FadeIn key={pillar.num} delay={idx * 0.15} y={30} className={idx !== 0 ? 'sm:pl-6 lg:pl-8 pt-8 sm:pt-0' : ''}>
              <div className="space-y-4">
                <span className="font-podium text-white/40 text-4xl sm:text-5xl block">
                  {pillar.num}
                </span>
                <h4 className="font-podium text-white text-xl sm:text-2xl uppercase tracking-wide">
                  {pillar.title}
                </h4>
                <p className="text-white/70 text-xs sm:text-sm font-inter leading-relaxed">
                  {pillar.desc}
                </p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
