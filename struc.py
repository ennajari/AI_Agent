import os

def describe_directory_structure(directory, indent=0):
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                print("  " * indent + f"📂 {item}/")
                describe_directory_structure(item_path, indent + 1)  # Recursive call
            else:
                print("  " * indent + f"📄 {item}")
    except PermissionError:
        print("  " * indent + "🚫 Access Denied")

# Define the directory path
directory_path = r"C:\Users\Abdel\Desktop\AI_Agent"

# Start exploring
print(f"Structure of: {directory_path}\n")
describe_directory_structure(directory_path)
