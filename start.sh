if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/CyberTG/Kindipro.git /Kindipro
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Kindirpo
fi
cd /master_personal
pip3 install -U -r requirements.txt
echo "Starting Kindipro...."
python3 bot.py

