if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Azanpopz/Kindipro.git /Kindipro
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Kindipro
fi
cd /Kindipro
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py

