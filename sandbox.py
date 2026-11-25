import os
import sys
import resource
import subprocess
import tempfile
import shutil

TIME_LIMIT_SEC = 3
MEMORY_LIMIT_MB = 64
MAX_PROCESSES = 10

def set_limits():
    resource.setrlimit(resource.RLIMIT_CPU, (TIME_LIMIT_SEC, TIME_LIMIT_SEC))
    mem_bytes = MEMORY_LIMIT_MB * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
    resource.setrlimit(resource.RLIMIT_NPROC, (MAX_PROCESSES, MAX_PROCESSES))

def run_in_sandbox(target_script):
    if not os.path.exists(target_script):
        print(f"[ERROR] File tidak ditemukan: {target_script}")
        return

    sandbox_dir = tempfile.mkdtemp(prefix="sandbox_env_")
    isolated_script = os.path.join(sandbox_dir, "payload.py")
    shutil.copy(target_script, isolated_script)

    print("=== Memulai Eksekusi Mini Sandbox Runner ===")
    print(f"Target : {target_script}")
    print(f"Batas  : Waktu={TIME_LIMIT_SEC}s | RAM={MEMORY_LIMIT_MB}MB\n")

    try:
        result = subprocess.run(
            ["python3", "payload.py"],
            cwd=sandbox_dir,
            env={"PATH": "/usr/bin:/bin"},
            preexec_fn=set_limits,
            capture_output=True,
            text=True,
            timeout=TIME_LIMIT_SEC + 1
        )
        print(f"[STATUS] Selesai (Exit Code: {result.returncode})")
        if result.stdout:
            print(f"[OUTPUT]\n{result.stdout.strip()}")
        if result.stderr:
            print(f"[STDERR]\n{result.stderr.strip()}")
    except subprocess.TimeoutExpired:
        print(f"[ALERT] Proses dihentikan paksa! Melebihi batas waktu ({TIME_LIMIT_SEC} detik).")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan sistem: {e}")
    finally:
        shutil.rmtree(sandbox_dir, ignore_errors=True)
        print("\n=== Direktori Sandbox Dibersihkan ===")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan: python3 src/sandbox.py <path_ke_skrip.py>")
        sys.exit(1)
    run_in_sandbox(sys.argv[1])
