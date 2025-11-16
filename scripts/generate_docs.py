#!/usr/bin/env python3
"""
Generate documentation for all encoders from their source code.

This script:
1. Reads all encoder source files from src/usenc/encoders/
2. Extracts encoder information (name, description, parameters, examples)
3. Generates individual markdown files in docs/encoders/
4. Generates the main encoders.md listing all encoders
"""

import sys
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Any

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from usenc.encoders import ENCODERS


def extract_docstring_parts(docstring: str) -> Tuple[str, str, List[str]]:
    """
    Extract parts from encoder docstring.

    Args:
        docstring: The class docstring

    Returns:
        tuple: (short_description, long_description, examples_list)
    """
    if not docstring:
        return "", "", []

    # Split into lines and clean
    lines = docstring.strip().split('\n')
    cleaned_lines = [line.strip() for line in lines]

    # First non-empty line is short description
    short_desc = ""
    long_desc_lines = []
    examples = []

    state = "short"  # short, long, examples

    for line in cleaned_lines:
        if not line:
            if state == "short":
                state = "long"
            continue

        # Check if we're entering examples section
        if line.lower().startswith('examples:'):
            state = "examples"
            continue

        if state == "short":
            short_desc = line
            state = "long"
        elif state == "long":
            long_desc_lines.append(line)
        elif state == "examples":
            # Parse example lines like "hello world -> hello%20world"
            examples.append(line)

    long_desc = '\n'.join(long_desc_lines)

    return short_desc, long_desc, examples


def format_param_flag(param_name: str) -> str:
    """Convert parameter name to CLI flag format."""
    return f"--{param_name.replace('_', '-')}"


def generate_encoder_markdown(encoder_name: str, encoder_class: Any) -> str:
    """
    Generate markdown documentation for a single encoder.

    Args:
        encoder_name: Name of the encoder (e.g., 'url')
        encoder_class: The encoder class

    Returns:
        str: Markdown formatted documentation
    """
    # Extract information from docstring
    docstring = encoder_class.__doc__ or ""
    short_desc, long_desc, examples = extract_docstring_parts(docstring)

    # Build markdown document
    md = []

    # NAME section
    md.append("### NAME")
    md.append("")
    md.append(f"`{encoder_name}` - {short_desc}")
    md.append("")

    # DESCRIPTION section (if long description exists)
    if long_desc:
        md.append("### DESCRIPTION")
        md.append("")
        md.append(long_desc)
        md.append("")

    # OPTIONS section
    if hasattr(encoder_class, 'params') and encoder_class.params:
        md.append("### OPTIONS")
        md.append("")

        for param_name, param_spec in encoder_class.params.items():
            flag = format_param_flag(param_name)
            help_text = param_spec.get('help', '')

            md.append("")
            md.append(f"#### {flag}")
            md.append('<div class="option-desc">')
            if help_text:
                md.append(help_text)
            md.append('</div>')

        md.append("")

    # EXAMPLES section
    if examples:
        md.append("### EXAMPLES")
        md.append("")
        md.append("Sample  |   Encoded")
        md.append("--- | ---")

        for example in examples:
            # Parse "input -> output" format
            if '->' in example:
                parts = example.split('->', 1)
                if len(parts) == 2:
                    input_str = parts[0].strip()
                    output_str = parts[1].strip()
                    md.append(f"`{input_str}` | `{output_str}`")

    return '\n'.join(md)

def copy_readme(project_root: Path, docs_dir: Path):
    """
    Copy README.md from project root to docs directory as index.md.

    Args:
        project_root: Path to project root
        docs_dir: Path to docs directory
    """
    readme_src = project_root / "README.md"
    readme_dst = docs_dir / "index.md"

    if readme_src.exists():
        shutil.copy2(readme_src, readme_dst)
        print(f"  ✓ Copied README.md to docs/index.md")
    else:
        print(f"  ⚠ Warning: README.md not found at {readme_src}")


def main():
    """Main function to generate all documentation."""
    # Get project paths
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs"
    encoders_dir = docs_dir / "encoders"

    # Create encoders directory if it doesn't exist
    encoders_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Generating Encoder Documentation")
    print("=" * 60)
    print()

    # Copy README.md to docs directory
    print("Copying README.md...")
    copy_readme(project_root, docs_dir)
    print()

    # Generate documentation for each encoder
    print(f"Found {len(ENCODERS)} encoders")
    print()

    for encoder_name in sorted(ENCODERS.keys()):
        encoder_class = ENCODERS[encoder_name]

        print(f"  ✓ Generating docs for '{encoder_name}'")

        # Generate the markdown documentation
        doc_content = generate_encoder_markdown(encoder_name, encoder_class)

        # Write to file
        doc_file = encoders_dir / f"{encoder_name}.md"
        doc_file.write_text(doc_content, encoding='utf-8')

    print()
    print(f"Generated {len(ENCODERS)} encoder documentation files")
    print(f"  → {encoders_dir}/")
    print()

    print("=" * 60)
    print("Documentation Generation Complete!")
    print("=" * 60)


if __name__ == '__main__':
    main()