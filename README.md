# Multipurpose Bootstrap Template

This repository provides a production-ready, multi-page Bootstrap 5 starter that you can clone and customize for client projects, landing pages, portfolios, or blogs. Each page is hand-crafted with responsive sections, reusable UI patterns, and accessible markup.

## Features

- **Multi-page structure** covering the most common marketing use-cases: home, about, services, portfolio, blog, and contact pages.
- **Bootstrap 5.3.3** via CDN with Bootstrap Icons and Google Fonts for modern typography.
- **Custom theme layer** in `assets/css/styles.css` with gradients, timeline styling, and hover effects.
- **JavaScript enhancements** in `assets/js/scripts.js` for responsive navigation and automatic copyright year handling.
- **Ready-to-use sections** including hero areas, feature grids, pricing tables, testimonials, FAQs, forms, accordions, and embeddable media.
- **SEO-friendly metadata** with canonical links and descriptive meta tags on each page.

## Getting Started

1. Open `templates/index.html` in your browser to preview the homepage.
2. Update navigation links, copy, and imagery to match your brand.
3. Customize theme colors or spacing inside `assets/css/styles.css`.
4. Extend the JavaScript helper in `assets/js/scripts.js` for additional interactive behavior.
5. Deploy the `templates` directory (and supporting `assets` folders) to any static hosting provider.

## Development Tips

- Use a local web server such as `python -m http.server` from the repository root to preview changes across pages.
- Replace external image and video URLs with your own assets or host them locally under `assets/img/`.
- Adjust the Bootstrap theme (`data-bs-theme` attribute) to support dark mode or alternative styling.

## Testing

A lightweight pytest suite verifies that each HTML page includes the required Bootstrap dependencies and key structural elements. Install `pytest` if needed (`pip install pytest`) and run:

```bash
pytest
```

## License

This template is released under the MIT License. See [LICENSE](LICENSE) for details.
