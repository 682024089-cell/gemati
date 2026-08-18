#!/usr/bin/env python3
"""
Standardize video file extensions to lowercase for consistency.
This ensures compatibility with case-sensitive systems like Linux.
"""

import os
import shutil

VIDEO_DIR = os.path.join(os.path.dirname(__file__), 'static', 'video')

def normalize_video_files():
    """Rename video files with uppercase extensions to lowercase."""
    if not os.path.isdir(VIDEO_DIR):
        print(f"Video directory not found: {VIDEO_DIR}")
        return False
    
    files_to_rename = []
    
    for filename in os.listdir(VIDEO_DIR):
        if filename.upper().endswith('.MP4'):
            # File has uppercase MP4 extension
            filepath = os.path.join(VIDEO_DIR, filename)
            if os.path.isfile(filepath):
                new_filename = filename[:-4] + '.mp4'  # Replace last 4 chars (.MP4) with .mp4
                new_filepath = os.path.join(VIDEO_DIR, new_filename)
                
                if filename != new_filename:
                    files_to_rename.append((filepath, new_filepath, filename, new_filename))
    
    if not files_to_rename:
        print("All video files already have lowercase extensions.")
        return True
    
    print(f"Found {len(files_to_rename)} file(s) to rename:")
    
    for old_path, new_path, old_name, new_name in files_to_rename:
        try:
            if os.path.exists(new_path):
                print(f"  Skipping '{old_name}' (target '{new_name}' already exists)")
            else:
                shutil.move(old_path, new_path)
                print(f"  ✓ Renamed: {old_name} → {new_name}")
        except Exception as e:
            print(f"  ✗ Error renaming '{old_name}': {e}")
            return False
    
    return True

if __name__ == '__main__':
    success = normalize_video_files()
    exit(0 if success else 1)
