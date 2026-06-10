import re
import subprocess
import os
import json

md_path = 'Docs/RELATORIO.md'
with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'```mermaid\n(.*?)\n```', re.DOTALL)
matches = pattern.findall(content)

os.makedirs('Docs/img', exist_ok=True)

# Create puppeteer config to avoid sandbox issues
puppeteer_config = "puppeteer-config.json"
with open(puppeteer_config, 'w') as f:
    json.dump({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}, f)

new_content = content
for i, m in enumerate(matches):
    mmd_filename = f'temp_mermaid_{i}.mmd'
    png_filename = f'Docs/img/mermaid_diagram_{i}.png'
    
    with open(mmd_filename, 'w', encoding='utf-8') as f:
        f.write(m)
        
    print(f"Generating image for diagram {i}...")
    try:
        # Run mmdc using npx.cmd for Windows
        subprocess.run(['npx.cmd', '-y', '@mermaid-js/mermaid-cli', '-i', mmd_filename, '-o', png_filename, '-p', puppeteer_config, '-b', 'transparent'], check=True)
        print(f"Success: {png_filename}")
        
        # Replace the original block with image reference
        original_block = f'```mermaid\n{m}\n```'
        img_ref = f'![Diagrama Mermaid {i}](img/mermaid_diagram_{i}.png)'
        new_content = new_content.replace(original_block, img_ref)
    except Exception as e:
        print(f"Failed to generate {png_filename}: {e}")
    finally:
        if os.path.exists(mmd_filename):
            os.remove(mmd_filename)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

if os.path.exists(puppeteer_config):
    os.remove(puppeteer_config)

print("Processamento concluído. O arquivo RELATORIO.md foi atualizado.")
