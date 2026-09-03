import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

export default function NinjaSwordCursor() {
  const [pos, setPos] = useState({ x: -100, y: -100 });
  const [isSlashing, setIsSlashing] = useState(false);
  const [slashes, setSlashes] = useState<{ id: number; x: number; y: number }[]>([]);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setPos({ x: e.clientX, y: e.clientY });
    };

    const handleMouseDown = (e: MouseEvent) => {
      setIsSlashing(true);
      const newSlash = { id: Date.now(), x: e.clientX, y: e.clientY };
      setSlashes((prev) => [...prev.slice(-4), newSlash]);
      setTimeout(() => setIsSlashing(false), 220);
    };

    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('mousedown', handleMouseDown);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mousedown', handleMouseDown);
    };
  }, []);

  return (
    <>
      {/* Global CSS override to suppress standard browser cursor */}
      <style>{`
        *, html, body, a, button, input, textarea, select {
          cursor: none !important;
        }
      `}</style>

      {/* Click Slash Spark Trails */}
      <AnimatePresence>
        {slashes.map((slash) => (
          <motion.div
            key={slash.id}
            initial={{ opacity: 1, scale: 0.5, rotate: -45 }}
            animate={{ opacity: 0, scale: 1.8, rotate: 25 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.35, ease: 'easeOut' }}
            style={{ left: slash.x - 40, top: slash.y - 40 }}
            className="fixed pointer-events-none z-50 w-20 h-20 flex items-center justify-center"
          >
            {/* Acid Green / Blue Ninja Slash Arc Glow */}
            <div className="w-full h-1.5 bg-gradient-to-r from-transparent via-[#CCFF00] to-cyan-400 rounded-full shadow-[0_0_18px_#CCFF00] rotate-45 transform" />
          </motion.div>
        ))}
      </AnimatePresence>

      {/* Main Katana Sword Pointer Element */}
      <div
        className="fixed pointer-events-none z-50 transition-transform duration-75 ease-out"
        style={{
          left: pos.x,
          top: pos.y,
          transform: `translate(-4px, -4px) rotate(${isSlashing ? '-55deg' : '-15deg'}) scale(${isSlashing ? 1.25 : 1})`,
          transformOrigin: '4px 4px',
        }}
      >
        <svg
          width="52"
          height="52"
          viewBox="0 0 64 64"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="drop-shadow-[0_0_10px_rgba(204,255,0,0.7)]"
        >
          {/* Katana Blade Body */}
          <path
            d="M 2 2 L 28 28 L 24 32 L 2 6 Z"
            fill="url(#bladeGradient)"
            stroke="#FFFFFF"
            strokeWidth="0.8"
          />
          
          {/* Blade Razor Edge Line */}
          <path
            d="M 2 2 L 28 28"
            stroke="#E0F7FA"
            strokeWidth="1.5"
            strokeLinecap="round"
          />

          {/* Acid Green / Ninja Turtle Glow Line along fuller */}
          <path
            d="M 4 8 L 24 28"
            stroke="#CCFF00"
            strokeWidth="1"
            strokeOpacity="0.9"
          />

          {/* Tsuba (Golden Katana Crossguard) */}
          <ellipse
            cx="27"
            cy="27"
            rx="6.5"
            ry="3.5"
            transform="rotate(-45 27 27)"
            fill="url(#tsubaGradient)"
            stroke="#B78103"
            strokeWidth="0.8"
          />

          {/* Tsuka (Wrapped Handle - Leonardo Blue / Dark Leather) */}
          <path
            d="M 28 28 L 46 46 L 42 50 L 24 32 Z"
            fill="#0F172A"
            stroke="#0284C7"
            strokeWidth="1"
          />

          {/* Handle Wrappings (Diamond Pattern) */}
          <path d="M 30 30 L 34 34 M 35 35 L 39 39 M 40 40 L 44 44" stroke="#38BDF8" strokeWidth="1.5" />

          {/* Kashira (Pommel Cap - Gold) */}
          <circle cx="45" cy="48" r="3.5" fill="#EAB308" stroke="#713F12" strokeWidth="0.8" />

          {/* Gradients */}
          <defs>
            <linearGradient id="bladeGradient" x1="2" y1="2" x2="28" y2="28" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#FFFFFF" />
              <stop offset="40%" stopColor="#CBD5E1" />
              <stop offset="100%" stopColor="#64748B" />
            </linearGradient>

            <linearGradient id="tsubaGradient" x1="21" y1="21" x2="33" y2="33" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#FDE047" />
              <stop offset="50%" stopColor="#CA8A04" />
              <stop offset="100%" stopColor="#854D0E" />
            </linearGradient>
          </defs>
        </svg>
      </div>
    </>
  );
}
