const fs = require('fs');
const path = require('path');

const srcDir = __dirname;
const outDir = path.join(__dirname, 'dist');

// Create dist directory
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

// Copy directories
const dirs = ['css', 'js', 'assets', 'blog', 'images'];
dirs.forEach(dir => {
  const src = path.join(srcDir, dir);
  const dest = path.join(outDir, dir);
  if (fs.existsSync(src)) {
    console.log(`Copying ${dir}...`);
    fs.cpSync(src, dest, { recursive: true });
  }
});

// Copy HTML files
const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.html'));
files.forEach(file => {
  console.log(`Copying ${file}...`);
  fs.copyFileSync(path.join(srcDir, file), path.join(outDir, file));
});

console.log('Build complete!');
