export ts_env=${1:-'dev'}
twitch_stitch_root="${PWD%/*}"

echo "\n"
echo "start migrations"

cd ./migrations
if [ ! -d ./venv ]; then
    rm -rf ./venv
    rm -rf ./__pycache__
    virtualenv ./venv -p /usr/local/bin/python3
    source venv/bin/activate
    pip3 install --process-dependency-links -r requirements.txt
    cd $twitch_stitch_root/ts_shared
    pip3 install --process-dependency-links -e ./ts_config
    deactivate
fi

source venv/bin/activate
alembic upgrade head
export ts_env='dev'

echo "done migrations"
echo "\n"
