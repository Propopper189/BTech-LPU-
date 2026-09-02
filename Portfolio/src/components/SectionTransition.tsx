import React from 'react';
import { motion } from 'framer-motion';

interface SectionTransitionProps {
  children: React.ReactNode;
  direction?: 'left' | 'right' | 'up';
  delay?: number;
  className?: string;
}

export default function SectionTransition({
  children,
  direction = 'left',
  delay = 0,
  className = '',
}: SectionTransitionProps) {
  const getInitial = () => {
    switch (direction) {
      case 'left':
        return { opacity: 0, x: -140, scale: 0.985 };
      case 'right':
        return { opacity: 0, x: 140, scale: 0.985 };
      default:
        return { opacity: 0, y: 70, scale: 0.985 };
    }
  };

  return (
    <div className="overflow-hidden w-full">
      <motion.div
        initial={getInitial()}
        whileInView={{ opacity: 1, x: 0, y: 0, scale: 1 }}
        viewport={{ once: false, amount: 0.12 }}
        transition={{
          type: 'spring',
          stiffness: 170,
          damping: 24,
          mass: 0.85,
          delay,
        }}
        className={`w-full ${className}`}
      >
        {children}
      </motion.div>
    </div>
  );
}
