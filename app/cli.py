import click
from app.ciphers import (
    caesar_encrypt,
    caesar_decrypt,
    morse_encrypt,
    morse_decrypt,
    emoji_encrypt,
    emoji_decrypt,
    dino_encrypt,
    dino_decrypt,
    hero_encrypt,
    hero_decrypt,
)


CIPHER_MAP = {
    'caesar': caesar_encrypt,
    'morse': morse_encrypt,
    'emoji': emoji_encrypt,
    'dino': dino_encrypt,
    'hero': hero_encrypt
}

DECRYPT_MAP = {
    'caesar': caesar_decrypt,
    'morse': morse_decrypt,
    'emoji': emoji_decrypt,
    'dino': dino_decrypt,
    'hero': hero_decrypt
}

@click.group()
def cli():
    """Secret Agent Academy - Cipher Command Line Tool 🕵️‍♂️"""
    pass

@cli.command()
@click.argument('message')
@click.option(
    '--cipher', '-c',
    type=click.Choice(['caesar', 'atbash', 'morse', 'binary', 'pigpen'], case_sensitive=False),
    required=True,
    help='The cipher to use for encryption'
)
@click.option('--shift', '-s', default=3, help='Shift value for Caesar cipher (default: 3)')
def encrypt(message: str, cipher: str, shift: int):
    """Encrypt a message using the specified cipher.
    
    Example: python -m app.cli encrypt "Hello Agent" -c caesar
    """
    try:
        cipher_module = CIPHER_MAP[cipher.lower()]
        if cipher == 'caesar':
            result = cipher_module(message, shift=shift)
        else:
            result = cipher_module(message)
        
        click.echo(click.style("\n🔒 Encrypted Message:", fg="green", bold=True))
        click.echo(click.style(f"{result}\n", fg="bright_green"))
        
        # Show a fun spy message
        click.echo(click.style("Mission Status:", fg="yellow", bold=True))
        click.echo(click.style("Message successfully encrypted! 🎯\n", fg="yellow"))
        
    except Exception as e:
        click.echo(click.style("\n🚨 Mission Alert!", fg="red", bold=True))
        click.echo(click.style(f"Error: {str(e)}\n", fg="red"))

@cli.command()
@click.argument('message')
@click.option(
    '--cipher', '-c',
    type=click.Choice(['caesar', 'atbash', 'morse', 'binary', 'pigpen'], case_sensitive=False),
    required=True,
    help='The cipher to use for decryption'
)
@click.option('--shift', '-s', default=3, help='Shift value for Caesar cipher (default: 3)')
def decrypt(message: str, cipher: str, shift: int):
    """Decrypt a message using the specified cipher.
    
    Example: python -m app.cli decrypt "KHOOR DJHQW" -c caesar
    """
    try:
        cipher_module = DECRYPT_MAP[cipher.lower()]
        if cipher == 'caesar':
            result = cipher_module(message, shift=shift)
        else:
            result = cipher_module(message)
        
        click.echo(click.style("\n🔓 Decrypted Message:", fg="blue", bold=True))
        click.echo(click.style(f"{result}\n", fg="bright_blue"))
        
        # Show a fun spy message
        click.echo(click.style("Mission Status:", fg="yellow", bold=True))
        click.echo(click.style("Message successfully decrypted! 🎯\n", fg="yellow"))
        
    except Exception as e:
        click.echo(click.style("\n🚨 Mission Alert!", fg="red", bold=True))
        click.echo(click.style(f"Error: {str(e)}\n", fg="red"))

@cli.command()
def list_ciphers():
    """List all available ciphers and their descriptions."""
    click.echo(click.style("\n🔍 Available Ciphers:", fg="cyan", bold=True))
    
    descriptions = {
        'caesar': 'Shifts each letter in the message by a specified number of positions',
        'atbash': 'Replaces each letter with its opposite from the alphabet',
        'morse': 'Converts text to/from Morse code using dots and dashes',
        'binary': 'Converts text to/from binary code (8-bit ASCII)',
        'pigpen': 'Uses symbols to represent letters based on their position in a grid'
    }
    
    for cipher, desc in descriptions.items():
        click.echo(click.style(f"\n• {cipher.title()}", fg="bright_cyan", bold=True))
        click.echo(click.style(f"  {desc}", fg="cyan"))
    
    click.echo("\n") 