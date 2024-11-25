import os
import argparse
from datetime import datetime

def get_file_emoji(file_path):
    """Returns appropriate emoji based on file type"""
    if os.path.isdir(file_path):
        return "📂"
    
    # Get the file extension
    _, ext = os.path.splitext(file_path.lower())
    
    # Map extensions to emojis
    emoji_map = {
        # Programming files
        '.py': "🐍",
        '.js': "💛",
        '.html': "🌐",
        '.css': "🎨",
        '.java': "☕",
        '.cpp': "⚡",
        '.c': "⚡",
        
        # Documentation
        '.md': "📝",
        '.txt': "📄",
        '.pdf': "📕",
        '.doc': "📘",
        '.docx': "📘",
        
        # Configuration
        '.json': "⚙️",
        '.yml': "⚙️",
        '.yaml': "⚙️",
        '.xml': "⚙️",
        '.ini': "⚙️",
        '.env': "🔒",
        '.gitignore': "🔒",
        
        # Data files
        '.csv': "📊",
        '.xlsx': "📊",
        '.db': "🗄️",
        '.sql': "🗄️",
        
        # Media files
        '.jpg': "🖼️",
        '.jpeg': "🖼️",
        '.png': "🖼️",
        '.gif': "🖼️",
        '.mp3': "🎵",
        '.mp4': "🎥",
        
        # Archives
        '.zip': "📦",
        '.rar': "📦",
        '.tar': "📦",
        '.gz': "📦",
        
        # Special files
        'license': "📜",
        'readme': "📖",
    }
    
    # Check for special filenames first (case-insensitive)
    lower_name = os.path.basename(file_path).lower()
    for special_name, emoji in emoji_map.items():
        if special_name in lower_name:
            return emoji
    
    # Then check extensions
    return emoji_map.get(ext, "📄")  # Default to generic file emoji

def write_tree(directory_path, outfile, prefix=""):
    """Recursively writes the tree structure to the output file"""
    entries = os.listdir(directory_path)
    entries.sort()
    
    for i, entry in enumerate(entries):
        entry_path = os.path.join(directory_path, entry)
        is_last = i == len(entries) - 1
        
        # Get appropriate emoji
        emoji = get_file_emoji(entry_path)
        
        if is_last:
            outfile.write(f"{prefix}└── {emoji} {entry}\n")
            new_prefix = prefix + "    "
        else:
            outfile.write(f"{prefix}├── {emoji} {entry}\n")
            new_prefix = prefix + "│   "
        
        if os.path.isdir(entry_path):
            write_tree(entry_path, outfile, new_prefix)

def scan_directory(directory_path, output_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Write header
            outfile.write(f"📋 Directory Scan Report\n")
            outfile.write(f"⏰ Generated on: {timestamp}\n")
            outfile.write(f"📍 Scanned directory: {os.path.abspath(directory_path)}\n")
            outfile.write("=" * 80 + "\n\n")
            
            # First, write the tree view
            outfile.write("🌳 DIRECTORY STRUCTURE:\n")
            outfile.write("-" * 80 + "\n")
            write_tree(directory_path, outfile)
            outfile.write("\n" + "=" * 80 + "\n\n")
            
            # Then, write file contents
            outfile.write("📚 FILE CONTENTS:\n")
            outfile.write("-" * 80 + "\n\n")
            
            # Walk through the directory
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory_path)
                    emoji = get_file_emoji(file_path)
                    
                    # Write file header
                    outfile.write(f"File: {emoji} {relative_path}\n")
                    outfile.write("-" * 80 + "\n")
                    
                    # Try to read and write file contents
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(content)
                    except Exception as e:
                        outfile.write(f"❌ [Error reading file: {str(e)}]\n")
                    
                    outfile.write("\n" + "=" * 80 + "\n\n")
        
        print(f"✅ Scan completed successfully. Output written to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Scan a directory and create a report of tree view and file contents'
    )
    parser.add_argument(
        'directory',
        help='Directory path to scan'
    )
    parser.add_argument(
        '-o', '--output',
        default='scan_report.txt',
        help='Output file path (default: scan_report.txt)'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if directory exists
    if not os.path.isdir(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        return
    
    # Run the scanner
    scan_directory(args.directory, args.output)

if __name__ == "__main__":
    main()