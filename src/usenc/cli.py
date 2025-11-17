#!/usr/bin/env python3
"""
URL Parameter Encoder - Encode URL parameters in various formats
"""
import sys
import argparse
from pathlib import Path
from contextlib import contextmanager
from typing import TextIO
from .encoders import ENCODERS
from .core import encode, decode

@contextmanager
def smart_open(filename: Path | None, mode: str, default_stream: TextIO):
    """
    Context manager that opens a file or uses a default stream (stdin/stdout)
    """
    if filename is None:
        # Use default stream (don't close it)
        yield default_stream
    else:
        # Open and close the file
        with filename.open(mode, encoding='utf-8') as f:
            yield f

def process_encoding(input_file: Path | None, output_file: Path | None, isDecoding: bool, global_params: dict, encoder_name: str, encoder_params: dict):
    """
    Process encoding from input to output
    """

    method = decode if isDecoding else encode

    with smart_open(input_file, 'r', sys.stdin) as infile, \
         smart_open(output_file, 'w', sys.stdout) as outfile:
        for line in infile:
            encoded = method(line, encoder_name, **global_params, **encoder_params)
            outfile.write(encoded)

def add_encoder_params(parser: argparse.ArgumentParser, encoder_name: str):
    """Add encoder-specific parameters to argument parser"""
    encoder = ENCODERS.get(encoder_name)
    if not encoder or not hasattr(encoder, 'params'):
        return

    for param_name, param_spec in encoder.params.items():
        flag = f"--{param_name.replace('_', '-')}"
        kwargs = {'help': param_spec.get('help', '')}

        # Handle boolean flags with action='store_true'
        if 'action' in param_spec:
            kwargs['action'] = param_spec['action']
        else:
            kwargs['type'] = param_spec.get('type', str)
            kwargs['default'] = param_spec.get('default')

        parser.add_argument(flag, **kwargs)

def add_default_params(parser: argparse.ArgumentParser):
    """ Setup default parameters for the parser """

    parser.add_argument(
        'encoder',
        choices=ENCODERS.keys(),
        help='Encoding format to use'
    )

    parser.add_argument(
        '-d', '--decode',
        action='store_true',
        help='Decode input to output'
    )

    parser.add_argument(
        '-i', '--input',
        type=Path,
        help='Input file (reads from stdin if not provided)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output file (writes to stdout if not provided)'
    )

    # group = parser.add_argument_group('global')

    # group.add_argument(
    #     '--include',
    #     type=str,
    #     help='Force these characters to be encoded',
    #     default=''
    # )


def main():
    argparse_header = { "description":'Encode URL parameters in various formats',
        "formatter_class":argparse.RawDescriptionHelpFormatter,
        "epilog":f"""
Available encoders:
  {', '.join(ENCODERS.keys())}

Examples:
  echo "hello world" | %(prog)s url
  %(prog)s url -i input.txt -o output.txt
  cat input.txt | %(prog)s base64 > output.txt
        """
    }

    # First pass: parse just the encoder to know which params to add
    pre_parser = argparse.ArgumentParser(**argparse_header, add_help=False)
    add_default_params(pre_parser)

    # Print global help if there is no encoder
    if len(sys.argv) == 2 and ('-h' in sys.argv or '--help' in sys.argv):
        pre_parser.print_help()
        sys.exit(0)
    pre_args, _ = pre_parser.parse_known_args()
    encoder_name = pre_args.encoder

    # Second pass: Main parser with encoder-specific params
    parser = argparse.ArgumentParser(**argparse_header)
    add_default_params(parser)

    # Add encoder-specific parameters
    group = parser.add_argument_group('encoder')
    add_encoder_params(group, encoder_name)

    args = parser.parse_args()
    global_params = {}
    # global_params['include'] = args.include

    # Extract encoder parameters
    encoder = ENCODERS[args.encoder]
    encoder_params = {}
    if hasattr(encoder, 'params'):
        for param_name in encoder.params.keys():
            param_value = getattr(args, param_name, None)
            if param_value is not None:
                encoder_params[param_name] = param_value

    try:
        process_encoding(args.input, args.output, args.decode, global_params, args.encoder, encoder_params)
    
    except KeyboardInterrupt:
        sys.exit(130)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

