#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AWS Solutions Architect Professional - Portuguese Translation Script
Automatically translates all .md files maintaining Portuguese on top and English below
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from googletrans import Translator
import time

class MarkdownTranslator:
    def __init__(self, project_root, output_log="translation_log.json"):
        self.project_root = Path(project_root)
        self.translator = Translator()
        self.output_log = self.project_root / "translation-script" / output_log
        self.translated_files = self.load_progress()
        self.separator = "\n\n---\n\n"
        
    def load_progress(self):
        """Load previously translated files from log"""
        if self.output_log.exists():
            try:
                with open(self.output_log, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_progress(self):
        """Save translation progress to log"""
        with open(self.output_log, 'w', encoding='utf-8') as f:
            json.dump(self.translated_files, f, ensure_ascii=False, indent=2)
    
    def get_all_md_files(self):
        """Get all .md files excluding already translated ones"""
        md_files = []
        for root, dirs, files in os.walk(self.project_root):
            # Skip translation-script directory and images directories
            if 'translation-script' in root or 'images' in root:
                continue
            
            for file in files:
                if file.endswith('.md'):
                    full_path = Path(root) / file
                    relative_path = str(full_path.relative_to(self.project_root))
                    
                    # Check if already has separator (already translated)
                    if not self.file_already_translated(full_path):
                        md_files.append(full_path)
        
        return sorted(md_files)
    
    def file_already_translated(self, file_path):
        """Check if file already has translation markers"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                return '---' in content and content.count('\n---\n') >= 1
        except:
            return False
    
    def translate_text(self, text, source_lang='en', target_lang='pt'):
        """Translate text using Google Translate"""
        if not text or len(text.strip()) < 5:
            return text
        
        try:
            # Split text into chunks if too long (API limitation)
            max_chars = 4500
            if len(text) > max_chars:
                chunks = self.split_text(text, max_chars)
                translated_chunks = []
                for chunk in chunks:
                    translated = self.translator.translate(chunk, src_language=source_lang, dest_language=target_lang)
                    translated_chunks.append(translated['text'])
                    time.sleep(0.5)  # Rate limiting
                return ''.join(translated_chunks)
            else:
                result = self.translator.translate(text, src_language=source_lang, dest_language=target_lang)
                return result['text']
        except Exception as e:
            print(f"❌ Translation error: {str(e)}")
            return text
    
    def split_text(self, text, max_length):
        """Split text by paragraphs for translation"""
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = ""
        
        for para in paragraphs:
            if len(current_chunk) + len(para) < max_length:
                current_chunk += para + '\n\n'
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = para + '\n\n'
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks
    
    def should_translate_line(self, line):
        """Determine if a line should be translated (skip URLs, code, etc)"""
        line = line.strip()
        # Skip empty lines, URLs, code blocks, and image references
        if (not line or 
            line.startswith('![') or 
            line.startswith('[') or 
            line.startswith('http') or
            line.startswith('```') or
            line.startswith('    ') or
            '://' in line or
            line.startswith('#') and '```' in line):
            return False
        return True
    
    def translate_markdown_content(self, content):
        """Translate markdown content preserving structure"""
        lines = content.split('\n')
        translated_lines = []
        in_code_block = False
        
        for line in lines:
            # Toggle code block state
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                translated_lines.append(line)
            elif in_code_block:
                # Don't translate code blocks
                translated_lines.append(line)
            elif self.should_translate_line(line):
                try:
                    translated = self.translate_text(line)
                    translated_lines.append(translated)
                    time.sleep(0.2)  # Rate limiting between lines
                except:
                    translated_lines.append(line)
            else:
                translated_lines.append(line)
        
        return '\n'.join(translated_lines)
    
    def process_file(self, file_path):
        """Translate a single markdown file"""
        try:
            relative_path = str(file_path.relative_to(self.project_root))
            print(f"📄 Processing: {relative_path}...", end=' ')
            
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Skip if file is empty or already translated
            if not original_content.strip() or self.file_already_translated(file_path):
                print("⏭️  Already translated or empty")
                return False
            
            # Translate content
            print("🔄 Translating...", end=' ')
            translated_content = self.translate_markdown_content(original_content)
            
            # Combine translated and original
            final_content = translated_content + self.separator + original_content
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            # Log progress
            self.translated_files[relative_path] = {
                'timestamp': datetime.now().isoformat(),
                'status': 'completed'
            }
            self.save_progress()
            
            print("✅ Done!")
            return True
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            self.translated_files[relative_path] = {
                'timestamp': datetime.now().isoformat(),
                'status': f'error: {str(e)}'
            }
            self.save_progress()
            return False
    
    def run(self):
        """Main execution function"""
        print("=" * 80)
        print("🌍 AWS Solutions Architect Professional - Portuguese Translator")
        print("=" * 80)
        
        md_files = self.get_all_md_files()
        
        if not md_files:
            print("✅ No files to translate! All files are already processed.")
            return
        
        print(f"\n📊 Found {len(md_files)} files to translate")
        print(f"⏱️  Estimated time: ~{len(md_files) * 3} seconds (3s per file)\n")
        
        start_time = time.time()
        successful = 0
        failed = 0
        
        for idx, file_path in enumerate(md_files, 1):
            print(f"[{idx}/{len(md_files)}]", end=' ')
            if self.process_file(file_path):
                successful += 1
            else:
                failed += 1
            
            # Rate limiting to avoid API throttling
            time.sleep(1)
        
        elapsed_time = time.time() - start_time
        
        print("\n" + "=" * 80)
        print("📈 Translation Summary")
        print("=" * 80)
        print(f"✅ Successfully translated: {successful} files")
        print(f"❌ Failed: {failed} files")
        print(f"⏱️  Total time: {elapsed_time:.1f} seconds")
        print(f"📝 Log saved to: {self.output_log}")
        print("=" * 80)


def main():
    # Get project root (parent directory of translation-script folder)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print(f"📂 Project root: {project_root}\n")
    
    translator = MarkdownTranslator(project_root)
    translator.run()


if __name__ == "__main__":
    main()
