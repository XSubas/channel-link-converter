if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/XSubas/Channel-link-Converter.git /Channel-link-Converter
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /Channel-link-Converter
fi
cd /Channel-link-Converter
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
