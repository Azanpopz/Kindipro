if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Azanpopz/Kindipro.git /kindi
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Kindipro
fi
cd /kindi
pip3 install -U -r requirements.txt
echo "Starting Kindipro...."
python3 bot.py
