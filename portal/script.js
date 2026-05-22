/* script.js */
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('file-browser');
    if (typeof FILE_TREE !== 'undefined' && container) {
        renderTree(FILE_TREE, container);
        updateProgress();
    }
});

function renderTree(data, container, parentCheckbox = null) {
    data.forEach(item => {
        const nodeDiv = document.createElement('div');
        nodeDiv.className = 'tree-node';
        
        const storageKey = 'path_' + (item.path || item.name);
        
        if (item.type === 'directory') {
            const card = document.createElement('div');
            card.className = 'module-card';
            
            const header = document.createElement('div');
            header.className = 'module-header';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = storageKey;
            checkbox.className = 'folder-check';
            
            const arrow = document.createElement('span');
            arrow.className = 'arrow';
            arrow.textContent = '▶';
            
            const title = document.createElement('span');
            title.className = 'module-title';
            title.textContent = item.name;
            
            header.appendChild(checkbox);
            header.appendChild(arrow);
            header.appendChild(title);
            card.appendChild(header);
            
            const childList = document.createElement('div');
            childList.className = 'file-list hidden';
            card.appendChild(childList);
            
            nodeDiv.appendChild(card);
            
            // Expand/Collapse
            header.onclick = (e) => {
                if (e.target === checkbox) return;
                const isHidden = childList.classList.toggle('hidden');
                header.parentElement.classList.toggle('expanded', !isHidden);
                arrow.textContent = isHidden ? '▶' : '▼';
            };

            // Folder Checkbox Logic: Toggle all children
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
            
            // Initial folder state based on children
            const childCbs = childList.querySelectorAll('input[type="checkbox"]');
            if (childCbs.length > 0) {
                const allChecked = Array.from(childCbs).every(cb => localStorage.getItem(cb.id) === 'true');
                checkbox.checked = allChecked;
                localStorage.setItem(storageKey, allChecked);
            }

        } else {
            const fileItem = document.createElement('div');
            fileItem.className = 'file-item';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = storageKey;
            checkbox.checked = localStorage.getItem(storageKey) === 'true';
            
            const link = document.createElement('a');
            link.href = 'https://github.com/rmia46/fluent-data-science/blob/main/' + item.path;
            link.target = '_blank';
            link.textContent = '📄 ' + item.name;
            
            fileItem.appendChild(checkbox);
            fileItem.appendChild(link);
            nodeDiv.appendChild(fileItem);
            
            checkbox.onchange = () => {
                localStorage.setItem(storageKey, checkbox.checked);
                if (parentCheckbox) {
                    const siblingCbs = container.querySelectorAll('input[type="checkbox"]');
                    const allChecked = Array.from(siblingCbs).every(cb => cb.checked);
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
    const allFileCheckboxes = document.querySelectorAll('.file-item input[type="checkbox"]');
    const total = allFileCheckboxes.length;
    const checked = Array.from(allFileCheckboxes).filter(cb => cb.checked).length;
    const percent = total > 0 ? Math.round((checked / total) * 100) : 0;
    
    const progressEl = document.getElementById('progress-percent');
    if (progressEl) {
        progressEl.textContent = percent + '%';
    }
}
