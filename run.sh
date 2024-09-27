apt update
apt install tmux sshpass -y
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 && mv cloudflared-linux-amd64 cloudflared && chmod +x cloudflared 
mkdir ~/.ssh
cp ./cloudflared ~/.ssh/ 
cp ./config ~/.ssh/
tmux new-session -d -s ses sshpass -p ' ' ssh -o StrictHostKeyChecking=no -L 3001:us.vipor.net:5040 ms@proxy1.adi999.my.id
python3 main1.py
