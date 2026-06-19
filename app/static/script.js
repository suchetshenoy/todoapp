document.addEventListener('DOMContentLoaded', () => {
    // Accordion toggle
    document.querySelectorAll('.list-title, .toggle-icon').forEach(el => {
        el.addEventListener('click', (e) => {
            const card = e.target.closest('.list-card');
            if (card) {
                card.classList.toggle('expanded');
            }
        });
    });

    // Add micro-animations or subtle effects
    const cards = document.querySelectorAll('.list-card');

    // Auto-focus input when a form is clicked (if it's not already focused)
    const forms = document.querySelectorAll('.add-item-form, .add-list-form');
    forms.forEach(form => {
        form.addEventListener('click', () => {
            const input = form.querySelector('input[type="text"]');
            if (document.activeElement !== input) {
                input.focus();
            }
        });
    });

        // Initialize List Sorting
    const listsContainer = document.getElementById('lists-container');
    if (listsContainer) {
        new Sortable(listsContainer, {
            handle: '.list-drag-handle', // Only drag when clicking the handle
            animation: 150,              // Smooth animation
            ghostClass: 'sortable-ghost',
            onEnd: function () {
                // Get new order of list IDs
                const listIds = Array.from(listsContainer.querySelectorAll('.list-card'))
                    .filter(el => el.hasAttribute('data-id'))
                    .map(el => el.getAttribute('data-id'));
                
                // Send new order to backend
                fetch('/reorder_lists', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ order: listIds })
                });
            }
        });
    }

    // Initialize Item Sorting for each individual list
    const itemsContainers = document.querySelectorAll('.items-container');
    itemsContainers.forEach(container => {
        new Sortable(container, {
            handle: '.item-drag-handle',
            animation: 150,
            ghostClass: 'sortable-ghost',
            onEnd: function () {
                const listId = container.getAttribute('data-list-id');
                const itemIds = Array.from(container.querySelectorAll('.item'))
                    .map(el => el.getAttribute('data-id'));
                
                fetch(`/list/${listId}/reorder_items`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ order: itemIds })
                });
            }
        });
    });
});


