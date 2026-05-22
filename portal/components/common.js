/* portal/components/common.js */

// 1. Detect Path Depth (to handle relative links for sub-folders like learn/)
const isSubfolder = window.location.pathname.includes('/learn/');
const root = isSubfolder ? '../' : '';

const navHTML = `
    <nav class="bg-[#2e7d32] p-2 sticky top-0 z-50 shadow-md">
        <div class="container mx-auto flex justify-between items-center max-w-5xl px-4">
            <a href="${root}index.html" class="text-white font-bold text-lg">Fluent Data Science</a>
            <div class="hidden md:flex space-x-6">
                <a href="${root}index.html" class="text-white hover:text-green-100 transition">Home</a>
                <a href="${root}plan.html" class="text-white hover:text-green-100 transition">Plan</a>
                <a href="${root}learn.html" class="text-white hover:text-green-100 transition">Learn</a>
                <a href="${root}materials.html" class="text-white hover:text-green-100 transition">Materials</a>
            </div>
            <button id="menu-btn" class="md:hidden text-white focus:outline-none">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>
        <div id="mobile-menu" class="hidden md:hidden bg-[#1b5e20] flex flex-col space-y-4 p-4 mt-2 border-t border-[#2e7d32]">
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

// Inject components on load
document.addEventListener('DOMContentLoaded', () => {
    // Inject Nav
    const body = document.body;
    body.insertAdjacentHTML('afterbegin', navHTML);
    
    // Inject Footer into the main container (usually max-w-5xl)
    const container = document.querySelector('.container') || body;
    container.insertAdjacentHTML('beforeend', footerHTML);

    // Mobile Menu Logic
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuBtn && mobileMenu) {
        menuBtn.onclick = () => mobileMenu.classList.toggle('hidden');
    }
});

// Global Helpers
window.toggleAnswer = function(id) {
    const el = document.getElementById(id);
    if (el) el.classList.toggle('hidden');
};
