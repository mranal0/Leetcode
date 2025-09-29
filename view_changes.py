#!/usr/bin/env python3
"""
LeetCode Solutions Change Viewer
Helps track and view changes to your LeetCode solutions repository.
"""

import subprocess
import os
import sys
from datetime import datetime, timedelta
import argparse

def run_git_command(command):
    """Run a git command and return the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception as e:
        print(f"Error running command: {e}")
        return None

def get_recent_changes(days=7):
    """Get recent changes in the last N days."""
    since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    cmd = f'git log --since="{since_date}" --pretty=format:"%h|%ad|%s" --date=short --name-only'
    output = run_git_command(cmd)
    
    if not output:
        print(f"No changes found in the last {days} days.")
        return
    
    print(f"📅 Changes in the last {days} days:\n")
    
    lines = output.split('\n')
    current_commit = None
    
    for line in lines:
        if '|' in line:  # This is a commit line
            parts = line.split('|')
            hash_val, date, message = parts[0], parts[1], parts[2]
            current_commit = hash_val
            print(f"🔸 {date} [{hash_val}] {message}")
        elif line.strip() and not line.startswith(' '):  # This is a file name
            if line.startswith('Solutions/'):
                print(f"  📝 {line}")
            else:
                print(f"  📄 {line}")
    print()

def get_solution_stats():
    """Get statistics about solutions."""
    java_count = run_git_command('find Solutions -name "*.java" | wc -l')
    cpp_count = run_git_command('find Solutions -name "*.cpp" | wc -l')
    py_count = run_git_command('find Solutions -name "*.py" | wc -l')
    
    print("📊 Solution Statistics:")
    print(f"  ☕ Java solutions: {java_count or 0}")
    print(f"  💻 C++ solutions: {cpp_count or 0}")
    print(f"  🐍 Python solutions: {py_count or 0}")
    print(f"  📝 Total solutions: {int(java_count or 0) + int(cpp_count or 0) + int(py_count or 0)}")
    print()

def show_file_changes(filename):
    """Show changes to a specific file."""
    cmd = f'git log --follow -p -- "{filename}"'
    output = run_git_command(cmd)
    
    if not output:
        print(f"No changes found for {filename}")
        return
    
    print(f"📜 Change history for {filename}:\n")
    print(output)

def list_solutions():
    """List all available solutions."""
    cmd = 'find Solutions -name "*.java" -o -name "*.cpp" -o -name "*.py" | sort'
    output = run_git_command(cmd)
    
    if not output:
        print("No solutions found.")
        return
    
    print("📚 Available Solutions:\n")
    for file in output.split('\n'):
        if file.strip():
            # Extract problem number and name from filename
            basename = os.path.basename(file)
            name_without_ext = os.path.splitext(basename)[0]
            ext = os.path.splitext(basename)[1]
            
            # Get language emoji
            lang_emoji = "☕" if ext == ".java" else "💻" if ext == ".cpp" else "🐍"
            
            print(f"  {lang_emoji} {name_without_ext}")
    print()

def main():
    parser = argparse.ArgumentParser(description='View changes in your LeetCode solutions repository')
    parser.add_argument('--recent', '-r', type=int, default=7, 
                       help='Show changes from the last N days (default: 7)')
    parser.add_argument('--stats', '-s', action='store_true',
                       help='Show solution statistics')
    parser.add_argument('--list', '-l', action='store_true',
                       help='List all solutions')
    parser.add_argument('--file', '-f', type=str,
                       help='Show change history for a specific file')
    
    args = parser.parse_args()
    
    print("🚀 LeetCode Solutions Change Viewer\n")
    
    # Check if we're in a git repository
    if not run_git_command('git rev-parse --git-dir'):
        print("❌ Error: Not in a git repository")
        sys.exit(1)
    
    if args.file:
        show_file_changes(args.file)
    elif args.list:
        list_solutions()
    elif args.stats:
        get_solution_stats()
    else:
        get_recent_changes(args.recent)
        get_solution_stats()

if __name__ == "__main__":
    main()