#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check translation status - Verify how many files have been translated
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def check_status():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    log_file = script_dir / "translation_log.json"
    
    print("\n" + "=" * 80)
    print("📊 Translation Status Report")
    print("=" * 80 + "\n")
    
    # Load log
    if log_file.exists():
        with open(log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
    else:
        log_data = {}
    
    # Count by status
    status_count = defaultdict(int)
    for file_path, info in log_data.items():
        status = info.get('status', 'unknown')
        status_count[status] += 1
    
    # Count total markdown files
    total_md_files = 0
    for root, dirs, files in os.walk(project_root):
        if 'translation-script' in root or 'images' in root:
            continue
        total_md_files += len([f for f in files if f.endswith('.md')])
    
    # Display statistics
    completed = status_count.get('completed', 0)
    failed = len([s for s in status_count.keys() if s.startswith('error')])
    untranslated = total_md_files - completed - failed
    
    print(f"📈 Overall Statistics:")
    print(f"  Total .md files: {total_md_files}")
    print(f"  ✅ Translated: {completed}")
    print(f"  ❌ Failed: {failed}")
    print(f"  ⏳ Untranslated: {untranslated}")
    print(f"  📊 Progress: {(completed/total_md_files*100):.1f}%" if total_md_files > 0 else "  📊 Progress: 0%")
    
    print(f"\n📋 Files by Status:")
    for status, count in sorted(status_count.items()):
        print(f"  {status}: {count} files")
    
    # Show some recent translations
    if log_data:
        print(f"\n📝 Recent Translations:")
        recent = sorted(log_data.items(), key=lambda x: x[1].get('timestamp', ''))[-5:]
        for file_path, info in recent:
            timestamp = info.get('timestamp', 'N/A')[:16]
            status = info.get('status', 'unknown')
            print(f"  • {file_path}: {status} ({timestamp})")
    
    print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    check_status()
