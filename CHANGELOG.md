# 📝 Changelog

All notable changes to this LeetCode solutions repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## 🚀 How to View Changes

You can view changes in several ways:

### Using the Change Viewer Script
```bash
# View recent changes (last 7 days)
python3 view_changes.py

# View changes from last 30 days  
python3 view_changes.py --recent 30

# Show solution statistics
python3 view_changes.py --stats

# List all solutions
python3 view_changes.py --list

# View change history for a specific file
python3 view_changes.py --file "Solutions/121. Best Time to Buy and Sell Stock.java"
```

### Using Git Commands
```bash
# View recent commits
git log --oneline -10

# View changes in the last week
git log --since="1 week ago" --oneline

# View detailed changes for a specific file
git log -p -- "Solutions/filename.java"

# See what files were changed in recent commits
git log --name-only --oneline -5
```

---

## [Unreleased]

### Added
- 📜 `view_changes.py` - Interactive script to view repository changes
- 📝 `CHANGELOG.md` - This changelog file to track all changes
- 🔍 Enhanced documentation for viewing changes

### Removed
- 🗑️ Removed placeholder `blah` file from Solutions directory

---

## [2025-09-08] - Repository Enhancement

### Added
- 🖼️ Added contribution snake animation to README
- 📚 Enhanced README with better usage instructions
- ☕ **121. Best Time to Buy and Sell Stock** - Java solution with comments
- 💻 **1342. Number of Steps to Reduce a Number to Zero** - C++ solution
- 💻 **1672. Richest Customer Wealth** - C++ solution
- 💻 **412. Fizz Buzz** - C++ solution  
- ☕ **42. Trapping Rain Water** - Java solution with detailed logic

### Changed
- 📖 Updated README with comprehensive usage guide
- 🎯 Added clear goals and learning objectives
- 📬 Added contact information and social links

---

## Legend
- ☕ Java solutions
- 💻 C++ solutions  
- 🐍 Python solutions
- 📚 Documentation updates
- 🔧 Tools and utilities
- 🐛 Bug fixes
- 🗑️ Removals