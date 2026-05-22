/* script.js */
fetch('file_tree.json')
    .then(response => response.json())
    .then(data => renderTree(data, document.getElementById('file-browser')));

function renderTree(data, container) {
    data.forEach(item => {
        const div = document.createElement('div');
        div.className = 'tree-node';
        if (item.type === 'directory') {
            div.innerHTML = `<span class="folder"><span class="arrow">▶</span> ${item.name}</span>`;
            const childContainer = document.createElement('div');
            childContainer.className = 'hidden';
            div.appendChild(childContainer);
            div.onclick = (e) => {
                e.stopPropagation();
                const arrow = div.querySelector('.arrow');
                arrow.textContent = childContainer.classList.contains('hidden') ? '▼' : '▶';
                childContainer.classList.toggle('hidden');
            };
            renderTree(item.children, childContainer);
        } else {
            div.innerHTML = `<span class="file">📄 ${item.name}</span>`;
        }
        container.appendChild(div);
    });
}
