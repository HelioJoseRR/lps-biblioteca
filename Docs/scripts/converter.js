const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

const mdPath = path.join(__dirname, '..', 'RELATORIO.md');
let content = fs.readFileSync(mdPath, 'utf8');

const regex = /```mermaid\n([\s\S]*?)\n```/g;
let match;
let count = 0;

const imgDir = path.join(__dirname, '..', 'img');
if (!fs.existsSync(imgDir)){
    fs.mkdirSync(imgDir, { recursive: true });
}

const configPath = path.join(__dirname, 'puppeteer-config.json');
fs.writeFileSync(configPath, JSON.stringify({ args: ["--no-sandbox", "--disable-setuid-sandbox"] }));

let newContent = content;

// Precisamos coletar os matches primeiro para não bugar o regex.exec com as substituições
const matches = [...content.matchAll(regex)];

for (const m of matches) {
    const code = m[1];
    const mmdFile = path.join(__dirname, `temp_${count}.mmd`);
    const pngFile = path.join(__dirname, '..', 'img', `mermaid_${count}.png`);
    
    fs.writeFileSync(mmdFile, code);
    
    console.log(`Gerando diagrama ${count}...`);
    try {
        execSync(`npx.cmd -y @mermaid-js/mermaid-cli -i "${mmdFile}" -o "${pngFile}" -p "${configPath}" -b transparent`, { stdio: 'inherit' });
        console.log(`Sucesso: mermaid_${count}.png`);
        
        const originalBlock = m[0];
        const imgRef = `![Diagrama Mermaid ${count}](img/mermaid_${count}.png)`;
        newContent = newContent.replace(originalBlock, imgRef);
    } catch (err) {
        console.error(`Falha no diagrama ${count}:`, err.message);
    }
    
    if (fs.existsSync(mmdFile)) fs.unlinkSync(mmdFile);
    count++;
}

fs.writeFileSync(mdPath, newContent);
if (fs.existsSync(configPath)) fs.unlinkSync(configPath);

console.log('RELATORIO.md atualizado com sucesso com as imagens estáticas!');
