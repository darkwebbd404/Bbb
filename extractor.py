import json

def extract_uid_password(json_file_path):
    """
    Extract UID and password from JSON file and format them as requested
    """
    try:
        # Read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Extract UID and password for each entry
        extracted_data = []
        for item in data:
            if 'uid' in item and 'password' in item:
                extracted_data.append({
                    "uid": item['uid'],
                    "password": item['password']
                })
        
        # Print the formatted output
        print("Extracted UID and Password data:")
        print("[")
        for i, item in enumerate(extracted_data):
            print("  {")
            print(f'    "uid": "{item["uid"]}",')
            print(f'    "password": "{item["password"]}"')
            if i < len(extracted_data) - 1:
                print("  },")
            else:
                print("  }")
        print("]")
        
        # Also save to a new JSON file with the same name as source file
        import os
        source_filename = os.path.basename(json_file_path)
        output_file = f"extracted_{source_filename}"
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(extracted_data, file, indent=2, ensure_ascii=False)
        
        print(f"\nData also saved to: {output_file}")
        print(f"Total entries extracted: {len(extracted_data)}")
        
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file_path}'.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("=== UID & Password Extractor ===")
    print("Enter the path to your JSON file:")
    print("Example: D:\\download\\MAJOR_REGISTER\\M_JAHID.json")
    print("Or just press Enter to use current directory files")
    print("-" * 50)
    
    # Get file path from user
    json_file_path = input("File path: ").strip()
    
    # If user just pressed Enter, show available JSON files
    if not json_file_path:
        import os
        json_files = [f for f in os.listdir('.') if f.endswith('.json') and not f.startswith('extracted_')]
        
        if not json_files:
            print("No JSON files found in current directory!")
            exit()
        
        print("\nAvailable JSON files:")
        for i, file in enumerate(json_files, 1):
            print(f"{i}. {file}")
        
        try:
            choice = int(input(f"\nSelect file (1-{len(json_files)}): ")) - 1
            if 0 <= choice < len(json_files):
                json_file_path = json_files[choice]
            else:
                print("Invalid selection!")
                exit()
        except ValueError:
            print("Invalid input!")
            exit()
    
    # Remove quotes if user added them
    json_file_path = json_file_path.strip('"\'')
    
    print(f"\nProcessing: {json_file_path}")
    print("-" * 50)
    
    # Extract UID and password
    extract_uid_password(json_file_path)
