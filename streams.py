# Reading from standard input (stdin)
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Writing to standard output (stdout)
print("This is a regular message.")

# Writing to standard error (stderr)
print("This is an error message.", file=sys.stderr)