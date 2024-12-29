import os
import re

def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def sanitize_filename(name):
    # Convert to lowercase, replace spaces with hyphens
    name = name.lower().strip()
    name = re.sub(r'[^a-z0-9-]', '-', name)
    name = re.sub(r'-+', '-', name)  # Replace multiple hyphens with single hyphen
    return name.strip('-')

def create_markdown_file(filepath, title, content=''):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n{content}')

def process_section(lines, base_path, current_indent=0):
    current_section = None
    section_content = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
            
        # Calculate the indent level of the current line
        indent = len(line) - len(line.lstrip())
        
        if indent == current_indent and line.strip().startswith('-'):
            # This is a new section at the current level
            if current_section:
                # Process the previous section
                section_path = os.path.join(base_path, sanitize_filename(current_section))
                create_directory_if_not_exists(section_path)
                create_markdown_file(
                    os.path.join(section_path, 'index.md'),
                    current_section,
                    '\n'.join(section_content)
                )
            
            current_section = line.strip('- \n')
            section_content = []
            
        elif indent > current_indent:
            # This is a subsection
            subsection_lines = []
            while i < len(lines) and (not lines[i].strip() or len(lines[i]) - len(lines[i].lstrip()) > current_indent):
                subsection_lines.append(lines[i])
                i += 1
            i -= 1  # Adjust for the outer loop increment
            
            if current_section:
                section_path = os.path.join(base_path, sanitize_filename(current_section))
                process_section(subsection_lines, section_path, indent)
        else:
            # Line is part of the current section's content
            if line.strip() and not line.strip().startswith('#'):
                section_content.append(line.strip())
        
        i += 1
    
    # Process the last section
    if current_section:
        section_path = os.path.join(base_path, sanitize_filename(current_section))
        create_directory_if_not_exists(section_path)
        create_markdown_file(
            os.path.join(section_path, 'index.md'),
            current_section,
            '\n'.join(section_content)
        )

def main():
    # Create base directory structure
    base_dirs = [
        'docs',
        'docs/assets',
        'docs/assets/images',
    ]
    for dir_path in base_dirs:
        create_directory_if_not_exists(dir_path)
    
    # Read the input file
    with open('paste.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines and process
    lines = content.split('\n')
    process_section(lines, 'docs', 0)
    
    # Create main index.md
    create_markdown_file(
        'docs/index.md',
        'Zudello Knowledge Base',
        'Welcome to the Zudello Knowledge Base. This documentation will help you understand and effectively use the Zudello platform.\n\n' +
        'Please navigate through the sections below to find the information you need.'
    )

if __name__ == '__main__':
    main()