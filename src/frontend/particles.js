const particlesContainer = document.getElementById('particles');
const particleCount = 100; // Number of particles

for (let i = 0; i < particleCount; i++) {
  const particle = document.createElement('div');
  particle.classList.add('particle');

  // Random position
  particle.style.top = Math.random() * window.innerHeight + 'px';
  particle.style.left = Math.random() * window.innerWidth + 'px';

  // Random size
  const size = Math.random() * 9 + 2;
  particle.style.width = size + 'px';
  particle.style.height = size + 'px';

  // Random animation duration
  const duration = Math.random() * 10 + 5;
  particle.style.animationDuration = duration + 's';

  particlesContainer.appendChild(particle);
}
