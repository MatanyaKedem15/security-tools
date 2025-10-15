import hashlib
import sys

def compute_hash(file_path, algorithm="sha256"):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        h = hashlib.new(algorithm)
        h.update(data)
        print(f"{algorithm.upper()} hash for {file_path}:\n{h.hexdigest()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hash_util.py <file_path> [algorithm: sha256|md5]")
    else:
        compute_hash(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "sha256")
