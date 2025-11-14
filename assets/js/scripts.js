document.addEventListener('DOMContentLoaded', () => {
  const yearTarget = document.getElementById('currentYear');
  if (yearTarget) {
    yearTarget.textContent = new Date().getFullYear();
  }

  const navbar = document.getElementById('mainNav');
  if (navbar) {
    const collapseElement = navbar.querySelector('.navbar-collapse');
    const navLinks = navbar.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach((link) => {
      link.addEventListener('click', () => {
        if (collapseElement && collapseElement.classList.contains('show')) {
          const collapse = bootstrap.Collapse.getInstance(collapseElement) || new bootstrap.Collapse(collapseElement, { toggle: false });
          collapse.hide();
        }
      });
    });
  }
});
