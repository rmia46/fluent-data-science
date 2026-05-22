/* portal/components/common.js */

// 1. Inject Tailwind Config
const configScript = document.createElement('script');
configScript.innerHTML = `
    tailwind.config = {
        theme: {
            extend: {
                colors: { primary: '#2e7d32', dark: '#1b5e20', light: '#e8f5e9' },
                fontFamily: { mono: ['ui-monospace', 'monospace'] }
            }
        }
    }
`;
document.head.appendChild(configScript);

// 2. Global Styles
const styleHTML = `
<style type="text/tailwindcss">
    @layer base {
        * { border-radius: 0 !important; }
        body { font-family: ui-monospace, monospace; background-color: #f3f4f6; }
    }
    .page-container { 
        @apply max-w-5xl mx-auto px-6 md:px-16 py-10; 
    }
    /* Typography Refinement */
    .page-container h2 { @apply text-xl font-bold text-dark mb-4 border-b-2 border-primary pb-1 tracking-tight mt-10; }
    .bg-dark h2 { @apply text-white border-white border-opacity-30 !important; }
    .bg-dark p { @apply text-white opacity-80 !important; }
    .page-container h3 { @apply text-lg font-semibold text-dark mb-3 mt-8; }
    .page-container p { @apply mb-6 text-gray-700 leading-relaxed text-sm; }
    .card-standard { @apply bg-white border-2 border-gray-200 shadow-md p-6; }
    .btn-primary { @apply bg-[#2e7d32] text-white px-8 py-3 font-bold hover:bg-[#1b5e20] transition shadow-lg inline-block text-center; }
    .btn-secondary { @apply bg-[#1b5e20] text-white px-8 py-3 font-bold hover:bg-[#2e7d32] transition shadow-lg inline-block text-center; }
    .hidden { display: none; }
</style>
`;
document.head.insertAdjacentHTML('beforeend', styleHTML);

const isSubfolder = window.location.pathname.includes('/learn/');
const root = isSubfolder ? '../' : '';

const navHTML = `
    <nav class="bg-[#2e7d32] py-3 sticky top-0 z-50 shadow-md">
        <div class="max-w-5xl mx-auto flex justify-between items-center px-6 md:px-16">
            <a href="${root}index.html" class="text-white font-bold text-lg tracking-tight">Fluent Data Science</a>
            <div class="hidden md:flex space-x-8 text-sm">
                <a href="${root}index.html" class="text-white hover:text-green-100 transition">Home</a>
                <a href="${root}plan.html" class="text-white hover:text-green-100 transition">Plan</a>
                <a href="${root}learn.html" class="text-white hover:text-green-100 transition font-bold">Learn</a>
                <a href="${root}materials.html" class="text-white hover:text-green-100 transition">Materials</a>
            </div>
            <button id="menu-btn" class="md:hidden text-white focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>
        <div id="mobile-menu" class="hidden md:hidden bg-[#1b5e20] flex flex-col space-y-4 p-6 mt-1 border-t border-[#2e7d32]">
            <a href="${root}index.html" class="text-white">Home</a>
            <a href="${root}plan.html" class="text-white">Plan</a>
            <a href="${root}learn.html" class="text-white">Learn</a>
            <a href="${root}materials.html" class="text-white">Materials</a>
        </div>
    </nav>
`;

const footerHTML = `
    <footer class="mt-20 pt-8 border-t border-gray-300 text-center text-gray-500 text-sm pb-10">
        <p>Prepared by Roman Mia @rmia46</p>
    </footer>
`;

document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject Nav
    document.body.insertAdjacentHTML('afterbegin', navHTML);
    
    // 2. Highlight Active Page
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a, #mobile-menu a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;
        
        const cleanHref = href.replace('../', '');
        const isHome = (currentPath.endsWith('index.html') || currentPath.endsWith('portal/')) && cleanHref === 'index.html';
        const isMatch = currentPath.includes(cleanHref) && cleanHref !== 'index.html';
        const isLearnSub = currentPath.includes('/learn/module') && cleanHref === 'learn.html';

        if (isHome || isMatch || isLearnSub) {
            link.classList.add('underline', 'underline-offset-8', 'font-bold', 'text-white');
            link.classList.remove('hover:text-green-100');
        }
    });

    // 3. Inject Footer
    const container = document.querySelector('.page-container') || document.body;
    container.insertAdjacentHTML('beforeend', footerHTML);

    // 4. Mobile Menu Toggle
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuBtn && mobileMenu) {
        menuBtn.onclick = () => mobileMenu.classList.toggle('hidden');
    }
});

window.toggleAnswer = function(id) {
    const el = document.getElementById(id);
    if (el) el.classList.toggle('hidden');
};

window.switchTab = function(tabId, groupClass, contentClass) {
    document.querySelectorAll(`.${contentClass}`).forEach(el => el.classList.add('hidden'));
    const targetContent = document.getElementById(tabId);
    if (targetContent) targetContent.classList.remove('hidden');
    document.querySelectorAll(`.${groupClass}`).forEach(el => {
        el.classList.remove('border-primary', 'text-primary', 'bg-white', 'border-b-4');
        el.classList.add('border-transparent', 'text-gray-500', 'bg-gray-50');
    });
    const btn = event.currentTarget;
    btn.classList.add('border-primary', 'text-primary', 'bg-white', 'border-b-4');
    btn.classList.remove('border-transparent', 'text-gray-500', 'bg-gray-50');
};
