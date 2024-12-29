import os

def sanitize_name(name):
    """Convert a title to a filename-friendly format"""
    # Replace forward slashes with hyphens
    name = name.replace('/', '-')
    return name.lower().strip().replace(' ', '-').replace('(', '').replace(')', '').replace('&', 'and')

def create_file(path, content):
    """Create a file with given content"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def process_section(section_text):
    """Process a section of text to extract title and articles"""
    lines = section_text.strip().split('\n')
    title = lines[0].replace('## ', '').strip()
    articles = []
    
    for line in lines[1:]:
        if line.strip() and line.startswith('- '):
            # Only process top-level bullets
            article = line.replace('- ', '').strip()
            if not article.startswith('  '):  # Skip indented bullets
                articles.append(article)
    
    return title, articles

def create_kb_structure(text):
    """Create the knowledge base structure from the given text"""
    # Create base docs directory
    os.makedirs('docs', exist_ok=True)
    
    # Split into sections
    sections = text.split('## ')[1:]  # Skip the initial "Article List" header
    
    for section in sections:
        title, articles = process_section(section)
        section_dir = os.path.join('docs', sanitize_name(title))
        
        # Create section directory
        os.makedirs(section_dir, exist_ok=True)
        
        # Create index.md for the section
        index_content = f"# {title}\n\n"
        index_content += "Choose from the following topics:\n\n"
        
        # Create article files and add them to index
        for article in articles:
            article_filename = f"{sanitize_name(article)}.md"
            article_path = os.path.join(section_dir, article_filename)
            
            # Create article file
            article_content = f"# {article}\n\n[Add content for {article}]\n"
            create_file(article_path, article_content)
            
            # Add to index
            index_content += f"- [{article}]({article_filename})\n"
        
        # Save index file
        create_file(os.path.join(section_dir, 'index.md'), index_content)

# Read the input file and create structure
with open('paste.txt', 'r', encoding='utf-8') as f:
    content = f.read()

create_kb_structure(content)
print("Knowledge base structure created successfully!")