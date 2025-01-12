# Workflow to make and commit changes

Making Changes (Internal Work):

1. Switch to working-docs branch in GitHub Desktop
2. Open Obsidian and work in the Internal folder
3. Make your changes
4. Check changes in GitHub Desktop
5. Write a commit message describing your changes
6. Click "Commit to working-docs"
7. Click "Push origin"

Publishing to Public Documentation:

1. Copy the file(s) you want to publish from Internal folder to Knowledge Base folder
2. Review and remove any internal-only content
3. Still in working-docs branch:
    - Check changes in GitHub Desktop
    - Write commit message like "Add X to public documentation"
    - Click "Commit to working-docs"
    - Click "Push origin"

Publishing to GitBook:

1. Switch to main branch in GitHub Desktop
2. Click "Choose a branch to merge into main"
3. Select working-docs
4. Click "Create merge commit"
5. Click "Push origin"

Important Notes:

- Always check you're on the correct branch before making changes
- Internal content stays in the Internal folder and only appears in working-docs branch
- Public content goes in Knowledge Base folder and appears in both branches
- Changes only appear on GitBook after merging to main and pushing