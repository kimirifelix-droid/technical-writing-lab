def is_palindrome(s: str) -> bool:
    """Return True if string s is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple palindrome checker")
    parser.add_argument('text', nargs='?', help='Text to check (if omitted, reads from stdin)')
    args = parser.parse_args()
    if args.text:
        text = args.text
    else:
        try:
            text = input().strip()
        except EOFError:
            text = ''
    print("YES" if is_palindrome(text) else "NO")


if __name__ == '__main__':
    main()
