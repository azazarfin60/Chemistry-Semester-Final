import os

workspace = "/home/azaz/AntigravityData/Chemistry-Semester-Final"

# Walk through all directories and subdirectories
for root, dirs, files in os.walk(workspace):
    # Skip hidden directories like .git
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    # Find all markdown files in the current directory
    md_files = sorted([f for f in files if f.endswith('.md') and f != 'index.md'])
    
    if not md_files:
        continue

    # Get relative path for display purposes
    rel_path = os.path.relpath(root, workspace)
    dir_name = os.path.basename(root)
    if dir_name == '':
        dir_name = "Workspace Root"
        
    print(f"Processing directory: {rel_path} with {len(md_files)} files.")

    # Create index.md
    index_path = os.path.join(root, "index.md")
    
    with open(index_path, 'w') as f:
        f.write(f"# 📚 {dir_name} Index\n\n")
        f.write("---\n\n")
        for md_file in md_files:
            # Create a readable display name
            display = md_file.replace('.md', '').replace('_', ' ')
            f.write(f"- [{display}]({md_file})\n")
        f.write("\n---\n")

    # Add navigation to each file
    total_files = len(md_files)
    for i, md_file in enumerate(md_files):
        file_path = os.path.join(root, md_file)
        
        # Determine previous link
        if i == 0:
            prev_link = "*(start)*"
        else:
            prev_file = md_files[i-1]
            prev_display = prev_file.replace('.md', '').replace('_', ' ')
            prev_link = f"[⬅ {prev_display}]({prev_file})"
            
        # Determine next link
        if i == total_files - 1:
            next_link = "*(end)*"
        else:
            next_file = md_files[i+1]
            next_display = next_file.replace('.md', '').replace('_', ' ')
            next_link = f"[{next_display} ➡]({next_file})"
            
        nav_bar = f"{prev_link} | [🏠 Index](index.md) | {next_link}"
        
        # Read content
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Check if navigation is already present
        if "🏠 Index" in content[:200]:
            print(f"  ⏭ Skipping {md_file} (navigation already present)")
            continue
            
        # Add navigation at the top and bottom
        new_content = f"{nav_bar}\n\n---\n\n{content}\n\n---\n\n{nav_bar}\n"
        
        with open(file_path, 'w') as f:
            f.write(new_content)
        
        print(f"  ✅ Added navigation to {md_file}")

print("All directories recursively processed.")
