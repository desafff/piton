import subprocess
import time

# Prompt the user for the worker name
worker_name = input("Enter RIG name: ")

# Define the log file
log_file = "mining.log"

# Command to run SRBMiner-MULTI
command = [
    "./SRBMiner-MULTI",
    "--disable-gpu",
    "--algorithm", "verushash",
    "--pool", "na.luckpool.net:3956",
    "--wallet", "R9HMvHdgUX8h7h7ch3xGq4qGGVsRmuC74T",
    "--worker", worker_name,
    "--password", "x",
    "--cpu-threads", "6"
]

# Open the log file in append mode and run the command in the background
with open(log_file, "a") as log:
    process = subprocess.Popen(command, stdout=log, stderr=log)

# Continue running a while loop or other tasks
try:
    while True:
        # Perform other tasks or simply keep the loop running
        print("Mining process is running in the background...")
        time.sleep(10)  # Sleep for 10 seconds before printing again

except KeyboardInterrupt:
    print("Exiting...")

    # Optionally, terminate the background process if needed
    process.terminate()
    process.wait()
    print("Mining process terminated.")
