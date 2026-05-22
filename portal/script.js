/* portal/script.js */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Handle Mobile Menu Toggle
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuBtn && mobileMenu) {
        menuBtn.onclick = () => {
            mobileMenu.classList.toggle('hidden');
        };
    }

    // 2. Handle File Browser (only on materials.html)
    const browserContainer = document.getElementById('file-browser');
    if (typeof FILE_TREE !== 'undefined' && browserContainer) {
        renderTree(FILE_TREE, browserContainer);
        updateProgress();
    }
});

function renderTree(data, container, parentCheckbox = null) {
    data.forEach(item => {
        const nodeDiv = document.createElement('div');
        nodeDiv.className = 'my-2';
        
        const storageKey = 'path_' + (item.path || item.name);
        
        if (item.type === 'directory') {
            const card = document.createElement('div');
            card.className = 'bg-white border-2 border-gray-200 shadow-sm';
            
            const header = document.createElement('div');
            header.className = 'flex items-center p-4 bg-light cursor-pointer hover:bg-green-100 transition';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = storageKey;
            checkbox.className = 'w-5 h-5 accent-primary cursor-pointer mr-4';
            
            const arrow = document.createElement('span');
            arrow.className = 'inline-block w-6 font-mono transition-transform duration-200';
            arrow.textContent = '▶';
            
            const title = document.createElement('span');
            title.className = 'flex-grow font-bold text-dark';
            title.textContent = item.name;
            
            header.appendChild(checkbox);
            header.appendChild(arrow);
            header.appendChild(title);
            card.appendChild(header);
            
            const childList = document.createElement('div');
            childList.className = 'hidden pl-8 pr-4 py-2 border-t border-gray-100';
            card.appendChild(childList);
            
            nodeDiv.appendChild(card);
            
            // Expand/Collapse logic
            header.onclick = (e) => {
                if (e.target === checkbox) return;
                const isHidden = childList.classList.toggle('hidden');
                arrow.textContent = isHidden ? '▶' : '▼';
            };

            // Cascading Checkbox logic
            checkbox.onclick = (e) => {
                e.stopPropagation();
                const childrenCheckboxes = childList.querySelectorAll('input[type="checkbox"]');
                childrenCheckboxes.forEach(childCb => {
                    childCb.checked = checkbox.checked;
                    localStorage.setItem(childCb.id, childCb.checked);
                });
                localStorage.setItem(storageKey, checkbox.checked);
                updateProgress();
            };

            renderTree(item.children, childList, checkbox);
            
            // Initial folder state (sync with local storage)
            const childCbs = childList.querySelectorAll('input[type="checkbox"]');
            if (childCbs.length > 0) {
                const allChecked = Array.from(childCbs).every(cb => localStorage.getItem(cb.id) === 'true');
                checkbox.checked = allChecked;
                localStorage.setItem(storageKey, allChecked);
            }

        } else {
            const fileItem = document.createElement('div');
            fileItem.className = 'flex items-center py-2 text-sm';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = storageKey;
            checkbox.className = 'w-4 h-4 accent-primary cursor-pointer mr-3';
            checkbox.checked = localStorage.getItem(storageKey) === 'true';
            
            const link = document.createElement('a');
            link.href = 'https://github.com/rmia46/fluent-data-science/blob/main/' + item.path;
            link.target = '_blank';
            link.className = 'text-primary hover:underline hover:text-dark';
            link.textContent = '📄 ' + item.name;
            
            fileItem.appendChild(checkbox);
            fileItem.appendChild(link);
            nodeDiv.appendChild(fileItem);
            
            checkbox.onchange = () => {
                localStorage.setItem(storageKey, checkbox.checked);
                if (parentCheckbox) {
                    const siblingCbs = container.querySelectorAll('.file-item input[type="checkbox"]'); // Scoped to siblings
                    // For simpler logic, we re-scan the container's checkboxes
                    const allCbs = container.querySelectorAll('input[type="checkbox"]');
                    const allChecked = Array.from(allCbs).every(cb => cb.checked);
                    parentCheckbox.checked = allChecked;
                    localStorage.setItem(parentCheckbox.id, allChecked);
                }
                updateProgress();
            };
        }
        container.appendChild(nodeDiv);
    });
}

function updateProgress() {
    // Only count leaf files (not folders) for progress
    const allFileCheckboxes = document.querySelectorAll('.tree-node > .flex input[type="checkbox"]');
    const total = allFileCheckboxes.length;
    const checked = Array.from(allFileCheckboxes).filter(cb => cb.checked).length;
    const percent = total > 0 ? Math.round((checked / total) * 100) : 0;
    
    const progressEl = document.getElementById('progress-percent');
    if (progressEl) {
        progressEl.textContent = percent + '%';
    }
}
