// ===== BECK E7 智能鎖 - JavaScript 互動功能 v2.1 =====

// ----- 頁面載入完成 -----
document.addEventListener('DOMContentLoaded', function () {
    init();
});

// ----- 初始化所有功能 -----
function init() {
    initLoader();
    initNav();
    initScrollProgress();
    initParticles();
    initAnimations();
    init3DProduct();
    initUnlockDemo();
    initBackToTop();
    initCounters();
}

// ----- 載入動畫（修復：使用簡單 timeout）-----
function initLoader() {
    const loader = document.getElementById('pageLoader');
    if (!loader) return;

    // 使用簡單的 timeout，確保 1.5 秒後載入器消失
    setTimeout(() => {
        loader.classList.add('loaded');
    }, 1500);
}

// ----- 導覽列互動 -----
function initNav() {
    const navbar = document.getElementById('navbar');
    const mobileToggle = document.getElementById('mobileMenuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    const mobileMenuItems = document.querySelectorAll('.mobile-menu-item');

    // 滾動時改變導覽列樣式
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 漢堡選單切換
    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            mobileMenu.classList.toggle('active');
        });
    }

    // 點擊選單項目後關閉選單
    mobileMenuItems.forEach(item => {
        item.addEventListener('click', () => {
            mobileToggle.classList.remove('active');
            mobileMenu.classList.remove('active');
        });
    });

    // 平滑滾動
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

// ----- 滾動進度條 -----
function initScrollProgress() {
    const progressBar = document.getElementById('scrollProgress');

    window.addEventListener('scroll', () => {
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight - windowHeight;
        const scrolled = window.scrollY;
        const progress = (scrolled / documentHeight) * 100;

        progressBar.style.width = progress + '%';
    });
}

// ----- 粒子背景系統 -----
function initParticles() {
    const canvas = document.getElementById('particleCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let particles = [];
    let mouse = { x: null, y: null, radius: 150 };

    // 設定 canvas 尺寸
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // 粒子類別
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 0.5;
            this.speedX = (Math.random() - 0.5) * 0.5;
            this.speedY = (Math.random() - 0.5) * 0.5;
            this.opacity = Math.random() * 0.5 + 0.2;
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            // 邊界檢查
            if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
            if (this.y > canvas.height || this.y < 0) this.speedY *= -1;

            // 滑鼠互動
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < mouse.radius) {
                const force = (mouse.radius - distance) / mouse.radius;
                this.x -= dx * force * 0.02;
                this.y -= dy * force * 0.02;
            }
        }

        draw() {
            ctx.fillStyle = `rgba(255, 215, 0, ${this.opacity})`;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // 創建粒子
    function createParticles() {
        const particleCount = Math.floor((canvas.width * canvas.height) / 15000);
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }
    }
    createParticles();

    // 滑鼠移動事件
    window.addEventListener('mousemove', (e) => {
        mouse.x = e.x;
        mouse.y = e.y;
    });

    window.addEventListener('mouseout', () => {
        mouse.x = null;
        mouse.y = null;
    });

    // 動畫循環
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });

        // 連接近距離粒子
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 100) {
                    const opacity = (1 - distance / 100) * 0.2;
                    ctx.strokeStyle = `rgba(255, 215, 0, ${opacity})`;
                    ctx.lineWidth = 0.5;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }

        requestAnimationFrame(animate);
    }
    animate();
}

// ----- 滾動動畫 (Intersection Observer) -----
function initAnimations() {
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('in-view');
                }, delay);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-on-scroll, .advanced-card');
    animatedElements.forEach(el => observer.observe(el));
}

// ----- 3D 產品互動 -----
function init3DProduct() {
    const container = document.getElementById('product3D');
    if (!container) return;

    const img = container.querySelector('.product-img-3d');
    if (!img) return;

    let isDragging = false;
    let startX = 0;
    let currentRotation = 0;

    container.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX;
        container.style.cursor = 'grabbing';
    });

    window.addEventListener('mouseup', () => {
        isDragging = false;
        container.style.cursor = 'grab';
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;

        const deltaX = e.clientX - startX;
        const rotation = currentRotation + deltaX * 0.3;
        const clampedRotation = Math.max(-15, Math.min(15, rotation));

        img.style.transform = `perspective(1500px) rotateY(${clampedRotation}deg) scale(1.02)`;
    });

    container.addEventListener('touchstart', (e) => {
        isDragging = true;
        startX = e.touches[0].clientX;
    });

    window.addEventListener('touchend', () => {
        isDragging = false;
        img.style.transform = '';
    });

    window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;

        const deltaX = e.touches[0].clientX - startX;
        const rotation = currentRotation + deltaX * 0.3;
        const clampedRotation = Math.max(-15, Math.min(15, rotation));

        img.style.transform = `perspective(1500px) rotateY(${clampedRotation}deg) scale(1.02)`;
    });
}

// ----- 解鎖按鈕演示 -----
function initUnlockDemo() {
    const unlockBtn = document.getElementById('unlockBtn');
    const unlockStatus = document.getElementById('unlockStatus');

    if (!unlockBtn || !unlockStatus) return;

    unlockBtn.addEventListener('click', () => {
        unlockBtn.classList.add('success');

        const icon = unlockBtn.querySelector('i');
        icon.classList.remove('fa-lock');
        icon.classList.add('fa-unlock');

        unlockStatus.innerHTML = '<span style="color:#06c755"><i class="fas fa-check-circle"></i> 解鎖成功，門已開啟</span>';

        setTimeout(() => {
            unlockBtn.classList.remove('success');
            icon.classList.remove('fa-unlock');
            icon.classList.add('fa-lock');
            unlockStatus.textContent = '訪客請求進入...';
        }, 3000);
    });
}

// ----- 返回頂部按鈕 -----
function initBackToTop() {
    const backToTopBtn = document.getElementById('backToTop');
    if (!backToTopBtn) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ----- 數據計數動畫 -----
function initCounters() {
    const counters = document.querySelectorAll('.stat-number');
    let hasAnimated = false;

    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasAnimated) {
                hasAnimated = true;
                counters.forEach(counter => {
                    animateCounter(counter);
                });
            }
        });
    }, observerOptions);

    if (counters.length > 0) {
        observer.observe(counters[0]);
    }
}

function animateCounter(counter) {
    const target = parseFloat(counter.dataset.count);
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;

    const updateCounter = () => {
        current += increment;
        if (current < target) {
            counter.textContent = Math.floor(current);
            requestAnimationFrame(updateCounter);
        } else {
            counter.textContent = target;
        }
    };

    updateCounter();
}

// ----- 3D 爆炸圖標註互動 -----
document.querySelectorAll('.feature-marker').forEach(marker => {
    const label = marker.querySelector('.marker-label');

    marker.addEventListener('click', (e) => {
        e.stopPropagation();

        document.querySelectorAll('.marker-label').forEach(l => {
            if (l !== label) {
                l.style.opacity = '0';
                l.style.visibility = 'hidden';
            }
        });

        if (label.style.opacity === '1') {
            label.style.opacity = '0';
            label.style.visibility = 'hidden';
        } else {
            label.style.opacity = '1';
            label.style.visibility = 'visible';
        }
    });
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('.feature-marker')) {
        document.querySelectorAll('.marker-label').forEach(label => {
            label.style.opacity = '0';
            label.style.visibility = 'hidden';
        });
    }
});

// ----- 控制台訊息 -----
console.log('%c BECK E7 智能鎖 ', 'background: #FFD700; color: #000; font-size: 20px; font-weight: bold; padding: 10px;');
console.log('%c 網站已載入完成 ✓ ', 'background: #06c755; color: #fff; font-size: 14px; padding: 5px;');
