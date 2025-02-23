import hashlib

def crack_hash(hash_value, hash_type, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            for word in file:
                word = word.strip()
                hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()
                
                if hashed_word == hash_value:
                    print(f"[+] Password Found: {word}")
                    return word
            
        print("[-] Password Not Found in Wordlist")
        return None
    
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
    except ValueError:
        print("[!] Invalid hash type specified.")

if __name__ == "__main__":
    hash_value = input("Enter the hash to crack: ")
    hash_type = input("Enter hash type (md5, sha1, sha256, etc.): ")
    wordlist_path = input("Enter path to wordlist: ")
    
    crack_hash(hash_value, hash_type, wordlist_path)
