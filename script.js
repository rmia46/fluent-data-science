document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
    // Load state
    checkboxes.forEach(cb => {
        cb.checked = localStorage.getItem(cb.id) === 'true';
        cb.addEventListener('change', () => {
            localStorage.setItem(cb.id, cb.checked);
        });
    });
});
