document.addEventListener('DOMContentLoaded', function () {
    const filters = document.querySelectorAll('.filters li');
    const projectContainers = document.querySelectorAll('.project-container');

    filters.forEach(filter => {
        filter.addEventListener('click', function () {
            const filterValue = this.getAttribute('data-filter');

            // Activate the clicked filter
            filters.forEach(btn => btn.classList.remove('filter-active'));
            this.classList.add('filter-active');

            // Add class for transition effects
            projectContainers.forEach(container => {
                if (filterValue === '*' || container.classList.contains(filterValue.substring(1))) {
                    container.classList.remove('hidden');
                    container.classList.add('show');
                } else {
                    container.classList.add('hidden');
                    container.classList.remove('show');
                }
            });

            // Ensure the project containers are updated for smooth transition
            setTimeout(() => {
                projectContainers.forEach(container => {
                    if (container.classList.contains('hidden')) {
                        container.style.display = 'none';
                    } else {
                        container.style.display = 'block';
                    }
                });
            }, 500); // Match the CSS transition duration
        });
    });
});
