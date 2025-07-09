let currentInput = '';
const display = document.getElementById('display');

const botones = document.querySelectorAll('.pixel-button');

botones.forEach(boton => {
  boton.addEventListener('click', () => {
    const valor = boton.textContent;

    switch (valor) {
      case 'AC':
        currentInput = '';
        actualizarDisplay();
        break;
      case 'DEL':
        currentInput = currentInput.slice(0, -1);
        actualizarDisplay();
        break;
      case '=':
        calcularResultado();
        break;
      case 'cos':
      case 'tan':
      case '√':
        currentInput += valor;
        actualizarDisplay();
        break;
      default:
        currentInput += valor;
        actualizarDisplay();
    }
  });
});

function actualizarDisplay() {
  display.textContent = currentInput || '0';
}


function degToRad(grados) {
  return grados * (Math.PI / 180);
}

function calcularResultado() {
  try {
    let expresion = currentInput;

    
    expresion = procesarFunciones(expresion);

    
    expresion = expresion
      .replace(/\^/g, '**')
      .replace(/%/g, '/100');

    
    let resultado = eval(expresion);
    currentInput = resultado.toString();
    actualizarDisplay();
  } catch (error) {
    currentInput = '';
    display.textContent = 'Error';
  }
}

function procesarFunciones(expr) {
 
  expr = expr.replace(/√(\d+(\.\d+)?|\([^)]*\))/g, (_, contenido) => {
    return `Math.sqrt(${contenido})`;
  });

  
  expr = expr.replace(/cos(\d+(\.\d+)?|\([^)]*\))/g, (_, contenido) => {
    return `Math.cos(degToRad(${contenido}))`;
  });

 
  expr = expr.replace(/tan(\d+(\.\d+)?|\([^)]*\))/g, (_, contenido) => {
    return `Math.tan(degToRad(${contenido}))`;
  });

  return expr;
}


// esto es aparte, solo son las particulas 

const canvas = document.getElementById('particles-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];

function createParticle() {
  const size = Math.random() * 2 + 1;
  particles.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    size,
    speedX: (Math.random() - 0.5) * 0.5,
    speedY: (Math.random() - 0.5) * 0.5,
    color: ['#ffeaa7', '#fab1a0', '#fdcb6e', '#81ecec'][Math.floor(Math.random() * 4)]
  });
}

function animateParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    ctx.fillStyle = p.color;
    ctx.fillRect(p.x, p.y, p.size, p.size);

    p.x += p.speedX;
    p.y += p.speedY;

    
    if (p.x < 0 || p.x > canvas.width) p.speedX *= -1;
    if (p.y < 0 || p.y > canvas.height) p.speedY *= -1;
  });

  requestAnimationFrame(animateParticles);
}

for (let i = 0; i < 100; i++) {
  createParticle();
}
animateParticles();

window.addEventListener('resize', () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});
