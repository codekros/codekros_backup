# Krishna Gawande - Portfolio

A modern, dynamic portfolio website built with HTML, CSS, and JavaScript featuring a rich dark theme and responsive design.

## 🎨 Features

### Design & Theme
- **Rich Dark Theme**: Sophisticated dark color palette with accent colors
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Responsive Design**: Mobile-first approach that works on all devices
- **Smooth Transitions**: CSS animations and hover effects throughout

### Technical Features
- **Dynamic Navigation**: Fixed navigation bar with smooth scrolling
- **Interactive Elements**: Hover effects, animations, and micro-interactions
- **Form Validation**: Contact form with client-side validation
- **Project Filtering**: Categorized project showcase with filtering
- **Loading Animations**: Smooth page transitions and loading states

## 🏗️ Architecture

### File Structure
```
html/
├── index.html          # Main landing page
├── about.html          # About page with skills and experience
├── projects.html       # Portfolio showcase with filtering
├── contact.html        # Contact form and information
├── styles.css          # Main stylesheet with CSS variables
└── script.js           # JavaScript functionality and interactions

images/
└── favicon.jpeg        # Site favicon

README.md               # Project documentation
```

### Technology Stack
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern CSS with custom properties (variables)
- **JavaScript (ES6+)**: Dynamic interactions and functionality
- **Font Awesome**: Icon library for visual elements
- **Google Fonts**: Inter font family for typography

### CSS Architecture
- **CSS Custom Properties**: Centralized color and spacing variables
- **Component-Based**: Modular CSS classes for reusability
- **Responsive Grid**: CSS Grid and Flexbox for layouts
- **Animation System**: Keyframe animations and transitions

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Local web server (optional, for development)

### Installation
1. Clone or download the project files
2. Open `html/index.html` in your web browser
3. Navigate through the different pages using the navigation menu

### Development Setup
1. Set up a local web server (e.g., Live Server in VS Code)
2. Make changes to HTML, CSS, or JavaScript files
3. Refresh the browser to see changes

## 📱 Pages Overview

### 1. Home Page (`index.html`)
- **Hero Section**: Eye-catching introduction with call-to-action buttons
- **Skills Preview**: Quick overview of technical skills
- **Quick Links**: Direct access to resume, LinkedIn, and contact

### 2. About Page (`about.html`)
- **Personal Introduction**: Detailed background and experience
- **Technical Skills**: Comprehensive skill showcase with icons
- **Experience & Education**: Professional background information
- **Core Competencies**: Key strengths and capabilities

### 3. Projects Page (`projects.html`)
- **Project Categories**: Filterable project showcase
- **Project Cards**: Detailed project information with tags
- **Interactive Filtering**: Category-based project filtering
- **GitHub Integration**: Links to open source contributions

### 4. Contact Page (`contact.html`)
- **Contact Information**: Multiple ways to get in touch
- **Contact Form**: Functional contact form with validation
- **Availability Status**: Response time and availability information
- **Social Links**: Direct links to professional profiles

## 🎯 Key Components

### Navigation System
- Fixed navigation bar with backdrop blur effect
- Active page highlighting
- Smooth scrolling to page sections
- Mobile-responsive design

### Button System
- Primary buttons for main actions
- Secondary buttons for alternative actions
- Hover effects with animations
- Consistent styling across all pages

### Card Components
- Project cards with hover effects
- Skill cards with icons
- Information cards for content sections
- Consistent spacing and typography

### Form System
- Contact form with validation
- Styled form inputs and textareas
- Error handling and success messages
- Responsive form layout

## 🎨 Design System

### Color Palette
- **Primary Background**: `#0a0a0a` (Deep Black)
- **Secondary Background**: `#111111` (Dark Gray)
- **Card Background**: `#1e1e1e` (Medium Gray)
- **Primary Accent**: `#6366f1` (Indigo)
- **Secondary Accent**: `#8b5cf6` (Purple)
- **Success**: `#10b981` (Green)
- **Warning**: `#f59e0b` (Amber)

### Typography
- **Primary Font**: Inter (Google Fonts)
- **Monospace Font**: JetBrains Mono (for code elements)
- **Font Weights**: 300, 400, 500, 600, 700
- **Responsive Sizing**: Fluid typography that scales with viewport

### Spacing System
- **Base Unit**: 1rem (16px)
- **Small**: 0.5rem (8px)
- **Medium**: 1rem (16px)
- **Large**: 1.5rem (24px)
- **Extra Large**: 2rem (32px)

## 🔧 Customization

### Changing Colors
Modify the CSS custom properties in `styles.css`:
```css
:root {
  --accent-primary: #your-color;
  --bg-primary: #your-background;
}
```

### Adding New Pages
1. Create new HTML file following the existing structure
2. Include navigation bar and footer
3. Add page-specific styles to `styles.css`
4. Update navigation links in all pages

### Modifying Projects
Edit the project cards in `projects.html`:
```html
<div class="project-card" data-category="your-category">
  <!-- Project content -->
</div>
```

## 📱 Responsive Design

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

### Mobile Optimizations
- Stacked navigation layout
- Single-column card grids
- Optimized button layouts
- Touch-friendly interactions

## 🚀 Performance Features

### Optimizations
- CSS custom properties for efficient theming
- Minimal JavaScript for core functionality
- Optimized animations with CSS transforms
- Efficient DOM manipulation

### Loading States
- Smooth page transitions
- Loading animations
- Progressive enhancement
- Graceful degradation

## 🔒 Browser Support

### Supported Browsers
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

### Features
- CSS Grid and Flexbox
- CSS Custom Properties
- ES6+ JavaScript
- Modern CSS animations

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

- **Email**: krishna@example.com
- **LinkedIn**: [Krishna Gawande](https://in.linkedin.com/in/krishna-gawande22)
- **GitHub**: [GitHub Profile](https://github.com)

---

Built with ❤️ by Krishna Gawande
