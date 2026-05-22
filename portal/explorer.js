/* portal/explorer.js */

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('file-browser');
    if (typeof FILE_TREE !== 'undefined' && container) {
        // Detect if we are in a specific module view (e.g., learn/module01.html)
        const isModuleView = window.location.pathname.includes('/learn/module');
        let dataToRender = FILE_TREE;

        if (isModuleView) {
            const moduleNum = window.location.pathname.match(/module(\d+)/)[1];
            const targetDir = FILE_TREE.find(item => item.name.startsWith(moduleNum));
            dataToRender = targetDir ? [targetDir] : [];
        }

        renderTree(dataToRender, container);
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
            header.className = 'flex items-center p-4 bg-[#e8f5e9] cursor-pointer hover:bg-green-100 transition';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = storageKey;
            checkbox.className = 'w-5 h-5 accent-[#2e7d32] cursor-pointer mr-4 folder-check';
            
            const arrow = document.createElement('span');
            arrow.className = 'inline-block w-6 font-mono transition-transform duration-200';
            arrow.textContent = '▶';
            
            const title = document.createElement('span');
            title.className = 'flex-grow font-bold text-[#1b5e20]';
            title.textContent = item.name;
            
            header.appendChild(checkbox);
            header.appendChild(arrow);
            header.appendChild(title);
            card.appendChild(header);
            
            const childList = document.createElement('div');
            childList.className = 'hidden pl-8 pr-4 py-2 border-t border-gray-100';
            card.appendChild(childList);
            
            nodeDiv.appendChild(card);
            
            header.onclick = (e) => {
                if (e.target === checkbox) return;
                const isHidden = childList.classList.toggle('hidden');
                arrow.textContent = isHidden ? '▶' : '▼';
            };

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
            
            // Sync initial state
            const childCbs = childList.querySelectorAll('input[type="checkbox"]');
            if (childCbs.length > 0) {
                const allChecked = Array.from(childCbs).every(cb => localStorage.getItem(cb.id) === 'true');
                checkbox.checked = allChecked;
                localStorage.setItem(storageKey, allChecked);
            }

        } else {
            const fileItem = document.createElement('div');
            fileItem.className = 'flex items-center justify-between py-2 text-sm group/file';
            
            const leftPart = document.createElement('div');
            leftPart.className = 'flex items-center';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = storageKey;
            checkbox.className = 'w-4 h-4 accent-[#2e7d32] cursor-pointer mr-3 file-check';
            checkbox.checked = localStorage.getItem(storageKey) === 'true';
            
            const link = document.createElement('a');
            link.href = 'https://github.com/rmia46/fluent-data-science/blob/main/' + item.path;
            link.target = '_blank';
            link.className = 'text-[#2e7d32] hover:underline';
            link.textContent = '📄 ' + item.name;
            
            leftPart.appendChild(checkbox);
            leftPart.appendChild(link);
            
            const downloadBtn = document.createElement('a');
            downloadBtn.href = 'https://github.com/rmia46/fluent-data-science/raw/main/' + item.path;
            downloadBtn.className = 'ml-4 opacity-0 group-hover/file:opacity-100 bg-gray-100 hover:bg-primary hover:text-white px-2 py-1 text-[10px] font-bold uppercase tracking-widest transition-all';
            downloadBtn.textContent = 'Download';
            downloadBtn.setAttribute('download', '');

            fileItem.appendChild(leftPart);
            fileItem.appendChild(downloadBtn);
            nodeDiv.appendChild(fileItem);
            
            checkbox.onchange = () => {
                localStorage.setItem(storageKey, checkbox.checked);
                if (parentCheckbox) {
                    const allCbs = container.querySelectorAll('input.file-check');
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
    const allFileCheckboxes = document.querySelectorAll('input.file-check');
    const total = allFileCheckboxes.length;
    const checked = Array.from(allFileCheckboxes).filter(cb => cb.checked).length;
    const percent = total > 0 ? Math.round((checked / total) * 100) : 0;
    
    const progressEl = document.getElementById('progress-percent');
    if (progressEl) {
        progressEl.textContent = percent + '%';
    }
}
