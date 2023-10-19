import subprocess

if __name__ == "__main__":
    script1 = "script1.py"
    script2 = "script2.py"
    try:
        subprocess.run(["python", script2], check=True)
        time.sleep(5)
        subprocess.run(["python", script1], check=True)
        time.sleep(5)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script2}: {e}")
        print(f"Error running {script1}: {e}")    
