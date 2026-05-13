#!/usr/bin/env python3
"""
Phase 4 & 5: Rename Cemical-Bond files and bulk formatting cleanup.

Phase 4: Renames Cemical-Bond*.md -> Chemical-Bond*.md and updates all internal references.
Phase 5: Strips trailing whitespace and reduces excessive blank lines across all .md files.
"""

import os
import re
import glob

WORKSPACE = "/home/azaz/AntigravityData/Chemistry-Semester-Final"

# ============================================================
# PHASE 4: Rename Cemical-Bond -> Chemical-Bond
# ============================================================

def phase4_rename():
    """Rename files and update all references."""
    bond_dir = os.path.join(WORKSPACE, "ResourcesGivenByTeachers", "Chemical-Bond")
    
    # Step 1: Rename files
    renamed = 0
    for i in range(1, 9):
        old = os.path.join(bond_dir, f"Cemical-Bond{i:02d}.md")
        new = os.path.join(bond_dir, f"Chemical-Bond{i:02d}.md")
        if os.path.exists(old):
            os.rename(old, new)
            renamed += 1
            print(f"  Renamed: Cemical-Bond{i:02d}.md -> Chemical-Bond{i:02d}.md")
    
    # Step 2: Update ALL references across the entire workspace
    refs_updated = 0
    for root, dirs, files in os.walk(WORKSPACE):
        # Skip .git and .obsidian
        dirs[:] = [d for d in dirs if d not in ('.git', '.obsidian')]
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'Cemical-Bond' in content:
                new_content = content.replace('Cemical-Bond', 'Chemical-Bond')
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count = content.count('Cemical-Bond')
                refs_updated += count
                print(f"  Updated {count} reference(s) in: {os.path.relpath(fpath, WORKSPACE)}")
    
    print(f"\n  Phase 4 Summary: {renamed} files renamed, {refs_updated} references updated.")


# ============================================================
# PHASE 5: Bulk formatting cleanup
# ============================================================

def phase5_cleanup():
    """Strip trailing whitespace and reduce excessive blank lines."""
    files_modified = 0
    trailing_ws_fixed = 0
    blank_lines_fixed = 0
    
    for root, dirs, files in os.walk(WORKSPACE):
        dirs[:] = [d for d in dirs if d not in ('.git', '.obsidian')]
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # 1. Strip trailing whitespace from each line
            lines = content.split('\n')
            new_lines = []
            for line in lines:
                stripped = line.rstrip()
                if stripped != line:
                    trailing_ws_fixed += 1
                new_lines.append(stripped)
            content = '\n'.join(new_lines)
            
            # 2. Reduce 3+ consecutive blank lines to exactly 2
            while '\n\n\n\n' in content:
                old_content = content
                content = re.sub(r'\n{4,}', '\n\n\n', content)
                if content != old_content:
                    blank_lines_fixed += 1
                else:
                    break
            
            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_modified += 1
    
    print(f"\n  Phase 5 Summary: {files_modified} files modified, {trailing_ws_fixed} trailing whitespace instances fixed, {blank_lines_fixed} excessive blank line sequences fixed.")


# ============================================================
# PHASE 6: Convert broken image links to descriptive placeholders
# ============================================================

def phase6_image_placeholders():
    """Convert broken image references to descriptive placeholders."""
    images_converted = 0
    files_modified = 0
    
    # Pattern to match ![alt text](file:///...) or ![alt text](relative_path_to_missing_image)
    img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    
    for root, dirs, files in os.walk(WORKSPACE):
        dirs[:] = [d for d in dirs if d not in ('.git', '.obsidian')]
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            def replace_broken_image(match):
                alt_text = match.group(1)
                img_path = match.group(2)
                
                # Check if the image path is broken
                is_broken = False
                
                # file:// absolute paths to Downloads (all broken)
                if img_path.startswith('file:///'):
                    is_broken = True
                # Relative paths - check if file exists
                elif not img_path.startswith('http'):
                    abs_img = os.path.join(os.path.dirname(fpath), img_path)
                    if not os.path.exists(abs_img):
                        is_broken = True
                
                if is_broken:
                    return f'> 📷 **[Diagram]** {alt_text}'
                return match.group(0)
            
            content = img_pattern.sub(replace_broken_image, content)
            
            if content != original:
                count = original.count('![') - content.count('![')
                images_converted += count
                files_modified += 1
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Converted {count} image(s) in: {os.path.relpath(fpath, WORKSPACE)}")
    
    print(f"\n  Phase 6 Summary: {files_modified} files modified, {images_converted} broken image links converted to placeholders.")


if __name__ == '__main__':
    print("=" * 60)
    print("PHASE 4: Renaming Cemical-Bond -> Chemical-Bond")
    print("=" * 60)
    phase4_rename()
    
    print("\n" + "=" * 60)
    print("PHASE 5: Bulk Formatting Cleanup")
    print("=" * 60)
    phase5_cleanup()
    
    print("\n" + "=" * 60)
    print("PHASE 6: Broken Image Links -> Placeholders (Option A)")
    print("=" * 60)
    phase6_image_placeholders()
    
    print("\n" + "=" * 60)
    print("ALL PHASES COMPLETE")
    print("=" * 60)
