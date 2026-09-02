import React from 'react';
import { motion } from 'framer-motion';

interface PopUpProps {
  children: React.ReactNode;
  delay?: number;
  y?: number;
  scale?: number;
  className?: string;
}

export default function PopUp({
  children,
  delay = 0,
  y = 45,
  scale = 0.88,
  className = '',
}: PopUpProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y, scale }}
      whileInView={{ opacity: 1, y: 0, scale: 1 }}
      viewport={{ once: true, margin: '-40px' }}
      transition={{
        type: 'spring',
        stiffness: 220,
        damping: 18,
        delay,
      }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
